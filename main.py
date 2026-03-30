# main.py
# part 1 configure 
v = "5b17" #  # 62 TOA_Shortwave_Flux_-_All-Sky_March
#  bug 44  part44_ceres_eei is local main line 116
# CERES_EBAF-TOA_Ed4.2.1_TOA_Shortwave_Flux_-_All-Sky_March-2000toJanuary-2026.txt
# 
# ok horizontal 1.8°C line is T value

# part 2.2 plot CO2 Mauna Loa
# part 2.3 plot23_Glen_CO2 
# part 2.5 plot25_long_CO2  -800 000 years ppm CO2 file
#
# part 3.4 plot34_CO2_emission summed
#
# part 4 EEI CERES data
# part41_ceres_eei = 3 # print EEI 12 month running mean. Info in line 3 below the plot
# part42_ceres_eei = 4 # print EEI 48 month running mean. Info in line 4 below the plot
# part44_ceres_eei = 11 #  print EEI 77 month running mean. Info in line 5 below the plot
#
# part 5.2 plot52_delta_CO2_red_bars
# part 5.3 plot53_CO2_orange2025
# part 5.4 plot54_Glen_delta_on
# part 5.5 plot55_population_on human earth population 
#
# play_61_CERES = 12     # 12 CERES EEI 12 month like part41_ceres_eei 
#
# part 71 plot quadratic temperature with right y axis
# part 72 plot temperature ECS = 8°C with right y axis
# part 73 plot temperature ECS = 4.5°C with right y axis
# part 74 plot Hansen GIS temperature 1880 2027
# part 75      Hansen 2015 .41°C linear fit
# part 76  my  T 
# part 77 deepseek.com 
#
# part 8 print headline, axis numbers. around figue
# 8.2 print the headline above the plot
# 8.3 print the left y axis 
# 8.4 
# 8.5 configure the right y axis legend  
# 8.6 print the vertical lines CO2=constant
# 8.7 print the right y axis
# 8.8 print the x axis 
# 8.9 print the horizontal lines year 2026

# yl_mode = 2 ppm CO2 y axis left mode
# yl_mode = 3 Gt CO2 y axis left mode
# yl_mode = 4 EEI in W/m2 y axis left mode
# yl_mode = 5 delta ppm CO2 y axis left mode
# yl_mode = 7 Temperature in °C y axis left mode

# part 9 print line 1 to 5 below the figure 

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
import sys

# Import modules
from config import *
from data_processing import *
from plotting import *
from data_processing import *
from text_annotations import *

from config import play_61_CERES
from config import play_62_CERES
# bug from config import part44_ceres_eei

def get_active_temperature_axis(ax1):
    """Find which temperature axis is active"""
    if plot71_temperature > 0:
        return ax1.twinx()
    elif plot72_AESS_T > 0:
        return ax1.twinx()
    elif plot73_ECS_T > 0:
        return ax1.twinx()
    elif plot74_GIS_T > 0:
        return ax1.twinx()
    elif linear_41_75 > 0:
        return ax1.twinx()
    return None



