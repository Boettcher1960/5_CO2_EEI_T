# main.py
v = "5H71" # H61 = albedo67 as line 2
#          43 work on albedo 12 month
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


if print_debug > 9:
   print("main_030: start main ", line2_play , line3_play , line4_play)


def process_ceres_data():
    """Process CERES data based on configuration"""
    # main.play_61_EEI line 65
    if play_61_EEI > 0: # part 6 
       df61b = convert_ceres_to_csv('work/61_in__2026_08_EEI_CERES.txt', 
                                    'work/61b_out_in_ceres.csv')
       if print_debug > 9:
          print(f"main_067: create work/61b_out_in_ceres.csv'  61.b ={play_61_EEI}")
       
       window_months=play_61_EEI

       if play_61_EEI > 11:
          min1_periods=12
       else:
          min1_periods=play_61_EEI
       use_center=False
       keep_original=True,
       
       df61c = create_running_average( 'work/61b_out_in_ceres.csv', 
                                       'work/61c_out_EEI.csv',
                                            window_months=play_61_EEI,
                                            min_periods=min1_periods,
                                            center=use_center,
                                            column_name='EEI')
        
       if print_debug > 9:
          print(f"main_086: create work/61c_out_EEI.csv  61.gut ={play_61_EEI}")


    # main.play_62_EEA line 90 
    # CERES Outgoing Longwave Radiation OLR     # _62_in__2026_02_Longwave.txt
    if play_62_EEA > 1: #  
       # 62.11 convert download.txt to CERES.csv (no averaging)
       df62b = convert62_txt_to_csv('work/61_in__2026_08_EEI_CERES.txt', 
                                      'work/62b_EEA.csv',
                                      'EEI'          )
       # 62.33  CERES.csv (perform averaging)
       use_center=False
       columnname ='EEI36'
       column_read    ='EEI'
       column_average ='EEI36'
       # 62.37  CERES.csv (perform running average over play_62_EEA months)
       df62c = create66_running_average( 'work/62b_EEA.csv', 
                                         'work/62c_EEA.csv',
                                          column_read,             #  column_name='EEI')
                                          column_average,          #  column_name='EEI36')
                                          columnname,              #  column_name='EEI36')
                                            window_months=play_62_EEA,
                                            min_periods=12,
                                            center=use_center,
                                            column_name=columnname)
       # 62.51. read above created CSV-file
       df62g = pd.read_csv("work/62c_EEA.csv")

       # 62.52. summ the averaged column "EEI36" and store it in new column 'EEA'
       factor = 1.37  #     then multiplied by a constant 16.087 to convert it to ZJ. 
       df62g["EEA"] = df62g["EEI36"].cumsum() * factor
       
       # 62.53. store 62g*csv to print it later, or copy it and use for other plots
       df62g.to_csv("work/62g_EEA.csv", index=False, float_format='%.6f')

       # part 62.e  CERES.csv (add averaging column to plotable-csv)
       #df62e = add_62_csv_column( 'work/62b_EEA.csv', 
       #                           'read_csv/_42_EEI48month_2026_08.csv', 
       #                           'work/62e_EEA.csv',
       #                                     window_months=play_62_EEA,
       #                                     min_periods=12,
       #                                     center=use_center,
       #                                     column_name='LongWave')
       if print_debug > 9:
          print(f"main_133: create work/62e_EEA.csv   62    ={play_62_EEA}")

# main.play_64_ASR_anomaly line 124
if play_64_ASR_anomaly > 1: #  
       df64b = convert_ceres_to_csv('work/64a_in__2026_08_ASR_anomaly.txt', 
                                    'read_csv/_64b_ASR.csv')
       if print_debug > 9:
          print(f"main_152: create read_csv/_64b_ASR.csv  64.b ={play_64_ASR_anomaly}")
       
       window_months=play_64_ASR_anomaly
       min_periods=12
       use_center=False
       keep_original=True,
       df64c = create_running_average( 'read_csv/_64b_ASR.csv', 
                                       'read_csv/_64c_ASR.csv',
                                            window_months=play_64_ASR_anomaly,
                                            min_periods=12,
                                            center=use_center,
                                            column_name='ASR')
       if print_debug > 9:
          print(f"main_138: create read_csv/_62e_LongWave.csv 64    ={play_64_ASR_anomaly}")

