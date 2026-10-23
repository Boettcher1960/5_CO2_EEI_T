# config.py 
# version 5c80
# Configuration parameters for the climate analysis tool

# part61_EEI # like part41_ceres_eei make EEI 120 month csv
# line 2 defines the left Y axis. example
# line 3 defines the right Y axis with 10 pixel to the right of plot area
# line 4 defines the right Y axis with 70 pixel to the right of plot area
# line 5 defines the right Y axis with 130 pixel to the right of plot area
# line 6 is developv part61_EEI 

# 8.3 print the left y axis 
# line 2 defines the left Y axis. example

# 8.5 configure the right axis legend 
yr_60  = 60  # 60 (0=no right yaxis) 60 * 4 = 240 pixel to the right
yr_150    = 150  #  240 - 150 = 90 ( 60 * 4 = 240      plot8_right_y_axe_for_T_74
yr_delete = 1 # 9 = delete all axes delete axe 4

# Plot configuration flags
plot22_CO2_Mauna_Loa = 0 # 2 ,3    22.1 declare global integer variable (2= print in line 2)
plot23_Glen_CO2 = 0      # 2, 3 , 23.1 declare global integer variable (4= print in line 4)
plot25_long_CO2 = 0   # 2, 3 25.1 

plot31_CO2_emission = 0  # 2, 3, 4   # 31.1 CO2_emission 1800 Gt CO2 Carbon Brief made with play_63_CB 
plot32_CO2_emission = 0  # 2, 3 # CO2_emission 600 GtC Carbon Brief made with play_63_CB 

plot34_CO2_emission = 0      # 4,     # 34.1 row 4 
plot34_CO2_emission_mode = 0 # 4, 2, 4   # 34.1 mode 
# plot31__CO2_emission mode 1 # plot32__CO2_emission mode 2 # plot33__CO2_emission mode 3
plot34_CO2 = 0 # 0     plot34_CO2_emission mode 4

plot42_EEI_48month = 0  # 2,3,4,5 print EEI 48 month running mean. Info in line 4 below the plot
plot43_eei_12month = 0  # 2, 3, 4 ,5 2=left y axis 3,4 print EEI 12 month running mean. [W/m2]
part44_ceres_eei = 0  # 47, 3, 48,   is local 
plot45_OLR = 0 # 2, 3, 4 looks like simons 48 months. Outgoing Longwave Radiation OLR updated to 2026_07
plot46_ASR = 0 # 2, 3 ASR Absorbed Solar Radiation from _CERES_ASR 48 months average [W/m2]
plot47_albedo48 = 0  # 4  

plot52_delta_CO2_red_bars = 0 # 3 (3=print numbers)
plot53_CO2_orange2025 = 0 # no curve is visible 3, 4
plot54_Glen_delta_on = 0 # no curve is visible 3, 4
plot55_population_on = 0 # 5 word with y axis right
plot56_delta_CO2_4years = 0 # # no curve is visible 3, 4 
# https://bsky.app/profile/thomas-boettcher.bsky.social/post/3mnkupgsz7s2k

play_61_EEI = 24    # 12, 24, 36, 48 create 1..12..48..99 CERES EEI.csv _c61_out_ceres.csv // copy to 41_ceres_eei
play_62_EEA = 24    # 12, 24, 36, 48  Earth Energy Accumulated EEA is sum of EEI
play_63_CB    = 0 # 5 carbon brief CO2 values https://ourworldindata.org/grapher/cumulative-co-emissions?country=~OWID_WRL&overlay=download-data
play_64_ASR_anomaly = 0 # 12 # 12, 48 # absorbed solar radiation ASR anomaly = 1.48 W/m² 2.1_anom_TOA_Shortwave_Flux_-_All-Sky
play_65_ASR = 0 # 12 ASR = 242 W/m² TOA_Shortwave_Flux_-_All-Sky
play_66_OLR = 0 # 12, 24 looks like GISS temp 48, 36, 24, 12 ok outgoing longwave radiation OLR = 240 [W/m2]
play_67_albedo = 0   # create 1..12..48..99 CERES
play68_ERA = 720 # 1461, 1095, 720, 365, 24     # https://sites.ecmwf.int/data/climatepulse/data/series/era5_daily_series_2t_global.csv

