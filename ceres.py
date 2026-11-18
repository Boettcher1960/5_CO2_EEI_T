# ceres.py

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.ticker import MultipleLocator
import pandas as pd
import numpy as np
import os
import sys

# Import modules
from main import *
from config import *
from data_processing import *
from models import *
from plotting import *
from text import *
from Rovang import *


def ceres_process_data():
    """Process CERES data based on configuration""" 
    if print_debug > 19:
        print(f"ceres_36: play_60_T_E=1    60.00    ={play_60_T_E}")
        print(f"")
    
    # plot28_E_T    # add 0.00208°C for every 1 W/m²/month    Piers Forster 1 W/m² in 1month warmes 0.00208°C 
    if plot28_E_T> 1: #  
       # 28.12. summ the averaged column "quadratic_value" and store it in new column 'T_A'
       # 28.    Piers Forster: An EEI of 2 W/m² sustained over a decade would add roughly half a degree of warming.
       factor = 0.00208  #     then multiplied by a constant 0.00208 to convert it to °C. 
       #                       a60_start = 2005
       #                       a60_offset = 0.2 # add offset 0.2°C at start of adding
       #
       # 28.14 add the temperature for every month, no averaging is done 
       if print_debug > 9:
           print(f"ceres_37: plot28_E_T   28.25    ={plot28_E_T}")
       # 28.39 read the file created in figure404    work/_404EEI_48Month.csv
       df28g = pd.read_csv("work/_404EEI_48Month.csv")
       # 28.41
       df28g["T_E"] = (
              df28g["linear_fit"]
              .where(df28g["digital_date"] >= a28_start)
              .cumsum()
              * factor          # factor = 0.00208 to convert it to °C
              + a28_offset      # add offset 0.2°C at start of adding
           )
       # 28.43. store 62g*csv to print it later, or copy it and use for other plots
       df28g.to_csv("work/28g_T_E.csv", index=False, float_format='%.6f')
       if print_debug > 9:
           print(f"ceres_51: create work/28g_T_E.csv   28    ={plot28_E_T}")
    
    if plot29_ETq > 1: #  
        # 29.12. summ the averaged column "quadratic_value" and store it in new column 'T_A'
        # 29.    Piers Forster: An EEI of 2 W/m² sustained over a decade would add roughly half a degree of warming.
        factor = 0.00208  #     then multiplied by a constant 0.00208 to convert it to °C. 
        # 29.14 add the temperature for every month, no averaging is done 
        if print_debug > 9:
            print(f"ceres_62: plot29_ETq   28.25    ={plot29_ETq}")
        # 29.39 read the file created in figure404    work/_404EEI_48Month.csv
        df29g = pd.read_csv("work/_404EEI_48Month.csv")
        # 29.41
        df29g["T_E"] = (
            df29g["quadratic_value"]
            .where(df29g["digital_date"] >= a29_start)
            .cumsum()
            * factor          # factor = 0.00208 to convert it to °C
            + a29_offset      # add offset 0.2°C at start of adding
         )
        # 29.43. store 62g*csv to print it later, or copy it and use for other plots
        df29g.to_csv("work/29g_T_E.csv", index=False, float_format='%.6f')
        if print_debug > 9:
            print(f"ceres_76: create work/29g_T_E.csv   28    ={plot29_ETq }")





    
    # play_60_T_E = 48    # add 0.00208°C for every 1 W/m²/month    Piers Forster 1 W/m² in 1month warmes 0.00208°C 
    # Earth Energy Accumulated EEA is sum of EEI
    if play_60_T_E > 1: #  
       # 60.11 convert download.txt to CERES.csv (no averaging)
       print(f"ceres_42: play_60_T_E=1    60.11    ={play_60_T_E}")
       df60b = convert62_txt_to_csv('work/61_in__2026_08_EEI_CERES.txt', 
                                      'work/60b_EEI.csv',
                                      'EEI'          )
       # 60.12. summ the averaged column "EEI36" and store it in new column 'T_A'
       # 60.    Piers Forster: An EEI of 2 W/m² sustained over a decade would add roughly half a degree of warming.
       factor = 0.00208  #     then multiplied by a constant 0.00208 to convert it to °C. 
       #                       a60_start = 2005
       #                       a60_offset = 0.2 # add offset 0.2°C at start of adding
       #
       # 60.14 add the temperature for every month, no averaging is done for play_60_T_E=1
       if print_debug > 19:
           print(f"ceres_53: play_60_T_E=1    60.25    ={play_60_T_E}")
       if play_60_T_E < 3: # bug play_60_T_E =1 does not work
           print(f"ceres_54: play_60_T_E=1    60.25    ={play_60_T_E}")
           # 60.15 read csv produced in 60.11
           use_center=False
           columnname ='EEI36'
           column_read    ='EEI'
           column_average ='EEI36'
           # 60.17  CERES.csv (perform running average over play_60_T_E months)
           df60c = create66_running_average( 'work/60b_EEI.csv', 
                                         'work/60c_T_E.csv',
                                          column_read,             #  column_name='EEI')
                                          column_average,          #  column_name='EEI36')
                                          columnname,              #  column_name='EEI36')
                                            window_months=12,
                                            min_periods=12,
                                            center=use_center,
                                            column_name=columnname)
           # 60.19 read above created CSV-file
           df60g = pd.read_csv("work/60c_T_E.csv")
           # 60.21
           df60g["T_E"] = (
              df60g["EEI"]
              .where(df60g["year"] >= a60_start)
              .cumsum()
              * factor          # factor = 0.00208 to convert it to °C
              + a60_offset      # add offset 0.2°C at start of adding
           )
           # 60.23. store 62g*csv to print it later, or copy it and use for other plots
           df60g.to_csv("work/60g_T_E.csv", index=False, float_format='%.6f')
           if print_debug > 9:
              print(f"ceres_84: create work/60g_T_E.csv   60    ={play_60_T_E}")
       # 60.23 add the temperature for every month, some averaging  done for play_60_T_E=2,3,4,5,6,7,8,9,10,11
       elif play_60_T_E < 12: # prints for 11
           print(f"ceres_86: play_60_T_E= 3,4,5,6,7,8,9,10,11  60.25    ={play_60_T_E}")
           # 60.23  CERES.csv (perform averaging)
           use_center=False
           columnname ='EEI36'
           column_read    ='EEI'
           column_average ='EEI36'
           # 60.27  CERES.csv (perform running average over play_60_T_E months)
           df60c = create66_running_average( 'work/60b_EEI.csv', 
                                         'work/60c_T_E.csv',
                                          column_read,             #  column_name='EEI')
                                          column_average,          #  column_name='EEI36')
                                          columnname,              #  column_name='EEI36')
                                            window_months=play_60_T_E,
                                            min_periods=play_60_T_E-1,
                                            center=use_center,
                                            column_name=columnname)
           # 60.29 read above created CSV-file
           df60g = pd.read_csv("work/60c_T_E.csv")
           # 60.31
           df60g["T_E"] = (
              df60g["EEI36"]
              .where(df60g["year"] >= a60_start)
              .cumsum()
              * factor          # factor = 0.00208 to convert it to °C
              + a60_offset      # add offset 0.2°C at start of adding
           )
           # 60.33. store 62g*csv to print it later, or copy it and use for other plots
           df60g.to_csv("work/60g_T_E.csv", index=False, float_format='%.6f')
           if print_debug > 9:
              print(f"ceres116: create work/60g_T_E.csv   60    ={play_60_T_E}")

       # 60.32 add the temperature for every month, some averaging  done for play_60_T_E=2,3,4,5,6,7,8,9,10,11
       else: 
           # 60.33  CERES.csv (perform averaging)
           use_center=False
           columnname ='EEI36'
           column_read    ='EEI'
           column_average ='EEI36'
           # 60.37  CERES.csv (perform running average over play_60_T_E months)
           df60c = create66_running_average( 'work/60b_EEI.csv', 
                                         'work/60c_T_E.csv',
                                          column_read,             #  column_name='EEI')
                                          column_average,          #  column_name='EEI36')
                                          columnname,              #  column_name='EEI36')
                                            window_months=play_60_T_E,
                                            min_periods=12,
                                            center=use_center,
                                            column_name=columnname)
           # 60.39 read above created CSV-file
           df60g = pd.read_csv("work/60c_T_E.csv")
           # 60.41
           df60g["T_E"] = (
              df60g["EEI36"]
              .where(df60g["year"] >= a60_start)
              .cumsum()
              * factor          # factor = 0.00208 to convert it to °C
              + a60_offset      # add offset 0.2°C at start of adding
           )
           # 60.43. store 62g*csv to print it later, or copy it and use for other plots
           df60g.to_csv("work/60g_T_E.csv", index=False, float_format='%.6f')
           if print_debug > 9:
              print(f"ceres118: create work/60g_T_E.csv   60    ={play_60_T_E}")

    # main.play_61_EEI line 65
    if play_61_EEI > 0: # 61.10
       df61b = convert_ceres_to_csv('work/61_in__2026_08_EEI_CERES.txt', 
                                    'work/61b_out_in_ceres.csv')
       if print_debug > 9:
          print(f"ceres125: create work/61b_out_in_ceres.csv'  61.b ={play_61_EEI}")
       
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
          print(f"ceres123: create work/61c_out_EEI.csv  61.gut ={play_61_EEI}")

    # Earth Energy Accumulated EEA is sum of EEI
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
       if print_debug > 9:
          print(f"ceres147: create work/62e_EEA.csv   62    ={play_62_EEA}")

    # 64.20 
    if play_64_ASR_anomaly > 1: #  
       df64b = convert_ceres_to_csv('work/64a_in__2026_08_ASR_anomaly.txt', 
                                    'work/64b_ASR.csv')
       if print_debug > 9:
          print(f"ceres214: create    work/64b_ASR.csv  64.b ={play_64_ASR_anomaly}")
       
       window_months=play_64_ASR_anomaly
       min_periods=12
       use_center=False
       keep_original=True,
       df64c = create_running_average( 'work/64b_ASR.csv', 
                                       'read_csv/_64c_ASR.csv',
                                            window_months=play_64_ASR_anomaly,
                                            min_periods=12,
                                            center=use_center,
                                            column_name='ASR')
       if print_debug > 19:
          print(f"ceres227: create read_csv/_64c_ASR.csv 64    ={play_64_ASR_anomaly}")

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
       if print_debug > 9:
          print(f"ceres245: created.  work/_CERES_65_ASR.csv  65.50 ={play_65_ASR}")


    # CERES Outgoing Longwave Radiation OLR  # _66_TOA_OLR_all_sky_2026_07.txt
    if play_66_OLR > 1: #  
       # part 66.b convert download.txt to CERES.csv (no averaging)
       # CERES_EBAF-TOA_Ed4.2.1_TOA_Longwave_Flux_-_All-Sky_March-2000toJuly-2026.txt downloaded
       # copy to 'work/_66_TOA_OLR_all_sky_2026_07.txt'
       # copy to 'work/66a_CERES_EBAF-TOA_Ed4.2.1_TOA_Longwave_Flux_-_All-Sky_March-2000toAugust-2026.txt
       df66b = convert66_txt_to_csv('work/66a_CERES_EBAF-TOA_Ed4.2.1_TOA_Longwave_Flux_-_All-Sky_March-2000toAugust-2026.txt', 
                                    'work/66b_OLR_raw.csv',
                                    'OLR'
                                    )
       if print_debug > 9:
          print(f"ceres169: created.  work/66b_OLR.csv  66.b ={play_66_OLR}")
       
       window_months=play_66_OLR
       min_periods=12
       use_center=False
       keep_original=True
       columnname ='OLR48'
       column_read    ='OLR'
       column_average ='OLR48'
       # part 66.c  CERES.csv (perform averaging)
       df66c = create66_running_average( 'work/66b_OLR_raw.csv', 
                                         'work/_66c_OLR.csv',
                                          column_read,             #  column_name='OLR')
                                          column_average,          #  column_name='OLR48')
                                          columnname,              #  column_name='SW_in')
                                            window_months=play_66_OLR,
                                            min_periods=12,
                                            center=use_center,
                                            column_name=columnname)
       if print_debug > 9:
          print(f"ceres210: created. OLR48 work/_66c_OLR.csv  66.c ={play_66_OLR}")


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
    if play_67_albedo > 0: #       
       # part 67.1 to part 67.32 read 
       df67b = ceres67_to_csv(      'work/_67b_sw_out.csv',  # output1 not used
                                    'work/_CERES_raw.csv')   # output 2 used a lot
       # part 67.33 print
       if print_debug > 19:
          print(f"ceres208: _CERES_raw.csv 67.b play_67_albedo={play_67_albedo}")

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
          print(f"ceres242:  done play_67_albedo={play_67_albedo}")


    # 68.12 the main.py part line 266
    if play68_ERA > 0: #       
       if print_debug > 9:
          print(f"ceres248:  68.13 play68_ERA={play68_ERA}")

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
       # df68c = create68_running_average( 'work/_68_era5_daily_series_2026_10_13.csv', 
       df68c = create68_running_average( 'work/68_era5_daily_series_2026_10_30.csv', 
                                         'work/_68_out.csv',
                                          column_read,             #  column_name='ano_91-20')
                                          column_average,          #  column_name='temp_average')
                                            window_months=play68_ERA,
                                            min_periods=12,
                                            center=use_center)
    if play69_AA > 1:                                       # 69.20  main.py   line 267  if play69_AA > 1: 
       df69b = convert62_txt_to_csv( play69_AA_in,      # 69.22    input file
                                    'work/69b_AA.csv',  # 69.23    'work/69b_AA.csv') // output file
                                    'AlbedoA')          # 69.24  'AlbedoA' is new column in 69b_AA.csv'
       if print_debug > 9:
          print(f"ceres273: create albedo work/69b_AA.csv  69.25 ={play69_AA}")
       
       window_months=play69_AA                          # 69.26
       min_periods=12                                   # 69.27
       use_center=False                                 # 69.28
       keep_original=True,                              # 69.29
       column_read    ='AlbedoA'                        # 69.30 input column name
       column_average ='AA12'                           # 69.31 output column name for average  
       df69c = create67_running_average( 'work/69b_AA.csv',   # 69.32 input file name   part 67.37
                                         'work/69c_AA.csv',   # 69.33 output file name
                                            column_read,      # 69.34  column_name='AlbedoA')
                                          column_average,     # 69.35  column_name='AA')
                                          window_months=play69_AA, # 69.36  
                                          min_periods=1,     # 69.37    min_periods=12 was ok
                                          center=use_center) # 69.38  # end part 67.51
       if print_debug > 9:
          print(f"ceres289:   part 69.52   play69_AA   ={play69_AA}")




