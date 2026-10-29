# models.py
# version 5G50
# includes the documentation

import numpy as np
import pandas as pd
from config import *


C280 = 280




def T_model76(t):
    """My best temperature model"""
    x = t - 2000
    return 0.00034 * x**2 + 0.0238 * x + 0.74






#########################################################
# plot22_CO2_Mauna_Loa  ##############################
#########################################################
# https://gml.noaa.gov/webdata/ccgg/trends/co2/co2_annmean_mlo.txt
#                           2023   421.08     0.12
#                           2024   424.61     0.12    add+3.53
#                           2025   427.35     0.12    add+2.74
#                           https://gml.noaa.gov/ccgg/trends/mlo.html
#                           https://gml.noaa.gov/ccgg/trends/global.html
#                           part 2.3 plot23_Glen_CO2 
# 2026.10.15 plots using plot22_CO2_Mauna_Loa = 2
#
# part 2.5 plot25_long_CO2  -800 000 years ppm CO2 file



#########################################################
# plot23_Glen_CO2  ##############################
#########################################################
# CO2 concentration in ppm   CO2= 0.0132t² - 51t + 49,536   (CO2 emission linear)  23
#  plot23_Glen_CO2 = 0.013t² - 51t + 49,536 in dark blue 
#  source a plot with the formula explained in a thread
#  source https://x.com/Gergyl/status/1810632238230589564
# 2026.10.15 plots using plot23_Glen_CO2 = 2 
# 2026.10.15 plots using plot23_Glen_CO2 = 3 




# plot24 ist frei

#########################################################
# plot25_long_CO2  ##############################
#########################################################
# plot25_long_CO2 = 2      # 2, 3 25.1 
#  part 2.5 plot25_long_CO2  -800 000 years ppm CO2 file
# 2026.10.15 plots using plot25_long_CO2 = 2
# 2026.10.15 plots using plot25_long_CO2 = 3




#########################################################
# plot31_CO2_emission  ##############################
#########################################################
# plot31_CO2_emission =    3 
# 2026.10.15 plots using plot31_CO2_emission = 2
# 2026.10.15 plots using plot31_CO2_emission = 3 
# 2026.10.15 plots using plot31_CO2_emission = 4 



#########################################################
# plot31_CO2_emission  ##############################
#########################################################
# plot31_CO2_emission = 2, 3 
# 2026.10.15 plots using 


#########################################################
# plot32_CO2_emission  ##############################
#########################################################
# plot32_CO2_emission = 2, 3 
# 2026.10.15 plots using 3


#########################################################
# plot34_CO2  3 variable is complex
#   ##############################
#########################################################
# plot34_CO2_emission =    4   # 34.1 row 4 
# plot34_CO2_emission_mode = 4 # 2, 4 34.1 mode 
#      plot31__CO2_emission mode 1 # plot32__CO2_emission mode 2 # plot33__CO2_emission mode 3
# plot34_CO2_emission_mode = 2 # 34.1 mode 
# plot34_CO2 = 0
#
# 2026.10.15 plots using   plot34_CO2_emission = 4  plot34_CO2_emission_mode = 4
# bug 2 Yachsen auf der rechten Seite
# 2026.10.15 plots using    plot34_CO2_emission = 4  plot34_CO2_emission_mode = 4 plot34_CO2 = 0


