import numpy as np
import scipy.io as sio
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from scipy import odr
from scipy.interpolate import Akima1DInterpolator
import os
try:
    from .load_primary_data import load_datasets
except ImportError:
    from load_primary_data import load_datasets
import os as _os
_HERE=_os.path.dirname(_os.path.abspath(__file__))
DATA=_os.environ.get('DIAGRAM_DATA', _os.path.join(_HERE,'data'))
OUTDIR=_os.environ.get('OUTDIR', _HERE)
_os.makedirs(OUTDIR, exist_ok=True)

C0     = 280.0
# Anchor for converting published anomaly reconstructions to absolute GMST.
# The 1850-1900 mean of the Berkeley Earth series - the conventional
# preindustrial baseline - so a single zero applies to every series here.
T_1850 = 13.8605
age_grid_yr  = np.arange(1000, 800001, 1000)
age_grid_myr = age_grid_yr / 1e6

def york_reg(x, y, sx, sy):
    model  = odr.Model(lambda p, x: p[0]*x + p[1])
    data   = odr.RealData(x, y, sx=np.maximum(sx,1e-6), sy=np.maximum(sy,1e-6))
    result = odr.ODR(data, model, beta0=[8.0, 0.0]).run()
    S, b   = result.beta
    y_pred = S*x + b
    r      = np.sqrt(max(0, 1 - np.sum((y-y_pred)**2)/np.sum((y-y.mean())**2)))
    return S, b, result.sd_beta[0], r, result.sd_beta[1]

# ── Bereiter CO2 (tc in Myr) ──────────────────────────────────────────────
mat = sio.loadmat(os.path.join(DATA,'CO2.mat'))
tc_raw=mat['tc'].flatten(); c_raw=mat['c'].flatten(); uc_raw=mat['uc'].flatten()
idx=np.argsort(tc_raw); tc_s=tc_raw[idx]; c_s=c_raw[idx]; uc_s=uc_raw[idx]
# Akima interpolation for Bereiter CO2 (matches Cael et al. 2026 methodology)
aki_c  = Akima1DInterpolator(tc_s, c_s)
aki_uc = Akima1DInterpolator(tc_s, uc_s)
c_grid  = aki_c(age_grid_myr)
uc_grid = aki_uc(age_grid_myr)
# Clip any extrapolation NaNs at boundaries
valid_grid = np.isfinite(c_grid) & np.isfinite(uc_grid)
age_grid_myr = age_grid_myr[valid_grid]
age_grid_yr  = age_grid_yr[valid_grid]
c_grid  = c_grid[valid_grid]
uc_grid = uc_grid[valid_grid]
co2_epica_grid = C0 * 2**c_grid

# ── EPICA EDC temp ────────────────────────────────────────────────────────
edc = pd.read_csv(os.path.join(DATA,'edc3deuttemp2007.txt'),
                  skiprows=92, sep=r'\s+', header=None,
                  names=['Bag','ztop','Age','Deuterium','Temperature'],
                  on_bad_lines='skip')
edc['Age']         = pd.to_numeric(edc['Age'],         errors='coerce')
edc['Temperature'] = pd.to_numeric(edc['Temperature'], errors='coerce')
edc = edc.dropna(subset=['Age','Temperature'])
edc = edc[edc['Age'] > 0]
age_edc=edc['Age'].values; dT_edc=edc['Temperature'].values
idx_e=np.argsort(age_edc)
gmst_edc_full = dT_edc[idx_e]*0.55 + T_1850
gmst_epica = np.interp(age_grid_yr, age_edc[idx_e], gmst_edc_full)
ut_epica   = np.full_like(gmst_epica, 0.5)
S_ep, b_ep, se_ep, r_ep, sb_ep = york_reg(c_grid, gmst_epica, uc_grid, ut_epica)

# ── Modern + SSP from primary loader (xlsx retired); EPICA OLS line retired ──
_D = load_datasets(DATA)
mod_co2,mod_gmst,mod_yr = _D['mod_co2'],_D['mod_gmst'],_D['mod_yr']
ssp_yr,ssp_co2,ssp_gmst = _D['ssp_yr'],_D['ssp_co2'],_D['ssp_gmst']
ssp_p05,ssp_p95 = _D['ssp_p05'],_D['ssp_p95']