def process_ceres_data():
    """Process CERES data based on configuration"""
    if part41_ceres_eei > 10:
        df41a = convert_ceres_to_csv('csv/csv41/csv41a_in_CERES.txt', 
                                      'work/c41b_ceres.csv')
    # run1 part41_ceres_eei = 12 c41d12_ceres
    # run2 part41_ceres_eei = 48 c41d48_ceres
    # run3 part41_ceres_eei = 50 c41d50_ceres
    if part41_ceres_eei == 12:
        df_with_12avg = create_running_average('work/c41b_ceres.csv', 
                                               'work/c41d12_ceres.csv',
                                               window_months=12)
    
    elif part41_ceres_eei == 48:
        df_with_48avg = create_running_average('work/c41b_ceres.csv', 
                                               'work/c41d48_ceres.csv',
                                               window_months=48)
    
    elif part41_ceres_eei == 50:
        df_with_48avg = create_running_average('work/c41b_ceres.csv', 
                                               'work/c41d50_ceres.csv',
                                               window_months=48, center=False)
    


    # Process part44_ceres_eei
    if print_debug > 19:
        print(f"main_115: local variable 44.3 ={part44_ceres_eei}")

        # bug redifine part44_ceres_eei as local variable 
        part44_ceres_eei = 11 # UnboundLocalError: cannot access local variable 'part44_ceres_eei

        out = f"csv/csv44/csv44d_EEI_{part44_ceres_eei}_month.csv"
        if print_debug > 9:
           print(f"main_120: local variable 44.4 ={part44_ceres_eei}")
        # /Dokumente/Python/5_CO2_EEI_T/read_csv/2016_01_EEI_CERES_TOA Net Flux.txt
        df44 = convert_ceres_to_csv('read_csv/2016_01_EEI_CERES_TOA Net Flux.txt', 
                                    'work/c44b_ceres.csv')
        if print_debug > 9:
           print(f"main_125: created c44b_ceres.csv 44.5 ={part44_ceres_eei}")
        if part44_ceres_eei % 2 == 0:
            use_center = True
            min_periods = part44_ceres_eei // 2 # deepseak
            # min_periods = part44_ceres_eei 
            avg_type = "CENTERED"
            if print_debug > 9:
               print(f"main_132: centered: 44.5 ={part44_ceres_eei}")
        else: # 47 make trailing 48 month runnin average
            use_center = False
            min_periods = part44_ceres_eei
            avg_type = "TRAILING"
            part44_ceres_eei = part44_ceres_eei + 1
            if print_debug > 9:
               print(f"main_139: trailing: 44.6 ={part44_ceres_eei}")
        df_with_avg = create_running_average('work/c44b_ceres.csv', 
                                            "work/c44d_ceres.csv",
                                            window_months=part44_ceres_eei,
                                            min_periods=min_periods,
                                            center=use_center,
                                            column_name='EEI')
        
        if print_debug > 9:
           print(f"main_148: {avg_type} average for {part44_ceres_eei}-month window 44.7")
        if print_debug > 9:
               print(f"main_150: created c44d_ceres.csv 44.7 ={part44_ceres_eei}")
    if play_61_CERES > 1: # part 6 
       df61b = convert_ceres_to_csv('read_csv/2016_01_EEI_CERES.txt', 
                                      'work/c61b_ceres.csv')
       if print_debug > 9:
          print(f"main_156: create work/c61b_ceres.csv  61.b ={play_61_CERES}")
       
       window_months=play_61_CERES
       min_periods=12
       use_center=False
       keep_original=True,
       df61c = create_running_average( 'work/c61b_ceres.csv', 
                                          'work/c61gut_ceres.csv',
                                            window_months=play_61_CERES,
                                            min_periods=12,
                                            center=use_center,
                                            column_name='EEI')

       if print_debug > 9:
          print(f"main_170: create work/c61gut_ceres.csv  61.gut ={play_61_CERES}")


       
# CERES_EBAF-TOA_Ed4.2.1_TOA_Shortwave_Flux_-_All-Sky_March-2000toJanuary-2026.txt
# 2016_01_TOA_Shortwave_Flux_-AllSky.txt
if play_62_CERES > 1: # part 6 
       df62b = convert_ceres_to_csv('read_csv/2016_01_TOA_Shortwave_Flux_-AllSky.txt', 
                                      'work/c62b_ceres.csv')
       if print_debug > 9:
          print(f"main_179: create work/c62b_ceres.csv  62.b ={play_62_CERES}")
       
       window_months=play_62_CERES
       min_periods=12
       use_center=False
       keep_original=True,
       df61c = create_running_average( 'work/c62b_ceres.csv', 
                                          'work/c62d_ceres.csv',
                                            window_months=play_61_CERES,
                                            min_periods=12,
                                            center=use_center,
                                            column_name='EEI')

       if print_debug > 9:
          print(f"main_193: create work/c62d_ceres.csv  62.gut ={play_61_CERES}")