#################################################################
# 41 process 4 CERES files 
#################################################################
#  open https://ceres-tool.larc.nasa.gov/ord-tool/srbavg
#      select file 3 
# 41.2 download CERES_EBAF-TOA_Ed4.2.1_TOA_Net_Flux_-_All-Sky_March-2000toAugust-2026.txt
# 41.3 copy txt to work/_61_in__2026_08_EEI_CERES.txt
#      select file 1
# 41.6 download CERES_EBAF-TOA_Ed4.2.1_TOA_Shortwave_Flux_-_All-Sky_March-2000toAugust-2026.txt
# 41.7 copy txt to work/_66_TOA_Shortwave_Flux_All_Sky2026_08.txt
#      select file 2
# 41.10 download CERES_EBAF-TOA_Ed4.2.1_TOA_Longwave_Flux_-_All-Sky_March-2000toAugust-2026.txt
# 41.11 copy txt to work/_66_TOA_OLR_all_sky_2026_08.txt
#      select file 4
# 41.14 download CERES_EBAF-TOA_Ed4.2.1_Incoming_Solar_Flux_March-2000toAugust-2026.txt
# 41.15 copy txt to work/_66_TOA_Incoming_Solar_2026_08.txt
############################ play_66_OLR = 48 #####################################
# 41.17 in config.py set play_66_OLR = 48 
# 41.18 in main.py  line 164       df66b = convert66_txt_to_csv('work/_66_TOA_OLR_all_sky_2026_07.txt', 
# 41.19 in main.py  line 164       df66b = convert66_txt_to_csv('work/_66_TOA_OLR_all_sky_2026_08.txt', 
# 41.20                                         the new file     work/66c_OLR.csv has the column OLR48
# 41.21 copy the new file  work/66c_OLR.csv has the column OLR48
# 41.22 to   read_csv/_45_OLR_48month_2026_08.csv
# 41.23 old in main.py  line 311     data['ceres_45'] = pd.read_csv("read_csv/_45_OLR_48month_2026_07.csv")
# 41.24 new in main.py  line 311     data['ceres_45'] = pd.read_csv("read_csv/_45_OLR_48month_2026_08.csv")
############################ play_67_albedo = 48 #####################################
# 41.25 no good in config.py set play_65_ASR = 48
# 41.26 config.py set play_67_albedo = 48
# 41.27 old in data_processing.py  line 307   with open('read_csv/_66_TOA_Shortwave_Flux_All_Sky2026_07.txt', 'r') as f:
# 41.28 new in data_processing.py  line 307   with open('work/_66_TOA_Shortwave_Flux_All_Sky2026_08.txt', 'r') as f:
# 41.29 old in data_processing.py  line 338   with open('read_csv/_66_TOA_Incoming_Solar_2026_07.txt', 'r') as f:
# 41.30 new in data_processing.py  line 338   with open('work/_66_TOA_Incoming_Solar_2026_08.txt', 'r') as f:
# 41.31 old in data_processing.py  line 361   with open('read_csv/_67_EEI_TOA_Net_Flux_2026_07.txt', 'r') as f:
# 41.32 new in data_processing.py  line 361   with open('work/_61_in__2026_08_EEI_CERES.txt', 'r') as f:
# 41.33 old in data_processing.py  line 387   with open('read_csv/_67_TOA_Longwave_Flux_2026_07.txt', 'r') as f:
# 41.34 new in data_processing.py  line 387   with open('work/_66_TOA_OLR_all_sky_2026_08.txt', 'r') as f:
############################ plot46_ASR = 2 #####################################
# 41.38  copy dokumente/5_CO2_EEI_T/work/_CERES_ASR.csv to
# 41.39       dokumente/5_CO2_EEI_T/read_csv/_46_ASR_48month_2026_08.csv
# 41.40 old in main.py  line 315      data['ceres_46'] = pd.read_csv("read_csv/_46_ASR_48month_2026_07.csv")
# 41.41 new in main.py  line 315      data['ceres_46'] = pd.read_csv("read_csv/_46_ASR_48month_2026_08.csv")                                               
############################ plot42_EEI_48month #####################################
# 41.43 old in main.py  line 64  df61b = convert_ceres_to_csv('read_csv/_61_in__2026_07_EEI_CERES.txt', 
# 41.44 new in main.py  line 64  df61b = convert_ceres_to_csv('work/61_in__2026_08_EEI_CERES.txt',   
# 41.45 new in main.py  line 65                               'work/61b_out_in_ceres.csv')
# 42.46 run with play_61_EEI = 48
# 42.47 copy           work/61c_out_EEI.csv to 
# 42.48      read_csv/_42_EEI48month_2026_08.csv
# 41.49 old in main.py  line 298      data['ceres_42'] = pd.read_csv("read_csv/_42_EEI48month_2026_07.csv")
# 41.50 new in main.py  line 298      data['ceres_42'] = pd.read_csv("read_csv/_42_EEI48month_2026_08.csv")
# 41.51 works with august data plot42_EEI_48month = 4 
############################ plot43_eei_12month #####################################
# 41.52 set    play_61_EEI = 12 
# 41.53 set    plot43_eei_12month = 4 
# 41.54 old in main.py  line 339      data['ceres_61'] = pd.read_csv("read_csv/_61c_out_ceres.csv")
# 41.55 new in main.py  line 339      data['ceres_61'] = pd.read_csv("work/61c_out_EEI.csv")
# 41.56 copy           work/61c_out_EEI.csv to 
# 41.57  to    read_csv/_43_EEI12month_2026_08.csv
############################ plot47_albedo48 #####################################
# 41.58 run with play_67_albedo = 48
# 41.59 copy dokumente/5_CO2_EEI_T/work/_CERES_albedo.csv to
# 41.60      dokumente/5_CO2_EEI_T/read_csv/_47_albedo_48month_2026_08.csv
# 41.61 old in main.py  line 320      data['ceres_47'] = pd.read_csv("read_csv/_47_albedo_48month_2026_07.csv")
# 41.62 new in main.py  line 320      data['ceres_47'] = pd.read_csv("read_csv/_47_albedo_48month_2026_08.csv")
#




#################################################################
# plot42_EEI_48month ############################################
############### see 41 process 4 CERES files ####################
# 42.1 open https://ceres-tool.larc.nasa.gov/ord-tool/srbavg
# 41.2 download CERES_EBAF-TOA_Ed4.2.1_TOA_Net_Flux_-_All-Sky_March-2000toAugust-2026.txt
# 41.3 copy txt to work/_61_in__2026_08_EEI_CERES.txt
# 42.4 run with play_61_EEI = 48
# 42.6 copy to read_csv/_42_EEI48month_2026_08.csv
# 42.8 set plot42_EEI_48month = 3  # 2,3,4,5 print EEI 48 month running mean
# 2026.10.15 plots  plot42_EEI_48month = 2
# 2026.10.15 plots  plot42_EEI_48month = 3
# 2026.10.20 plots  plot42_EEI_48month = 4


#################################################################
# plot43_eei_12month ############################################
############### see 41 process 4 CERES files ####################
# 43.1 open https://ceres-tool.larc.nasa.gov/ord-tool/srbavg
# 41.2 download CERES_EBAF-TOA_Ed4.2.1_TOA_Net_Flux_-_All-Sky_March-2000toAugust-2026.txt
# 41.3 copy txt to work/_61_in__2026_08_EEI_CERES.txt
# 41.52 set    play_61_EEI = 12 
# 42.56 copy           work/61c_out_EEI.csv to 
# 42.57  to    read_csv/_43_EEI12month_2026_08.csv
# 2026.10.15 plots plot43_eei_12month = 2
# 2026.10.15 plots plot43_eei_12month = 3
# 2026.10.20 plots plot43_eei_12month = 4