plot71_temperature = 0 # 2 3 5
plot72_AESS_T = 0 # 2 , 3 
plot73_ECS_T = 0 # 3
plot74_GIS_T = 6 # 2, 3,4,5,6,7 =right y axis
linear_41_75 = 0 # 3 4 5
plot76_my_T = 0 # 3, 5
plot_T_77 = 0 # 3, 4
plot_T_78 = 3 # 3 , 4 , 5 Tom Harris

# variable to show play variable in line 4
line2_play = 68   # 61  62
line3_play = 0  #  play_62_EEA #   68 play68_ERA = 720
line4_play = 61  # 61 play_61_EEI = 36 
line5_play = 62   # 62 61

parameter84_save_png = 8

# Colors
c21 = "blue"
c22 = "blue"
c23 = "#4554A8C6"
c25 = "green"
c31 = "#9B107F90"
c32 = "#10929B90"
c32 = "red"
c34 = "#942296C5"
c41 = "#289C1684"
c42 = "purple"
c42 = "#13DF2F84"
c43 = "green" # "#70A915B1"
c44 = "blue"
c45 = "#DE2B1ACC"
c46 = "#481725DC"
c47 = "#31A28ADC"
c52 = "#7C8825FA"
c52bar = "#C1D43408"
c55 = "#34D48FC7"
c61 = "#1E0ED2A0"
c62 = "#BEBE21DD"
c63 = "#1652D490"
c64 = "#9522AA90"
c65 = "#390509E1"
c66 = "#AB263590"
c67 = "#0F9BE190"
c68 = "#36970FD4"

c71 = "red"
c71 =  "#AB263590"
c72 =  "#31BD9590"
c73 =  "red"
c74 = "red"
#c74 = "#9522AA90"
c75 = "#371EA484"
c76 = "#13DF2F84"
c77 = "#34753D84"
c78 = "#9D2A9984"

# Text definitions (added missing print texts)
blue22_text      = "blue dots: CO2 measured at Mauna Loa (2025 = 427.35 ppm)                          22"
text23 = "CO2 calculated dashed blue line      CO2 = 0.0132251t² - 51.0337t + 49,536 ppm    23"
text25 = "green: CO2 NOAA     800_000 year ice data                                                   25"

text31 = "dots: cumulative CO2 emissions in GtCO2     Carbon Brief / Our World in Data           31"
text32 = "dots: cumulative CO2 emissions in GtC       Carbon Brief / Our World in Data              32"
text34 = "purple dots: cumulative CO2 emissions Carbon Brief 34 mode                                   34"

text41 = "Earth Energy Imbalance W/m² moving average 12 month 41"
text42 = "Earth Energy Imbalance W/m² moving average 48 month 42"
text43 = "Earth Energy Imbalance in W/m²                                  moving average 12 month    43"
text44 = "Earth Energy Imbalance W/m² moving average 44"
text55 = "Green line: Earth Population in billion                                               55"

text71 = "Temperature in °C 0.000618t² - 2.459 t + 2446.0579            from  @reescatophul     71"
# "Temperature in °C 0.000618t² - 2.459 t + 2446.0579                       @reescatophul     71", 
# "Temperature in °C 0.0004t² + 0.0019 t + 0.5079     from Tom Harris                         71", 
text72 = "Temperature in °C   AESS Apparent Earth System Sensitivity = 8°C * log2(CO2/C0  72"
text73 = "Temperature in °C   Earth Climate sensitivity              dT = ECS * log2 ( C / C0 )      73"
text74 = "Temperature in °C   giss.nasa.gov   Hansen+0.3°C                                                   74"  
text75 = "Hansen linear fit   from 2015    +0.41°C                       75"  # Added for linear_41_75
text76 = "Temperature in °C   my guess quadratic increase                                                      76" 
text77 = "Temperature in °C   quadratic           1950=0.2°C     2013=1°C     2022=1.5°C       77" 
text78 = "Temperature in °C   quadratic       Tom Harris  y = 0.0004x2 + 0.0019x + 0.5079      78" 