def create_temperature_plots(ax1):
    """Create temperature plots based on configuration"""
    temp_axes = {}
    
    if plot71_temperature > 0:
        years = np.arange(x_anf, x_end + 1)
        values = T_model71(years)
        ax = ax1.twinx()
        ax.plot(years, values, '--', color=c71, linewidth=3)
        temp_axes['71'] = configure_right_y_axis(ax, y_Tmin, y_Tmax, c71, 
                                                   "Δ Temperature in °C 71")
    
    if plot72_AESS_T > 0:
        years = np.arange(x_anf, x_end + 1)
        values = T_model72(years)
        ax = ax1.twinx()
        ax.plot(years, values, '--', color=c72, linewidth=3)
        temp_axes['72'] = configure_right_y_axis(ax, y_Tmin, y_Tmax, c72, 
                                                   "Δ Temperature calc72 in °C")
    
    if plot73_ECS_T > 0:
        years = np.arange(x_anf, x_end + 1)
        values = T_model73(years)
        ax = ax1.twinx()
        ax.plot(years, values, '--', color=c73, linewidth=3)
        temp_axes['73'] = configure_right_y_axis(ax, y_Tmin, y_Tmax, c73, 
                                                   "Δ Temperature in °C (ECS = 4.5°C)")
    
    if plot74_GIS_T > 0:
        df = pd.read_csv("csv/csv7/csv_74_gis_temperature.csv")
        ax = ax1.twinx()
        ax.plot(df["Year74"], df["GIS_temp"] + 0.3, '-', color=c74, linewidth=3)
        temp_axes['74'] = configure_right_y_axis(ax, y_Tmin, y_Tmax, c74, 
                                                   "Δ GIS Temperature in °C 74")
    
    if linear_41_75 > 0:
        df = pd.read_csv("csv/csv7/csv_75_hansen.csv")
        ax = ax1.twinx()
        ax.plot(df["Year75"], df["temp"] + 0.1, '--', color=c75, linewidth=2)
        temp_axes['75'] = configure_right_y_axis(ax, y_Tmin, y_Tmax, c75, 
                                                   "Hansen linear fit 75")
    
    return temp_axes


def hide_other_right_axes(ax1, keep_axis):
    """Hide all right y-axes except the one we want to keep"""
    # Get all axes in the figure
    all_axes = ax1.get_figure().get_axes()
    
    for ax in all_axes:
        if ax != ax1 and ax != keep_axis:
            # Check if this is a right y-axis (has a spine on the right)
            if ax.spines['right'].get_visible():
                ax.spines["right"].set_visible(False)
                ax.tick_params(right=False, labelright=False)





def load_plot_data():
    """Load all data needed for plotting"""
    data = {}
    
    # Load CO2 data if needed
    if plot22_CO2_Mauna_Loa > 0:
        data['co2'] = load_co2_mauna_loa(x_anf, x_end)
    
    # Load GIS temperature data
    if plot74_GIS_T > 0:
        data['gis_temp'] = load_gis_temperature()
    
    # Load CERES data
    if part41_ceres_eei > 0:
        data['ceres_12'] = pd.read_csv("csv/csv44/_plot_41_41g12.csv")
    
    if part42_ceres_eei > 0:
        data['ceres_48'] = pd.read_csv("csv/csv44/_plot_42_41g50.csv")
    
    if part43_ceres_eei > 0: # 43.2 read1
        data['ceres_43'] = pd.read_csv("read_csv/a44d_ceres_12month_EEI.csv")
        if print_debug > 19:
           print(f"main_236: 43.2 read ={part43_ceres_eei}")
           #data['ceres_43'] = pd.read_csv("csv/csv44/_plot_41_41g12.csv")

    if part44_ceres_eei > 0:
        if print_debug > 19:
           print(f"main_253: custom-read 44.7 ={part44_ceres_eei}")
        data['ceres_custom'] = pd.read_csv("work/c44d_ceres.csv")
        # data['ceres_custom'] = pd.read_csv("csv/csv44/csv44d_out.csv")
        # data['ceres_custom'] = pd.read_csv("work/c44d_ceres.csv")

    if play_61_CERES > 0: # 61.9 read
        data['ceres_61'] = pd.read_csv("work/c61gut_ceres.csv")
        if print_debug > 9:
           print(f"main_287: 61.9 read ={play_61_CERES}")
           
    return data