#################################################################
# part44_ceres_eei ############################################
############### old EEI processing ####################
# 44.1 open https://ceres-tool.larc.nasa.gov/ord-tool/srbavg
# 44.2 download CERES_EBAF-TOA_Ed4.2.1_TOA_Net_Flux_-_All-Sky_March-2000toJuly-2026.txt
# 44.3 copy txt to read_csv/_61_in__2026_07_EEI_CERES.txt
# 44.4 run with play_61_EEI = 12 the file /_61c_out_ceres.csv is produced 
#    /_61c_out_ceres.csv column EEI has the 12 month average
# 44.5 copy           tbd read_csv/_61c_out_ceres.csv
# 44.6 paste to        work/c44d_ceres.csv
# 2026.10.15 plots part44_ceres_eei = 3   # makes 3 month average
# 2026.10.15 plots part44_ceres_eei = 47  # makes same 12 month average best
# 2026.10.15 plots part44_ceres_eei = 36  # makes same 3 month average


#########################################################
# 45_OLR_48month_2026_07.csv ############################
#########################################################
# 1 open https://ceres-tool.larc.nasa.gov/ord-tool/srbavg
# 41.10 download CERES_EBAF-TOA_Ed4.2.1_TOA_Longwave_Flux_-_All-Sky_March-2000toAugust-2026.txt
# 41.11 copy txt to work/_66_TOA_OLR_all_sky_2026_08.txt
# 41.17 in config.py set play_66_OLR = 48 
# 41.21 copy the new file  work/66c_OLR.csv has the column OLR48
# 41.22 to   read_csv/_45_OLR_48month_2026_08.csv
# plot45_OLR = 2 # 2, 3, 4 looks like simons 48 months. Outgoing Longwave Radiation OLR updated to 2026_07
# 2026.10.15 plots plot45_OLR = 2
# 2026.10.15 plots plot45_OLR = 3
# 2026.10.20 plots plot45_OLR = 3


#########################################################
# 46     plot46_ASR          ############################
#########################################################
# 1 open https://ceres-tool.larc.nasa.gov/ord-tool/srbavg
# 41.6 download CERES_EBAF-TOA_Ed4.2.1_TOA_Shortwave_Flux_-_All-Sky_March-2000toAugust-2026.txt
# 41.7 copy txt to work/_66_TOA_Shortwave_Flux_All_Sky2026_08.txt
# 41.14 download CERES_EBAF-TOA_Ed4.2.1_Incoming_Solar_Flux_March-2000toAugust-2026.txt
# 41.15 copy txt to work/_66_TOA_Incoming_Solar_2026_08.txt
# 41.26 config.py set play_67_albedo = 48
#       dokumente/5_CO2_EEI_T/work/_CERES_raw.csv is produced with column ASR
# 46.28 copy dokumente/5_CO2_EEI_T/work/_CERES_ASR.csv to
#            dokumente/5_CO2_EEI_T/read_csv_46_ASR_48month_2026_08.csv
# 46.30 looks like https://bsky.app/profile/leonsimons.com/post/3mwy3xgypts2y
#       line DataP423 df2['ASR'] = df2['sw_in'] - df2['sw_out']
# 2026.10.15 plots plot46_ASR = 2
# 2026.10.15 plots plot46_ASR = 3
# 2026.10.20 plots plot46_ASR = 2


#########################################################
# plot47_albedo48 ############################
#########################################################
# 47.1 open https://ceres-tool.larc.nasa.gov/ord-tool/srbavg
# 41.6 download CERES_EBAF-TOA_Ed4.2.1_TOA_Shortwave_Flux_-_All-Sky_March-2000toAugust-2026.txt
# 41.7 copy txt to work/_66_TOA_Shortwave_Flux_All_Sky2026_08.txt
# 41.14 download CERES_EBAF-TOA_Ed4.2.1_Incoming_Solar_Flux_March-2000toAugust-2026.txt
# 41.15 copy txt to work/_66_TOA_Incoming_Solar_2026_08.txt
# 41.58 run with play_67_albedo = 48
# 41.59 copy dokumente/5_CO2_EEI_T/work/_CERES_albedo.csv to
# 41.60      dokumente/5_CO2_EEI_T/read_csv/_47_albedo_48month_2026_08.csv
# 2026.10.15 plots plot47_albedo48 = 4
# 2026.10.20 plots plot47_albedo48 = 4

#########################################################
# 48   plank48_= 5 #       plank feedback   #############
#########################################################
# https://substack.com/home/post/p-221922327 Figure 3
# Tom Harris starts at Februar 2003 plank surface radiation 0...2.5W/m/m
# 4year averge era4 T is 0.74°C  0.740300°C
# plank48_= 5 # plank feedback is 68_ERA temperature * 3.22
# run play68_ERA = 1461 creates work/_68_out.csv create68_running_average()
# copy /_68_out.csv to work/_48_era5_in.csv
#
#
#
def load48_plank_T():
    return pd.read_csv("work/_48_era5_in.csv")
#




#########################################################
# plot52_delta_CO2_red_bars ############################
#########################################################
# delta 2025 = 2.74 ppm
# 
# 2026.10.15 plots plot52_delta_CO2_red_bars = 3 # (3=print numbers)


#--------------------------------------------------------
# plot53_CO2_orange2025 ---------------------------------
#--------------------------------------------------------
# plot53_CO2_orange2025 = 3 # no curve is visible 3# 
# plot53_CO2_orange2025 = 4 # no curve is visible


#--------------------------------------------------------
# plot54_Glen_delta_on ---------------------------------
#--------------------------------------------------------
# plot54_Glen_delta_on = 4 # no curve is visible 3, 4 



#########################################################
# 55     plot55_population_on ###########################
#########################################################
# text55 = "Green line: Earth Population in billion                                               55"
# plot55_population_on = 5 # 5 word with y axis right
#
# 2026.10.15 plots plot55_population_on = 5 # 5 word with y axis right



