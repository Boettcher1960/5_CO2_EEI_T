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
# plot42_EEI_48month ############################################
###############see 61 How to make EEI files #####################
# 42.1 open https://ceres-tool.larc.nasa.gov/ord-tool/srbavg
# 42.2 download CERES_EBAF-TOA_Ed4.2.1_TOA_Net_Flux_-_All-Sky_March-2000toJuly-2026.txt
# 42.3 copy txt to read_csv/_61_in__2026_07_EEI_CERES.txt
# 42.4 run with play_61_EEI = 48
# 42.6 copy to read_csv/_42_EEI48month_2026_07.csv
# 42.8 set plot42_EEI_48month = 3  # 2,3,4,5 print EEI 48 month running mean


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






# text55 = "Green line: Earth Population in billion                                               55"
# plot55_population_on = 5 # 5 word with y axis right