# Axis ranges
y_min = 310 # 250 ppm CO2 
y_max = 430 # 500 ppm CO2  

y_25min = 250 # nok   only for y axis 
y_25max = 430 # only for y axis
y_Gmin = 0 # 250 ppm CO2 
y_Gmax = 2000 # 2500 Gt CO2  
y_31Gmin = 0 # 250 ppm CO2  
y_31Gmax = 2000 # 2500 Gt CO2  
y_32min = 0   #   0 GtC
y_32max = 800 # 800 GtC

y_34min = 0   #   0 GtC
y_34max = 600 # 800 GtC

y_Emin = 0.0 #   EEI in W/m2 y axis left mode
y_Emax = 2 #   EEI in W/m2 y axis left mode

y_TOAmin = 97  # bug is double set in plotting.py line 56
y_TOAmax = 100 # bug is double set in plotting.py line 57

y_42min = 0 #   EEI in W/m2 y axis left mode
y_42max = 1.8 #   EEI in W/m2 y axis left mode
y_43min = 0    # EEI in W/m2
y_43max = 2  # EEI in W/m2
y_44min = 0.0 #   EEI in W/m2 y axis left mode
y_44max = 2 #   EEI in W/m2 y axis left mode

y_45min = 240    # OLR in W/m2
y_45max = 242.8  # OLR in W/m2
y_46min = 240    # ASR in W/m2
y_46max = 242.8  # ASR in W/m2
y_47min = 0.294 # albedo in %
y_47max = 0.286 # albedo in %

y_52min = 0 # plot52_delta_CO2_red_bars
y_52max = 4 # plot52_delta_CO2_red_bars
y_55min = 2 # plot55_population_on = 5
y_55max = 9 # plot55_population_on = 5

y_61min = 0  #   EEI in W/m2 y axis left mode
y_61max = 2  #   EEI in W/m2 y axis left mode

y_62min = 0  # EEA in ZJ
y_62max = 400  # EEA in ZJ

y_64min = 0.4  # in W/m2
y_64max = -2.3  # in W/m2
y_65min = 239.5  # ASR in W/m2
y_65max = 243.5  # 242.8  # ASR in W/m2

y_66min = 239.5  # OLR in W/m2
y_66max = 243.5 # 242.8  # OLR in W/m2

y_67min = 0.285  # albedo in %
y_67max = 0.295  # albedo in %
y_67min = 0.2936  # 0.294 albedo in %
y_67max = 0.2862  # 0.286 albedo in %
y_67min = 0.294 # albedo in %
y_67max = 0.286 # albedo in %

y_68min = 0  # for era5 Temperature
y_68max = 1.6  # for era5 Temperature 

y_Tmin = 0
y_Tmax = 2 # 1.7
y_71min = 0
y_71max = 3 # 1.7
y_72min = 0
y_72max = 6 # 
y_73min = 0
y_73max = 6 # 
y_74min = 0  # for GIS Temperature 
y_74max = 1.6  # for GIS Temperature 
y_75min = 0 #  Temperature  
y_75max = 2   #  Temperature 
y_76min = 0 #  Temperature  
y_76max = 4   #  Temperature 
y_77min = 0 #  Temperature  
y_77max = 4 #  Temperature 
y_78min = 0 #  for Tom Harris Temperature 
y_78max = 1.6 #  for Tom Harris Temperature
x_anf = 2004
x_end = 2027

# constants
# C280 =275 in Zack Labe plots.
C280 = 280

# Text positioning
tr1x = -0.09
tr2x = 0.03 # 0.01
tr3x = 0.03 # only 63 row 5
tr1y = -.19
tr2y = -.26
tr3y = -.33
tr4y = -.40
tr5y = -.46
tr6y = -.51
tr7y = -.57
trs = 20

# Legend line positions
lr2x1 = 0.065
lr2x2 = 0.085
lr1y = 0.248
lr2y = 0.211
lr3y = 0.168
lr4y = 0.129
lr5y = 0.095
lr6y = 0.064
lr7y = 0.034


# Figure size
scale_mode = 10 # other values are not used
print_debug = 10 # print some items 