#--------------------------------------------------------
# plot56_delta_CO2_4years ---------------------------------
#--------------------------------------------------------
# plot56_delta_CO2_4years = 3 # no curve is visible 3, 4 




#########################################################
# 61    play_61_EEI = 12   ##############################
#########################################################
#--- see 41 process 4 CERES files ---------------------
# 61.1 open https://ceres-tool.larc.nasa.gov/ord-tool/srbavg
# https://ceres-tool.larc.nasa.gov/ord-tool/srbavg
# 61.2  https://ceres.larc.nasa.gov/data/
# 61.3 https://ceres-tool.larc.nasa.gov/ord-tool/jsp/EBAFTOA421Selection.jsp
# 61.4 t.boettcher@directbox.com enter email adress
# 61.5 Order Data - left mouse click
# 61.6 select
# 61.7 global mean
# 61.8 Visualize Data - left mouse click
# 61.9 global mean https://ceres-tool.larc.nasa.gov/ord-tool/srbavg
# 61.10 select first item
# 61.11 CERES_EBAF-TOA_Ed4.2.1 - Global Data Charts up to Feb. 2026 is shown
# 61.12 six small curves are shown
# 61.13 select item 3 Label TOA Net Flux All Sky -10 to +10 W/m/m monthly values
# 61.14 big window appears with one curve only
# 61.15 left mouse select save Data as ASCII File
# 61.16.1 CERES_EBAF-TOA_Ed4.2.1_TOA_Net_Flux_-_All-Sky_March-2000toFebruary-2026.txt is downloaded
# 61.16.2 CERES_EBAF-TOA_Ed4.2.1_TOA_Net_Flux_-_All-Sky_March-2000toJuly-2026.txt is downloaded
# 61.17.1 rename      to _61_in__2026_02_EEI_CERES.txt and save to dokumente/5_CO2_EEI_T/read_csv/
# 61.17.2 rename      to _61_in__2026_07_EEI_CERES.txt and save to dokumente/5_CO2_EEI_T/read_csv/
# 61.18 run with play_61_EEI = 48 
# 61.19 copy dokumente/5_CO2_EEI_T/read_csv/_61c_out_ceres.csv to
# 61.20.1      dokumente/5_CO2_EEI_T/read_csv/_42_EEI48month_2026_02.csv
# 61.20.2                           'read_csv/_42_EEI48month_2026_07.csv', 
# 61.21 run   plot42_EEI_48month=2 reading new _42_EEI48month_2026_02.csv file
# 
# 61.22 run with play_61_EEI = 12 
# 61.23 copy dokumente/5_CO2_EEI_T/read_csv/_61c_out_ceres.csv.csv to
#       dokumente/5_CO2_EEI_T/read_csv/_43_EEI12month_2026_02.csv
# 61.24 run   plot43_eei_12month=3 reading new _43_EEI12month_2026_02.csv file
#
# 2026.10.25 plots play_61_EEI = 12    # 12, 24, 36, 48 create 1..12..48..99 CERES EEI.csv 
####### o k ##################################################


##################################################################
# 62     play_62_EEA = 12       Earth Energy Accumulated #########
##################################################################
# --- see 41 process 4 CERES files ---------------------
# ----------------------------------------------
# old 62.21 open
# https://ceres-tool.larc.nasa.gov/ord-tool/srbavg
#  old_62.22 select first item
#  old_62.23 CERES_EBAF-TOA_Ed4.2.1 - Global Data Charts up to Feb. 2026 is shown
#  old_62.24 six small curves are shown
#  old_62.25 select item 2 Label TOA Long Wave Flux All Sky 235 to 245 W/m/m monthly values
#  old_62.26 big window appears with one curve only
#  old_62.27 left mouse select save Data as ASCII File
#  old_62.28.1 CERES_EBAF-TOA_Ed4.2.1_TOA_Longwave_Flux_-_All-Sky_March-2000toFebruary-2026.txt is downloaded
#  old_62.28.2 CERES_EBAF-TOA_Ed4.2.1_TOA_Longwave_Flux_-_All-Sky_March-2000toJuly-2026.txt is downloaded
#  old_62.29.1 rename      to _62_in__2026_02_Longwave.txt and save to dokumente/5_CO2_EEI_T/read_csv/
#  old_62.29.2 rename      to _66_TOA_OLR_all_sky_2026_07.txt and save to dokumente/5_CO2_EEI_T/work/
#  old_62.30.1 run with play_62_CERES = 48
#    read read_csv/_62_in__2026_02_Longwave.txt main 124
#    output1 read_csv/_62b_LongWave.csv'
#  old_62.30.2 run with play_66_OLR = 48
#  old_62.31.1 run with play_62_CERES = 48
#    input1  read_csv/_62_in__2026_02_Longwave.txt main 124
#    input2  read_csv/_42_EEI48month_2026_02.csv   main 141
#    output2 read_csv/_62c_LongWave.csv with column LongWave for  48 month running average 
#    output3.1 read_csv/_62e_LongWave.csv with column EEI copy from input2 for  48 month running average 
#    output3.2 read_csv/_62e_LongWave.csv with column LongWave for  48 month running average 
#    output3.3 read_csv/_62e_LongWave.csv with column OLR_EEI = LongWave + EEI   48 month running average 
#  old_62.32.1 copy dokumente/5_CO2_EEI_T/read_csv/_62e_LongWave.csv to
#         dokumente/5_CO2_EEI_T/read_csv/_45_OLR_EEI_48month_2026_02.csv
#  old_62.32.2 copy dokumente/5_CO2_EEI_T/work/_66c_OLR.csv to
#           dokumente/5_CO2_EEI_T/read_csv/_45_OLR_48month_2026_07.csv file, column OLR48 
# Tom Harris on substack https://substack.com/@drtomharris/note/c-366539763
#     Thanks, yes it is a 36 month rolling average.
#     The EEA is simply a monthly rolling sum of the monthly (36m smoothed) EEI, 
#     then multiplied by a constant 16.087 to convert it to ZJ. 
#     1 W/m2 is 1 joule per second per square meter. 
#     The constant above is seconds per month x area of Earth / 10^21 (zeta)
#  python how to sum up 62c_EEA.csv column EEI36 and store it to new column EEA
#  1. CSV-Datei einlesen
#  df = pd.read_csv("62c_EEA.csv")
# 2. Laufende Summe (kumulierte Summe) bilden und in 'EEA' speichern
# df["EEA"] = df["EEI36"].cumsum()
# 3. CSV-Datei speichern
# df.to_csv("62c_EEA_aktualisiert.csv", index=False)
#  python how to sum up 62c_EEA.csv column EEI36 and multiply with 1.23    and store it to new column EEA
#      play_62_EEA = 12 line4_play = 62
# 2026.10.25 plots play_62_EEA = 12 line4_play = 62
####### o k ##################################################



