# -*- coding: utf-8 -*-
"""
Rovang_figure_303.py

Figure 1 (v5) - the equilibrium relationship and how the band is defined.

Three reconstructions, each with its own marker, and the York fit to each.
The gray envelope is the union of the three fits, widened by each fit's slope
uncertainty, and is the band used in every later figure.

No annotation is drawn - labelling is done in PowerPoint. Waypoint values are
printed to the console instead.

Conventions: round axis limits, band extending past the data on all sides,
legend entries giving the range each record covers rather than a point count.
"""
import io
import os
import contextlib

import numpy as np
import matplotlib
# matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import Patch, Rectangle

from config import *
from main import v

GRAY = "#b8b8b8"
JUDD = "#111111"          # black diamonds, the established default
EP = "#8e6fc7"            # EPICA, the original purple
CLK = "#3b1f8f"           # Clark, deep violet-blue - separated from EPICA in hue and value
XLO, XHI = 125, 1500        # see config.py for the x axis CO2 limits, x_303min, x_303max
YLO, YHI = 5, 40            # see config.py for the y axis T limits, y_303min, y_303max
def _create_figure(linear_x=False):
    """Create a Rovang figure using logarithmic or linear CO2 scaling."""
    with contextlib.redirect_stdout(io.StringIO()):
        try:
            from . import build_york_final as B
        except ImportError:
            import build_york_final as B

    out_dir = os.environ.get(
        "OUTDIR", os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    )
    figure_dir = os.path.join(out_dir, "Rovang")
    os.makedirs(figure_dir, exist_ok=True)
    filename = "figure_304_Rovang.png" if linear_x else "figure_303_Rovang.png"
    output_path = os.path.join(figure_dir, filename)

    Lg = lambda p: np.log2(np.asarray(p, float) / B.C0)
    fits = [
        ("Judd et al. 2024, Cenozoic, 66\u20130 Ma", B.S_judd, B.b_judd,
         B.se_judd, B.sb_judd, JUDD, "--"),
        ("EPICA Dome C \u00d70.55, 1\u2013800 kyr", B.S_ep, B.b_ep,
         B.se_ep, B.sb_ep, EP, "-."),
        ("Clark et al. 2024, 1\u2013800 kyr", B.S_clk, B.b_clk,
         B.se_clk, B.sb_clk, CLK, ":"),
    ]

    # 303.60 create the figure and axes with a specific size
    # fig, ax = plt.subplots(figsize=(15, 10.625))
    # figure1 is , ax = plt.subplots(figsize=(13, 7))
    fig, ax = plt.subplots(figsize=(13, 11))

    p = np.linspace(XLO * 0.9, XHI * 1.1, 800)
    x = Lg(p)
    lo = np.full_like(x, np.inf)
    hi = np.full_like(x, -np.inf)
    for _name, slope, intercept, slope_error, intercept_error, _color, _style in fits:
        value = slope * x + intercept
        uncertainty = slope_error * np.abs(x) + intercept_error
        lo = np.minimum(lo, value - uncertainty)
        hi = np.maximum(hi, value + uncertainty)
    ax.fill_between(
        p, lo, hi, color=GRAY, alpha=0.75, lw=0, zorder=1,
        label="Equilibrium relationship, last 66 Myr ($\\pm1\\sigma$)",
    )

    ax.plot(B.C0 * 2 ** B.c_grid, B.gmst_epica, "o", ms=2.6, mfc=EP, mec="none",
            alpha=0.70, zorder=3, label="EPICA Dome C \u00d70.55, 1\u2013800 kyr")
    ax.plot(B.C0 * 2 ** B.c_clk, B.gmst_clk_f, "^", ms=2.8, mfc=CLK, mec="none",
            alpha=0.70, zorder=3, label="Clark et al. 2024, 1\u2013800 kyr")
    ax.plot(B.C0 * 2 ** B.jx, B.jgm_f, "D", ms=7.5, mfc=JUDD, mec="white",
            mew=0.9, zorder=12,
            label="Judd et al. 2024, Cenozoic stages, 66\u20130 Ma")

    print("Figure 303 \u2014 fits and where each record sits\n")
    xs = np.linspace(Lg(XLO), Lg(XHI), 400)
    for name, slope, intercept, _sg, _sb, color, style in fits:
        src = B.jx if "Judd" in name else (
            B.c_grid if "EPICA" in name else B.c_clk
        )
        ax.plot(B.C0 * 2 ** xs, slope * xs + intercept, color=color, ls=style,
                lw=2.2, zorder=7, label=f"{name}: {slope:.2f} K/doubling")
        print(
            f"  {name:42s} {B.C0*2**src.min():6.0f}\u2013"
            f"{B.C0*2**src.max():6.0f} ppm   slope {slope:5.2f}"
        )

    if not linear_x:
        ax.set_xscale("log", base=2)
    # ax.set_xlim(XLO, XHI)
    ax.set_xlim(x_303min, x_303max)
    ticks = (
        np.linspace(x_303min, x_303max, 6)
        if linear_x
        else [125, 250, 500, 1000, 1500]
    )
    ax.set_xticks(ticks)
    ax.set_xticklabels([f"{tick:,}" for tick in ticks])
    ax.set_ylim(y_303min, y_303max)
    ax.set_yticks(np.arange(y_303min, y_303max + 1, 5))
    figure_label = "4" if linear_x else "3"
    scale_label = "ppm" if linear_x else "ppm, log$_2$ scale"
    # 303.80 print the headline above the plot
    headline1 = "Global mean surface temperature vs Atmospheric CO$_2$"
    ax.text(
        -0.1, 1.05, headline1, color="black", fontname="Arial", fontsize=20,
        transform=ax.transAxes,
    )
    # 303.82 print the x axis text below the plot
    ax.set_xlabel(
        f"Figure 304: Atmospheric CO$_2$ ({scale_label}) is the x axis - after Dean Rovang ",
        fontsize=16,
        loc="left",
    )
    # 303.83 move  the x axis text
    ax.xaxis.set_label_coords(-0.1, -0.11)

    # 303.85 print the y axis text left of the plot
    ax.set_ylabel("Global Mean Surface Temperature (\u00b0C)", fontsize=18)
    ax.tick_params(axis="both", labelsize=13)
    ax.grid(True, alpha=0.22)
   
    # 303.96 blue band for 15.5°C the 2024 Temperature 
    paris_band_color = "#add8e6"
    ax.axhspan(15.5, 16, color=paris_band_color, alpha=0.55, zorder=2)

    # 303.97 blue band for 430 ppm the 2026 CO2 atmosphere level
    co2_band_color = "#87ceeb"
    ax.axvspan(430, 480, color=co2_band_color, alpha=0.35, zorder=2)
    reference_color = "#228B22"

    # 303.99 green dashed line for 14°C the 1850 to 1900 Temperaturelevel
    ax.axhline(14, color=reference_color, ls="--", lw=1.8, zorder=6)

    # 303.100 green dashed line for 280 ppm the 1850 to 1900 CO2 atmosphere level
    ax.plot([280, 280], [5, 19], color=reference_color, ls="--", lw=1.8, zorder=6)

     # 303.101 legend with the 3 fits and the 4 bands
    handles = [
        Patch(facecolor=GRAY, alpha=0.75,
              label="Equilibrium relationship, last 66 Myr ($\\pm1\\sigma$)"),
        # Patch(facecolor=paris_band_color, alpha=0.55,
        #      label="1.5\u00b0C Paris treaty below 2°C"),
        # Patch(facecolor=co2_band_color, alpha=0.35,
        #      label="430 ppm in 2026 (430\u2013480 ppm range)"),
        Line2D([], [], ls="none", marker="o", ms=9, mfc=EP, mec="none",
               label="EPICA Dome C \u00d70.55, 1\u2013800 kyr"),
        # Line2D([], [], ls="none", marker="^", ms=9, mfc=CLK, mec="none",
        #       label="Clark et al. 2024, 1\u2013800 kyr"),
        Line2D([], [], ls="none", marker="D", ms=9, mfc=JUDD, mec="white",
               mew=0.9, label="Judd et al. 2024, Cenozoic stages, 66\u20130 Ma"),
        Line2D([], [], color=reference_color, ls="--", lw=1.8,
               label="280 ppm, 14\u00b0C preindustrial"),
    ]
    for name, slope, _intercept, _sg, _sb, color, style in fits:
        handles.append(
            Line2D([], [], color=color, ls=style, lw=2.4,
                   label=f"{name}: {slope:.2f} K/doubling")
        )
    # 303.109 plot the legend with the 3 fits and the 4 bands
    ax.legend(handles=handles, fontsize=10.5, loc="upper left", framealpha=0.96)

    # 303.121 print line 2 github with version number below the plot
    text_below3 = (f""
                  f"https://github.com/Boettcher1960/5_CO2_EEI_T"
                  f" {filename} version {v} ")
    t3y2 = -0.22    # 303.122 print line 2 t3y2 = -0.22
    # 303.123 print line 2 github with version number below the plot
    ax.text(-0.1, t3y2, text_below3, color="black", fontname="Arial", fontsize=14,
            transform=ax.transAxes)


    t3y3 = -0.28    # 303.124 print line 3 t3y3 = -0.28
    # 303.125 in legend, line 3, add a blue band
    ax.add_patch(   
        Rectangle(
            (-0.1, t3y3 - 0.005), 0.035, 0.025,
            transform=ax.transAxes, facecolor=paris_band_color,
            edgecolor="none", clip_on=False,
        )
    )
    # 303.127 print line 3 below the plot
    label3="blue band for 1.5\u00b0C, the Paris treaty 14\u00b0C+2\u00b0C = 16\u00b0C"
    # 303.128 print the text for line 3 below the plot
    ax.text(-0.055, t3y3, label3, color="black", fontname="Arial", fontsize=14,
            transform=ax.transAxes)
    
    # 303.131  fig.subplots_adjust(left=0.12, right=0.98, top=0.88, bottom=0.30)
    # sets the plot area’s margins within the figure. The values are fractions of the figure dimensions:
    # left=0.12: plot starts 12% from the left.
    # right=0.98: plot ends 2% from the right.
    # top=0.88: plot ends 12% below the top.
    # bottom=0.30: plot starts 30% above the bottom, leaving room below for captions.
    fig.subplots_adjust(left=0.12, right=0.98, top=0.92, bottom=0.40)
    
    t3y4 = -0.35    # 303.124 print line 6 
    label4="label 4 in line 4"
    # 303.135 print line 3 below the plot
    ax.text(-0.1, t3y4, label4, color="black", fontname="Arial", fontsize=14,
            transform=ax.transAxes)

    t3y5 = -0.42    # 303.124 print line 6 
    label5="label 5 in line 5"
    # 303.136 print line 3 below the plot
    ax.text(-0.1, t3y5, label5, color="black", fontname="Arial", fontsize=14,
            transform=ax.transAxes)

    t3y6 = -0.49    # 303.124 print line 6 
    # 303.139 in legend, line 6, add a blue band
    ax.add_patch(   
        Rectangle(
            (-0.1, t3y6 - 0.005), 0.035, 0.025,
            transform=ax.transAxes, facecolor=paris_band_color,
            edgecolor="none", clip_on=False,
        )
    )


    label6="blue band for 430 ppm in 2026 (430\u2013480 ppm range)"
    # 303.145 print line 6 below the plot
    ax.text(-0.055, t3y6, label6, color="black", fontname="Arial", fontsize=14,
            transform=ax.transAxes)



    fig.savefig(output_path, dpi=200, bbox_inches="tight")
    plt.show()
    plt.close(fig)

    print(
        f"\n  band at the frame corners: {np.interp(Lg(XLO), x, lo):.1f} to "
        f"{np.interp(Lg(XHI), x, hi):.1f} C   frame is {YLO} to {YHI}"
    )
    print(f"\nwrote end figure:{figure_label}  {output_path}")
    return output_path


def figure_303_Rovang():
    """Create the logarithmic-x Rovang figure and save figure_303_Rovang.png."""
    return _create_figure()


def figure_304_Rovang():
    """Create the linear-x Rovang figure and save figure_304_Rovang.png."""
    return _create_figure(linear_x=True)


if __name__ == "__main__":
    figure_303_Rovang()
