"""
load_primary_data.py  — primary-source loader for the CO2-GMST diagram.

Replaces GMST_vs_CO2_solid.xlsx for the two blocks the build scripts still read
from it: the modern instrumental record and the SSP2-4.5 projection. (The former
EPICA-OLS block, xlsx cols 4,5, has been retired in favour of EPICA York, which
the build scripts already compute from primaries.)

Every series here traces to a primary archive or to a small, documented,
regenerable CSV — no aggregator, no master spreadsheet.

Inputs (all in `data_dir`):
  SUPPLEMENT_DataTables_Meinshausen_6May2020.xlsx
        sheet 'T2 - History Year 1750 to 2014'  -> modern CO2 1850-2014 (CMIP6 historical, Meinshausen 2017)
        sheet 'T5 - SSP2-4.5 '                  -> SSP2-4.5 CO2 2025-2100
  noaa_global_co2_2015-2025.csv      <- NOAA GML global annual mean, 2015-2025 (co2_annmean_gl.txt)
  berkeley_gmst_1850-2025_annual.csv <- Berkeley Earth Global_TAVG_monthly.txt, annual mean + 14.109 degC
  tas_global_SSP2_4_5.xlsx           <- IPCC AR6 / CEDA SSP2-4.5 GMST anomaly (Year, 5%, Mean, 95%)

Cross-check only (not read here): modern_co2_1850-2025_primary.csv from splice_co2.py
  (Law Dome -> Mauna Loa -> NOAA global mean), an independent all-primary reconstruction.
"""
import os, csv
import numpy as np
import pandas as pd

C0      = 280.0
GMST_PI = 13.8605   # 1850-1900 absolute mean, for SSP anomaly -> absolute
_HERE   = os.path.dirname(os.path.abspath(__file__))


def _read_year_value(path):
    out = {}
    with open(path) as f:
        for row in csv.reader(f):
            if not row:
                continue
            try:
                y = int(float(row[0])); v = float(row[1])
            except (ValueError, IndexError):
                continue            # header / comment / blank
            out[y] = v
    return out


def load_modern(data_dir=_HERE):
    """Modern instrumental record, 1850-2025.  Returns (co2, gmst, year).

    CO2 is the OFFICIAL community-standard series: CMIP6 historical concentrations
    (Meinshausen et al. 2017, sheet 'T2 - History Year 1750 to 2014') for 1850-2014,
    spliced to the NOAA GML globally averaged marine-surface annual mean for 2015-2025
    -- the exact recipe used to force CMIP-class models. (The all-primary Law Dome ->
    Mauna Loa -> NOAA splice in splice_co2.py is retained as an independent cross-check;
    it reproduces this series to 1.1 ppm RMS over 1850-2014.)
    """
    m = pd.read_excel(os.path.join(data_dir, 'SUPPLEMENT_DataTables_Meinshausen_6May2020.xlsx'),
                      sheet_name='T2 - History Year 1750 to 2014', header=None)
    yr  = pd.to_numeric(m.iloc[12:, 0], errors='coerce')
    co2 = pd.to_numeric(m.iloc[12:, 1], errors='coerce')   # CO2 World (ppm)
    co2map = {int(y): float(c) for y, c in zip(yr, co2)
              if np.isfinite(y) and np.isfinite(c) and 1850 <= y <= 2014}
    co2map.update(_read_year_value(os.path.join(data_dir, 'noaa_global_co2_2015-2025.csv')))

    gmst = _read_year_value(os.path.join(data_dir, 'berkeley_gmst_1850-2025_annual.csv'))
    yrs  = sorted(set(co2map) & set(gmst))
    return (np.array([co2map[y] for y in yrs]),
            np.array([gmst[y]   for y in yrs]),
            np.array(yrs, dtype=float))


def load_ssp(data_dir=_HERE):
    """SSP2-4.5 projection, 2025-2100.  Returns (year, co2, gmst, p05, p95).

    CO2: Meinshausen SSP2-4.5 'World', exact from 2035; 2025 anchored to the
         observed modern value; 2026-2034 = Meinshausen minus a linearly
         tapering observed-minus-model offset (continuity at the 2025 handoff).
    GMST: CEDA/AR6 anomaly + 13.8605 degC; 2025 mean anchored to the observed
          Berkeley Earth value; 2100 carries the 2099 value (CEDA ends 2099).
    """
    obs_co2_2025, obs_gmst_2025 = (load_modern(data_dir)[0][-1],
                                   load_modern(data_dir)[1][-1])

    m = pd.read_excel(os.path.join(data_dir, 'SUPPLEMENT_DataTables_Meinshausen_6May2020.xlsx'),
                      sheet_name='T5 - SSP2-4.5 ', header=None)
    yr  = pd.to_numeric(m.iloc[12:, 0], errors='coerce')
    co2 = pd.to_numeric(m.iloc[12:, 1], errors='coerce')   # CO2 World (ppm)
    mein = {int(y): float(c) for y, c in zip(yr, co2) if np.isfinite(y) and np.isfinite(c)}
    offset = mein[2025] - obs_co2_2025

    t = pd.read_excel(os.path.join(data_dir, 'tas_global_SSP2_4_5.xlsx'), header=1)
    t.columns = ['Year', 'p05', 'Mean', 'p95']
    t = t.apply(pd.to_numeric, errors='coerce').dropna()
    tas = {int(r.Year): (r.Mean, r.p05, r.p95) for _, r in t.iterrows()}
    last_tas = max(tas)

    # GMST observed-minus-model offset at the 2025 handoff, tapered to 0 by 2035
    # (same continuity treatment as CO2; shifts mean and band together).
    gmst_offset = obs_gmst_2025 - (tas[2025][0] + GMST_PI)

    yrs = list(range(2025, 2101))
    co2_out, gm, p05, p95 = [], [], [], []
    for y in yrs:
        taper = max(0.0, (2035 - y) / 10.0)
        # CO2
        if y == 2025:
            co2_out.append(obs_co2_2025)
        elif y <= 2035:
            co2_out.append(mein[y] - offset * taper)
        else:
            co2_out.append(mein[y])
        # GMST mean + band (carry last available CEDA year past its end)
        mean, lo, hi = tas[min(y, last_tas)]
        shift = gmst_offset * taper
        gm.append(mean + GMST_PI + shift)
        p05.append(lo + GMST_PI + shift)
        p95.append(hi + GMST_PI + shift)

    return (np.array(yrs, dtype=float), np.array(co2_out),
            np.array(gm), np.array(p05), np.array(p95))


def load_datasets(data_dir=_HERE):
    mc, mg, my = load_modern(data_dir)
    sy, sc, sg, s05, s95 = load_ssp(data_dir)
    return dict(mod_co2=mc, mod_gmst=mg, mod_yr=my,
                ssp_yr=sy, ssp_co2=sc, ssp_gmst=sg, ssp_p05=s05, ssp_p95=s95)


if __name__ == '__main__':
    d = load_datasets()
    print('modern:', d['mod_yr'][0], '-', d['mod_yr'][-1], 'n=', len(d['mod_yr']))
    print('ssp:   ', d['ssp_yr'][0], '-', d['ssp_yr'][-1], 'n=', len(d['ssp_yr']))