# main.play_65_ASR line 141
# CERES Outgoing Longwave Radiation OLR  # _66_TOA_OLR_all_sky_2026_07.txt
if play_65_ASR > 1: #  
       column_read    ='ASR'
       column_average ='ASR_average'
       use_center=False
       # part 65.37  CERES.csv (perform averaging for albedo)
       # note part 67.31 write df2 to  work/_CERES_raw.csv'
       df65a = create67_running_average( 'work/_CERES_raw.csv', 
                                         'work/_CERES_65_ASR.csv',
                                                column_read,             #  column_name='ASR')
                                                column_average,          #  column_name='ASR_average')
                                                window_months=play_65_ASR,
                                                min_periods=12,
                                                center=use_center
                                                )
       # column_read    ='ASR'
       # column_average ='ASR12'
       # use_center=False
       # part 66.35  CERES.csv (perform averaging for ASR)
       # df67d = create67_running_average( 'work/_CERES_raw.csv', 
       #                                  'work/_65c_CERES_ASR.csv',
       #                                   column_read,             #  column_name='ASR')
       #                                   column_average,          #  column_name='ASR12')
       #                                   window_months=play_65_ASR,
       #                                   min_periods=12,
       #                                   center=use_center)
       if print_debug > 9:
          print(f"main_165: created.  work/_CERES_65_ASR.csv  65.50 ={play_65_ASR}")


# main.play_66_OLR line 144
# CERES Outgoing Longwave Radiation OLR  # _66_TOA_OLR_all_sky_2026_07.txt
if play_66_OLR > 1: #  
       # part 66.b convert download.txt to CERES.csv (no averaging)
       # CERES_EBAF-TOA_Ed4.2.1_TOA_Longwave_Flux_-_All-Sky_March-2000toJuly-2026.txt downloaded
       # copy to 'work/_66_TOA_OLR_all_sky_2026_07.txt'
       df66b = convert66_txt_to_csv('work/_66_TOA_OLR_all_sky_2026_08.txt', 
                                    'work/_66b_OLR_raw.csv',
                                    'OLR'
                                    )
       if print_debug > 9:
          print(f"main_169: created.  work/_66b_OLR.csv  66.b ={play_66_OLR}")
       
       window_months=play_66_OLR
       min_periods=12
       use_center=False
       keep_original=True
       columnname ='OLR48'
       column_read    ='OLR'
       column_average ='OLR48'
       # part 66.c  CERES.csv (perform averaging)
       df66c = create66_running_average( 'work/_66b_OLR_raw.csv', 
                                         'work/_66c_OLR.csv',
                                          column_read,             #  column_name='OLR')
                                          column_average,          #  column_name='OLR48')
                                          columnname,              #  column_name='SW_in')
                                            window_months=play_66_OLR,
                                            min_periods=12,
                                            center=use_center,
                                            column_name=columnname)
       if print_debug > 9:
          print(f"main_210: created. OLR48 work/_66c_OLR.csv  66.c ={play_66_OLR}")


