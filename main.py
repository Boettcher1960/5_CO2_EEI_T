# main.py
# part 1 configure 
v = "5E32" # plot42_EEI_48month = 2
# plan txt to csv to png play 64 
# ocean stratification https://bsky.app/profile/thomas-boettcher.bsky.social/post/3mj7zx7fzsc26
# https://drtomharris.substack.com/p/the-great-decoupling-how-ocean-stratification
# http://www.ocean.iap.ac.cn/ftp/images_files/Stratification_global_time_series.txt
#
# https://www.nature.com/articles/s43247-026-03427-w#
# https://bsky.app/profile/thomas-boettcher.bsky.social/post/3miz5mmll3k2z
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
# part 77 T with 2 values
#
# part 8 print headline, axis numbers. around figue
# 8.3 print the left y axis 
# 8.5 configure the right y axis legend  
# 8.6 print the vertical lines CO2=constant
# 8.7 print the right y axis
# 8.8 print the x axis 
# 8.9 print the horizontal lines year 2026
# part 9 print line 1 to 5 below the figure 

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
import sys

# Import modules
from config import *
from plotting import *
from data_processing import *
from text import *
from models import *

#from config import play_62_CERES


if print_debug > 19:
   print("main_057: TOA", y_TOAmin, y_TOAmax, play_62_CERES, part44_ceres_eei)


def process_ceres_data():
    """Process CERES data based on configuration"""
    # Process part44_ceres_eei
    if print_debug > 19:
        print(f"main_115: local variable 44.3 ={part44_ceres_eei}")
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
    if play_61_CERES > 0: # part 6 
       df61b = convert_ceres_to_csv('read_csv/_61_in__2026_02_EEI_CERES.txt', 
                                    'read_csv/_61b_out_in_ceres.csv')
       if print_debug > 9:
          print(f"main_156: create read_csv/_61b_out_in_ceres.csv  61.b ={play_61_CERES}")
       
       window_months=play_61_CERES

       if play_61_CERES > 11:
          min1_periods=12
       else:
          min1_periods=play_61_CERES
       use_center=False
       keep_original=True,
       
       df61c = create_running_average( 'read_csv/_61b_out_in_ceres.csv', 
                                       'read_csv/_61c_out_ceres.csv',
                                            window_months=play_61_CERES,
                                            min_periods=min1_periods,
                                            center=use_center,
                                            column_name='EEI')
        
       if print_debug > 9:
          print(f"main_122: create read_csv/_61c_out_ceres.csv  61.gut ={play_61_CERES}")


       
    # CERES Outgoing Longwave Radiation OLR
    # _62_in__2026_02_Longwave.txt
    if play_62_CERES > 1: # part 6 
       df62b = convert_ceres_to_csv('read_csv/_62_in__2026_02_Longwave.txt', 
                                    'read_csv/_62b_LongWave.csv')
       if print_debug > 9:
          print(f"main_127: create read_csv/_62b_LongWave.csv  62.b ={play_62_CERES}")
       
       window_months=play_62_CERES
       min_periods=12
       use_center=False
       keep_original=True,
       df62c = create_running_average( 'read_csv/_62b_LongWave.csv', 
                                       'read_csv/_62c_LongWave.csv',
                                            window_months=play_62_CERES,
                                            min_periods=12,
                                            center=use_center,
                                            column_name='LongWave')

       df62e = add_62_csv_column( 'read_csv/_62b_LongWave.csv', 
                                  'read_csv/_42_EEI48month_2026_02.csv', 
                                  'read_csv/_62e_LongWave.csv',
                                            window_months=play_62_CERES,
                                            min_periods=12,
                                            center=use_center,
                                            column_name='LongWave')



       if print_debug > 9:
          print(f"main_151: create read_csv/_62e_LongWave.csv 62    ={play_62_CERES}")


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
    if plot22_CO2_Mauna_Loa > 0:  # 22.3 load the mauna loa CO2 data
        data['co2'] = load_co2_mauna_loa(x_anf, x_end)
        if print_debug > 19:
           print(f"main_168: plot22_CO2_Mauna_Loa 22.3 ={plot22_CO2_Mauna_Loa}")
           print(f"main_169: Last 3 CO2 rows: {data['co2'][-3:] if len(data['co2']) >= 3 else data['co2']}")        
    if plot42_EEI_48month > 0: # _plot_42_41g50.csv"
        data['ceres_42'] = pd.read_csv("read_csv/_42_EEI48month_2026_02.csv")
        # 249 bug data['ceres_48'] = pd.read_csv("read_csv/_42_EEI48month_made_by_61c.csv")
    if plot43_eei_12month > 0: # 43.2 read1 _43_EEI12month_made_by_61c.csv a44d_ceres_12month_EEI
        data['ceres_43'] = pd.read_csv("read_csv/_43_EEI12month_2026_02.csv")
        if print_debug > 19:
           print(f"main_176: 43.2 read ={plot43_eei_12month}")
           #data['ceres_43'] = pd.read_csv("csv/csv44/_plot_41_41g12.csv")
    if part44_ceres_eei > 0:
        if print_debug > 19:
           print(f"main_180: custom-read 44.7 ={part44_ceres_eei}")
        data['ceres_custom'] = pd.read_csv("work/c44d_ceres.csv")
    if plot45_OLR > 0: # Outgoing Longwave Radiation OLR
        data['ceres_45'] = pd.read_csv("read_csv/_62e_LongWave.csv")
        if print_debug > 9:
           print(f"main_190: OLR read 45.1 ={plot45_OLR}")



    # part 5.2 plot52_delta_CO2_red_bars
    # part 5.3 plot53_CO2_orange2025
    # part 5.4 plot54_Glen_delta_on
    # part 5.5 plot55_population_on human earth population 
    # -----------------------------
    # part 5.2 plot52_delta_CO2_red_bars
    # 5.2.2 ΔCO₂ berechnen (per pandas) Balken
    # df52["CO2"].diff() Calculates the difference between consecutive CO₂ values
    # -----------------------------
    if plot52_delta_CO2_red_bars > 0: # 52.3
        if print_debug > 9:
           print(f"main_193: plot52_delta_CO2_red_bars # 52.3 ={plot52_delta_CO2_red_bars}")
    if play_61_CERES > 0: # 61.9 read
        data['ceres_61'] = pd.read_csv("read_csv/_61c_out_ceres.csv")
        if print_debug > 9:
           print(f"main_197: 61.9 read ={play_61_CERES}")
    if play_62_CERES > 0: # 62.9 read
        data['ceres_62'] = pd.read_csv("read_csv/_62c_LongWave.csv")
        # data['ceres_62'] = pd.read_csv("work/c62d_ceres.csv")
        if print_debug > 9:
           print(f"main_201: 62.9 read ={play_62_CERES}")    
    # Load GIS temperature data
    if plot74_GIS_T > 0: # 74.3
        data['gis_temp'] = load_gis_temperature()
    return data
    # end load_plot_data():


