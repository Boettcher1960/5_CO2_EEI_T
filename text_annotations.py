# text_annotations.py
import os
import sys
from matplotlib.lines import Line2D

def add_header(ax1, x_anf, x_end, yl_mode):
    """Add header text above the plot"""
    trs = 20
    if yl_mode == 4:
        header = f"Earth Energy Imbalance CERES_EBAF-TOA_Ed4.2.1 Jan. 2026 data. Plot {x_anf} to {x_end}."
        ax1.text(-0.1, 1.05, header, color="black", fontname="Arial", fontsize=20,
                transform=ax1.transAxes)
# 9 part 9 print information below the plot field
# 9.1.1 print line 1 the text below the figure tr1x = -0.09 # tr1y = -.16 
def add_bottom_text(fig, ax1, filename, v, header_parameter, tr1y, tr2x):
    """Add text below the plot"""
    trs = 12
    text_below = (f"Figure from {filename} v {v}  "
                  f"https://github.com/Boettcher1960/5_CO2_EEI_T       Parameter {header_parameter}")
    ax1.text(-0.1, tr1y, text_below, color="black", fontname="Arial", fontsize=trs,
            transform=ax1.transAxes)

def add_legend_line(fig, x1, x2, y, color, linewidth=2, marker="o", markersize=5):
    """Add a legend line to the figure"""
    line = Line2D([x1, x2], [y, y], transform=fig.transFigure,
                  marker=marker, markersize=markersize, color=color, linewidth=linewidth)
    fig.add_artist(line)
    return line

def add_text_row(ax, x, y, text, color, fontsize=20):
    """Add a text row below the plot"""
    ax.text(x, y, text, color=color, fontname="Arial", fontsize=fontsize,
           transform=ax.transAxes)