# ── Snyder ────────────────────────────────────────────────────────────────
sny=sio.loadmat(os.path.join(DATA,'Temp_Snyder.mat'))
tT_sny=sny['tT'].flatten(); T_sny=sny['T'].flatten(); uT_sny=sny['uT'].flatten()
gmst_sny_full=T_sny+T_1850
mask_sny=(tT_sny>=tc_s.min())&(tT_sny<=tc_s.max())&np.isfinite(gmst_sny_full)
tT_sny_f=tT_sny[mask_sny]; gmst_sny_f=gmst_sny_full[mask_sny]; uT_sny_f=uT_sny[mask_sny]
c_sny=aki_c(tT_sny_f); uc_sny=aki_uc(tT_sny_f)
val_sny=np.isfinite(c_sny)&np.isfinite(uc_sny)
tT_sny_f=tT_sny_f[val_sny]; gmst_sny_f=gmst_sny_f[val_sny]; uT_sny_f=uT_sny_f[val_sny]
c_sny=c_sny[val_sny]; uc_sny=uc_sny[val_sny]
co2_sny=C0*2**c_sny
S_sny, b_sny, se_sny, r_sny, sb_sny = york_reg(c_sny, gmst_sny_f, uc_sny, uT_sny_f)

# ── Clark (use fixed sy=0.5 for consistency with prior session) ───────────
clk=pd.read_excel(os.path.join(DATA,'science_adi1908_data_s1.xlsx'),sheet_name='Sheet1')
age_clk=clk['Age (Ma)'].values
gmst_clk=clk['Global mean surface temp (GMST) (oC) area weighted'].values+T_1850
# Clark sigma: (GMST+1stdev - GMST-1stdev) / 2  (per data_provenance_v9)
up_clk=clk['GMST +1stdev'].values; um_clk=clk['GMST -1stdev'].values
sigma_clk=(up_clk - um_clk)/2
# 1-800 kyr BP: upper limit because CO2 comes from the ice-core record;
# lower limit so the youngest sample does not carry an interpolated
# industrial-era CO2 value. Matches the EPICA grid, which starts at 1 kyr.
mask_clk=(age_clk<=0.8)&(age_clk>=0.001)&np.isfinite(gmst_clk)&np.isfinite(sigma_clk)
age_clk_f=age_clk[mask_clk]; gmst_clk_f=gmst_clk[mask_clk]; uT_clk_f=sigma_clk[mask_clk]
# Akima interp for Clark CO2 (consistent with Cael et al. 2026)
c_clk=aki_c(age_clk_f); uc_clk=aki_uc(age_clk_f)
val_clk=np.isfinite(c_clk)&np.isfinite(uc_clk)
age_clk_f=age_clk_f[val_clk]; gmst_clk_f=gmst_clk_f[val_clk]
uT_clk_f=uT_clk_f[val_clk]; c_clk=c_clk[val_clk]; uc_clk=uc_clk[val_clk]
co2_clk=C0*2**c_clk
S_clk, b_clk, se_clk, r_clk, sb_clk = york_reg(c_clk, gmst_clk_f, uc_clk, uT_clk_f)

# ── Judd: CENOZOIC ONLY (<=66 Ma) for confirmed 8.24/R=0.97 ──────────────
judd=pd.read_csv(os.path.join(DATA,'PhanDA_GMSTandCO2_percentiles.csv'))
jage=judd['LowerAge'].values
jco2=judd['CO2_50'].values; jco2_16=judd['CO2_16'].values; jco2_84=judd['CO2_84'].values
jgm=judd['GMST_50'].values; jgm_16=judd['GMST_16'].values; jgm_84=judd['GMST_84'].values

# Cenozoic filter (<=66 Ma) + plot window
mask_j = np.isfinite(jco2)&np.isfinite(jgm)&(jco2>0)&(jage<=66)
jco2_f=jco2[mask_j]; jgm_f=jgm[mask_j]; jage_f=jage[mask_j]
jco2_16_f=jco2_16[mask_j]; jco2_84_f=jco2_84[mask_j]
jgm_16_f=jgm_16[mask_j]; jgm_84_f=jgm_84[mask_j]

jx  = np.log2(jco2_f/C0)
jsx = (np.log2(jco2_84_f/C0) - np.log2(jco2_16_f/C0)) / 2
jsy = (jgm_84_f - jgm_16_f) / 2
jsx = np.maximum(jsx, 1e-6); jsy = np.maximum(jsy, 1e-6)
S_judd, b_judd, se_judd, r_judd, sb_judd = york_reg(jx, jgm_f, jsx, jsy)

