# text_annotations.py
# version 5b85
# text_1_print_line(fig, ax1, filename, v, header_parameter, tr1y): line 15
# text_2_print_head_line(ax1, x_anf, x_end, yl_mode): line 30
# text_3_add_legend_line(fig, x1, x2, y, color, linewidth=2, marker="o", markersize=5): line48
# text_9_print_7_lines line 117

import os
import sys
from matplotlib.lines import Line2D

# Import modules
from config import *
from data_processing import *
from plotting import *
from data_processing import *
from main import v

# text_1_print_line(fig, ax1, filename, v, header_parameter, tr1y): line 15
def text_1_print_line(fig, ax1, filename, v, header_parameter, tr1y):
    """Add text below the plot (line 1)"""
    text_below = (f"Figure from  "
                  f"https://github.com/Boettcher1960/5_CO2_EEI_T      "
                  f" {filename} version {v} ")
    
    # f"https://github.com/Boettcher1960/co2_python       Parameter {header_parameter}")
    ax1.text(-0.1, tr1y, text_below, color="black", fontname="Arial", fontsize=16,
            transform=ax1.transAxes)



# text_2_print_head_line(ax1, x_anf, x_end, yl_mode): line 30
def text_2_print_head_line(ax1, x_anf, x_end, yl_mode):
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

# text_3_add_legend_line(fig, x1, x2, y, color, linewidth=2, marker="o", markersize=5): line48
def text_3_add_legend_line(fig, x1, x2, y, color, linewidth=2, marker="o", markersize=5):
    """Add a legend line to the figure"""
    line = Line2D([x1, x2], [y, y], transform=fig.transFigure,
                  marker=marker, markersize=markersize, color=color, linewidth=linewidth)
    fig.add_artist(line)
    return line

def text_4_add_text(ax, x, y, text, color, fontsize=20):
    """Add a text row below the plot"""
    ax.text(x, y, text, color=color, fontname="Arial", fontsize=fontsize,
           transform=ax.transAxes)

text_plot23_Glen="calculated CO2 dashed blue line = 0.0132251t² - 51.0337t + 49,536 ppm 23"





# 9.6 not called print line 6 below the plot explainations
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
    else:
        text6_left = f"Left axis: EEI = {y_Emin:.1f} ... {y_Emax:.1f} W/m²"
        ax.text(-0.12, tr5y, text6_left, color=c42, fontname="Arial", fontsize=trs,
                transform=ax.transAxes)

    # Add parameter line (second line at bottom)
    text_params = f"Parameter code: {header_parameter}"
    ax.text(-0.12, tr6y - 0.07, text_params, color="black", fontname="Arial", fontsize=12,
            transform=ax.transAxes)
    # end 9.6 not called print line 6 below the plot explainations