##################################################################
# 63     play_63_CB = 5      Carbon Brief CO2 cummulated #########
##################################################################
# 63.1 open
# https://ourworldindata.org/grapher/cumulative-co-emissions?country=OWID_WR~OWID_WRL
# 63.2 select item world (a red hockex stick is visible 1.8tntCO2) (1800GtCO2)
# 63.3        Download item below the curve  
# 63.4        right item Data (not visualization)
# 63.5        Download displayed data with 275 rows
# 63.6        zip with cumulative-co-emissions.csv is downloaded
# 63.7        Duplizieren ; rename as work/63a_cumulative-co-emissions_world.csv
# 63.
# 63.
# 63.
#             play_63_CB =5=world     plan    play_63_CB=2=germany..
#
# 2026.10.25 plots   line3_play = 63 and play_63_CB = 5
####### o k ##########################################################



##################################################################
# 64    play_64_ASR_anomaly #########   _64_in__2026_02_ASR_anomaly.txt
##################################################################
# play_64_ASR_anomaly = 12 # absorbed solar radiation ASR = 1.48 W/m² 
# 64.1 open
# https://ceres-tool.larc.nasa.gov/ord-tool/srbavg
# 64.2 select first item
# 64.3 CERES_EBAF-TOA_Ed4.2.1 - Global Data Charts up to Aug. 2026 is shown
# 64.4 six small curves are shown
# 64.5 select item 1 Label TOA ShortWave Flux All Sky 90 to 110 W/m/m monthly values
# 64.6 big window appears with one curve only
# 64.7 left mouse select Show Anomaly
# 64.8 TOA ShortWave Flux All Sky -3 to 3 W/m/m monthly values shows
# 64.9 left mouse select save Data as ASCII File
#       CERES_EBAF-TOA_Ed4.2.1_anom_TOA_Shortwave_Flux_-_All-Sky_March-2000toAugust-2026.txt
# 64.10 CERES_EBAF-TOA_Ed4.2.1_anom_TOA_Shortwave_Flux_-_All-Sky_March-2000toFebruary-2026.txt is downloaded
# 64.11                                rename move     to work/64a_in__2026_08_ASR_anomaly.txt 
# 64.12 run with play_64_ASR_anomaly = 12
#    read     work/64a_in__2026_08_ASR_anomaly.txt   main.py 
#    output1 read_csv/_64b_ASR.csv')
#    output2 read_csv/_64c_ASR.csv'
# 53 copy dokumente/5_CO2_EEI_T/read_csv/_64c_ASR.csv to
#         dokumente/5_CO2_EEI_T/read_csv/_47_ASR_12month_2026_02.csv
# 54 run with play_64_ASR_anomaly = 48
#    read read_csv/_64_in__2026_02_ASR_anomaly.txt   main.py 
#    output1 read_csv/_64b_ASR.csv')
#    output2 read_csv/_64c_ASR.csv'
# 55 copy dokumente/5_CO2_EEI_T/read_csv/_64c_ASR.csv to
#         dokumente/5_CO2_EEI_T/read_csv/_48_ASR_48month_2026_02.csv
# plan txt to csv to png play 64 
# ocean stratification https://bsky.app/profile/thomas-boettcher.bsky.social/post/3mj7zx7fzsc26
# https://drtomharris.substack.com/p/the-great-decoupling-how-ocean-stratification
# http://www.ocean.iap.ac.cn/ftp/images_files/Stratification_global_time_series.txt
#
# https://www.nature.com/articles/s43247-026-03427-w#
# https://bsky.app/profile/thomas-boettcher.bsky.social/post/3miz5mmll3k2z
# 2026.10.25 plots   line3_play = 64 and play_64_ASR_anomaly = 12 
# 2026.10.25 plots   line3_play = 64 and play_64_ASR_anomaly = 24
# 2026.10.25 plots   line3_play = 64 and play_64_ASR_anomaly = 48 