# play_64_ASR_anomaly = 12 # absorbed solar radiation ASR = 1.48 W/m² 
# 41 open
# https://ceres-tool.larc.nasa.gov/ord-tool/srbavg
# 42 select first item
# 43 CERES_EBAF-TOA_Ed4.2.1 - Global Data Charts up to Feb. 2026 is shown
# 44 six small curves are shown
# 45 select item 1 Label TOA ShortWave Flux All Sky 90 to 110 W/m/m monthly values
# 46 big window appears with one curve only
# 47 left mouse select Show Anomaly
# 48 TOA ShortWave Flux All Sky -3 to 3 W/m/m monthly values shows
# 49 left mouse select save Data as ASCII File
# 50 CERES_EBAF-TOA_Ed4.2.1_anom_TOA_Shortwave_Flux_-_All-Sky_March-2000toFebruary-2026.txt is downloaded
# 51 rename      to _64_in__2026_02_ASR_anomaly.txt and save to dokumente/5_CO2_EEI_T/read_csv/
# 52 run with play_64_ASR_anomaly = 12
#    read read_csv/_64_in__2026_02_ASR_anomaly.txt   main.py 
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
# part 5.3 plot53_CO2_orange2025
# part 5.4 plot54_Glen_delta_on
# part 5.5 plot55_population_on human earth population 