# Judd plot points: Cenozoic only (<=66 Ma)
mask_j_all=np.isfinite(jco2)&np.isfinite(jgm)&(jco2>0)&(jage<=66)
jco2_all=jco2[mask_j_all]; jgm_all=jgm[mask_j_all]; jage_all=jage[mask_j_all]
jco2_16_all=jco2_16[mask_j_all]; jco2_84_all=jco2_84[mask_j_all]
jgm_16_all=jgm_16[mask_j_all]; jgm_84_all=jgm_84[mask_j_all]

print(f"EPICA York:  S={S_ep:.2f}, b={b_ep:.3f}, R={r_ep:.2f}")
print(f"Snyder York: S={S_sny:.2f}, b={b_sny:.3f}, R={r_sny:.2f}")
print(f"Clark York:  S={S_clk:.2f}, b={b_clk:.3f}, R={r_clk:.2f}")
print(f"Judd York:   S={S_judd:.2f}, b={b_judd:.3f}, R={r_judd:.2f}")

x_mod=np.log2(mod_co2/C0); c_mod=np.polyfit(x_mod,mod_gmst,1)
S_mod=c_mod[0]; b_mod=c_mod[1]
yp_mod=S_mod*x_mod+b_mod
r_mod=np.sqrt(max(0,1-np.sum((mod_gmst-yp_mod)**2)/np.sum((mod_gmst-mod_gmst.mean())**2)))
x_ssp=np.log2(ssp_co2/C0); c_ssp=np.polyfit(x_ssp,ssp_gmst,1)
S_ssp=c_ssp[0]; b_ssp=c_ssp[1]
yp_ssp=S_ssp*x_ssp+b_ssp
r_ssp=np.sqrt(max(0,1-np.sum((ssp_gmst-yp_ssp)**2)/np.sum((ssp_gmst-ssp_gmst.mean())**2)))
print(f"Modern OLS:  S={S_mod:.2f}, b={b_mod:.3f}, R={r_mod:.2f}")
print(f"SSP OLS:     S={S_ssp:.2f}, b={b_ssp:.3f}, R={r_ssp:.2f}")

# ═══════════════════════════════════════════════════════════════════════════
# Plotting helpers
# ═══════════════════════════════════════════════════════════════════════════
ppm_min, ppm_max = 100, 700
ppm_line = np.linspace(ppm_min, ppm_max, 500)
x_line   = np.log2(ppm_line/C0)
def fl(S,b): return S*x_line+b

COL_CLARK='#6baed6'; COL_SNY='#c45e3a'; COL_EPICA='#6a4c93'
COL_JUDD='black';    COL_MOD='#2d8a2d'; COL_SSP='#c0392b'; COL_SSP_SH='#e07070'
ATTR = 'Bereiter et al. 2015 CO₂  ·  Berkeley Earth GMST (2026)  ·  CMIP6/AR6 SSP2-4.5'

def plot_clouds(ax):
    ax.scatter(co2_epica_grid, gmst_epica, s=1.5, color=COL_EPICA,
               alpha=0.3, zorder=1, rasterized=True, label='EPICA Dome C (×0.55)')
    ax.scatter(co2_sny, gmst_sny_f, s=1.5, color=COL_SNY,
               alpha=0.3, zorder=1, rasterized=True, label='Snyder (2016)')
    ax.scatter(co2_clk, gmst_clk_f, s=1.5, color=COL_CLARK,
               alpha=0.3, zorder=1, rasterized=True, label='Clark et al. 2024')

def plot_judd_points(ax):
    pwin=(jco2_all>=ppm_min)&(jco2_all<=ppm_max)
    pq=pwin&(jage_all>2.58); qq=pwin&(jage_all<=2.58)
    def eb(m, filled):
        xe=[jco2_all[m]-jco2_16_all[m], jco2_84_all[m]-jco2_all[m]]
        ye=[jgm_all[m]-jgm_16_all[m],   jgm_84_all[m]-jgm_all[m]]
        kw=dict(fmt='D',ms=5,ecolor='gray',elinewidth=0.7,capsize=2,zorder=4)
        if filled:
            ax.errorbar(jco2_all[m],jgm_all[m],xerr=xe,yerr=ye,
                        color='black',label='Judd et al. 2024 (pre-Quaternary)',**kw)
        else:
            ax.errorbar(jco2_all[m],jgm_all[m],xerr=xe,yerr=ye,
                        mfc='white',mec='black',color='black',
                        label='Judd et al. 2024 (Quaternary)',**kw)
    eb(pq,True); eb(qq,False)