#########################################################
# 67    play_67_albedo     ##############################
#########################################################
# Calculate Albedo: Compute planetary or surface albedo by 
# dividing the upward shortwave radiation flux (toa_sw_all) 
# by the incoming solar radiation (solar_mon).
#  67.1 open  https://ceres-tool.larc.nasa.gov/ord-tool/srbavg
#  67.2       https://ceres.larc.nasa.gov/data/
#  67.3       https://ceres-tool.larc.nasa.gov/ord-tool/jsp/EBAFTOA421Selection.jsp
#  67.4 t.boettcher@directbox.com enter email adress
#  67.5 Order Data - left mouse click
#  67.6 select
#  67.7 global mean
#  67.8 Visualize Data - left mouse click
#  67.9 global mean https://ceres-tool.larc.nasa.gov/ord-tool/srbavg
#  67.10 select first item
#  67.11 CERES_EBAF-TOA_Ed4.2.1 - Global Data Charts up to Feb. 2026 is shown
#  67.12 six small curves are shown
#  67.13 select item 1 Label TOA Shortwave Flux All Sky 90 to +110 W/m/m monthly values
#  67.14 big window appears with one curve only
#  67.15 left mouse select save Data as ASCII File
# 67.16 download CERES_EBAF-TOA_Ed4.2.1_TOA_Shortwave_Flux_-_All-Sky_March-2000toAugust-2026.txt
# 67.17 copy txt to work/_66_TOA_Shortwave_Flux_All_Sky2026_08.txt
# 67.18 select Parameter Solar Flux
# 67.19 global mean
# 67.20 Visualize Data - left mouse click
# 67.21 big window appears with one curve only 325 to 360 W/m2
# 67.22 left mouse click window gets big 328 to 352 W/m2
# 67.23 left mouse select save Data as ASCII File
# 67.24 download CERES_EBAF-TOA_Ed4.2.1_Incoming_Solar_Flux_March-2000toAugust-2026.txt
# 67.25 copy txt to work/_66_TOA_Incoming_Solar_2026_08.txt
# 67.30 download CERES_EBAF-TOA_Ed4.2.1_TOA_Net_Flux_-_All-Sky_March-2000toJuly-2026.txt
# 67.31 copy to 'read_csv/_67_EEI_TOA_Net_Flux_2026_07.txt'
# 67.35 download CERES_EBAF-TOA_Ed4.2.1_TOA_Longwave_Flux_-_All-Sky_March-2000toJuly-2026.txt
# 67.36 copy to 'read_csv/_67_EEI_TOA_Net_Flux_2026_07.txt'
# 67.31 with   play_67_albedo = 48  work/_CERES_albedo.csv is created with averaged albedo48 column
# 67.33 copy to work/_67_albedo48months_2026_08.csv'
# 2026.10.20 play_67_albedo = 48 
# 2026.10.26 play_67_albedo = 12 same as  https://bsky.app/profile/climatecasino.net/post/3mypajgq73c2f


#########################################################
# 68   play68_ERA          ##############################
#########################################################
#  https://pulse.climate.copernicus.eu/
#  https://cds.climate.copernicus.eu/datasets/reanalysis-era5-single-levels?tab=download
#  https://cds.climate.copernicus.eu/datasets/reanalysis-era5-single-levels
#        https://earthkit.ecmwf.int/
# 68.1 https://bsky.app/profile/climatecasino.net/post/3mxoo2l7acs26 made a 4 years 
#  running average plot with this path 
#  https://sites.ecmwf.int/data/climatepulse/data/series/era5_daily_series_2t_global.csv
# 68.2 make empty csv file work/_era5_empty.csv
# 68.3 open https://sites.ecmwf.int/data/climatepulse/data/series/era5_daily_series_2t_global.csv
# 68.4 select all and copy
# 68.5 in csv file work/_era5_empty.csv paste all
# 68.6 save as work/_88_era5_daily_series_2026_10_13.csv and delete the first lines with #
#   the columns are date,2t,clim_91-20,ano_91-20,status
# 68.7 the column ano_91-20 are the temperature data 
# 68.8 in config.py declare   play68_ERA = 48
# 68.10 the main.py part lin2 266
# 68.15  call create68_running_average for global era5 temperature from main
# 68.17 DP read work/_68_era5_daily_series_2026_10_13.csv data-frame
# 68.33 data_processing.py end line 507 (end perform averaging for play68_ERA )
# 68.39 main.py line 377 read  work/_68_out.csv into  'era_68'
# 66.44 plotting.py line 1044 plot era_68 data
# 2026.10.20 works with play68_ERA = 1095 # 1461, 1095, 720, 365, 24  