#########################################################
# 161 How to make EEI files ##############################
#########################################################
#
# download 2016_01_EEI_CERES.txt
# rename      to 2016_01_EEI_CERES.txt
# 
# #8T44 2 download asci file TOA flux
# CERES_EBAF-TOA_Ed4.2.1 - Global Data Charts
# csv41_CERES_TOA_FluxtoJanuary-2026.txt
# https://ceres-tool.larc.nasa.gov/ord-tool/jsp/EBAFTOA421Selection.jsp
# https://ceres-tool.larc.nasa.gov/ord-tool/srbavg
# https://bsky.app/profile/thomas-boettcher.bsky.social/post/3mhuowkhfq22h
# save file as csv41_CERES_TOA_FluxtoJanuary-2026.txt
# part44_ceres_eei = 47
#         https://ceres-tool.larc.nasa.gov/ord-tool/srbavg
# 1) goto https://ceres-tool.larc.nasa.gov/ord-tool/srbavg
# 2) enter email + password
# https://ceres-tool.larc.nasa.gov/ord-tool/jsp/EBAFTOA421Selection.jsp
# 4) select TOA top of atmosphere
#    select monthly
#    select global mean
#    enter email 
# 5) hit "Visualize Data" (on the bottom left)
# 6) a new window appears with 6 blue sinus curves
# 7) select curve number 3
#    TOA Net Flux
# 8) the TOA Net Flux gets yellow color
#    click with left mouse button
# 9) a new window "March -2000 TOA Net Flux" appears
#     not hit "Show Anomaly" gives low 
# 11) the window changes -2 to +2 W/m2
# 12) hit "Save Data as ASCII File" on the bottom
# 13) the download starts
# 14) open the download folder
# 15) CERES_EBAF-TOA_Ed4.2.1_anom_TOA_Net_Flux_-_All-Sky_March-2000toJanuary-2026 (2).txt
# 16) copy CERES_EBAF-TOA_Ed4.2.1_anom_TOA_Net_Flux_-_All-Sky_March-2000toJanuary-2026 (2).txt
#     to the 
#     /read_csv/ folder
#     /Dokumente/Python/5_CO2_EEI_T/read_csv/
# 17) rename CERES_EBAF-TOA_Ed4.2.1_anom_TOA_Net_Flux_-_All-Sky_March-2000toJanuary-2026 (2).txt
#     to
#     /Dokumente/Python/5_CO2_EEI_T/read_csv/_61_in__2016_01_EEI_CERES.txt
# 
# 18) in config.py set play_61_EEI = 12 
# 19) read_csv/_61b_out_in_ceres.csv is created from read_csv/_61_in__2016_01_EEI_CERES.txt
# 19) read_csv/_61c_out_ceres.csv is created from read_csv/_61b_out_in_ceres.csv
# 19) _61c_out_ceres.csv is plotted as documented in line 5
#
# 20) copy  _61c_out_ceres.csv to  _43_EEI12month_made_by_61c.csv
#     note: _61c_out_ceres.csv is same as a44d_ceres_12month_EEI.csv made by 41 chain
# 21) plot _43_EEI12month_made_by_61c.csv using plot43_eei_12month = 4
#
# 22) in config.py set play_61_EEI = 48 
# 23) read_csv/_61b_out_in_ceres.csv is created from read_csv/_61_in__2016_01_EEI_CERES.txt
# 23) read_csv/_61c_out_ceres.csv is created from read_csv/_61b_out_in_ceres.csv
# 23) _61c_out_ceres.csv is plotted as documented in line 5
# 24) copy  _61c_out_ceres.csv to  _42_EEI48month_made_by_61c.csv
#     note: _61c_out_ceres.csv is same as a44d_ceres_12month_EEI.csv made by 41 chain
# 25) plot _43_EEI12month_made_by_61c.csv using plot43_eei_12month = 4
#
#
#            read_csv/_61c_out_ceres.csv
# 21)  set part44_ceres_eei = 47
# 22) /Dokumente/Python/5_CO2_EEI_T/main.py reads 
#     /Dokumente/Python/5_CO2_EEI_T/read_csv/2016_01_EEI_CERES_TOA Net Flux.txt
#        df44 = convert_ceres_to_csv('read_csv/2016_01_EEI_CERES_TOA Net Flux.txt', 
#                                   'work/c44b_ceres.csv')
# 23) the file /Dokumente/Python/5_CO2_EEI_T/work/c44b_ceres.csv is created with year as decimal
# 24) the file /Dokumente/Python/5_CO2_EEI_T/work/c44d_ceres.csv is created 
#                      with 48 month trailing average in new column EEI
#                               df_with_avg = create_running_average('work/c44b_ceres.csv', 
#                                            "work/c44d_ceres.csv",
#                                            column_name='EEI')
# 25) copy /work/c44d_ceres.csv to /read_csv/c44d_ceres_48month_EEI.csv
#
# 31)  set part44_ceres_eei = 11
# 32) /Dokumente/Python/5_CO2_EEI_T/main.py reads 
#     /Dokumente/Python/5_CO2_EEI_T/read_csv/2016_01_EEI_CERES_TOA Net Flux.txt
#        df44 = convert_ceres_to_csv('read_csv/2016_01_EEI_CERES_TOA Net Flux.txt', 
#                                   'work/c44b_ceres.csv')
# 33) the file /Dokumente/Python/5_CO2_EEI_T/work/c44b_ceres.csv is created with year as decimal
# 34) the file /Dokumente/Python/5_CO2_EEI_T/work/c44d_ceres.csv is created 
#                      with 48 month trailing average in new column EEI
# 35) copy /work/c44d_ceres.csv to /read_csv/c44d_ceres_12month_EEI.csv
#
#########################################################
# 163 How to make TOA_Shortwave_Fluxfiles ################
#########################################################
# download https://ceres-tool.larc.nasa.gov/ord-tool/srbavg
#      63  TOA Longwave Flux - All-Sky
#          CERES_EBAF-TOA_Ed4.2.1_TOA_Longwave_Flux_-_All-Sky_March-2000toJanuary-2026
#          2026_01_TOA_Longwave_Flux_All-Sky.txt

#      63  TOA Longwave Flux - All-Sky
#          CERES_EBAF-TOA_Ed4.2.1_TOA_Longwave_Flux_-_All-Sky_March-2000toJanuary-2026
#          2026_01_TOA_Longwave_Flux_All-Sky.txt
# 
#  ceres olr csv download 
# https://neo.gsfc.nasa.gov/view.php?datasetId=CERES_LWFLUX_M
#The monthly climatology-corrected Earth's Energy Imbalance was record high in December 2025, at +2.57 W/m²!
#https://bsky.app/profile/leonsimons.com/post/3mfchkvjyjs2k
#https://bsky.app/profile/thomas-boettcher.bsky.social/post/3mfcnnsfkgk2h
# NASA CERES Earth's Energy Imbalance
#—Absorbed Solar Radiation (ASR)
#—Outgoing Longwave Radiation (OLR)