def plot_fit_lines(ax):
    ax.plot(ppm_line,fl(S_clk, b_clk), color=COL_CLARK,ls='-.',lw=1.5,
            label=f'Clark York AESS: {S_clk:.2f} K/dbl, R={r_clk:.2f}')
    ax.plot(ppm_line,fl(S_sny, b_sny), color=COL_SNY,  ls='-.',lw=1.5,
            label=f'Snyder York AESS: {S_sny:.2f} K/dbl, R={r_sny:.2f}')
    ax.plot(ppm_line,fl(S_ep,  b_ep),  color=COL_EPICA,ls='-.',lw=1.5,
            label=f'EPICA York AESS: {S_ep:.2f} K/dbl, R={r_ep:.2f}')
    ax.plot(ppm_line,fl(S_judd,b_judd),color=COL_JUDD, ls='--',lw=2.0,
            label=f'Judd York AESS: {S_judd:.2f} K/dbl, R={r_judd:.2f}')

def plot_modern(ax):
    ax.scatter(mod_co2,mod_gmst,s=8,color=COL_MOD,zorder=5,
               label='Modern record (Berkeley Earth GMST + CMIP6/NOAA CO₂, 1850–2025)')
    for yr_t in [1850, 2025]:
        i=np.argmin(np.abs(mod_yr-yr_t))
        ax.plot(mod_co2[i],mod_gmst[i],'o',ms=8,
                mfc=(0,0,0,0),mec='black',mew=1.5,zorder=6)

def plot_ssp(ax):
    ax.fill_between(ssp_co2,ssp_p05,ssp_p95,alpha=0.25,color=COL_SSP_SH,zorder=3)
    ax.plot(ssp_co2,ssp_gmst,color=COL_SSP,lw=2,ls='--',zorder=5,
            label='SSP2-4.5 projection (CMIP6/AR6, 2025–~2100)')
    ax.plot(ssp_co2[-1],ssp_gmst[-1],'o',ms=8,
            mfc=(0,0,0,0),mec=COL_SSP,mew=1.5,zorder=6)

def setup_ax(ax):
    ax.set_xlim(100,700); ax.set_ylim(5,25)
    ax.set_xlabel('Atmospheric CO₂ (ppm)',fontsize=11)
    ax.set_ylabel('GMST (°C)',fontsize=11)
    ax.tick_params(labelsize=10); ax.grid(True,alpha=0.3)

def add_attr(fig):
    fig.text(0.5,0.005,ATTR,ha='center',fontsize=7,color='gray',style='italic')

OUT=OUTDIR+_os.sep

# ── Figure 1: york_no_modern ──────────────────────────────────────────────
fig,ax=plt.subplots(figsize=(10,7))
plot_clouds(ax); plot_judd_points(ax); plot_fit_lines(ax)
setup_ax(ax); ax.legend(fontsize=8,loc='upper left',framealpha=0.85)
ax.set_title('Paleoclimate CO₂–Temperature Relationship (Cenozoic)',fontsize=12)
add_attr(fig); plt.tight_layout(rect=[0,0.03,1,1])
plt.savefig(OUT+'york_no_modern.png',dpi=180,bbox_inches='tight'); plt.close()
print('✓ york_no_modern.png')

# ── Figure 2: york_modern_only ────────────────────────────────────────────
fig,ax=plt.subplots(figsize=(10,7))
plot_clouds(ax); plot_judd_points(ax); plot_fit_lines(ax); plot_modern(ax)
setup_ax(ax); ax.legend(fontsize=8,loc='upper left',framealpha=0.85)
ax.set_title('Paleoclimate + Modern Record (1850–2025)',fontsize=12)
add_attr(fig); plt.tight_layout(rect=[0,0.03,1,1])
plt.savefig(OUT+'york_modern_only.png',dpi=180,bbox_inches='tight'); plt.close()
print('✓ york_modern_only.png')