def create_plots(ax1, data):
    """Create all plots based on configuration"""
    # Plot CERES data
    if part41_ceres_eei > 0 and 'ceres_12' in data:
        ax41 = ax1.twinx()
        ax41.plot(data['ceres_12']["year41"], data['ceres_12']["EEI"], '-', 
                  label="EEI K41", color=c41, linewidth=2)
        ax41.tick_params(axis="y", labelcolor=c41)
        ax41.set_ylim(y_Emin, y_Emax)
    
    if part42_ceres_eei > 0 and 'ceres_48' in data:
        ax42 = ax1.twinx()
        ax42.plot(data['ceres_48']["year41"], data['ceres_48']["EEI"], '-', 
                  label="EEI K42", color=c42, linewidth=2)
        ax42.tick_params(axis="y", labelcolor=c42)
        ax42.set_ylim(y_Emin, y_Emax)
    

    if part43_ceres_eei > 0 and 'ceres_43' in data:
        ax43 = ax1.twinx()
        ax43.plot(data['ceres_43']["decimal_year"], data['ceres_43']["EEI"], '-', 
                  label="EEI K41", color=c43, linewidth=2)
        ax43.tick_params(axis="y", labelcolor=c43)
        ax43.set_ylim(y_Emin, y_Emax)
        if print_debug > 19:
           print(f"main_311: ax43 43.4 ={part43_ceres_eei}")
 
    if part44_ceres_eei > 0 and 'ceres_custom' in data:
        if print_debug > 19:
           print(f"main_291: ax44 44.7 ={part44_ceres_eei}")

        ax44 = ax1.twinx()
        ax44.plot(data['ceres_custom']["decimal_year"], data['ceres_custom']["EEI"], '-', 
                  label="EEI K44", color=c44, linewidth=2)
        ax44.tick_params(axis="y", labelcolor=c44)
        ax44.set_ylim(y_Emin, y_Emax)
    
    if play_61_CERES > 0 and 'ceres_61' in data:
        ax61 = ax1.twinx()
        ax61.plot(data['ceres_61']["decimal_year"], data['ceres_61']["EEI"], '-', 
                  label="EEI K61", color=c61, linewidth=2)
        ax61.tick_params(axis="y", labelcolor=c61)
        ax61.set_ylim(y_Emin, y_Emax)
        if print_debug > 9:
           print(f"main_330: ax61 43.8 ={play_61_CERES}")

    # Plot GIS temperature
    if plot74_GIS_T > 0 and 'gis_temp' in data:
        ax74 = ax1.twinx()
        ax74.plot(data['gis_temp']["Year74"], data['gis_temp']["GIS_temp"]+0.3, '-', 
                  label="T GIS K74", color=c74, linewidth=3)
        ax74.tick_params(axis="y", labelcolor=c74)
        ax74.set_ylim(y_Tmin, y_Tmax)

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
    if part43_ceres_eei == 2:
        add_legend_line(fig, lr2x1, lr2x2, lr2y, c43)
        add_text_row(ax1, tr2x, tr2y, 
                    "Earth Energy Imbalance W/m² moving average 12 month  43", 
                    c43, trs)
    elif plot74_GIS_T == 2:
        add_legend_line(fig, lr2x1, lr2x2, lr2y, c74)
        add_text_row(ax1, tr2x, tr2y, 
                    "Temperature in °C giss.nasa.gov Hansen+0.3°C   74", 
                    c74, trs)
    # print line 3 below the plot
    if part41_ceres_eei == 3:
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
    elif plot74_GIS_T == 3:
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
        p61_text = f"Earth Energy Imbalance {play_61_CERES}-month moving average 61 - main - line 350."
        add_text_row(ax1, tr2x, tr6y, p61_text, c61, trs) 


def save_png(fig, header_parameter):
    """Save the plot if configured"""
    if print_debug > 19:
           print(f"main_358 save png as file {fig}")
    # print(f"main_save_plot_389: {fig}")
    if parameter84_save_png > 0:
        filename = os.path.basename(__file__)[:parameter84_save_png]
        filename = f"{filename}_{header_parameter}{x_end}"
        filename = "figure_5_EEI"
        path2 = f"/Users/thomasboettcher/Desktop/{filename}"
        fig.savefig(path2, dpi=300, bbox_inches="tight")
        
        # https://github.com/Boettcher1960/5_CO2_EEI_T
        path = "/Users/thomasboettcher/documents/Python/5_CO2_EEI_T/5_CO2_EEI_T.png"
        fig.savefig(path, dpi=300, bbox_inches="tight")
        if print_debug > 9:
           print(f"main_382 saved png as file {path}")

