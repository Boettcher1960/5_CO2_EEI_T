# text_annotations.py
# version 5b48
import os
import sys
from matplotlib.lines import Line2D

# Import modules
from config import *
from data_processing import *
from plotting import *
from data_processing import *
from main import v



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


# 9.2 print line 2 blue Mauna Loa data below the figure
# 9.2.2 print line 22 below the plot explainations
# 9.3 print line 3 below the plot explainations
# 9.4 print line 4 below the plot explainations
# 9.5.2 print line 5 plot55_population_on marker="s"
def add_text_annotations(fig, ax1, header_parameter):
    """Add all text annotations to the plot"""
    filename = os.path.basename(sys.argv[0])
    
    # Add header
    add_header(ax1, x_anf, x_end, yl_mode)
    
    # Add bottom text
    add_bottom_text(fig, ax1, filename, v, header_parameter, tr1y)
    # def add_bottom_text(fig, ax1, filename, v, header_parameter, tr1y):
 

    # add_text_row(ax1, tr2x, tr5y, "--row5---main338--- tr5y", c43, trs)
    add_text_row(ax1, 0.9, tr6y, 
                    "-main330", 
                    c43, trs)

    # Add legend lines for active plots 
    # part 9.2 print line 2 below the plot main_350
    if plot22_CO2_Mauna_Loa == 2: # 22.5 legend
        add_legend_line(fig, lr2x1, lr2x2, lr2y, c22)
        add_text_row(ax1, tr2x, tr2y, 
                    blue22_text, 
                    c22, trs)
    elif part43_ceres_eei == 2:
        add_legend_line(fig, lr2x1, lr2x2, lr2y, c43)
        add_text_row(ax1, tr2x, tr2y, 
                    "Earth Energy Imbalance W/m² moving average 12 month  43", 
                    c43, trs)
    elif plot74_GIS_T == 2: # 74.5 legend
        add_legend_line(fig, lr2x1, lr2x2, lr2y, c74)
        add_text_row(ax1, tr2x, tr2y, 
                    "Temperature in °C giss.nasa.gov Hansen+0.3°C   74", 
                    c74, trs)
    # print line 3 below the plot
    if plot22_CO2_Mauna_Loa == 3:
        add_legend_line(fig, lr2x1, lr2x2, lr3y, c41)
        add_text_row(ax1, tr2x, tr3y, 
                    "plot22_CO2_Mauna_Loa   22", 
                    c41, trs)
    elif part41_ceres_eei == 3:
        add_legend_line(fig, lr2x1, lr2x2, lr3y, c41)
        add_text_row(ax1, tr2x, tr3y, 
                    "Earth Energy Imbalance W/m² moving average 12 month 41", 
                    c41, trs)
    elif part42_ceres_eei == 3:
        add_legend_line(fig, lr2x1, lr2x2, lr3y, c42)
        add_text_row(ax1, tr2x, tr3y, 
                    "Earth Energy Imbalance W/m² moving average 48 month  42", 
                    c42, trs)
    elif part43_ceres_eei == 3:
        add_legend_line(fig, lr2x1, lr2x2, lr3y, c43)
        add_text_row(ax1, tr2x, tr3y, 
                    "Earth Energy Imbalance W/m² moving average 12 month  43", 
                    c43, trs)
    elif plot74_GIS_T == 3: # 74.6
        add_legend_line(fig, lr2x1, lr2x2, lr3y, c74)
        add_text_row(ax1, tr2x, tr3y, 
                    "Temperature in °C giss.nasa.gov Hansen+0.3°C   74", 
                    c74, trs)

    if part42_ceres_eei == 4:
        add_legend_line(fig, lr2x1, lr2x2, lr4y, c42)
        add_text_row(ax1, tr2x, tr4y, 
                    "Earth Energy Imbalance W/m² moving average 48 month  42", 
                    c42, trs)
    
    # in row 5 display part44_ceres_eei
    if part44_ceres_eei > 0:
        add_legend_line(fig, lr2x1, lr2x2, lr5y, c44)
        p44_text = f"Earth Energy Imbalance {part44_ceres_eei}-month moving average 44"
        add_text_row(ax1, tr2x, tr5y, p44_text, c44, trs) 

    # in row 6 display play_61_CERES
    if play_61_CERES > 0:
        add_legend_line(fig, lr2x1, lr2x2, lr6y, c61)
        p61_text = f"Earth Energy Imbalance {play_61_CERES}-month moving average 61 - main - line 438."
        add_text_row(ax1, tr2x, tr6y, p61_text, c61, trs) 
    # in row 5 display play_62_CERES
    if play_62_CERES > 0:
        add_legend_line(fig, lr2x1, lr2x2, lr5y, c62)
        p62_text = f"TOA Shortwave Flux - All-Sky {play_62_CERES}-month moving average 62 - main - line 443."
        add_text_row(ax1, tr2x, tr5y, p62_text, c62, trs) 



# 9.6 print line 6 below the plot explainations

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