# ── Figure 3: york_modern_no_legend (modern+SSP labeled only) ────────────
fig,ax=plt.subplots(figsize=(10,7))
plot_clouds(ax); plot_judd_points(ax)
ax.plot(ppm_line,fl(S_clk, b_clk), color=COL_CLARK,ls='-.',lw=1.5)
ax.plot(ppm_line,fl(S_sny, b_sny), color=COL_SNY,  ls='-.',lw=1.5)
ax.plot(ppm_line,fl(S_ep,  b_ep),  color=COL_EPICA,ls='-.',lw=1.5)
ax.plot(ppm_line,fl(S_judd,b_judd),color=COL_JUDD, ls='--',lw=2.0)
plot_modern(ax); plot_ssp(ax)
setup_ax(ax)
handles=[
    Line2D([0],[0],color=COL_MOD,marker='o',ls='-',ms=5,
           label='Modern record (Berkeley Earth GMST + CMIP6/NOAA CO₂, 1850–2025)'),
    Line2D([0],[0],color=COL_SSP,lw=2,
           label='SSP2-4.5 projection (CMIP6/AR6, 2025–~2100)'),
]
ax.legend(handles=handles,fontsize=9,loc='upper left',framealpha=0.85)
ax.set_title('Paleoclimate + Modern Record + SSP2-4.5 Projection',fontsize=12)
add_attr(fig); plt.tight_layout(rect=[0,0.03,1,1])
plt.savefig(OUT+'york_modern_no_legend.png',dpi=180,bbox_inches='tight'); plt.close()
print('✓ york_modern_no_legend.png')

# ── Figure 4: york_with_modern (full legend) ──────────────────────────────
fig,ax=plt.subplots(figsize=(10,7))
plot_clouds(ax); plot_judd_points(ax); plot_fit_lines(ax); plot_modern(ax); plot_ssp(ax)
setup_ax(ax); ax.legend(fontsize=7.5,loc='upper left',framealpha=0.85)
ax.set_title('CO₂–Temperature: 66 Million Years to 2100',fontsize=12)
add_attr(fig); plt.tight_layout(rect=[0,0.03,1,1])
plt.savefig(OUT+'york_with_modern.png',dpi=180,bbox_inches='tight'); plt.close()
print('✓ york_with_modern.png')

print('\nAll four figures complete.')

# ── Figure 5: paleo_only — paleoclimate only, no Snyder ──────────────────
fig,ax=plt.subplots(figsize=(10,7))
# Clouds: EPICA and Clark only
ax.scatter(co2_epica_grid, gmst_epica, s=1.5, color=COL_EPICA,
           alpha=0.3, zorder=1, rasterized=True, label='EPICA Dome C (×0.55)')
ax.scatter(co2_clk, gmst_clk_f, s=1.5, color=COL_CLARK,
           alpha=0.3, zorder=1, rasterized=True, label='Clark et al. 2024')
plot_judd_points(ax)
# Fit lines: Clark, EPICA York, Judd, EPICA OLS — no Snyder
ax.plot(ppm_line,fl(S_clk, b_clk), color=COL_CLARK,ls='-.',lw=1.5,
        label=f'Clark York AESS: {S_clk:.2f} K/dbl, R={r_clk:.2f}')
ax.plot(ppm_line,fl(S_ep,  b_ep),  color=COL_EPICA,ls='-.',lw=1.5,
        label=f'EPICA York AESS: {S_ep:.2f} K/dbl, R={r_ep:.2f}')
ax.plot(ppm_line,fl(S_judd,b_judd),color=COL_JUDD, ls='--',lw=2.0,
        label=f'Judd York AESS: {S_judd:.2f} K/dbl, R={r_judd:.2f}')
setup_ax(ax); ax.legend(fontsize=8,loc='upper left',framealpha=0.85)
ax.set_title('Paleoclimate CO₂–Temperature Relationship (Cenozoic)', fontsize=12)
add_attr(fig); plt.tight_layout(rect=[0,0.03,1,1])
plt.savefig(_os.path.join(OUTDIR, 'paleo_only.png'),dpi=180,bbox_inches='tight')
plt.close(); print("✓ paleo_only.png")

# ── Shared no-Snyder helpers ───────────────────────────────────────────────
def plot_clouds_ns(ax):
    ax.scatter(co2_epica_grid, gmst_epica, s=1.5, color=COL_EPICA,
               alpha=0.3, zorder=1, rasterized=True, label='EPICA Dome C (×0.55)')
    ax.scatter(co2_sny, gmst_sny_f, s=1.5, color=COL_SNY,
               alpha=0.3, zorder=1, rasterized=True, label='Snyder (2016)')
    ax.scatter(co2_clk, gmst_clk_f, s=1.5, color=COL_CLARK,
               alpha=0.3, zorder=1, rasterized=True, label='Clark et al. 2024')

