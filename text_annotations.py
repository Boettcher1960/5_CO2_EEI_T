# text_annotations.py
# version 5b1
import os
import sys
from matplotlib.lines import Line2D

def add_header(ax1, x_anf, x_end, yl_mode):
    """Add header text above the plot"""
    trs = 20
    if yl_mode == 4:
        header = f"Earth Energy Imbalance CERES_EBAF-TOA_Ed4.2.1 Jan. 2026 data. Plot {x_anf} to {x_end}."
        ax1.text(-0.1, 1.05, header, color="black", fontname="Arial", fontsize=trs,
                transform=ax1.transAxes)
    elif yl_mode == 7:
        header = f"Temperature in °C year {x_anf} to {x_end}"
        ax1.text(-0.1, 1.05, header, color="black", fontname="Arial", fontsize=trs,
                transform=ax1.transAxes)
    else:
        header = f"CO2 measured at Mauna Loa {x_anf} to {x_end}"
        ax1.text(-0.1, 1.05, header, color="black", fontname="Arial", fontsize=trs,
                transform=ax1.transAxes)

def add_bottom_text(fig, ax1, filename, v, header_parameter, tr1y):
    """Add text below the plot (line 1)"""
    trs = 12
    text_below = (f"Figure from {filename} v {v}  "
                  f"https://github.com/Boettcher1960/5_CO2_EEI_T       Parameter {header_parameter}")
                  # f"https://github.com/Boettcher1960/co2_python       Parameter {header_parameter}")
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

def add_axis_info_line(ax, yl_mode, y_Emin, y_Emax, y_Tmin, y_Tmax, 
                       y_min, y_max, header_parameter, tr6y, c42):
    """Add line 6 with axis information"""
    trs = 20
    
    if yl_mode == 4:  # EEI mode
        # Left Y-axis info
        text6_left = f"Left Y axis: EEI = {y_Emin:.1f} ... {y_Emax:.1f} W/m²"
        ax.text(-0.12, tr5y, text6_left, color=c42, fontname="Arial", fontsize=trs,
                transform=ax.transAxes)
        
        # Right Y-axis info (Temperature)
        text6_right = f"Right Y axis: Temperature = {y_Tmin:.1f} ... {y_Tmax:.1f} °C"
        ax.text(0.42, tr5y, text6_right, color="red", fontname="Arial", fontsize=trs,
                transform=ax.transAxes)
    
    elif yl_mode == 2:  # CO2 mode
        text6_left = f"CO₂: {y_min} ... {y_max} ppm"
        ax.text(-0.12, tr6y, text6_left, color="blue", fontname="Arial", fontsize=trs,
                transform=ax.transAxes)
        
        text6_right = f"Temperature: {y_Tmin} ... {y_Tmax} °C"
        ax.text(0.42, tr6y, text6_right, color="red", fontname="Arial", fontsize=trs,
                transform=ax.transAxes)
    
    elif yl_mode == 7:  # Temperature mode
        text6_left = f"Temperature: {y_Tmin} ... {y_Tmax} °C"
        ax.text(-0.12, tr6y, text6_left, color="red", fontname="Arial", fontsize=trs,
                transform=ax.transAxes)
    
    # Add parameter line (second line at bottom)
    text_params = f"Parameter code: {header_parameter}"
    ax.text(-0.12, tr6y - 0.07, text_params, color="black", fontname="Arial", fontsize=12,
            transform=ax.transAxes)