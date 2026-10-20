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
# process 4 CERES files 
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
# 41.23 in main.py  line 311     data['ceres_45'] = pd.read_csv("read_csv/_45_OLR_48month_2026_07.csv")
# 41.24 in main.py  line 311     data['ceres_45'] = pd.read_csv("read_csv/_45_OLR_48month_2026_08.csv")
#  

#################################################################
# plot42_EEI_48month ############################################
###############see 61 How to make EEI files #####################
# 42.1 open https://ceres-tool.larc.nasa.gov/ord-tool/srbavg
# 42.2 download CERES_EBAF-TOA_Ed4.2.1_TOA_Net_Flux_-_All-Sky_March-2000toJuly-2026.txt
# 42.3 copy txt to read_csv/_61_in__2026_07_EEI_CERES.txt
# 42.4 run with play_61_EEI = 48
# 42.6 copy to read_csv/_42_EEI48month_2026_07.csv
# 42.8 set plot42_EEI_48month = 3  # 2,3,4,5 print EEI 48 month running mean
#
# 2026.10.15 plots  plot42_EEI_48month = 2
# 2026.10.15 plots  plot42_EEI_48month = 3


#################################################################
# plot43_eei_12month ############################################
# https://x.com/Pat_Schmidt_89/status/2110140450161987999/photo/1
############### see 61 How to make EEI files ####################
# 43.1 open https://ceres-tool.larc.nasa.gov/ord-tool/srbavg
# 43.2 download CERES_EBAF-TOA_Ed4.2.1_TOA_Net_Flux_-_All-Sky_March-2000toJuly-2026.txt
# 43.3 copy txt to read_csv/_61_in__2026_07_EEI_CERES.txt
# 43.4 run with play_61_EEI = 12 the file /_61c_out_ceres.csv is produced 
#    /_61c_out_ceres.csv column EEI has the 12 month average
# 43.5 copy            read_csv/_61c_out_ceres.csv
# 43.6 paste to        read_csv/_43_EEI12month_2026_07.csv
# 43.7.1 set plot43_eei_12month = 2  # 2,3,4,5 print EEI 48 month running mean
#        the left axis is EEI 43
# 43.7.2 set plot43_eei_12month = 3  # 2,3,4,5 print EEI 48 month running mean
# 43.8 run the plot
#
# 2026.10.15 plots plot43_eei_12month = 2
# 2026.10.15 plots plot43_eei_12month = 3


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
#
# 2026.10.15 plots part44_ceres_eei = 3   # makes 3 month average
# 2026.10.15 plots part44_ceres_eei = 47  # makes same 12 month average best
# 2026.10.15 plots part44_ceres_eei = 36  # makes same 3 month average




#########################################################
# 45_OLR_48month_2026_07.csv ############################
#########################################################
# 1 open https://ceres-tool.larc.nasa.gov/ord-tool/srbavg
# 2 download CERES_EBAF-TOA_Ed4.2.1_TOA_Longwave_Flux_-_All-Sky_March-2000toJuly-2026(2).txt
# 3 copy txt to work/_66_TOA_OLR_all_sky_2026_07.txt
# 4 run with play_66_OLR = 48
# 5 copy dokumente/5_CO2_EEI_T/work/_66c_OLR.csv to
#        dokumente/5_CO2_EEI_T/read_csv/_45_OLR_48month_2026_07.csv
#   looks like https://bsky.app/profile/leonsimons.com/post/3mwy3xgypts2y
#
#  plot45_OLR = 2 # 2, 3, 4 looks like simons 48 months. Outgoing Longwave Radiation OLR updated to 2026_07
#
# 2026.10.15 plots plot45_OLR = 2
# 2026.10.15 plots plot45_OLR = 3

