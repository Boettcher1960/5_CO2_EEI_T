# config.py 
# version 5b56
# Configuration parameters for the climate analysis tool

# part61_EEI # like part41_ceres_eei make EEI 120 month csv
# 
# line 2 defines the left Y axis. example
# part43_ceres_eei = 2  #  0..2 W/m2    EEI 12 month running mean.
#
# line 3 defines the right Y axis. example
# part43_ceres_eei = 3  # 43.1  3,4 print EEI 12 month running mean.

# line 4 makes additional right y axis 20 to the right

# line 5 makes additional right y axis 60 to the right

# line 6 is developv part61_EEI 

# 8.3 print the left y axis 
# Axis mode y axis left
yl_mode = 3  # 6 TOA energy in W/m2 y axis left mode
# 8.5 configure the right axis legend 
# Axis mode y axis right
yr_mode = 4  # (0=no yaxis) (7 one T °C y axis right mode)


# yl_mode = 2 ppm CO2 y axis left mode
# yl_mode = 3 Gt CO2 y axis left mode
# yl_mode = 4 EEI in W/m2 y axis left mode
# yl_mode = 5 delta ppm CO2 y axis left mode
# yl_mode = 6 # TOA energy in W/m2 y axis left mode
# yl_mode = 7 Temperature in °C y axis left mode



# Plot configuration flags
plot22_CO2_Mauna_Loa = 0 # 22.1 declare global integer variable (2= print in line 2)
plot23_Glen_CO2 = 0      # 23.1 declare global integer variable (4= print in line 4)
plot25_long_CO2 = 0      # 25.1 
plot34_CO2_emission =    4   # 34.1 row 4
plot34_CO2_emission_mode = 3 # 34.1 mode 

part41_ceres_eei = 0  # print EEI 12 month running mean. Info in line 3 below the plot
part42_ceres_eei = 0  # 3,4 print EEI 48 month running mean. Info in line 4 below the plot
part43_ceres_eei = 0  # 43.1 2=left y axis 3,4 print EEI 12 month running mean.
part44_ceres_eei = 0 # 47 is local 

plot52_delta_CO2_red_bars = 0
plot53_CO2_orange2025 = 0
plot54_Glen_delta_on = 0
plot55_population_on = 0

play_61_CERES = 0     # 12 CERES EEI 12 month like part41_ceres_eei 
play_62_CERES = 0     # 12 CERES EEI 12 month like part41_ceres_eei 

plot71_temperature = 0
plot72_AESS_T = 0
plot73_ECS_T = 0
plot74_GIS_T = 3 # 3=right y axis
linear_41_75 = 0
plot76_my_T = 0
plot_T_77 = 0
parameter84_save_png = 8

# Colors
c22 = "blue"
c23 = "#4554A8C6"
c25 = "green"
c34 = "#942296C5"
c41 = "#289C1684"
c42 = "purple"
c43 = "#13DF2F84"
c44 = "blue"
c61 = "#0D91A090"
c62 = "#9522AA90"

c71 = "red"
c72 = "red"
c74 = "red"
c75 = "#371EA484"
c76 = "red"


# Text definitions (added missing print texts)
blue22_text = "blue dots: CO2 measured at Mauna Loa (2025 = 427.35 ppm) 22"
text_plot23_Glen = "calculated CO2 dashed blue line = 0.0132251t² - 51.0337t + 49,536 ppm 23"
blue25_text = "green: CO2 NOAA 800_000 year ice data 25"
print34_text = "purple dots: cumulative CO2 emissions Carbon Brief 34 mode"
p41_text = "Earth Energy Imbalance W/m² moving average 12 month 41"
p42_text = "Earth Energy Imbalance W/m² moving average 48 month 42"
p43_text = "Earth Energy Imbalance W/m² moving average 12 month 43"
p44_text = "Earth Energy Imbalance W/m² moving average 44"
print74_text = "Temperature in °C giss.nasa.gov Hansen+0.3°C 74 n"
print75_text = "Hansen linear fit from 2015 +0.41°C 75"  # Added for linear_41_75
green55_text = "Green line: Earth Population in billion"
red71_text = "red quadratic Temperature = 0.000618t² - 2.459 t + 2446.0579 in °C 71"
red72_text = "AESS_T Apparent Earth System Sensitivity = 8°C * log2(CO2/C0) 72"
my76_text = "guessed quadratic temperature my_T 76"



# Axis ranges
y_min = 250 # 250 ppm CO2  yl_mode == 2:  # CO2 mode
y_max = 500 # 500 ppm CO2  yl_mode == 2:  # CO2 mode
y_Tmin = 0
y_Tmax = 2.5
y_Emin = 0 # yl_mode = 4  EEI in W/m2 y axis left mode
y_Emax = 2 # yl_mode = 4  EEI in W/m2 y axis left mode
y_TOAmin = 97  # bug is double set in plotting.py line 56
y_TOAmax = 100 # bug is double set in plotting.py line 57
x_anf = 1980
x_end = 2030

# constants
# C280 =275 in Zack Labe plots.
C280 = 280

# Text positioning
tr1x = -0.09
tr2x = 0.01
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
# test CO2 plots  ##############################
#########################################################


"""


-----------------------v = "5b4


-----------------------v = "5b44
plot22_CO2_Mauna_Loa = 2 
plot74_GIS_T = 3

-----------------------v = "5b40" #  test old plots
# Plot configuration flags

make a struct/df with 6 columns and 88 rows.

column 1 is integer 0 to 80
column 2 are the names ASCII
column 3 are integer 3 //  example plot and make legend in line 3
column 4 are colors // example "red" 
column 5 is the minimum // example 280
column 6 is the maximum scaling // example 450 ppm

below is column 2:
plot22_CO2_Mauna_Loa = 0
plot23_Glen_CO2 = 0
plot25_long_CO2 = 0
plot34_CO2_emission = 0

part41_ceres_eei = 0  # print EEI 12 month running mean. Info in line 3 below the plot
part42_ceres_eei = 0  # 3,4 print EEI 48 month running mean. Info in line 4 below the plot
part43_ceres_eei = 2  # 43.1 2=left y axis 3,4 print EEI 12 month running mean.
part44_ceres_eei = 0 # 47 is local 

plot52_delta_CO2_red_bars = 0
plot53_CO2_orange2025 = 0
plot54_Glen_delta_on = 0
plot55_population_on = 0

play_61_CERES = 48     # 12 CERES EEI 12 month like part41_ceres_eei 
play_62_CERES = 12     # 12 CERES EEI 12 month like part41_ceres_eei 

plot71_temperature = 0
plot72_AESS_T = 0
plot73_ECS_T = 0
plot74_GIS_T = 3 # 3=right y axis
linear_41_75 = 0
plot76_my_T = 0
plot_T_77 = 0

The struct/df (22) interfaces plot22_CO2_Mauna_Loa.
The struct/df (22 ) interfaces the color plot22_CO2_Mauna_Loa.


parameter84_save_png = 8
-----------------------v = "5b40" #  test old plots




 
"""


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
