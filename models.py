# models.py
# version 5G50
# includes the documentation

import numpy as np

from config import *


C280 = 280

def T_model71(t):
    """Quadratic temperature model from @reescatophuls.bsky"""
    return 0.000617965091650558 * t**2 - 2.45858656778789 * t + 2446.05792853123

def T_model72(t):
    """Apparent Earth System Sensitivity (AESS) model"""
    CO2 = 0.0132251 * t**2 - 51.0337 * t + 49536.7
    log2_value = np.log2(CO2 / C280)
    AESS = 8
    return AESS * log2_value

def T_model73(t):
    """Earth Climate Sensitivity (ECS) model"""
    CO2 = 0.0132251 * t**2 - 51.0337 * t + 49536.7
    log2_value = np.log2(CO2 / C280)
    ECS = 4.5
    return ECS * log2_value

def T_model76(t):
    """My best temperature model"""
    x = t - 2000
    return 0.00034 * x**2 + 0.0238 * x + 0.74


# 7 part 1
# red71_text="red @reescatophuls.bsky :  Temperature = 0.000618t² - 2.459 t + 2446.0579"
red71_text="red quadratic Temperature = 0.000618t² - 2.459 t + 2446.0579 in °C  71"
# 7.1 plot71_temperature @reescatophuls.bsky.social
# https://parisagreementtemperatureindex.com/gwfs-2-quadratic/
# (0.000617965091650558 * date*date) – (2.45858656778789*date) + 2446.05792853123
def T_model71(t):
   return 0.000617965091650558 * t**2 - 2.45858656778789 * t + 2446.05792853123
# 7.1.2 years scale x axis
years71 = np.arange(x_anf, x_end + 1 )
T_71values = T_model71(years71)
# 7.1.3. Create DataFrame for convenience
# df7 = pd.DataFrame({
#      "Year71": years71,
#      "Modeled71": T_71values })








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
# 46_ASR_48month_2026_07.csv ############################
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
# plot55_population_on ############################
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
# 61 How to make EEI files ##############################
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
# 2026.10.15 plots play_61_EEI = 12    # 12, 24, 36, 48 create 1..12..48..99 CERES EEI.csv 


# ----------------------------------------------
# play_62_CERES = 12 
# --- see 41 process 4 CERES files ---------------------
# Tom Harris on substack https://substack.com/@drtomharris/note/c-366539763
#     Thanks, yes it is a 36 month rolling average.
#     The EEA is simply a monthly rolling sum of the monthly (36m smoothed) EEI, 
#     then multiplied by a constant 16.087 to convert it to ZJ. 
#     1 W/m2 is 1 joule per second per square meter. 
#     The constant above is seconds per month x area of Earth / 10^21 (zeta)
#  python how to sum up 62c_EEA.csv column EEI36 and store it to new column EEA
#     # 1. CSV-Datei einlesen
#  df = pd.read_csv("62c_EEA.csv")
# 2. Laufende Summe (kumulierte Summe) bilden und in 'EEA' speichern
# df["EEA"] = df["EEI36"].cumsum()
# 3. CSV-Datei speichern
# df.to_csv("62c_EEA_aktualisiert.csv", index=False)
#  python how to sum up 62c_EEA.csv column EEI36 and multiply with 1.23    and store it to new column EEA



# ----------------------------------------------
# play_63_CERES = 12 
# --- see 41 process 4 CERES files ---------------------
# 63.41 open
# https://ceres-tool.larc.nasa.gov/ord-tool/srbavg
# 63.42 select first item
# 63.43 CERES_EBAF-TOA_Ed4.2.1 - Global Data Charts up to Feb. 2026 is shown
# 63.44 six small curves are shown
# 63.45 select item 1 Label TOA Short Wave Flux All Sky 90 to 110 W/m/m monthly values
# 63.46 big window appears with one curve only
# 63.47 left mouse select save Data as ASCII File
# 63.48 CERES_EBAF-TOA_Ed4.2.1_TOA_Shortwave_Flux_-_All-Sky_March-2000toFebruary-2026.txt is downloaded
# 63.49 rename      to _63_in__2026_02_Shortwave.txt and save to dokumente/5_CO2_EEI_T/read_csv/
#  run with play_61_EEI = 48 
#  copy dokumente/5_CO2_EEI_T/read_csv/_61c_out_ceres.csv.csv to
#       dokumente/5_CO2_EEI_T/read_csv/_42_EEI48month_2026_02.csv
#  run   plot42_EEI_48month=2 reading new _42_EEI48month_2026_02.csv file
# ----------------------------------------------



# ----------------------------------------------
# 62    play_62_CERES   ------------------------
# play_62_CERES ist doppelt zu play_66_OLR
# --- see 41 process 4 CERES files ---------------------
# play_62_CERES = 48 
# 62.21 open
# https://ceres-tool.larc.nasa.gov/ord-tool/srbavg
#  62.22 select first item
#  62.23 CERES_EBAF-TOA_Ed4.2.1 - Global Data Charts up to Feb. 2026 is shown
#  62.24 six small curves are shown
#  62.25 select item 2 Label TOA Long Wave Flux All Sky 235 to 245 W/m/m monthly values
#  62.26 big window appears with one curve only
#  62.27 left mouse select save Data as ASCII File
#  62.28.1 CERES_EBAF-TOA_Ed4.2.1_TOA_Longwave_Flux_-_All-Sky_March-2000toFebruary-2026.txt is downloaded
#  62.28.2 CERES_EBAF-TOA_Ed4.2.1_TOA_Longwave_Flux_-_All-Sky_March-2000toJuly-2026.txt is downloaded
#  62.29.1 rename      to _62_in__2026_02_Longwave.txt and save to dokumente/5_CO2_EEI_T/read_csv/
#  62.29.2 rename      to _66_TOA_OLR_all_sky_2026_07.txt and save to dokumente/5_CO2_EEI_T/work/
#  62.30.1 run with play_62_CERES = 48
#    read read_csv/_62_in__2026_02_Longwave.txt main 124
#    output1 read_csv/_62b_LongWave.csv'
#  62.30.2 run with play_66_OLR = 48
#  62.31.1 run with play_62_CERES = 48
#    input1  read_csv/_62_in__2026_02_Longwave.txt main 124
#    input2  read_csv/_42_EEI48month_2026_02.csv   main 141
#    output2 read_csv/_62c_LongWave.csv with column LongWave for  48 month running average 
#    output3.1 read_csv/_62e_LongWave.csv with column EEI copy from input2 for  48 month running average 
#    output3.2 read_csv/_62e_LongWave.csv with column LongWave for  48 month running average 
#    output3.3 read_csv/_62e_LongWave.csv with column OLR_EEI = LongWave + EEI   48 month running average 
#  62.32.1 copy dokumente/5_CO2_EEI_T/read_csv/_62e_LongWave.csv to
#         dokumente/5_CO2_EEI_T/read_csv/_45_OLR_EEI_48month_2026_02.csv
#  62.32.2 copy dokumente/5_CO2_EEI_T/work/_66c_OLR.csv to
#           dokumente/5_CO2_EEI_T/read_csv/_45_OLR_48month_2026_07.csv file, column OLR48 
#  62.33.1 run   plot45_OLR_48month=2 reading new _45_OLR_EEI_48month_2026_02.csv file
#  62.33.2 run   plot45_OLR = 3 reading new _45_OLR_48month_2026_07.csv file, column OLR48 
# ------- play_62_CERES ist doppelt zu play_66_OLR ---------


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