# part 62.b convert download.txt to CERES.csv (no averaging) convert_ceres_to_csv(input_file, output_file)
def convert_ceres_to_csv(input_file, output_file):
    """Convert CERES TOA flux ASCII file to CSV format"""
    data = []
    with open(input_file, 'r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            if not line or line.startswith('#') or line.startswith('CERES'):
                continue
            parts = line.split()
            if len(parts) >= 3:
                try:
                    year = int(parts[0])
                    month = int(parts[1])
                    flux = float(parts[2])
                    data.append([year, month, flux])
                except ValueError:
                    continue
    
    df = pd.DataFrame(data, columns=['year', 'month', 'toa_net_flux_w_m2'])
    df['date'] = pd.to_datetime(df['year'].astype(str) + '-' + df['month'].astype(str) + '-01')
    df['decimal_year'] = df['year'] + (df['month'] - 0.5) / 12
    df = df[['date', 'year', 'month', 'toa_net_flux_w_m2', 'decimal_year']]
    df.to_csv(output_file, index=False, float_format='%.6f')
    if print_debug_DP > 19:
        print(f"DataP_40: Successfully converted {len(df)} records to {output_file}")
    return df
    # end part 62.b convert download.txt to CERES.csv (no averaging)



# 200.2 ceres.py line 422 fig_202_era5_temp_quadratic
def fig_202_era5_temp_quadratic():
    """Plot the ERA5 running mean and its post-2000 quadratic trend."""
    # input_path = "work/_48_era5_in.csv"
    input_path = "work/_68_out.csv"
    output_path = "work/_48_era5_temp_average.png"
    # 200.3 read CSV and validate columns
    data = pd.read_csv(input_path)
    required_columns = {"date", "temp_average"}
    missing_columns = required_columns.difference(data.columns)
    # 200.4 raise error if required columns are missing
    if missing_columns:
        raise ValueError(
            f"{input_path} is missing required columns: {', '.join(sorted(missing_columns))}"
        )
    # 200.5 process data: convert types, drop NaNs, and sort by date
    data = data.loc[:, ["date", "temp_average"]].copy()
    # 200.6 convert date to datetime and temp_average to numeric, raising errors for invalid entries
    data["date"] = pd.to_datetime(data["date"], errors="raise")
    # 200.7 convert temp_average to numeric, raising errors for invalid entries
    data["temp_average"] = pd.to_numeric(data["temp_average"], errors="raise")
    # 200.8 drop rows with missing values and sort by date
    data = data.dropna(subset=["date", "temp_average"]).sort_values("date")
    if data.empty:
        raise ValueError(f"{input_path} has no valid date/temp_average rows")
    # 200.9 filter data for plotting and ensure enough points for quadratic fit
    plot_data = data.loc[data["date"] >= "2000-01-01"].copy()
    if len(plot_data) < 3:
        raise ValueError("At least three valid observations since 2000 are required for a quadratic fit")
    # 200.10 calculate decimal year for quadratic fitting
    plot_data["decimal_year"] = (
        plot_data["date"].dt.year
        + (plot_data["date"].dt.dayofyear - 1)
        / np.where(plot_data["date"].dt.is_leap_year, 366, 365)
    )
    # 200.11 perform quadratic fit and calculate R²
    x = plot_data["decimal_year"] - 2000
    # 200.12 fit a quadratic polynomial to the data
    coefficients = np.polyfit(x, plot_data["temp_average"], 2)
    # 200.13 evaluate the polynomial at the x values to get the trend
    trend = np.polyval(coefficients, x)
    # 200.14 calculate R² to assess the fit quality
    residual_sum_squares = np.sum((plot_data["temp_average"] - trend) ** 2)
    # 200.15 calculate total sum of squares for R² calculation
    total_sum_squares = np.sum(
        (plot_data["temp_average"] - plot_data["temp_average"].mean()) ** 2
    )
    # 200.16 calculate R² value
    r_squared = 1 - residual_sum_squares / total_sum_squares
    # 200.17 add the quadratic fit to the plot_data DataFrame for plotting
    plot_data["quadratic_fit"] = trend
    # 200.18 create the plot
    latest = plot_data.iloc[-1]
    # 200.19 define the benchmark temperature for reference
    benchmark = 1.5
    # 200.20 create the figure and axis for plotting
    fig, ax = plt.subplots(figsize=(13, 7))
    # 200.21 plot the ERA5 temperature anomaly
    ax.plot(
        plot_data["date"],
        plot_data["temp_average"],
        color="#b22222",
        linewidth=2,
        label="ERA5 temp_average",
    )
    # 200.22 plot the quadratic fit since 2000
    ax.plot(
        plot_data["date"],
        plot_data["quadratic_fit"],
        color="#1f4e79",
        linestyle=":",
        linewidth=2.5,
        label="Quadratic fit (2000 onward)",
    )
    # 200.23 add a horizontal line for the 1.5 °C benchmark
    ax.axhline(
        benchmark,
        color="black",
        linestyle="--",
        linewidth=1.5,
        label="1.5 °C is above the planetary boundary",
    )
    # 200.24 highlight the latest data point on the plot
    ax.scatter(latest["date"], latest["temp_average"], color="#b22222", zorder=3)
    # 200.25 add text annotations for the quadratic equation, R², and latest temperature

    text_below = ( f"https://github.com/Boettcher1960/5_CO2_EEI_T"
                   f"    version {v} ")

    ax.text(
        0.02, 0.84,
        (
            f"https://sites.ecmwf.int/data/climatepulse/data/series/era5_daily_series_2t_global.csv  (Nov. 1, 2026 downloaded)\n"
            f"https://github.com/Boettcher1960/5_CO2_EEI_T      version  {v} \n"
            f"T = {coefficients[0]:.6f}(year - 2000)^2 "
            f"{coefficients[1]:+.6f}(year - 2000) {coefficients[2]:+.6f} °C\n"
            f"R² = {r_squared:.4f}\n"
            f"Latest: {latest['temp_average']:.3f} °C ({latest['date']:%Y-%m-%d})"
        ),
        transform=ax.transAxes,
        va="top",
        bbox={"facecolor": "white", "alpha": 0.85, "edgecolor": "none"},
    )
    # 200.26 set the title, labels, limits, grid, and legend for the plot
    ax.set_title("The ERA5 temperature -4 years rolling average- is above the planetary boundary of 1.5 °C", fontsize=16)
    ax.set_xlabel("Date")
    ax.set_ylabel("Temperature anomaly (°C)")
    # 200.27 set y-axis limits to include the benchmark and data range with some padding
    ax.set_ylim(
        min(float(plot_data["temp_average"].min()), benchmark) - 0.05,
        max(float(plot_data["temp_average"].max()), benchmark) + 0.05,
    )
    # 200.28 set x-axis limits to the range of the data
    ax.grid(True, alpha=0.3)
    # 200.29 add a legend in the upper left corner with a specific bounding box
    ax.legend(loc="upper left", bbox_to_anchor=(0, 0.68))
    # 200.30 format the x-axis dates for better readability
    fig.autofmt_xdate()
    # 200.31 adjust layout and save the figure to the specified output path
    fig.tight_layout()
    # 200.32 save the figure with high resolution and tight bounding box
    fig.savefig(output_path, dpi=300, bbox_inches="tight")
    # 200.33 print the quadratic fit equation and R² value to the console
    print(
        "ceres540: Quadratic fit since 2000: "
        f"T = {coefficients[0]:.9f}(year - 2000)^2 "
        f"{coefficients[1]:+.9f}(year - 2000) {coefficients[2]:+.9f}; "
        f"R² = {r_squared:.6f}"
    )
    # 200.34 print the path where the visualization was saved
    print(f"ceres546: Saved ERA5 temperature visualization to {output_path}")
    # 200.35 show the plot and close the figure to free memory
    plt.show()
    # 200.36 close the figure to free up memory
    plt.close(fig)

# 404.10 make a separate new figure404 for
#        play_61_EEI = 12
#        this is file work/61c_out_EEI.csv column EEI
#        print the quadratic equation for EEI inside figure404
def fig_404_eei_quadratic():
    """Plot the selected CERES EEI running average with a quadratic fit."""
    # 402.11 comment 1
    # 402.12 comment 3
    #if figure404 not in (12, 24, 48):
    #    raise ValueError("Figure 404 must be set to 12, 24, or 48.")
    # 404.20 Use the configured averaging window when rebuilding the monthly EEI series.
    window_months = figure404
    min1_periods = 12
    use_center=False
    # 402.13  work/61b_out_in_ceres.csv is the input file
    # 402.14  work/404c_out_EEI.csv is the ouput file
    # 402.15 call the running average function with figure404 month averaging
    df404c = create404_running_average( 'work/61b_out_in_ceres.csv',
                                        'work/404c_out_EEI.csv',
                                            window_months=window_months,
                                            min_periods=min1_periods,
                                            center=use_center,
                                            column_name='EEI')


    # 404.21 Read the generated average and fail clearly if its expected columns are absent.
    input_path = "work/404c_out_EEI.csv"
    output_path = f"work/figure404_EEI_{figure404}month_quadratic.png"
    data = pd.read_csv(input_path)
    required_columns = {"date", "EEI"}
    missing_columns = required_columns.difference(data.columns)
    if missing_columns:
        raise ValueError(
            f"{input_path} is missing required columns: "
            f"{', '.join(sorted(missing_columns))}"
        )

    # 404.22 Normalize the date and EEI columns, remove invalid rows, and keep the requested years.
    plot_data = data.loc[:, ["date", "EEI"]].copy()
    plot_data["date"] = pd.to_datetime(plot_data["date"], errors="raise")
    plot_data["EEI"] = pd.to_numeric(plot_data["EEI"], errors="raise")
    plot_data = (
        plot_data.dropna(subset=["date", "EEI"])
        .sort_values("date")
        .reset_index(drop=True)
    )
    plot_data = plot_data.loc[
        plot_data["date"].dt.year.between(x_anf, x_end)
    ].reset_index(drop=True)
    if len(plot_data) < 3:
        raise ValueError(
            f"At least three valid EEI observations from {x_anf} through "
            f"{x_end} are required for a quadratic fit."
        )

    # 404.23 Convert dates to decimal years and center the fit's x-values at the first plot year.
    plot_data["decimal_year"] = (
        plot_data["date"].dt.year
        + (plot_data["date"].dt.dayofyear - 1)
        / np.where(plot_data["date"].dt.is_leap_year, 366, 365)
    )
    x = plot_data["decimal_year"] - x_anf
    coefficients = np.polyfit(x, plot_data["EEI"], 2)
    plot_data["quadratic_fit"] = np.polyval(coefficients, x)
    # 404.24 Calculate the linear fit used for both the plot and monthly CSV.
    linear_coefficients = np.polyfit(x, plot_data["EEI"], 1)
    plot_data["linear_fit"] = np.polyval(linear_coefficients, x)
    # 404.25 Generate one monthly forecast date from January 1990 through December 2200.
    forecast_months = pd.date_range("1990-01-01", "2200-12-01", freq="MS")
    # 404.26 Represent each month by its midpoint as a decimal (digital) year.
    forecast_digital_dates = (
        forecast_months.year + (forecast_months.month - 0.5) / 12
    )
    # 404.27 Evaluate both fits using their existing x_anf-centered year scale.
    forecast_values = np.polyval(
        coefficients, forecast_digital_dates - x_anf
    )
    forecast_linear_values = np.polyval(
        linear_coefficients, forecast_digital_dates - x_anf
    )
    # 404.28 Store the digital date, quadratic value, and linear fit as columns.
    forecast_data = pd.DataFrame(
        {
            "digital_date": forecast_digital_dates,
            "quadratic_value": forecast_values,
            "linear_fit": forecast_linear_values,
        }
    )
    # 404.29 Name the export for the averaging window used to calculate the fit.
    forecast_output_path = f"work/file404_{window_months}Month.csv"
    # 404.30 Ensure the output directory exists before writing the monthly series.
    os.makedirs(os.path.dirname(forecast_output_path), exist_ok=True)
    forecast_data.to_csv(
        forecast_output_path, index=False, float_format="%.9f"
    )

    # 404.31 Compute R² for both fits against the same observed EEI values.
    quadratic_residual_sum_squares = np.sum(
        (plot_data["EEI"] - plot_data["quadratic_fit"]) ** 2
    )
    linear_residual_sum_squares = np.sum(
        (plot_data["EEI"] - plot_data["linear_fit"]) ** 2
    )
    total_sum_squares = np.sum((plot_data["EEI"] - plot_data["EEI"].mean()) ** 2)
    if total_sum_squares > 0:
        quadratic_r_squared = 1 - quadratic_residual_sum_squares / total_sum_squares
        linear_r_squared = 1 - linear_residual_sum_squares / total_sum_squares
    else:
        quadratic_r_squared = linear_r_squared = float("nan")

    # 404.32 Create the canvas and axes for the Figure 404 plot.
    fig, ax = plt.subplots(figsize=(13, 9))
    # 404.33 Draw the averaged EEI observations as a red line.
    ax.plot(
        plot_data["date"],
        plot_data["EEI"],
        color="#b22222",  
        linewidth=3.5,
        label=f"CERES EEI {window_months}-month average",
    )
    # 404.34 Add the quadratic trend as a dashed purple line.
    ax.plot(
        plot_data["date"],
        plot_data["quadratic_fit"],
        color="purple",
        linestyle="--",
        linewidth=2.5,
        label="Quadratic fit",
    )
    # 404.35 Add the linear comparison as a dotted green line.
    ax.plot(
        plot_data["date"],
        plot_data["linear_fit"],
        color="#228B22",
        linestyle=":",
        linewidth=2.5,
        label="Linear fit",
    )

    # 404.36 Use axes-relative placement so annotations stay inside the plot.
    annotation_style = {
        "transform": ax.transAxes,
        "va": "top",
        "fontsize": 14,
        "bbox": {"facecolor": "white", "alpha": 0.9, "edgecolor": "#777777"},
    }
    # 404.37 Identify the figure, averaging window, repository, and version.
    ax.text(
        0.02,
        0.98,
        (
            f"Figure 404 ({window_months}-month average)\n"
            f"https://github.com/Boettcher1960/5_CO2_EEI_T      version  {v}"
        ),
        color="black",
        **annotation_style,
    )
    # 404.38 Display the quadratic equation and its goodness-of-fit value.
    ax.text(
        0.02,
        0.84,
        (
            f"EEI = {coefficients[0]:.6f}(year - {x_anf})^2 "
            f"{coefficients[1]:+.6f}(year - {x_anf}) "
            f"{coefficients[2]:+.6f} W/m²\n"
            f"Quadratic R² = {quadratic_r_squared:.4f} dashed purple"
        ),
        color="purple",
        **annotation_style,
    )
    # 404.39 Display the linear equation and its goodness-of-fit value.
    ax.text(
        0.02,
        0.71,
        (
            f"EEI = {linear_coefficients[0]:.6f}(year - {x_anf}) "
            f"{linear_coefficients[1]:+.6f} W/m²\n"
            f"Linear R² = {linear_r_squared:.4f} dotted"
        ),
        color="green",
        **annotation_style,
    )

    # 404.40 Build the headline with the averaging period and displayed year range.
    headline = (
        f"CERES Earth Energy Imbalance ({window_months}-month average) "
        f"     plotted years {x_anf} to {x_end}"
    )
    # 404.41 Specify the desired distance from the figure's top edge in points.
    headline_margin_points = 30
    # 404.42 Convert figure height from inches to points for positioning.
    figure_height_points = fig.get_figheight() * 72
    # 404.43 Add the headline before layout so its final position can be measured.
    headline_artist = fig.suptitle(
        headline,
        fontsize=20,
        y=1 - headline_margin_points / figure_height_points,
        va="top",
    )

    # 404.44 Label the horizontal axis with calendar year.
    ax.set_xlabel("year", fontsize=16, fontweight="black")
    # 404.45 Label the vertical axis with the EEI units.
    ax.set_ylabel("EEI (W/m²)", fontsize=16, fontweight="bold")
    # 404.46 Keep y-axis tick labels smaller than the axis title.
    ax.tick_params(axis="y", labelsize=12)
    # 404.47 Add unlabeled horizontal minor grid positions every 0.05 W/m².
    ax.yaxis.set_minor_locator(MultipleLocator(0.05))
    ax.tick_params(
        axis="y", which="minor",
        left=False, right=False, labelleft=False, labelright=False,
    )
    # 404.48 Keep y tick labels at normal weight and apply configured y bounds.
    for label in ax.get_yticklabels():
        label.set_fontweight("normal")
    ax.set_ylim(y_61min, y_61max)
    # 404.49 Mark every fifth year as a major tick and label.
    ax.xaxis.set_major_locator(mdates.YearLocator(5))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
    # 404.50 Add yearly minor ticks and labels between the five-year marks.
    ax.xaxis.set_minor_locator(mdates.YearLocator(1))
    ax.xaxis.set_minor_formatter(mdates.DateFormatter("%Y"))
    # 404.51 Style the five-year labels with the larger, heavier type.
    for label in ax.xaxis.get_majorticklabels():
        label.set_fontweight("black")
        label.set_fontsize(12)
    # 404.52 Style the intervening annual labels smaller and lighter.
    for label in ax.xaxis.get_minorticklabels():
        label.set_fontweight("normal")
        label.set_fontsize(9)
    # 404.53 Set the color used for major horizontal grid lines.
    mcolor="#9F2044"
    ax.grid(True, axis="y", which="major", color=mcolor, alpha=0.4, linewidth=1.3)
    # 404.54 Draw thinner black horizontal minor grid lines.
    ax.grid(True, axis="y", which="minor", color="black", alpha=0.25, linewidth=0.5)

    # 404.55 Draw the five-year vertical grid lines.
    ax.grid(True, axis="x", which="major", alpha=0.55, linewidth=1.5)
    # 404.56 Draw lighter vertical grid lines for individual years.
    ax.grid(True, axis="x", which="minor", alpha=0.3, linewidth=0.7)
    # 404.57 Show the yearly minor tick labels along the bottom edge.
    ax.tick_params(axis="x", which="minor", labelbottom=True)
    # 404.58 Let Matplotlib position the legend to avoid plotted data where possible.
    ax.legend(loc="best")
    # 404.59 Restrict the horizontal axis to the configured start and end years.
    ax.set_xlim(
        pd.Timestamp(year=x_anf, month=1, day=1),
        pd.Timestamp(year=x_end, month=12, day=31),
    )

    # 404.60 Rotate date labels as needed to prevent crowding.
    fig.autofmt_xdate()
    # 404.61 Apply Matplotlib's initial spacing before measuring the headline.
    fig.tight_layout()
    # 404.62 Render once so the headline's bounding box can be measured.
    fig.canvas.draw()
    renderer = fig.canvas.get_renderer()
    # 404.63 Measure the headline's top margin in points.
    headline_bbox = headline_artist.get_window_extent(renderer)
    top_margin_points = (fig.bbox.y1 - headline_bbox.y1) * 72 / fig.dpi
    # 404.64 Adjust the headline to the requested top margin.
    headline_artist.set_y(
        headline_artist.get_position()[1]
        + (top_margin_points - headline_margin_points) / figure_height_points
    )
    # 404.65 Re-render after moving the headline to refresh its measured bounds.
    fig.canvas.draw()
    headline_bbox = headline_artist.get_window_extent(fig.canvas.get_renderer())
    # 404.66 Convert the requested headline-to-plot gap from points to pixels.
    gap_pixels = headline_margin_points * fig.dpi / 72
    # 404.67 Calculate the plot area's top edge below the headline and gap.
    plot_top = (
        headline_bbox.y0 - gap_pixels - fig.bbox.y0
    ) / fig.bbox.height
    # 404.68 Read the current axes rectangle before changing its height.
    axes_position = ax.get_position()
    # 404.69 Keep the axes width and bottom while moving its top below the headline.
    ax.set_position(
        (
            axes_position.x0,
            axes_position.y0,
            axes_position.width,
            plot_top - axes_position.y0,
        )
    )
    # 404.70 Create the output folder if it does not already exist.
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    # 404.71 Save a high-resolution image, including labels outside the axes.
    fig.savefig(output_path, dpi=300, bbox_inches="tight")

    # 404.72 Print the quadratic fit equation and R-squared value.
    print(
        "Figure 404 quadratic fit: "
        f"EEI = {coefficients[0]:.9f}(year - {x_anf})^2 "
        f"{coefficients[1]:+.9f}(year - {x_anf}) "
        f"{coefficients[2]:+.9f} W/m²; "
        f"R² = {quadratic_r_squared:.6f}"
    )
    # 404.73 Print the linear fit equation and R-squared value.
    print(
        "Figure 404 linear fit: "
        f"EEI = {linear_coefficients[0]:.9f}(year - {x_anf}) "
        f"{linear_coefficients[1]:+.9f} W/m²; "
        f"R² = {linear_r_squared:.6f}"
    )
    # 404.74 Report where the generated image was saved.
    print(f"Saved Figure 404 to {output_path}")
    # 404.75 Report where the fitted monthly quadratic series was saved.
    print(f"Saved monthly quadratic values to {forecast_output_path}")
    # 404.76 Display the figure interactively.
    plt.show()
    # 404.77 Release the figure resources after it has been shown.
    plt.close(fig)



# part 62.c  CERES.csv (perform averaging) create_running_average(input_csv, output_csv, 
def create404_running_average(input_csv, 
                           output_csv, 
                           window_months,   # figure404
                          min_periods=None, 
                          center=True, 
                          keep_original=True,
                          column_name='EEI'):
    """Create a running average with forward and backward averages at the edges."""
    df = pd.read_csv(input_csv)
    df['date'] = pd.to_datetime(df['date'])
    df = df.sort_values('date').reset_index(drop=True)
    
    if min_periods is None:
        min_periods = window_months

    if figure404 == 3:
        min_periods = 2

    # 404.110 Keep the source series and calculate its regular middle average.
    source_values = df['toa_net_flux_w_m2']
    averaged_values = source_values.rolling(
        window=window_months, 
        center=center,
        min_periods=min_periods
    ).mean()

    # 404.120 Use forward averages at the beginning and backward averages at the end.
    edge_rows = window_months + 4    # edge_rows = figure404 + 4 = 48+4 = 52
    if len(df) < 2 * edge_rows:
        raise ValueError(
            f"At least {2 * edge_rows} monthly records are required for "
            f"non-overlapping {edge_rows}-month edge regions; found {len(df)}."
        )
    # 404.130 foreward_average is special with a sharp step
    #      EEI= 0.591875   2004.458333 
    #      EEI= 0.427917   2004.541667
    forward_average = (
        source_values.iloc[::-1]
        .rolling(window=window_months, min_periods=window_months)
        .mean()
        .iloc[::-1]
        .reset_index(drop=True)
    )
    # 404.140 backward_average is the normal average
    backward_average = source_values.rolling(
        window=window_months, min_periods=window_months
    ).mean()
    # 404.150 the first 48 months
    averaged_values.iloc[:edge_rows] = forward_average.iloc[:edge_rows]

    # 404.152 48 months # edge_rows = figure404 + 4 = 48+4 = 52
    if print_debug > 19:
        print(f"ceres__4: EEI= { averaged_values.values[edge_rows-4] } index {edge_rows-4}")
        print(f"ceres__3: EEI= { averaged_values.values[edge_rows-3] } index {edge_rows-3}")
        print(f"ceres__2: EEI= { averaged_values.values[edge_rows-2] } index {edge_rows-2}")
        print(f"ceres__1: EEI= { averaged_values.values[edge_rows-1] } index {edge_rows-1}")
        print(f"ceres___:       step")
        print(f"ceres__0: EEI= { averaged_values.values[edge_rows] } index {edge_rows}")
        print(f"ceres_+1: EEI= { averaged_values.values[edge_rows+1] } index {edge_rows+1}")
        print(f"ceres_+2: EEI= { averaged_values.values[edge_rows+2] } index {edge_rows+2}")
        print(f"ceres_+3: EEI= { averaged_values.values[edge_rows+3] } index {edge_rows+3}")
    v1 =  averaged_values.values[edge_rows-4]  
    v2 =  averaged_values.values[edge_rows-3]  
    v3 =  averaged_values.values[edge_rows-2]  
    v4 =  averaged_values.values[edge_rows-1]  
    v5 =  averaged_values.values[edge_rows]  
    v6 =  averaged_values.values[edge_rows+1]  
    v7 =  averaged_values.values[edge_rows+2]     
    v8 =  averaged_values.values[edge_rows+3]   
    #    ceres__4: EEI= 0.5139583333333334 index 48 bad v1
    #    ceres__3: EEI= 0.5554166666666667 index 49 bad v2
    #    ceres__2: EEI= 0.5435416666666667 index 50 bad v3
    #    ceres__1: EEI= 0.5918749999999999 index 51 bad v4
    #    ceres___:       step
    #    ceres__0: EEI= 0.42791666666666667 index 52  ok v5
    #    ceres_+1: EEI= 0.42812500000000003 index 53  ok v6
    #    ceres_+2: EEI= 0.44604166666666667 index 54  ok v7
    #    ceres_+3: EEI= 0.43979166666666664 index 55  ok v8
    # __: EEI= 0.5139583333333334  0.5554166666666667  0.5435416666666667  0.5918749999999999  
    #          0.42791666666666667  0.42812500000000003  0.44604166666666667   
    if print_debug > 9:
        print(f"__: EEI= { v1 }  { v2 }  { v3 }  { v4 } step { v5 }  { v6 }  { v7 }   { v8 } ")

        # averaged_values.index[edge_rows-1] = index = 51 = edge_rows-1}
        # averaged_values.values[edge_rows-1]

    # 404.154 after 48 months
    averaged_values.iloc[-edge_rows:] = backward_average.iloc[-edge_rows:]

    # 404.160 correct ceres__3: EEI= 0.5554166666666667 index 49 bad
    # 404.162 correct  ceres__2: EEI= 0.5435416666666667 index 50 bad v3
    # 404.164 ceres__1: EEI= 0.5918749999999999 index 51 bad v4
    # averaged_values.values[edge_rows-1] = ( v5 + v6 + v7 + v4 )/4
    averaged_values.values[edge_rows-5] = ( v4 + v4 + v4 + v4 + v4   + v5 )/6
    averaged_values.values[edge_rows-4] = ( v4 + v4 + v4 + v4   + v5 + v5 )/6
    averaged_values.values[edge_rows-3] = ( v4 + v4 + v4   + v5 + v5 + v5 )/6
    averaged_values.values[edge_rows-2] = ( v4 + v4   + v5 + v5 + v5 + v5 )/6
    averaged_values.values[edge_rows-1] = ( v4  + v5  + v5 + v5 + v5 + v5 )/6

    if print_debug > 9:
           print(f"ceres__4: EEI= { averaged_values.values[edge_rows-4] } index {edge_rows-4}")
           print(f"ceres__3: EEI= { averaged_values.values[edge_rows-3] } index {edge_rows-3}")
           print(f"ceres__2: EEI= { averaged_values.values[edge_rows-2] } index {edge_rows-2}")
           print(f"ceres__1: EEI= { averaged_values.values[edge_rows-1] } index {edge_rows-1}")
           print(f"ceres___:       step")
           print(f"ceres__0: EEI= { averaged_values.values[edge_rows] } index {edge_rows}")
           print(f"ceres_+1: EEI= { averaged_values.values[edge_rows+1] } index {edge_rows+1}")


    # 404.170 copy to df field column_name='EEI'
    df[column_name] = averaged_values

    # 404.160 48 months # edge_rows = figure404 + 4 = 48+4 = 52
    #      EEI= 0.591875   2004.458333 
    #      EEI= 0.427917   2004.541667
    
    

    # 404.180 configure the output csv 
    output_columns = ['date', 'year', 'month', 'decimal_year']
    if keep_original:
        output_columns.append('toa_net_flux_w_m2')
    output_columns.append(column_name)
    
    df_output = df[output_columns].copy()
    df_output.to_csv(output_csv, index=False, float_format='%.6f')
    
    valid_records = df_output[column_name].notna().sum()
    #print(f"{window_months}-month running average saved to {output_csv}")
    #print(f"Valid records: {valid_records} out of {len(df_output)}")
    if print_debug > 9:
        print(f"ceres935: Valid records: {valid_records} out of {len(df_output)}")
        print(f"ceres936: {window_months}-month running average saved to {output_csv} ")
    return df_output
    # end part 62.c  CERES.csv (perform averaging)
