# main.py
v = "5N01" #  Figure 6: Global Warming Temperature  calculated with constant EEI = 1.5     in 2050 = 2.4°C  "
# https://github.com/Boettcher1960/5_CO2_EEI_T
# ocean stratification https://bsky.app/profile/thomas-boettcher.bsky.social/post/3mj7zx7fzsc26
# https://drtomharris.substack.com/p/the-great-decoupling-how-ocean-stratification
# http://www.ocean.iap.ac.cn/ftp/images_files/Stratification_global_time_series.txt
#
# https://www.nature.com/articles/s43247-026-03427-w#
# https://bsky.app/profile/thomas-boettcher.bsky.social/post/3miz5mmll3k2z
# play68_ERA = 48 
# https://sites.ecmwf.int/data/climatepulse/data/series/era5_daily_series_2t_global.csv
#

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
import sys

# Import modules
from config import *
from data_processing import *
from models import *
from plotting import *
from text import *
from Rovang import *
from ceres import *

if print_debug > 9:
   print("")
   print("main_030: start main ", line2_play , line3_play , line4_play)


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
    data = {}
    # Load CO2 data if needed
    if plot22_CO2_Mauna_Loa > 0:  # 22.3 load the mauna loa CO2 data
        data['co2'] = load_co2_mauna_loa(x_anf, x_end)
        if print_debug > 19:
           print(f"main_168: plot22_CO2_Mauna_Loa 22.3 ={plot22_CO2_Mauna_Loa}")
           print(f"main_169: Last 3 CO2 rows: {data['co2'][-3:] if len(data['co2']) >= 3 else data['co2']}")     
    if plot28_E_T > 0: # 28.9 read
        # data['ceres_62'] = pd.read_csv("work/28g_T_E.csv")
        data['ceres_28'] = pd.read_csv("work/28g_T_E.csv")
        if print_debug > 9:
           print(f"main__56: 28.69 read ={plot28_E_T}")  
    if plot29_ETq > 0: # 29.9 read
        # data['ceres_62'] = pd.read_csv("work/29g_T_E.csv")
        data['ceres_29'] = pd.read_csv("work/29g_T_E.csv")
        if print_debug > 9:
            print(f"main__62: 29.69 read ={plot29_ETq}")  
    if plot30_c > 0: # 30.9 read
        # data['ceres_62'] = pd.read_csv("work/30g_T_E.csv")
        data['ceres_30'] = pd.read_csv("work/30g_T_E.csv")
        if print_debug > 9:
            print(f"main__62: 30.69 read ={plot30_c}")  
    if plot42_EEI_48month > 0: # _plot_42_41g50.csv"
        data['ceres_42'] = pd.read_csv("read_csv/_42_EEI48month_2026_08.csv")
        # 249 bug data['ceres_48'] = pd.read_csv("read_csv/_42_EEI48month_made_by_61c.csv")
    if plot43_eei_12month > 0: # 43.2 read1 _43_EEI12month_made_by_61c.csv a44d_ceres_12month_EEI
    #   data['ceres_43'] = pd.read_csv("read_csv/_43_EEI12month_2026_02.csv")
        data['ceres_43'] = pd.read_csv("read_csv/_43_EEI12month_2026_08.csv")
        if print_debug > 19:
           print(f"main_176: 43.2 read ={plot43_eei_12month}")
           #data['ceres_43'] = pd.read_csv("csv/csv44/_plot_41_41g12.csv")
    if part44_ceres_eei > 0:
        if print_debug > 19:
           print(f"main_180: custom-read 44.7 ={part44_ceres_eei}")
        data['ceres_custom'] = pd.read_csv("work/c44d_ceres.csv")
    if plot45_OLR > 0: # Outgoing Longwave Radiation OLR
        data['ceres_45'] = pd.read_csv("read_csv/_45_OLR_48month_2026_08.csv")
        if print_debug > 9:
           print(f"main_302: OLR read 45.1 ={plot45_OLR}")
    if plot46_ASR > 0: # Outgoing Longwave Radiation OLR
        data['ceres_46'] = pd.read_csv("read_csv/_46_ASR_48month_2026_08.csv")
        if print_debug > 9:
           print(f"main_302: ASR read 46.1 ={plot46_ASR}")
    if plot47_albedo48 > 0: # _64c_ASR.csv read_csv/_47_ASR_12month_2026_02.csv
        data['ceres_47'] = pd.read_csv("read_csv/_47_albedo_48month_2026_08.csv")
        if print_debug > 9:
           print(f"main_316: 47.2 read ={plot47_albedo48}")
    # Load 
    if plank48 > 0: #  pd.read_csv("work/_48_era5_in.csv")  _48monthly_era5_in.csv 
        data['plank4'] = pd.read_csv("work/_48monthly_era5_in.csv")
    if plot49 > 0: #  pd.read_csv("work/_48_era5_in.csv")
        create49_fb1_olr48_sum(
          "work/_49_in_plank_FB1.csv", # plank FB1 in 
          "work/_49_OLR_48month_2026_08.csv", # outgoing longwave radiation OLR
          "work/_49_FB1_plus_OLR48.csv", # 
         )
        data['plank5'] = pd.read_csv("work/_49_FB1_plus_OLR48.csv")
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

    if play_60_T_E > 0: # 60.9 read
        # data['ceres_62'] = pd.read_csv("work/62c_EEA.csv")
        data['ceres_60'] = pd.read_csv("work/60g_T_E.csv")
        if print_debug > 9:
           print(f"main_410: 60.69 read ={play_60_T_E}")  
    if play_61_EEI > 0: # 61.9 read
        data['ceres_61'] = pd.read_csv("work/61c_out_EEI.csv")
        if print_debug > 9:
           print(f"main_197: 61.9 read ={play_61_EEI}")
    if play_62_EEA > 0: # 62.9 read
        # data['ceres_62'] = pd.read_csv("work/62c_EEA.csv")
        data['ceres_62'] = pd.read_csv("work/62g_EEA.csv")
        if print_debug > 9:
           print(f"main_383: 62.69 read ={play_62_EEA}")    
    if play_64_ASR_anomaly > 0: # 62.9 read
        data['ceres_64'] = pd.read_csv("read_csv/_64c_ASR.csv")
        # data['ceres_64'] = pd.read_csv("work/c62d_ceres.csv")
        if print_debug > 9:
           print(f"main_362: 64.9 read ={play_64_ASR_anomaly}") 
    if play_65_ASR > 0: # 
        data['ceres_65'] = pd.read_csv("work/_CERES_65_ASR.csv")
        if print_debug > 9:
           print(f"main_355: 65.9 read ={play_65_ASR}")  
    if play_66_OLR > 0: # 66.9 read 'work/_66c_OLR.csv'
        data['ceres_66'] = pd.read_csv("work/_66c_OLR.csv")
        if print_debug > 9:
           print(f"main_357: 66.9 read ={play_66_OLR}")  
    if play_67_albedo > 0: # 67.49 read 
        data['ceres_67'] = pd.read_csv("work/_CERES_albedo.csv")
        if print_debug > 9:
           print(f"main_355: 67.49 read ={play_67_albedo}")  
    if play68_ERA > 0: # 68.39 main.py line 377 read  work/_68_out.csv into  'era_68'
        data['era_68'] = pd.read_csv("work/_68_out.csv")
        if print_debug > 9:
           print(f"main_380: 68.41 read ={play68_ERA}")  
    if play69_AA > 0: # 69.55 read
        data['ceres_69'] = pd.read_csv("work/69c_AA.csv") # 69.56 read into data field
        if print_debug > 9:
           print(f"main_386: 64.57 read 69c_AA.csv  play69_AA ={play69_AA}") 
    # Load GIS temperature data
    if plot74_GIS_T > 0: # 74.33 models.py line 600 
        data['gis_temp'] = load74_gis_T()
    if linear_41_75 > 0: # 75.55 read df75 = pd.read_csv("read_csv/_75_hansen_41C.csv") # our world in data file
        data['ceres_75'] = pd.read_csv("read_csv/_75_hansen_41C.csv") # 75.56 read into data field

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
def run_optional_figures():
    if figure202 > 0:
        fig_202_era5_temp_quadratic()
    if figure303 == 3:
        Figure_303()
    elif figure303 == 4:
        Figure_304()
    if figure404 > 1:
        fig_404_eei_quadratic()