# part 67.1 create work/_CERES_raw.csv with 13 columns
# https://ceres-tool.larc.nasa.gov/ord-tool/srbavg
# 67.1 download CERES_EBAF-TOA_Ed4.2.1_TOA_Shortwave_Flux_-_All-Sky_March-2000toJuly-2026.txt
# 67.2 copy to read_csv/_66_TOA_Shortwave_Flux_All_Sky2026_07.txt'
# 67.6 download CERES_EBAF-TOA_Ed4.2.1_Incoming_Solar_Flux_March-2000toJuly-2026.txt
# 67.7 copy to read_csv/_66_TOA_Incoming_Solar_2026_07.txt'
# 67.10 download CERES_EBAF-TOA_Ed4.2.1_TOA_Net_Flux_-_All-Sky_March-2000toJuly-2026.txt
# 67.11 copy to 'read_csv/_67_EEI_TOA_Net_Flux_2026_07.txt'
# 67.15 download CERES_EBAF-TOA_Ed4.2.1_TOA_Longwave_Flux_-_All-Sky_March-2000toJuly-2026.txt
# 67.16 copy to 'read_csv/_67_EEI_TOA_Net_Flux_2026_07.txt'
# part 67.31 write df2 to  work/_CERES_raw.csv'
# main.play_67_albedo line 176
if play_67_albedo > 0: #       
       # part 67.1 to part 67.32 read 
       df67b = ceres67_to_csv(      'work/_67b_sw_out.csv',  # output1 not used
                                    'work/_CERES_raw.csv')   # output 2 used a lot
       # part 67.33 print
       if print_debug > 9:
          print(f"main_237: _CERES_raw.csv 67.b play_67_albedo={play_67_albedo}")

       # part 67.34 set some variables
       window_months=play_67_albedo

       if play_67_albedo > 11:
          min1_periods=12
       else:
          min1_periods=play_67_albedo
       use_center=False
       keep_original=True,
       column_read    ='ASR'
       column_average ='ASR48'
       # part 66.35  CERES.csv (perform averaging for ASR)
       df67c = create67_running_average( 'work/_CERES_raw.csv', 
                                         'work/_CERES_ASR.csv',
                                          column_read,             #  column_name='ASR')
                                          column_average,          #  column_name='ASR48')
                                            window_months=play_67_albedo,
                                            min_periods=12,
                                            center=use_center)
       column_read    ='albedo'
       column_average ='albedo48'
       # part 67.37  CERES.csv (perform averaging for albedo)
       df67d = create67_running_average( 'work/_CERES_raw.csv', 
                                         'work/_CERES_albedo.csv',
                                                column_read,             #  column_name='albedo')
                                                column_average,          #  column_name='albedo48')
                                                window_months=play_67_albedo,
                                                min_periods=12,
                                                center=use_center)

        # part 66.58
       if print_debug > 9:
          print(f"main_242: all main jobs done play_67_albedo={play_67_albedo}")


# 68.12 the main.py part line 266
if play68_ERA > 0: #       
       if print_debug > 9:
          print(f"main_248:  68.13 play68_ERA={play68_ERA}")

       # part 68.13 set some variables
       window_months=play68_ERA
       if play68_ERA > 11:
          min1_periods=12
       else:
          min1_periods=play68_ERA
       use_center=False
       column_read    ='ano_91-20'
       column_average ='temp_average'
       # part 68.15  call create68_running_average for global era5 temperatue)
       df68c = create68_running_average( 'work/_68_era5_daily_series_2026_10_13.csv', 
                                         'work/_68_out.csv',
                                          column_read,             #  column_name='ano_91-20')
                                          column_average,          #  column_name='temp_average')
                                            window_months=play68_ERA,
                                            min_periods=12,
                                            center=use_center)
if play69_AA > 1: #  # 69.20  main.py   line 267  if play69_AA > 1: 
       df69b = convert62_txt_to_csv( play69_AA_in, 
                                    'work/69b_AA.csv',
                                    'AlbedoA')
       if print_debug > 9:
          print(f"main_271: create albedo work/69b_AA.csv  69.28 ={play69_AA}")
       
       window_months=play_64_ASR_anomaly
       min_periods=12
       use_center=False
       keep_original=True,
       df64c = create_running_average( 'read_csv/_64b_ASR.csv', 
                                       'read_csv/_64c_ASR.csv',
                                            window_months=play_64_ASR_anomaly,
                                            min_periods=12,
                                            center=use_center,
                                            column_name='ASR')
       if print_debug > 9:
          print(f"main_138: create read_csv/_62e_LongWave.csv 64    ={play_64_ASR_anomaly}")




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
           print(f"main_291: 64.9 read ={play_64_ASR_anomaly}") 
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

    # Load GIS temperature data
    if plot74_GIS_T > 0: # 74.33 models.py line 600 
        data['gis_temp'] = load74_gis_T()
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
                       f"{plot43_eei_12month}{plot45_OLR}{plot46_ASR} 5({plot52_delta_CO2_red_bars}"
                       f"{plot53_CO2_orange2025}{plot54_Glen_delta_on}{plot55_population_on}"
                       f" 6({play_61_EEI}{play_62_EEA}{play_63_CB}{play_64_ASR_anomaly}{play_65_ASR}{play_66_OLR}{play_67_albedo}{play68_ERA}{play69_AA}"
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

if __name__ == "__main__":
    main()


