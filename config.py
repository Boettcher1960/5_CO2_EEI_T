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
plot22_CO2_Mauna_Loa = 0 # 22.1 declare global integer variable (2= print in line 2)
plot23_Glen_CO2 = 0      # 23.1 declare global integer variable (4= print in line 4)
plot25_long_CO2 = 0      # 25.1 

plot31_CO2_emission =    0   # 31.1 CO2_emission 1800 Gt CO2 Carbon Brief made with play_63_CB 
plot32_CO2_emission =    0   # 32.1 CO2_emission 600 GtC Carbon Brief made with play_63_CB 


plot34_CO2_emission =    0   # 34.1 row 4 
plot34_CO2_emission_mode = 0 # 34.1 mode 
# plot31__CO2_emission mode 1
# plot32__CO2_emission mode 2
# plot33__CO2_emission mode 3
# plot34_CO2_emission mode 4
plot34_CO2 = 0

part41_ceres_eei = 0  # print EEI 12 month running mean. Info in line 3 below the plot
part42_ceres_eei = 2  # 5,3,4 print EEI 48 month running mean. Info in line 4 below the plot
part43_ceres_eei = 4  # 3 , 2=left y axis 3,4 print EEI 12 month running mean.
part44_ceres_eei = 0  # 47 is local 

plot52_delta_CO2_red_bars = 0 # (3=print numbers)
plot53_CO2_orange2025 = 0
plot54_Glen_delta_on = 0
plot55_population_on = 0 # 5 word with y axis right

play_61_CERES = 1     # create 1..12..48..99 CERES EEI.csv _c61_out_ceres.csv // copy to 41_ceres_eei
play_62_CERES = 0     # 12 CERES EEI 12 month like part41_ceres_eei 
play_63_CB    = 0 # 5 carbon brief CO2 values https://ourworldindata.org/grapher/cumulative-co-emissions?country=~OWID_WRL&overlay=download-data

plot71_temperature = 0
plot72_AESS_T = 0
plot73_ECS_T = 0
plot74_GIS_T = 3 # 3=right y axis
linear_41_75 = 0 # 4
plot76_my_T = 0
plot_T_77 = 0
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
c43 = "#13DF2F84"
c44 = "blue"
c52 = "#7C8825FA"
c52bar = "#C1D43408"
c55 = "#34D48FC7"
c61 = "#0D91A090"
c62 = "#9522AA90"
c63 = "#1652D490"

c71 = "red"
c72 =  "#BD316990"
c73 =  "#13DF2F84"
c74 = "red"
#c74 = "#9522AA90"
c75 = "#371EA484"
c76 = "#13DF2F84"
c77 = "#34753D84"

# Text definitions (added missing print texts)
blue22_text = "blue dots: CO2 measured at Mauna Loa (2025 = 427.35 ppm) 22"
text_plot23_Glen = "calculated CO2 dashed blue line = 0.0132251t² - 51.0337t + 49,536 ppm 23"
blue25_text = "green: CO2 NOAA 800_000 year ice data 25"
print31_text = "dots: cumulative CO2 emissions in Gt     Carbon Brief / Our World in Data             31"
print32_text = "dots: cumulative CO2 emissions in GtC     Carbon Brief / Our World in Data            32"

print34_text = "purple dots: cumulative CO2 emissions Carbon Brief 34 mode"
p41_text = "Earth Energy Imbalance W/m² moving average 12 month 41"
p42_text = "Earth Energy Imbalance W/m² moving average 48 month 42"
p43_text = "Earth Energy Imbalance W/m² moving average 12 month 43"
p44_text = "Earth Energy Imbalance W/m² moving average 44"
print74_text = "Temperature in °C giss.nasa.gov Hansen+0.3°C 74 n"
print75_text = "Hansen linear fit from 2015 +0.41°C 75"  # Added for linear_41_75
green55_text = "Green line: Earth Population in billion  55"
red71_text = "red quadratic Temperature = 0.000618t² - 2.459 t + 2446.0579 in °C 71"
red72_text = "AESS_T Apparent Earth System Sensitivity = 8°C * log2(CO2/C0) 72"
my76_text = "guessed quadratic temperature my_T 76"