# text_9_print_7_lines line 117
# 9.2 print line 2 blue Mauna Loa data below the figure
# 9.2.2 print line 22 below the plot explainations
# 9.3 print line 3 below the plot explainations
# 9.4 print line 4 below the plot explainations
# 9.5.2 print line 5 plot55_population_on marker="s"
def text_9_print_7_lines(fig, ax1, header_parameter):
    """Add all text annotations to the plot"""
    filename = os.path.basename(sys.argv[0])
    
    # Add header
    text_2_print_head_line(ax1, x_anf, x_end, yl_mode)
    
    # Add bottom text
    text_1_print_line(fig, ax1, filename, v, header_parameter, tr1y)
    # def text_1_print_line(fig, ax1, filename, v, header_parameter, tr1y):
 

    # text_4_add_text(ax1, tr2x, tr5y, "--row5---main338--- tr5y", c43, trs)
    text_4_add_text(ax1, 0.9, tr6y, 
                    "-main330", 
                    c43, 10)

    # Add legend lines for active plots 
    # part 9.2 print line 2 below the plot main_350
    if plot22_CO2_Mauna_Loa == 2: # 22.5.2 legend row 2
        text_3_add_legend_line(fig, lr2x1, lr2x2, lr2y, c22)
        text_4_add_text(ax1, tr2x, tr2y, 
                    blue22_text, 
                    c22, trs)
    elif plot25_long_CO2 == 2: # 25.9
       line25 = Line2D([lr2x1, lr2x2], [lr2y, lr2y], # y from 0 to 1
       transform=fig.transFigure,
       marker="o", markersize=3, color=c25, linewidth=2)
       fig.add_artist(line25)
       plt.text(tr2x, tr2y, blue25_text, color=c25, fontname="Arial", fontsize=trs,
       transform=plt.gca().transAxes)
       fig.add_artist(line25)
    elif plot31_CO2_emission == 2: # 31.8
       print("text_094: plot31_CO2_emission = ", plot31_CO2_emission,  " 31.8 ") # 31.8
       line31 = Line2D([lr2x1, lr2x2], [lr2y, lr2y], # y from 0 to 1
       transform=fig.transFigure,
       marker="o", markersize=3, color=c31, linewidth=2)
       fig.add_artist(line31)
       plt.text(tr2x, tr2y, print31_text, color=c31, fontname="Arial", fontsize=trs,
       transform=plt.gca().transAxes)
       fig.add_artist(line31)
    elif part41_ceres_eei == 2:
        text_3_add_legend_line(fig, lr2x1, lr2x2, lr2y, c41)
        text_4_add_text(ax1, tr2x, tr2y, 
                    "Earth Energy Imbalance W/m² moving average 12 month  41", 
                    c41, trs)
 


    elif part43_ceres_eei == 2:
        text_3_add_legend_line(fig, lr2x1, lr2x2, lr2y, c43)
        text_4_add_text(ax1, tr2x, tr2y, 
                    "Earth Energy Imbalance W/m² moving average 12 month  43", 
                    c43, trs)
    elif plot74_GIS_T == 2: # 74.5 legend
        text_3_add_legend_line(fig, lr2x1, lr2x2, lr2y, c74)
        text_4_add_text(ax1, tr2x, tr2y, 
                    "Temperature in °C giss.nasa.gov Hansen+0.3°C   74", 
                    c74, trs)
    
    # print line 3 below the plot
    if plot22_CO2_Mauna_Loa == 3: # 22.5.3 legend row 3
        text_3_add_legend_line(fig, lr2x1, lr2x2, lr3y, c22)
        text_4_add_text(ax1, tr2x, tr3y, 
                    blue22_text, 
                    c22, trs)
    elif plot23_Glen_CO2 == 3: # 23.5.4 legend row 4
        text_3_add_legend_line(fig, lr2x1, lr2x2, lr3y, c23)
        text_4_add_text(ax1, tr2x, tr3y, 
                    text_plot23_Glen, 
                    c23, trs)

    elif plot25_long_CO2 == 3: # 25.9
       line25 = Line2D([lr2x1, lr2x2], [lr3y, lr3y], # y from 0 to 1
       transform=fig.transFigure,
       marker="o", markersize=3, color=c25, linewidth=2)
       fig.add_artist(line25)
       plt.text(tr2x, tr3y, blue25_text, color=c25, fontname="Arial", fontsize=trs,
       transform=plt.gca().transAxes)
       fig.add_artist(line25)


    elif part41_ceres_eei == 3:
        text_3_add_legend_line(fig, lr2x1, lr2x2, lr3y, c41)
        text_4_add_text(ax1, tr2x, tr3y, 
                    "Earth Energy Imbalance W/m² moving average 12 month 41", 
                    c41, trs)
    elif part42_ceres_eei == 3:
        text_3_add_legend_line(fig, lr2x1, lr2x2, lr3y, c42)
        text_4_add_text(ax1, tr2x, tr3y, 
                    "Earth Energy Imbalance W/m² moving average 48 month  42", 
                    c42, trs)
    elif part43_ceres_eei == 3:
        text_3_add_legend_line(fig, lr2x1, lr2x2, lr3y, c43)
        text_4_add_text(ax1, tr2x, tr3y, 
                    "Earth Energy Imbalance W/m² moving average 12 month  43", 
                    c43, trs)
    elif plot74_GIS_T == 3: # 74.6
        text_3_add_legend_line(fig, lr2x1, lr2x2, lr3y, c74)
        text_4_add_text(ax1, tr2x, tr3y, 
                    "Temperature in °C giss.nasa.gov Hansen+0.3°C   74", 
                    c74, trs)

    # print line 4 below the plot
    print("text_218: plot34_CO2_emission = ", plot34_CO2_emission) # 34.8
    if plot22_CO2_Mauna_Loa == 4: # 22.5.4 legend row 4
        text_3_add_legend_line(fig, lr2x1, lr2x2, lr4y, c22)
        text_4_add_text(ax1, tr2x, tr4y, 
                    blue22_text, 
                    c22, trs)
    elif plot23_Glen_CO2 == 4: # 23.5.4 legend row 4
        text_3_add_legend_line(fig, lr2x1, lr2x2, lr4y, c23)
        text_4_add_text(ax1, tr2x, tr4y, 
                    text_plot23_Glen, 
                    c23, trs)
    elif plot31_CO2_emission == 4: # 31.8
       print("text_230: plot31_CO2_emission = ", plot31_CO2_emission,  " 31.8 ") # 31.8
       line31 = Line2D([lr2x1, lr2x2], [lr4y, lr4y], # y from 0 to 1
       transform=fig.transFigure,
       marker="o", markersize=3, color=c31, linewidth=2)
       fig.add_artist(line31)
       plt.text(tr2x, tr4y, print31_text, color=c31, fontname="Arial", fontsize=trs,
       transform=plt.gca().transAxes)
       fig.add_artist(line31)

    elif plot34_CO2_emission == 4: # 34.4
       print("text_149: plot34_CO2_emission  = ", plot34_CO2_emission, " mode ", plot34_CO2_emission_mode, " 34") # 34.9
       line34 = Line2D([lr2x1, lr2x2], [lr4y, lr4y], # y from 0 to 1
       transform=fig.transFigure,
       marker="o", markersize=3, color=c34, linewidth=2)
       fig.add_artist(line34)
       plt.text(tr2x, tr4y, print34_text, color=c34, fontname="Arial", fontsize=trs,
       transform=plt.gca().transAxes)
       fig.add_artist(line34)
    elif part42_ceres_eei == 4:
        text_3_add_legend_line(fig, lr2x1, lr2x2, lr4y, c42)
        text_4_add_text(ax1, tr2x, tr4y, 
                    "Earth Energy Imbalance W/m² moving average 48 month  42", 
                    c42, trs)
    
    if plot23_Glen_CO2 == 5: # 23.5.5 legend row 5
        text_3_add_legend_line(fig, lr2x1, lr2x2, lr5y, c23)
        text_4_add_text(ax1, tr2x, tr5y, 
                    text_plot23_Glen, 
                    c23, trs)



    # in row 5 display part44_ceres_eei
    if part44_ceres_eei > 0:
        text_3_add_legend_line(fig, lr2x1, lr2x2, lr5y, c44)
        p44_text = f"Earth Energy Imbalance {part44_ceres_eei}-month moving average 44"
        text_4_add_text(ax1, tr2x, tr5y, p44_text, c44, trs) 

    # in row 6 display play_61_CERES
    if play_61_CERES > 0:
        text_3_add_legend_line(fig, lr2x1, lr2x2, lr6y, c61)
        p61_text = f"Earth Energy Imbalance {play_61_CERES}-month moving average 61 - main - line 438."
        text_4_add_text(ax1, tr2x, tr6y, p61_text, c61, trs) 
    # in row 5 display play_62_CERES
    elif play_62_CERES > 0:
        text_3_add_legend_line(fig, lr2x1, lr2x2, lr5y, c62)
        p62_text = f"TOA Shortwave Flux - All-Sky {play_62_CERES}-month moving average 62 - main - line 443."
        text_4_add_text(ax1, tr2x, tr5y, p62_text, c62, trs) 
    else:
        p62_text = f"Parameter {header_parameter}  Text 192:"
        text_4_add_text(ax1, tr2x, tr6y, p62_text, "black", 16) 
 