##################################################################
# 69     play69_AA = 0 #   albedo anomaly      ###################
##################################################################
# 69.1 open https://ceres-tool.larc.nasa.gov/ord-tool/srbavg
# 69.2 select first item
# 69.3 CERES_EBAF-TOA_Ed4.2.1 - Global Data Charts up to Aug. 2026 is shown
# 69.4 six small curves are shown
# 69.5 select item 1 Label TOA ShortWave Flux All Sky 90 to 110 W/m/m monthly values
# 69.6 big window appears with one curve only
# 69.7 left mouse select Show Anomaly
# 69.8 TOA ShortWave Flux All Sky -3 to 3 W/m/m monthly values shows
# 69.9 left mouse select save Data as ASCII File
# 69.10      CERES_EBAF-TOA_Ed4.2.1_anom_TOA_Shortwave_Flux_-_All-Sky_March-2000toAugust-2026.txt is downloaded
#                  year month   data
#                  2000 03 1.01...
#                  2026 08 -0.90
# 69.11      open rename Bewegen     to work/69a_AA_Albedo_anomaly_2026_08.txt 
# 69.12  config.py   play69_AA = 12     line 56 
# 69.13  config.py   play69_AA_in = "69a_AA_Albedo_anomaly_2026_08.txt" input filename
# 69.14  config.py   line3_play = 69
# 69.15  config.py   c69 = "#1652D490"
# 69.16  config.py   y_69min = -2   # albedo anomaly in W/m2 
# 69.20  main.py   line 267  if play69_AA > 1: # 
# 69.22  main.py   line 268  df69b = convert_ceres_to_csv( play69_AA_in,  // input file
# 69.23  main.py   line 269                        'work/69b_AA.csv') // output file
# 69.24  main.py   line 270                        'AlbedoA' is new column in 69b_AA.csv'
# 69.25             print(f"main_271: create albedo work/69b_AA.csv  69.25 ={play69_AA}")
# 69.31 main.py    output column name for average
# 69.32            df69c = create67_running_average( 'work/69b_AA.csv',   # 69.32 input file name   part 67.37
# 69.33            output file name 'work/69c_AA.csv',   
# 69.39 data_processing.py line 280  part 67.39 read csv with raw ceres data into data-frame
# 69.39                      df = pd.read_csv(input_csv) # 'work/69b_AA.csv
# 69.45 data_processing.py   part 67.45 mean value (read column column_read)(store in column_average)
# 69.51 data_processing.py   df_output.to_csv(output_csv, index=False, float_format='%.6f') # 69.51
# 69.52 main.py              print(f"main_289:   part 69.52   play69_AA   ={play69_AA}") 
# 69.56 main.py    data['ceres_69'] = pd.read_csv("work/69c_AA.csv") # 69.56 read into data field
# 69.57 main.py            print(f"main_386: 64.57 read 69c_AA.csv  play69_AA ={play69_AA}") 
# 69.62 plotting.py 1259   make axis   ax69 = ax1.twinx()  
# 69.63                    ax69.plot(data['ceres_69']["decimal_year"], data['ceres_69']["AA12"], '-',   
# 69.69                    ax69.set_ylim(y_69min, y_69max)            # 69.69 scale the plot field
# 69.70                    print(f"plot1265:  69.70 ={play69_AA}")
# 69.72                    plot8_right_y_axe_for_C_69( ax69 , 0 ) # call   # 69.72 call  plotting.py 562
# 69.74 plotting.py 562 def plot8_right_y_axe_for_C_69(ax69,right62):       # 69.74 plotting.py 562
# 69.77             566    elif play69_AA > 0 and line3_play == 69:        # 69.77 configure right y axis line 3
# 69.82                    label the right y axis   ax69.set_ylabel("Albedo Anomaly [W/m2]     69"
# 69.84 plotting.py  574   scale the right y axis plotting.py 574
# 69.85 text.py line 347   write text   elif play69_AA > 0 and line3_play == 69:  
# 69.86                    write text f"AA    Albedo Anomaly in  [W/m²]     sw in / sw out           moving average {play69_AA} month    69"






#########################################################
# 71     plot71_temperature   ##############################
#########################################################
# reescatophuls works
# https://parisagreementtemperatureindex.com/gwfs-2-quadratic/
#
#    From 1970 -> July 2000, use the Loess-30-year-trend
#    From Aug 2000 -> 2050 use the quadratic best fit line:
#        (0.000617965091650558 * date*date) – (2.45858656778789*date) + 2446.05792853123
#        This quadratic best fit line has been calculated using the Copernicus ERA5 Data from 1995 to September 2025.
#
# reescatophuls works
#  def T_model71_copy1(t):
#      return 0.000617965091650558 * t**2 - 2.45858656778789 * t + 2446.05792853123
#  "red @reescatophuls.bsky :  Temperature = 0.000618t² - 2.459 t + 2446.0579"
#  "red quadratic Temperature = 0.000618t² - 2.459 t + 2446.0579 in °C  71"
# 
# https://parisagreementtemperatureindex.com/gwfs-2-quadratic/
# (0.000617965091650558 * date*date) – (2.45858656778789*date) + 2446.05792853123
# 71.44 models.px line 500
def T_71_rees(t):
    return 0.000617965091650558 * t**2 - 2.45858656778789 * t + 2446.05792853123
# 2026.10.22 plots plot71_temperature = 2
# 2026.10.22 plots plot71_temperature = 3
#


#########################################################
# 72     plot72_AESS_T     ##############################
#########################################################
#
# plot72_AESS_T= 4 # apparent Earth system sensitivity (AESS=7.7°C)
#       red72_text="AESS_T Apparent Earth System Sensitivity = 8°C * log2(CO2/C0) 72"
# 7.2 plot72_AESS_T # dT=ECS*log2(C/C0) # T560ppm=AESS*log2(560/280) 
# AESS=7.7°C  # (Judd 2024)
# https://www.science.org/doi/10.1126/science.adk3705) 
        # 2025
# https://www.annualreviews.org/content/journals/10.1146/annurev-earth-032320-064209
#
#
# def T_model72(t):
#          CO2= 0.0132251 * t**2 - 51.0337 * t + 49536.7 # Glen formula
#          log2_value = np.log2(CO2/C280)
#          AESS=8 # apparent Earth system sensitivity (AESS=7.7°C)
#          temp72=AESS * log2_value
#          return temp72
#        
#        years72 = np.arange(x_anf, x_end + 1 )
#
#        T_72values = T_model72(years72)
# # 72.44 call define T_72: from models.py line 540   
def T_72(t):
          CO2= 0.0132251 * t**2 - 51.0337 * t + 49536.7 # Glen formula
          log2_value = np.log2(CO2/C280)
          AESS=8 # apparent Earth system sensitivity (AESS=7.7°C)
          temp72=AESS * log2_value
          return temp72
# 2026.10.22 plots plot72_AESS_T = 2
# 2026.10.22 plots plot72_AESS_T = 3


#########################################################
# 73     plot73_ECS_T     ##############################
#########################################################
# plot73_ECS_T Earth Climate sensitivity 
# 7.3  dT=ECS*log2(C/C0) # T560ppm=ECS*log2(560/280) 
#
#
def T_model73_not_used(t):
    """Earth Climate Sensitivity (ECS) model"""
    CO2 = 0.0132251 * t**2 - 51.0337 * t + 49536.7
    log2_value = np.log2(CO2 / C280)
    ECS = 4.5
    return ECS * log2_value