# Axis ranges
y_min = 350 # 250 ppm CO2 
y_max = 430 # 500 ppm CO2  

y_25min = 250 # nok   only for y axis 
y_25max = 430 # only for y axis
y_Gmin = 0 # 250 ppm CO2 
y_Gmax = 2000 # 2500 Gt CO2  
y_31Gmin = 0 # 250 ppm CO2  
y_31Gmax = 2000 # 2500 Gt CO2  
y_32min = 0   #   0 GtC
y_32max = 800 # 800 GtC

y_Emin = -15 #   EEI in W/m2 y axis left mode
y_Emax = 16 #   EEI in W/m2 y axis left mode
y_TOAmin = 97  # bug is double set in plotting.py line 56
y_TOAmax = 100 # bug is double set in plotting.py line 57

y_52min = 0 # plot52_delta_CO2_red_bars
y_52max = 4 # plot52_delta_CO2_red_bars
y_55min = 6 # plot55_population_on = 5
y_55max = 9 # plot55_population_on = 5

y_Tmin = 0
y_Tmax = 2.6
y_74min = y_Tmin # for GIS Temperature only 
y_74max = y_Tmax # for GIS Temperature only 

x_anf = 2000
x_end = 2026

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
tr6y = -.57
trs = 20

# Legend line positions
lr2x1 = 0.065
lr2x2 = 0.085
lr1y = 0.248
lr2y = 0.211
lr3y = 0.168
lr4y = 0.129
lr5y = 0.095
lr6y = 0.034

# Figure size
scale_mode = 10 # other values are not used
print_debug = 10 # print some items 


#########################################################
# CO2 plots  ##############################
#########################################################
# part 2.2 plot CO2 Mauna Loa
# part 2.3 plot23_Glen_CO2 
# part 2.5 plot25_long_CO2  -800 000 years ppm CO2 file


"""

-----------------------v = "5c90


 
"""

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
# 61 How to make EEI files ##############################
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
#     /Dokumente/Python/5_CO2_EEI_T/read_csv/2016_01_EEI_CERES_TOA Net Flux.txt
# 
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
# with 5b2*pc set play_61_CERES = 48
# # run1 part41_ceres_eei = 12
# run2 part41_ceres_eei = 48
# run3 part41_ceres_eei = 50
#
# 
#
#########################################################
# 62 How to make TOA_Shortwave_Fluxfiles ################
#########################################################
# download https://ceres-tool.larc.nasa.gov/ord-tool/srbavg
# CERES_EBAF-TOA_Ed4.2.1_TOA_Shortwave_Flux_-_All-Sky_March-2000toJanuary-2026.txt

#########################################################
# 63 How to make TOA_Longwave Flux files ################
#########################################################
# download https://ceres-tool.larc.nasa.gov/ord-tool/srbavg
#      63  TOA Longwave Flux - All-Sky
#          CERES_EBAF-TOA_Ed4.2.1_TOA_Longwave_Flux_-_All-Sky_March-2000toJanuary-2026
#          2026_01_TOA_Longwave_Flux_All-Sky.txt

#      63  TOA Longwave Flux - All-Sky
#          CERES_EBAF-TOA_Ed4.2.1_TOA_Longwave_Flux_-_All-Sky_March-2000toJanuary-2026
#          2026_01_TOA_Longwave_Flux_All-Sky.txt
# 
# ok horizontal 1.8°C line is T value

#  ceres olr csv download 
# https://neo.gsfc.nasa.gov/view.php?datasetId=CERES_LWFLUX_M

# 
#1E318 
# ASR 48 months 

#The monthly climatology-corrected Earth's Energy Imbalance was record high in December 2025, at +2.57 W/m²!
#https://bsky.app/profile/leonsimons.com/post/3mfchkvjyjs2k
#https://bsky.app/profile/thomas-boettcher.bsky.social/post/3mfcnnsfkgk2h
# NASA CERES Earth's Energy Imbalance
#—Absorbed Solar Radiation (ASR)
#—Outgoing Longwave Radiation (OLR)