def plot_fits_ns(ax):
    ax.plot(ppm_line,fl(S_clk, b_clk), color=COL_CLARK,ls='-.',lw=1.5,
            label=f'Clark York AESS: {S_clk:.2f} K/dbl, R={r_clk:.2f}')
    ax.plot(ppm_line,fl(S_sny, b_sny), color=COL_SNY,  ls='-.',lw=1.5,
            label=f'Snyder York AESS: {S_sny:.2f} K/dbl, R={r_sny:.2f}')
    ax.plot(ppm_line,fl(S_ep,  b_ep),  color=COL_EPICA,ls='-.',lw=1.5,
            label=f'EPICA York AESS: {S_ep:.2f} K/dbl, R={r_ep:.2f}')
    ax.plot(ppm_line,fl(S_judd,b_judd),color=COL_JUDD, ls='--',lw=2.0,
            label=f'Judd York AESS: {S_judd:.2f} K/dbl, R={r_judd:.2f}')

# ── paleo_only ─────────────────────────────────────────────────────────────
fig,ax=plt.subplots(figsize=(10,7))
plot_clouds_ns(ax); plot_judd_points(ax); plot_fits_ns(ax)
setup_ax(ax); ax.legend(fontsize=8,loc='upper left',framealpha=0.85)
add_attr(fig); plt.tight_layout(rect=[0,0.03,1,1])
plt.savefig(_os.path.join(OUTDIR, 'paleo_only.png'),dpi=180,bbox_inches='tight')
plt.close(); print("✓ paleo_only.png")

# ── paleo_with_modern ──────────────────────────────────────────────────────
fig,ax=plt.subplots(figsize=(10,7))
plot_clouds_ns(ax); plot_judd_points(ax); plot_fits_ns(ax); plot_modern(ax)
setup_ax(ax); ax.legend(fontsize=8,loc='upper left',framealpha=0.85)
add_attr(fig); plt.tight_layout(rect=[0,0.03,1,1])
plt.savefig(_os.path.join(OUTDIR, 'paleo_with_modern.png'),dpi=180,bbox_inches='tight')
plt.close(); print("✓ paleo_with_modern.png")

# ── paleo_with_modern_and_ssp ──────────────────────────────────────────────
fig,ax=plt.subplots(figsize=(10,7))
plot_clouds_ns(ax); plot_judd_points(ax)
# fit lines unlabeled
ax.plot(ppm_line,fl(S_clk, b_clk), color=COL_CLARK,ls='-.',lw=1.5)
ax.plot(ppm_line,fl(S_sny, b_sny), color=COL_SNY,  ls='-.',lw=1.5)
ax.plot(ppm_line,fl(S_ep,  b_ep),  color=COL_EPICA,ls='-.',lw=1.5)
ax.plot(ppm_line,fl(S_judd,b_judd),color=COL_JUDD, ls='--',lw=2.0)
plot_modern(ax); plot_ssp(ax)
setup_ax(ax)
handles=[
    Line2D([0],[0],color=COL_MOD,marker='o',ls='-',ms=5,
           label='Modern record (Berkeley Earth GMST + CMIP6/NOAA CO₂, 1850–2025)'),
    Line2D([0],[0],color=COL_SSP,lw=2,
           label='SSP2-4.5 projection (CMIP6/AR6, 2025–~2100)'),
]
ax.legend(handles=handles,fontsize=9,loc='upper left',framealpha=0.85)
add_attr(fig); plt.tight_layout(rect=[0,0.03,1,1])
plt.savefig(_os.path.join(OUTDIR, 'paleo_with_modern_and_ssp.png'),dpi=180,bbox_inches='tight')
plt.close(); print("✓ paleo_with_modern_and_ssp.png")


# ── the band ─────────────────────────────────────────────────────────────
# Each fit is widened by its own standard errors in slope and intercept:
# at concentration C its envelope is the fitted line plus and minus
#     sigma_S * |log2(C/280)| + sigma_b
# The band is the union of the three. Intercept uncertainty is included
# because a fitted line is uncertain in position as well as in slope;
# without it the envelope would close to a point at the reference
# concentration, where the slope term vanishes.
BAND_FITS = [(S_judd, b_judd, se_judd, sb_judd),
             (S_ep,   b_ep,   se_ep,   sb_ep),
             (S_clk,  b_clk,  se_clk,  sb_clk)]


def band_edges(ppm):
    """Lower and upper edge of the band at the given concentration(s)."""
    x = np.log2(np.asarray(ppm, float) / C0)
    lo = np.full(np.shape(x), np.inf)
    hi = np.full(np.shape(x), -np.inf)
    for S, b, sS, sb in BAND_FITS:
        v = S * x + b
        h = sS * np.abs(x) + sb
        lo = np.minimum(lo, v - h)
        hi = np.maximum(hi, v + h)
    return lo, hi