# main program 
def main():
    """Main execution function"""
    # Create header parameter string
    header_parameter = (f"{plot22_CO2_Mauna_Loa}{plot23_Glen_CO2}{plot25_long_CO2}"
                       f"{plot34_CO2_emission} 4({part41_ceres_eei}{part42_ceres_eei}"
                       f"{part43_ceres_eei}{part44_ceres_eei}) 5({plot52_delta_CO2_red_bars}"
                       f"{plot53_CO2_orange2025}{plot54_Glen_delta_on}{plot55_population_on})"
                       f" 6({play_61_CERES}) "
                       f"7({plot71_temperature}{plot72_AESS_T}{plot73_ECS_T}{plot74_GIS_T}"
                       f"{linear_41_75}{plot76_my_T})")
    
    # Process CERES data
    process_ceres_data()
    
    # Setup figure
    fig, ax1 = setup_figure(scale_mode)
    
    # Load data
    data = load_plot_data()
    
    # 8.3 print the left y axis  # Configure axes plotting.py 
    ax1 = configure_axes(ax1, x_anf, x_end, y_min, y_max, y_Emin, y_Emax,
                         y_Tmin, y_Tmax, yl_mode, c22, c42, c74)
    
    # 8.7 print the right y axis
    label  ="Temperature in °C"
    axT = right_T_y_axis(ax1, y_Tmin, y_Tmax, c74, label)
    # axT is the temperature scaling
    # label  ="EEI in W line 449"
    # bug ax6 = right_EEI_y_axis(ax1, y_Emin, y_Emax, c74, label)
    # main_484: Axis 2: yaxis side = right, label = 'EEI in W line 449'
    # Create plots
    create_plots(ax1, data)
    
    # Add grid lines
    add_grid_lines(ax1)
    
    # Add vertical bands
    add_vertical_bands(ax1, C280)
    
    # Add temperature band if temperature plots are active
    if plot71_temperature > 0 or plot72_AESS_T > 0 or plot73_ECS_T > 0 or plot74_GIS_T > 0:
        if print_debug > 13:
            print(f"main_420: bug6 temperature band on left y axis only plot74_GIS_T={plot74_GIS_T} {'='*5}")
        add_temperature_band(ax1) # 1.5 to 2 on left y axis
        # Find the active temperature axis
        for ax in [ax1] + ax1.get_figure().get_axes():
            if hasattr(ax, 'get_ylabel') and 'Temperature' in ax.get_ylabel():
                add_temperature_band(ax)
                print(f"main_469{'='*1} temperature_band")
                break
    
    # Add text annotations
    add_text_annotations(fig, ax1, header_parameter)
    
    # Add x-axis label
    ax1.set_xlabel("year", fontsize=20)
    plt.xticks(fontsize=20)
    ax1.tick_params(axis="x", labelcolor="black", labelsize=20)
    
    # debug 
    print("main_480: All axes in figure:")
    for i, ax in enumerate(plt.gcf().get_axes()):
        # Get the y-axis label if it exists
        ylabel = ax.get_ylabel()
        print(f"main_484: Axis {i}: yaxis side = {ax.yaxis.get_ticks_position()}, label = '{ylabel}'")
    # main_484: Axis 0: yaxis side = left, label = 'Earth Energy Imbalance in W/m²'
    # main_484: Axis 1: yaxis side = right, label = 'Temperature in °C '
    # main_484: Axis 2: yaxis side = right, label = ''
    axes = plt.gcf().get_axes()
    # Keep axes 0, 1, 2, hide all others
    for i in range(2, len(axes)): # remove Axis 3, 4
        axes[i].yaxis.set_ticks([])  # Remove tick numbers
        axes[i].set_yticklabels([])  # Remove tick labels
        axes[i].spines['right'].set_visible(False)
        axes[i].set_ylabel('') # Remove any label
   
    # Adjust layout
    fig.tight_layout()
    plt.tight_layout()
    
    # Show plot
    plt.show()
    
    # Save plot
    save_png(fig, header_parameter)
    
    # Close figure
    plt.close(fig)

if __name__ == "__main__":
    main()