#########################################################
# 46_ASR_48month_2026_07.csv ############################
#########################################################
# 1 open https://ceres-tool.larc.nasa.gov/ord-tool/srbavg
# 2 download CERES_EBAF_Ed4.2.1_Incoming_Solar_Flux_March-2000toMay-2026.txt
# 3 copy to _66_TOA_Incoming_Solar_2026_07.txt
# 5 download CERES_EBAF-TOA_Ed4.2.1_TOA_Shortwave_Flux_-_All-Sky_March-2000toJuly-2026.txt
# 6 copy to _66_TOA_Shortwave_Flux_All_Sky2026_07.txt 
# 7 run with play_67_albedo = 48
#   dokumente/5_CO2_EEI_T/work/_CERES_raw.csv is produced with column ASR
# 8 copy dokumente/5_CO2_EEI_T/work/_CERES_ASR.csv to
#        dokumente/5_CO2_EEI_T/read_csv/_46_ASR_48month_2026_07.csv
# looks like https://bsky.app/profile/leonsimons.com/post/3mwy3xgypts2y
# line DataP423 df2['ASR'] = df2['sw_in'] - df2['sw_out']
# 2026.10.15 plots plot46_ASR = 2
# 2026.10.15 plots plot46_ASR = 3



#########################################################
# plot47_albedo48 ############################
#########################################################
# 47.1 open https://ceres-tool.larc.nasa.gov/ord-tool/srbavg
# 47.2 download CERES_EBAF_Ed4.2.1_Incoming_Solar_Flux_March-2000toMay-2026.txt
# 47.3 copy to _66_TOA_Incoming_Solar_2026_07.txt
# 47.5 download CERES_EBAF-TOA_Ed4.2.1_TOA_Shortwave_Flux_-_All-Sky_March-2000toJuly-2026.txt
# 47.6 copy to _66_TOA_Shortwave_Flux_All_Sky2026_07.txt 
# 47.7 run with play_67_albedo = 48
# 47.8 copy dokumente/5_CO2_EEI_T/work/_CERES_albedo.csv to
#           dokumente/5_CO2_EEI_T/read_csv/_47_albedo_48month_2026_07.csv
#      plot47_albedo48 = 4 - print text in line 4
#
# 2026.10.15 plots plot47_albedo48 = 4



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
#########################################################
# 1 open https://ceres-tool.larc.nasa.gov/ord-tool/srbavg
# https://ceres-tool.larc.nasa.gov/ord-tool/srbavg
# 2  https://ceres.larc.nasa.gov/data/
# 3 https://ceres-tool.larc.nasa.gov/ord-tool/jsp/EBAFTOA421Selection.jsp
# 4 t.boettcher@directbox.com enter email adress
# 5 Order Data - left mouse click
# 6 select
# 7 global mean
# 8 Visualize Data - left mouse click
# 9 global mean https://ceres-tool.larc.nasa.gov/ord-tool/srbavg
# 10 select first item
# 11 CERES_EBAF-TOA_Ed4.2.1 - Global Data Charts up to Feb. 2026 is shown
# 12 six small curves are shown
# 13 select item 3 Label TOA Net Flux All Sky -10 to +10 W/m/m monthly values
# 14 big window appears with one curve only
# 15 left mouse select save Data as ASCII File
# 16.1 CERES_EBAF-TOA_Ed4.2.1_TOA_Net_Flux_-_All-Sky_March-2000toFebruary-2026.txt is downloaded
# 16.2 CERES_EBAF-TOA_Ed4.2.1_TOA_Net_Flux_-_All-Sky_March-2000toJuly-2026.txt is downloaded
# 17.1 rename      to _61_in__2026_02_EEI_CERES.txt and save to dokumente/5_CO2_EEI_T/read_csv/
# 17.2 rename      to _61_in__2026_07_EEI_CERES.txt and save to dokumente/5_CO2_EEI_T/read_csv/
# 18 run with play_61_EEI = 48 
# 19 copy dokumente/5_CO2_EEI_T/read_csv/_61c_out_ceres.csv to
# 20.1      dokumente/5_CO2_EEI_T/read_csv/_42_EEI48month_2026_02.csv
# 20.2                           'read_csv/_42_EEI48month_2026_07.csv', 
# 21 run   plot42_EEI_48month=2 reading new _42_EEI48month_2026_02.csv file
# 
# 22 run with play_61_EEI = 12 
# 23 copy dokumente/5_CO2_EEI_T/read_csv/_61c_out_ceres.csv.csv to
#       dokumente/5_CO2_EEI_T/read_csv/_43_EEI12month_2026_02.csv
# 24 run   plot43_eei_12month=3 reading new _43_EEI12month_2026_02.csv file
#
# 2026.10.15 plots play_61_EEI = 12    # 12, 24, 36, 48 create 1..12..48..99 CERES EEI.csv 




