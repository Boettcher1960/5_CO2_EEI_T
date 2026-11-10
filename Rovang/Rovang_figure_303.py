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
 # 303.20 imports from Dean https://zenodo.org/records/22837428 
import io
import os
import contextlib

import numpy as np
import matplotlib
# matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import Patch, Rectangle

 # 303.22 my imports from  https://github.com/Boettcher1960/5_CO2_EEI_T
from config import *
from main import v

# 303.25 local variables for colors and axis limits
GRAY = "#b8b8b8"
JUDD = "#111111"          # black diamonds, the established default
EP = "#8e6fc7"            # EPICA, the original purple
CLK = "#3b1f8f"           # Clark, deep violet-blue - separated from EPICA in hue and value
XLO, XHI = 125, 1500        # see config.py for the x axis CO2 limits, x_303min, x_303max
YLO, YHI = 5, 40            # see config.py for the y axis T limits, y_303min, y_303max

# 303.30 create the figure and axes with a specific size
def _create_figure(linear_x=False):
    """Create a Rovang figure using logarithmic or linear CO2 scaling."""
    # 303.31 import the York fit parameters from build_york_final.py, suppressing stdout
    with contextlib.redirect_stdout(io.StringIO()):
        try:
            from . import build_york_final as B
        except ImportError:
            import build_york_final as B

    # 303.32 determine the output directory and filename based on the linear_x flag
    out_dir = os.environ.get(
        "OUTDIR", os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    )
    # 303.33 create the figure directory if it doesn't exist
    figure_dir = os.path.join(out_dir, "Rovang")
    # 303.34 create the output path for the figure
    os.makedirs(figure_dir, exist_ok=True)
    # 303.35 set the filename based on whether linear_x is True or False
    filename = "figure_304_Rovang.png" if linear_x else "figure_303_Rovang.png"
    # 303.36 create the full output path for the figure
    output_path = os.path.join(figure_dir, filename)
    # 303.37 define a lambda function to calculate the logarithm base 2 of the ratio of p to B.C0
    Lg = lambda p: np.log2(np.asarray(p, float) / B.C0)
    # 303.38 define the fits for the three datasets, including their slope, intercept, and uncertainties
    fits = [
        ("Judd et al. 2024, Cenozoic, 66\u20130 Ma", B.S_judd, B.b_judd,
         B.se_judd, B.sb_judd, JUDD, "--"),
        ("EPICA Dome C \u00d70.55, 1\u2013800 kyr", B.S_ep, B.b_ep,
         B.se_ep, B.sb_ep, EP, "-."),
        ("Clark et al. 2024, 1\u2013800 kyr", B.S_clk, B.b_clk,
         B.se_clk, B.sb_clk, CLK, ":"),
    ]

    # 303.40 create the figure and axes with a specific size
    # figure1 is , ax = plt.subplots(figsize=(13, 7))
    # 303.41 size the figure303 13items high, 11 items wide, to accommodate the text lines below the plot
    fig, ax = plt.subplots(figsize=(13, 11))
    # 303.42 create an array of 800 points between 90% of XLO and 110% of XHI for plotting the fits
    p = np.linspace(XLO * 0.9, XHI * 1.1, 800)
    # 303.43 calculate the logarithm base 2 of the ratio of p to B.C0 for the x-axis values
    x = Lg(p)
    # 303.44 initialize arrays to hold the lower and upper bounds of the uncertainty band
    lo = np.full_like(x, np.inf)
    # 303.45 initialize arrays to hold the lower and upper bounds of the uncertainty band
    hi = np.full_like(x, -np.inf)
    # 303.46 loop through each fit and calculate the uncertainty band based on the slope and intercept uncertainties
    for _name, slope, intercept, slope_error, intercept_error, _color, _style in fits:
        value = slope * x + intercept
        uncertainty = slope_error * np.abs(x) + intercept_error
        lo = np.minimum(lo, value - uncertainty)
        hi = np.maximum(hi, value + uncertainty)
    # 303.47 fill the area between the lower and upper bounds of the uncertainty band with a gray color and label it
    ax.fill_between(
        p, lo, hi, color=GRAY, alpha=0.75, lw=0, zorder=1,
        label="Equilibrium relationship, last 66 Myr ($\\pm1\\sigma$)",
    )
    # 303.48 plot the three datasets with their respective markers, sizes, colors, and labels
    ax.plot(B.C0 * 2 ** B.c_grid, B.gmst_epica, "o", ms=2.6, mfc=EP, mec="none",
            alpha=0.70, zorder=3, label="EPICA Dome C \u00d70.55, 1\u2013800 kyr")
    # 303.49 plot the Clark et al. 2024 dataset with triangle markers, size 2.8, filled with CLK color, no edge color, alpha 0.70, zorder 3, and label it
    ax.plot(B.C0 * 2 ** B.c_clk, B.gmst_clk_f, "^", ms=2.8, mfc=CLK, mec="none",
            alpha=0.70, zorder=3, label="Clark et al. 2024, 1\u2013800 kyr")
    # 303.50 plot the Judd et al. 2024 dataset with diamond markers, size 7.5, filled with JUDD color, white edge color, edge width 0.9, zorder 12, and label it
    ax.plot(B.C0 * 2 ** B.jx, B.jgm_f, "D", ms=7.5, mfc=JUDD, mec="white",
            mew=0.9, zorder=12,
            label="Judd et al. 2024, Cenozoic stages, 66\u20130 Ma")
    # 303.51 print the headline above the plot
    print("Figure 303: fits and where each record sits")
    # 303.52 create an array of 400 points between the logarithm base 2 of XLO and XHI for plotting the fits
    xs = np.linspace(Lg(XLO), Lg(XHI), 400)
    # 303.53 loop through each fit and plot the linear fit line with its respective color, style, and label it with the slope value
    for name, slope, intercept, _sg, _sb, color, style in fits:
        src = B.jx if "Judd" in name else (
            B.c_grid if "EPICA" in name else B.c_clk
        )
        # 303.54 plot the linear fit line for each dataset with its respective color, style, and label it with the slope value
        ax.plot(B.C0 * 2 ** xs, slope * xs + intercept, color=color, ls=style,
                lw=2.2, zorder=7, label=f"{name}: {slope:.2f} K/doubling")
        print(
            f"  {name:42s} {B.C0*2**src.min():6.0f}\u2013"
            f"{B.C0*2**src.max():6.0f} ppm   slope {slope:5.2f}"
        )
    # 303.55 set the x-axis scale to logarithmic base 2 if linear_x is False, otherwise keep it linear
    if not linear_x:
        ax.set_xscale("log", base=2)
    # ax.set_xlim(XLO, XHI)
    # 303.56 set the x-axis limits to x_303min and x_303max, which are defined in config.py
    ax.set_xlim(x_303min, x_303max)
    # 303.57 set the y-axis limits to y_303min and y_303max, which are defined in config.py
    ticks = (
        np.linspace(x_303min, x_303max, 6)
        if linear_x
        else [125, 250, 500, 1000, 1500]
    )
    # 303.58 set the x-axis ticks to the specified ticks and format them with commas for thousands
    ax.set_xticks(ticks)
    # 303.59 set the x-axis tick labels to the specified ticks and format them with commas for thousands
    ax.set_xticklabels([f"{tick:,}" for tick in ticks])
    # 303.60 set the y-axis limits to y_303min and y_303max, which are defined in config.py
    ax.set_ylim(y_303min, y_303max)
     # 303.61 set the y-axis ticks to range from y_303min to y_303max with a step of 5
    ax.set_yticks(np.arange(y_303min, y_303max + 1, 5))
    # 303.62 set the y-axis tick labels to range from y_303min to y_303max with a step of 5
    # 303.63 set the y-axis tick labels to range from y_303min to y_303max with a step of 5
    figure_label = "4" if linear_x else "3"
    scale_label = "ppm" if linear_x else "ppm, log$_2$ scale"
    # 303.65 print the headline above the plot
    headline1 = "Global mean surface temperature vs Atmospheric CO$_2$"
    ax.text(
        -0.1, 1.05, headline1, color="black", fontname="Arial", fontsize=20,
        transform=ax.transAxes,
    )
    # 303.68 print the x axis text below the plot
    ax.set_xlabel(
        f"Figure 304: Atmospheric CO$_2$ ({scale_label}) is the x axis - after Dean Rovang ",
        fontsize=16,
        loc="left",
    )
    # 303.69 move  the x axis text
    ax.xaxis.set_label_coords(-0.1, -0.11)

    # 303.70 print the y axis text left of the plot
    ax.set_ylabel("Global Mean Surface Temperature (\u00b0C)", fontsize=18)
    ax.tick_params(axis="both", labelsize=13)
    ax.grid(True, alpha=0.22)

    # 303.80 lines parallel to x axis
    # 303.80 green dashed line for 14°C the 1850 to 1900 Temperaturelevel
    reference_color = "#228B22"
    ax.axhline(14, color=reference_color, ls="--", lw=1.8, zorder=6)
    # 303.82 blue band for 15.5°C the 2024 Temperature
    paris_band_color = "#add8e6"
    # ax.axhspan(15.5, 16, color=paris_band_color, alpha=0.55, zorder=2)
    # 303.84 orange dashed line for 15.5°C the 2024 Temperaturelevel 1.5°C above preindustrial 14°C
    c305 = "#DE7525D8"
    ax.axhline(15.5, color=c305, ls="--", lw=1.8, zorder=6)

    # 303.90 lines parallel to y axis
    # 303.90 blue band for 430 ppm the 2026 CO2 atmosphere level
    c306 = "#87ceeb"
    ax.axvspan(430, 480, color=c306, alpha=0.35, zorder=2)

    # 303.82 green dashed line for 280 ppm the 1850 to 1900 CO2 atmosphere level
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
        # Line2D([], [], color=reference_color, ls="--", lw=1.8,
        #       label="280 ppm, 14\u00b0C preindustrial"),
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
    label4 = "1.5°C is the planetary boundary - 15.5°C in dashed orange line"
    ax.plot(
        [-0.1, -0.06], [t3y4 + 0.015, t3y4 + 0.015], color=c305, ls="--", lw=2,
        transform=ax.transAxes, clip_on=False,
    )
    # 303.135 print line 3 below the plot
    ax.text(-0.055, t3y4, label4, color="black", fontname="Arial", fontsize=14,
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