#
#
def T_73(t):
           CO2= 0.0132251 * t**2 - 51.0337 * t + 49536.7 # Glen formula
           log2_value = np.log2(CO2/C280)
           ECS = 4.5
           temp73 = ECS * log2_value
           return temp73
# 2026.10.22 plots plot73_ECS_T = 3



#########################################################
# 74   plot74_GIS_T   GISS   Hansen temperature #########
#########################################################
# best read_csv/_74_gis_temperature.csv
# https://data.giss.nasa.gov/gistemp/ 
# https://data.giss.nasa.gov/gistemp/gmsta/
# https://datahub.io/core/global-temp
# download GIS_annual.numbers
# https://github.com/datasets/global-temp
# https://www.columbia.edu/~jeh1/
# https://www.columbia.edu/~jeh1/Data/Temperature/
#    landocean_1880_full(1).txt
#    https://www.columbia.edu/~jeh1/Data/Temperature/#ref1
#
# data_processing.py line 560 plot74_GIS_T
def load74_gis_T():
    """Load GIS temperature data"""
    return pd.read_csv("read_csv/_74_gis_temperature.csv")
#
# 2026.10.22 plots plot74_GIS_T = 2


#########################################################
# 75    linear_41_75 = 3                        #########
#########################################################
#
# 2026.10.22 plots   linear_41_75 = 3 # 3 4 5


#########################################################
# 76   plot76_my_T                              #########
#########################################################
#
# years76 = np.arange(x_anf, x_end + 1 )
#       T_76values = T_model76(years76)
#       df76 = pd.DataFrame({
#             "Year76":      years76,
#             "Modeled76": T_76values })
# 76.4 plot76_temperature
#      print(df76.head(2))
#      print(T_model76(1950) ,"  1950")  # 0.2
#      print(T_model76(2013) ,"  2013")  # 1.0
#      print(T_model76(2023) ,"  2023")
#      print(T_model76(2026) ,"  2026")  # 1.5
#      print(T_model76(2028) ,"  2028")  # 1.5
#       my76_text="guessed quadratic temperature  my_T   76 "
#       0.39999   1950
#       1.10686   2013
#       1.46726   2023
#       1.58864   2026
#       1.6729600000000002   2028
#           def T_model76(t): # my best try
#               x = t - 2000
#               return 0.00034 * x**2 + 0.0238 * x + 0.74
def T_76(t): # my best try
        x = t - 2000
        return 0.00034 * x**2 + 0.0238 * x + 0.74
#
#
# 2026.10.22 plots plot76_my_T = 3



#########################################################
# 77   plot_T_77                                #########
#########################################################
#
#       def T_model77_old(t):
#        https://chat.deepseek.com/a/chat/s/d9a11bdb-f2ce-4c34-b14e-492b673e0a4e
#        Define the three points
#       t1, y1 = 1980, 0.5  # 
#               t1, y1 = 1950, 0.2 
#               t2, y2 = 2013, 1.0
#               t3, y3 = 2023, 1.5
#              # Lagrange interpolation
#               term1 = y1 * ((t - t2) * (t - t3)) / ((t1 - t2) * (t1 - t3))
#               term2 = y2 * ((t - t1) * (t - t3)) / ((t2 - t1) * (t2 - t3))
#               term3 = y3 * ((t - t1) * (t - t2)) / ((t3 - t1) * (t3 - t2))
#               return term1 + term2 + term3
#
#         def T_model77(t):
#                t1, y1 = 1950, 0.2 
#                t2, y2 = 2013, 1.0
#                t3, y3 = 2022, 1.5
#                # Lagrange interpolation
#                term1 = y1 * ((t - t2) * (t - t3)) / ((t1 - t2) * (t1 - t3))
#                term2 = y2 * ((t - t1) * (t - t3)) / ((t2 - t1) * (t2 - t3))
#                term3 = y3 * ((t - t1) * (t - t2)) / ((t3 - t1) * (t3 - t2))
#                return term1 + term2 + term3
#
def T_77(t):
        # https://chat.deepseek.com/a/chat/s/d9a11bdb-f2ce-4c34-b14e-492b673e0a4e
        # Define the three points
        #t1, y1 = 1980, 0.5  # 
        t1, y1 = 1950, 0.2 
        t2, y2 = 2013, 1.0
        t3, y3 = 2022, 1.5
        # Lagrange interpolation
        term1 = y1 * ((t - t2) * (t - t3)) / ((t1 - t2) * (t1 - t3))
        term2 = y2 * ((t - t1) * (t - t3)) / ((t2 - t1) * (t2 - t3))
        term3 = y3 * ((t - t1) * (t - t2)) / ((t3 - t1) * (t3 - t2))
        return term1 + term2 + term3
#
# 2026.10.22 plots   plot_T_77  = 3


#########################################################
# 78   plot_T_78  #     Tom Harris              #########
#########################################################
# plot_T_78 = 3 # Tom Harris
#
#        def T_model78(t):
#                 y = 0.0004x2 + 0.0019x + 0.5079 
#                https://substack.com/@drtomharris/note/c-365674298
#                Tom Harris  
#                return 0.0004 * x**2 + 0.0019 * x + 0.5079
#            x = t - 1980
#            return 0.0004 * x**2 + 0.0019 * x + 0.5079
def T_78(t):
    x = t - 1980
    return 0.0004 * x**2 + 0.0019 * x + 0.5079
#
# 2026.10.22 plots   plot_T_78  = 3 formula  good
# 2026.10.22 plots   plot_T_78  = 4 formula  good
# 2026.10.22 plots   plot_T_78  = 5 formula  good