def save_png(fig, header_parameter):
    """Save the plot if configured"""
    if print_debug > 19:
           print(f"main_213 save png as file {fig}")
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
    header_parameter = (f" "
                       f"2({plot22_CO2_Mauna_Loa}{plot23_Glen_CO2}{plot25_long_CO2}" 
                       f" 3({plot31_CO2_emission}{plot34_CO2_emission} 4({plot42_EEI_48month}"
                       f"{plot43_eei_12month}{plot45_OLR}{plot46_OLR_EEI} 5({plot52_delta_CO2_red_bars}"
                       f"{plot53_CO2_orange2025}{plot54_Glen_delta_on}{plot55_population_on}"
                       f" 6({play_61_CERES}{play_62_CERES}{play_63_CB}"
                       f" 7({plot71_temperature}{plot72_AESS_T}{plot73_ECS_T}{plot74_GIS_T}"
                       f"{linear_41_75}{plot76_my_T}")
    
    if print_debug > 9:
       print("main_237: begin ", header_parameter)


    # Process CERES data
    process_ceres_data()
    
    # Setup figure
    fig, ax1 = setup_figure(scale_mode)
    
    # Load data
    data = load_plot_data()
    
    # 8.3 print the left y axis  # Configure axes plotting.py 
    ax1 = plot_1_axe(ax1)
    
    # call plotting.py line 200 to line 500
    plot_9_create_all_plots(ax1, data)
    
    # Add grid lines
    add_grid_lines(ax1)
    
    # Add vertical bands
    add_vertical_bands(ax1, C280)
    
    # Add temperature band if temperature plots are active # 74.9
    if plot71_temperature > 0 or plot72_AESS_T > 0 or plot73_ECS_T > 0 or plot74_GIS_T > 0:
        if print_debug > 13:
            print(f"main_372: bug6 temperature band on left y axis only plot74_GIS_T={plot74_GIS_T} {'='*5}")
        add_temperature_band(ax1) # 1.5 to 2 on left y axis
        # Find the active temperature axis
        for ax in [ax1] + ax1.get_figure().get_axes():
            if hasattr(ax, 'get_ylabel') and 'Temperature' in ax.get_ylabel():
                add_temperature_band(ax)
                print(f"main_378{'='*1} temperature_band")
                break
    
    # Add text annotations
    text_9_print_7_lines(fig, ax1, header_parameter)
    
    # Add x-axis label
    ax1.set_xlabel("year", fontsize=20)
    plt.xticks(fontsize=20)
    ax1.tick_params(axis="x", labelcolor="black", labelsize=20)
    
    axes = plt.gcf().get_axes()
    # Keep axes 0, 1, 2, hide all others
    print("main_323: call plot_6_remove_axe1.")
    #plot_6_remove_axe1(axes,yr_delete)
    plot_6_remove_axe1(axes,-1) # -1= no delete, print only
    #plot_6_remove_axe1(axes,0) # delete axe 
    #plot_6_remove_axe1(axes,1) # delete axe 
    #plot_6_remove_axe1(axes,2) # delete axe 
    #plot_6_remove_axe1(axes,3) # delete axe 
    #plot_6_remove_axe1(axes,4) # delete axe 
    #plot_6_remove_axe1(axes,5) # delete axe 5, not axe 0
    #plot_6_remove_axe1(axes,6)  # delete axe 6
    
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


