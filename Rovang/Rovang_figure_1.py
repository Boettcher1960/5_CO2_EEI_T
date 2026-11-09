# -*- coding: utf-8 -*-
"""Figure 1 (v5) - the equilibrium relationship and how the band is defined.

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
from matplotlib.patches import Patch

GRAY = "#b8b8b8"
JUDD = "#111111"          # black diamonds, the established default
EP = "#8e6fc7"            # EPICA, the original purple
CLK = "#3b1f8f"            # Clark, deep violet-blue - separated from EPICA in hue and value
XLO, XHI = 125, 1500
YLO, YHI = 5, 40

def Rovang_figure_1():
    """Create Rovang Figure 1 and save it as Rovang/Rovang_figure_1.png."""
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
    output_path = os.path.join(figure_dir, "Rovang_figure_1.png")

    Lg = lambda p: np.log2(np.asarray(p, float) / B.C0)
    fits = [
        ("Judd et al. 2024, Cenozoic, 66\u20130 Ma", B.S_judd, B.b_judd,
         B.se_judd, B.sb_judd, JUDD, "--"),
        ("EPICA Dome C \u00d70.55, 1\u2013800 kyr", B.S_ep, B.b_ep,
         B.se_ep, B.sb_ep, EP, "-."),
        ("Clark et al. 2024, 1\u2013800 kyr", B.S_clk, B.b_clk,
         B.se_clk, B.sb_clk, CLK, ":"),
    ]

    fig, ax = plt.subplots(figsize=(11, 7.6))

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

    print("Figure 1 \u2014 fits and where each record sits\n")
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

    ax.set_xscale("log", base=2)
    ax.set_xlim(XLO, XHI)
    ticks = [125, 250, 500, 1000, 1500]
    ax.set_xticks(ticks)
    ax.set_xticklabels([f"{tick:,}" for tick in ticks])
    ax.set_ylim(YLO, YHI)
    ax.set_yticks(np.arange(YLO, YHI + 1, 5))
    ax.set_xlabel("Atmospheric CO$_2$ (ppm, log$_2$ scale) Dean Rovang figure 1", fontsize=16)
    ax.set_ylabel("Global Mean Surface Temperature (\u00b0C)", fontsize=16)
    ax.tick_params(axis="both", labelsize=13)
    ax.grid(True, alpha=0.22)
    paris_band_color = "#add8e6"
    ax.axhspan(15.5, 16, color=paris_band_color, alpha=0.55, zorder=2)
    co2_band_color = "#87ceeb"
    ax.axvspan(430, 480, color=co2_band_color, alpha=0.35, zorder=2)
    reference_color = "#228B22"
    ax.axhline(14, color=reference_color, ls="--", lw=1.8, zorder=6)
    ax.plot([280, 280], [5, 25], color=reference_color, ls="--", lw=1.8,
            zorder=6)
    handles = [
        Patch(facecolor=GRAY, alpha=0.75,
              label="Equilibrium relationship, last 66 Myr ($\\pm1\\sigma$)"),
        Patch(facecolor=paris_band_color, alpha=0.55,
              label="1.5\u00b0C Paris treaty below 2°C"),
        Patch(facecolor=co2_band_color, alpha=0.35,
              label="430 ppm in 2026 (430\u2013480 ppm range)"),
        Line2D([], [], ls="none", marker="o", ms=9, mfc=EP, mec="none",
               label="EPICA Dome C \u00d70.55, 1\u2013800 kyr"),
        Line2D([], [], ls="none", marker="^", ms=9, mfc=CLK, mec="none",
               label="Clark et al. 2024, 1\u2013800 kyr"),
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
    ax.legend(handles=handles, fontsize=10.5, loc="upper left", framealpha=0.96)
    plt.tight_layout()
    fig.savefig(output_path, dpi=200, bbox_inches="tight")
    plt.show()
    plt.close(fig)

    print(
        f"\n  band at the frame corners: {np.interp(Lg(XLO), x, lo):.1f} to "
        f"{np.interp(Lg(XHI), x, hi):.1f} C   frame is {YLO} to {YHI}"
    )
    print(f"\nwrote end figure:1  {output_path}")
    return output_path


if __name__ == "__main__":
    Rovang_figure_1()