def main():
    """Main execution function"""
    if figure100 == 0:
        if figure404 in (12, 24, 48):
            ceres_process_data()
        run_optional_figures()
        return

    # Create header parameter string
    header_parameter = (f" "
                       f"2({plot22_CO2_Mauna_Loa}{plot23_Glen_CO2}{plot25_long_CO2}" 
                       f" 3({plot31_CO2_emission}{plot34_CO2_emission} 4({plot42_EEI_48month}"
                       f"{plot43_eei_12month}{plot45_OLR}{plot46_ASR}{plot47_albedo48}_{plank48}{plot49} 5({plot52_delta_CO2_red_bars}"
                       f"{plot53_CO2_orange2025}{plot54_Glen_delta_on}{plot55_population_on}"
                       f" 6({play_61_EEI}{play_62_EEA}{play_63_CB}_{play_64_ASR_anomaly}{play_65_ASR}{play_66_OLR}_{play_67_albedo}{play68_ERA}{play69_AA}"
                       f" 7({plot71_temperature}{plot72_AESS_T}{plot73_ECS_T}{plot74_GIS_T}"
                       f"{linear_41_75}{plot76_my_T}")
    
    if print_debug > 9:
       print("main_213: begin ", header_parameter)

    # Process CERES data
    ceres_process_data()
    
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
    # print("main_468: call plot_6_remove_axe1.")
    #plot_6_remove_axe1(axes,yr_delete)
    plot_6_remove_axe1(axes,-1) # -1= no delete, print only
    #plot_6_remove_axe1(axes,0) # delete axe 
    # plot_6_remove_axe1(axes,1) # delete axe 
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
    run_optional_figures()


if __name__ == "__main__":
    if "--visualize-era5-temp-average" in sys.argv[1:]:
        fig_202_era5_temp_quadratic() # in ceres.py line 420
    else:
        main()
