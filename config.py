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
run_10_png = 0 # 2 , 4, 5, 6 , 11 run 5 figures : 0 = no automatic
figure100 = 0 #  0 means create no old figure 1= make old figuure
                # substack #28 uses 102 , 104 , 105 , 106 , 107 , 110 Global Warming EEI sets the World on Fire #28 Published 20. Nov. at 21:18
                #  0 means create no old figure 1= make old figuure
figure202 = 0 # 2=new figure with era5 temperature and quadratic curve 209
figure303 = 0 # 3 , 4 
              # for figure303 = 3 keep the x axis logarithmic and plot in Rovang_figure_1.png
              # for figure303 = 4 make linear x axis and plot in Rovang_figure_2.png
figure404 = 0 # 3 , 12, 24, 36 , 48 60 72 96   409 48=create quadratic-fit figure for matching play_61_EEI

figure504 = 5 # 1=create ERA5 trailing 365-day temperature figure
figure504_days_linear_fit = 350 # use 30 days for quadratic fit

figure4_9 = 6 # write figure 9 and use the 48 month averaging
figure505 = 0  # 1095 , 1461, 1095, 720, 365, 24  1826 3650  # https://sites.ecmwf.int/data/climatepulse/data/series/era5_daily_series_2t_global.csv
figure505_offset = 0.90 # 0.91 ClimateCasino 0.90 Zeke, Rahmstorf..Niko Freudsheim apply its 0.88 °C offset.
figure505_days_linear_fit = 720 # 10 years 3652, 1461, 1095, 720, 365,   1826

# 8.5 configure the right axis legend 
yr_60  = 60  # 60 50 (0=no right yaxis) 60 * 4 = 240 pixel to the right
yr_150    = 150  #  240 - 150 = 90 ( 60 * 4 = 240      plot8_right_y_axe_for_T_74
yr_delete = 1 # 9 = delete all axes delete axe 4

# Plot configuration flags
plot22_CO2_Mauna_Loa = 0 # 2 ,3    22.1 declare global integer variable (2= print in line 2)
plot23_Glen_CO2 = 0      # 2, 3 , 23.1 declare global integer variable (4= print in line 4)
plot25_long_CO2 = 0   # 4 2, 3 25.1 

# plot27_EsT = 0 #  EEI simulates EEI linear  every 1 W/m²/month 
plot28_E_T = 0 #  EEI simulates T linear add 0.00208°C for every 1 W/m²/month 
a28_start = 2026.5   # 2015 starting year of play_60_T_E
a28_offset = 1.5  
plot29_ETq = 5 #  EEI simulates T quadratic  add 0.00208°C for every 1 W/m²/month 
a29_start = 2026.5   # 2015 starting year of play_60_T_E
a29_offset = 1.5  
plot30_c = 0 #  EEI =1.5W T linear add 0.00208°C for every 1 W/m²/month 
a30_start = 2026.5   # 2015 starting year of play_60_T_E
a30_offset = 1.5  
a30_value = 1.5 # const value  W/m²

plot31_CO2_emission = 0  # 2, 3, 4   # 31.1 CO2_emission 1800 Gt CO2 Carbon Brief made with play_63_CB 
plot32_CO2_emission = 0  # 2, 3 # CO2_emission 600 GtC Carbon Brief made with play_63_CB 

plot34_CO2_emission = 0      # 4,     # 34.1 row 4 
plot34_CO2_emission_mode = 0 # 4, 2, 4   # 34.1 mode 
# plot31__CO2_emission mode 1 # plot32__CO2_emission mode 2 # plot33__CO2_emission mode 3
plot34_CO2 = 0 # 0     plot34_CO2_emission mode 4

plot42_EEI_48month = 0  # 2,3,4,5 print EEI 48 month running mean. Info in line 4 below the plot
plot43_eei_12month = 0  # 2, 3, 4 ,5 2=left y axis 3,4 print EEI 12 month running mean. [W/m2]
part44_ceres_eei   = 0  # 47, 3, 48,   is local 
plot45_OLR         = 0 # 2, 3, 4 looks like simons 48 months. Outgoing Longwave Radiation OLR updated to 2026_07
plot46_ASR         = 0 # 2, 3 ASR Absorbed Solar Radiation from _CERES_ASR 48 months average [W/m2]
plot47_albedo48    = 0  # 4  
plank48 = 0 # 3 , 5 plank feedback is 68_ERA temperature * 3.22
plot49 = 0  # 3 plot49 = plank48 - plot45_OLR missing   long wave radiation absorbed within the atmosphere

plot52_delta_CO2_red_bars = 0 # 3 (3=print numbers)
plot53_CO2_orange2025 = 0 # no curve is visible 3, 4
plot54_Glen_delta_on = 0 # no curve is visible 3, 4
plot55_population_on = 0 # 5 word with y axis right
plot56_delta_CO2_4years = 0 # # no curve is visible 3, 4 
# https://bsky.app/profile/thomas-boettcher.bsky.social/post/3mnkupgsz7s2k

play_60_T_E = 48   # 2=no average 12 , 24 , 48 add 0.00208°C for every 1 W/m²/month    Piers Forster 1 W/m² in 1month warmes 0.00208°C 
a60_start = 2005   # 2015 starting year of play_60_T_E
a60_offset = 1.01     # 1.01 1 , 0.85 add offset 0.2°C at start of adding
play_61_EEI = 0   # 2; 12, 24, 36, 48 create 1..12..48..99 CERES EEI.csv _c61_out_ceres.csv // copy to 41_ceres_eei
p61raw = "read_csv/CERES_EBAF-TOA_Ed4.2.1_TOA_Net_Flux_-_All-Sky_March-2000toSeptember-2026.txt" # raw CERES downloaded 
play_62_EEA = 0    # 12, 24, 36, 48  Earth Energy Accumulated EEA is sum of EEI
play_63_CB  = 0 # 5=world   plan 2=germany..
                # carbon brief CO2 values https://ourworldindata.org/grapher/cumulative-co-emissions?country=~OWID_WRL&overlay=download-data
play_64_ASR_anomaly = 0 #  12 , 24 , 48 # absorbed solar radiation ASR anomaly = 1.48 W/m² 2.1_anom_TOA_Shortwave_Flux_-_All-Sky
play_65_ASR         = 0 # 12 ASR = 242 W/m² TOA_Shortwave_Flux_-_All-Sky
play_66_OLR         = 0 # 12, 24 looks like GISS temp 48, 36, 24, 12 ok outgoing longwave radiation OLR = 240 [W/m2]
play_67_albedo      = 0   # line2 1..12..48..99 create 1..12..48..99 CERES
play68_ERA          = 1461 # 1461, 1095, 720, 365, 24  1826   # https://sites.ecmwf.int/data/climatepulse/data/series/era5_daily_series_2t_global.csv
play69_AA           = 0 # 48 , 3,  7 , 11, 12, 13,48    albedo anomaly  # 69.12
play69_AA_in = "work/69a_AA_Albedo_anomaly_2026_08.txt"  # 69.13  config.py   play69_AA_in = "69a_AA_Albedo_anomaly_2026_08.txt" input filename

plot71_temperature = 0 # 2 3 5
plot72_AESS_T = 0 # 2 , 3 
plot73_ECS_T = 0 # 3
global plot74_GIS_T 
plot74_GIS_T = 2 # 2, 3,4,5,6,7 =right y axis
linear_41_75 = 3 # 3 4 5
plot76_my_T = 0 # 3, 5
plot_T_77 = 0 # 3, 4
plot_T_78 = 0 # 3 , 4 , 5 Tom Harris

# variable to show play variable in line 4
line2_play = 0  # 60 61  62
line3_play = 68  # 60 play_62_EEA #   68 play68_ERA = 720
line4_play = 60 # 68 , 67 , 66 , 62 , 61 play_61_EEI = 36 
line5_play = 28  # 62 61 68
line6_play = 0
line7_play = 99 # 99 no line 7 

parameter84_save_png = 8

# Colors
c21 = "blue"
c22 = "blue"
c23 = "#4554A8C6"
c25 = "green"
c28 = "#E123539F"
c29 = "#1A27DECC"
c30 = "#0F9BE190"
c31 = "#9B107F90"
c32 = "#10929B90"
c32 = "red"
c34 = "#942296C5"
c41 = "#289C1684"
c42 = "purple"
#c42 = "#13DF2F84"
c43 = "green" # "#70A915B1"
c44 = "blue"
c45 = "#1A27DECC"
c46 = "#B72E1CEA"
c47 = "#31A28ADC"
c48 = "red"
c49 = "#DB1ADECC"

c52 = "#7C8825FA"
c52bar = "#C1D43408"
c55 = "#34D48FC7"
c60 = "#E14C239F"
c60a ="black"
c61 = "#34D48FC7"
c62 = "#BEBE21DD"
c63 = "#1652D490"
c64 = "#D91919A6"
c65 = "#1E37B9E0"
c66 = "#1E37B9E0"
c67 = "#0F9BE190"
c67 = "red"
c68 = "#0F9735D3"
c69 = "#1652D490"

c71 = "red"
c71 =  "#AB263590"
c72 =  "#31BD9590"
c73 =  "red"
c74 = "#26D00BC2"
c75 = "#6EC91FB3"
c76 = "#13DF2F84"
c77 = "#34753D84"
c78 = "#9D2A9984"

# Text definitions (added missing print texts)
blue22_text      = "blue dots: CO$_2$ measured at Mauna Loa (2025 = 427.35 ppm)                            22"
text23 = "CO$_2$ calculated dashed blue line      CO2 = 0.0132251t² - 51.0337t + 49,536 ppm    23"
text25 = "green: CO$_2$ in ppm    NOAA     800_000 year ice data                                                 25"
text28 = "Temperature in °C   with   calculated   linear      EEI = 0.04788 x + 0.408                  28" 
text29 = "Temperature in °C  with calculated  quadratic    EEI = 0.0008x² +0.0293x +0.474     29" 
text30 = "Temperature in °C   with constant EEI = 1.5 W/m²       warms 0.5°C in 14 years        30" 
text31 = "dots: cumulative CO2 emissions in GtCO2     Carbon Brief / Our World in Data           31"
text32 = "dots: cumulative CO2 emissions in GtC       Carbon Brief / Our World in Data              32"
text34 = "purple dots: cumulative CO2 emissions Carbon Brief 34 mode                                   34"

text41 = "Earth Energy Imbalance W/m² moving average 12 month 41"
text42 = "Earth Energy Imbalance W/m² moving average 48 month 42"
text43 = "Earth Energy Imbalance in W/m²                                  moving average 12 month    43"
text44 = "Earth Energy Imbalance W/m² moving average 44"
text45 = "out OLR Outgoing Longwave Radiation OLR in W/m²     moving average 48 month  45"
text48 = "out FB1 Plank Feedback    in W/m²     era5-4year average   -0.74) * 3.22                   48"
text49 = "missing Long Wave Radiation =  FB1 Plank Feedback -OLR   in W/m²   Tom Harris   49"
text55 = "Green line: Earth Population in billion                                               55"

text60a = "An EEI of 2 W/m² sustained over a decade would add roughly half a degree of warming."
text60b = "with EEI of 2 W/m²    sustained over decades:     2035=2°C    2055=3°C     2075=4°C"
# 10 years 0.5°C * 1.5/2 = 0.375°C x years = 10 * 2 /1.5 = 13.3 years 27 years for 1°C more
text60c = "with EEI of 1.5 W/m² sustained over decades:     2038=2°C    2065=3°C     2092=4°C"
text60 = "the measured EEI - CERES satellites -  warmed the earth 1.5°C in the year 2025     60"  # if figure100 > 99
  

text63 = "carbon brief cummulative CO2 emissions in GtCO2 since 1750    ourworldindata     63"
text68 = "Temperature in °C  from ERA5  with   calculated   linear  quadratic            68" 
text71 = "Temperature in °C 0.000618t² - 2.459 t + 2446.0579            from  @reescatophul     71"
# "Temperature in °C 0.000618t² - 2.459 t + 2446.0579                       @reescatophul     71", 
# "Temperature in °C 0.0004t² + 0.0019 t + 0.5079     from Tom Harris                         71", 
text72 = "Temperature in °C   AESS Apparent Earth System Sensitivity = 8°C * log2(CO2/C0  72"
text73 = "Temperature in °C   Earth Climate sensitivity              dT = ECS * log2 ( C / C0 )      73"
text74 = "Temperature in °C   giss.nasa.gov   Hansen+0.3°C                                                   74"  
text75 = "Hansen linear fit   from 2015    +0.41°C                       75"  # Added for linear_41_75
text76 = "Temperature in °C   my guess quadratic increase                                                      76" 
text77 = "Temperature in °C   quadratic           1950=0.2°C     2013=1°C     2022=1.5°C       77" 
text78 = "Temperature in °C   quadratic       Tom Harris   T = 0.0004x²  + 0.0019x + 0.5079      78" 


# Axis ranges
y_min = 310 # 250 ppm CO2 
y_max = 430 # 500 ppm CO2  

y_22min = 360 # ppm CO2
y_22max = 440 # ppm CO2
y_25min = 370 # nok   only for y axis 
y_25max = 430 # only for y axis

y_28min = 0.5 #  Temperature in °C y axis left mode
y_28max = 2.5  #  Temperature in °C y axis left mode
y_29min = 0.5  #  Temperature in °C y axis left mode
y_29max = 2.5 #  Temperature in °C y axis left mode
y_30min = 0.8  #  Temperature in °C y axis left mode
y_30max = 3.2  #  Temperature in °C y axis left mode
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

y_42min = 0.2 #   EEI in W/m2 y axis left mode
y_42max = 2.2 #   EEI in W/m2 y axis left mode
y_43min = 0    # EEI in W/m2
y_43max = 2  # EEI in W/m2
y_44min = 0.0 #   EEI in W/m2 y axis left mode
y_44max = 2 #   EEI in W/m2 y axis left mode

y_45min = 239.6    # OLR in W/m2
y_45max = 243.6  # OLR in W/m2 242.8
y_46min = 240    # ASR in W/m2
y_46max = 242.8  # ASR in W/m2
y_47min = 0.294 # albedo in %
y_47max = 0.286 # albedo in %
y_48min = 0
y_48max = 3
y_49min = 0
y_49max = 1.2

y_52min = 0 # plot52_delta_CO2_red_bars
y_52max = 4 # plot52_delta_CO2_red_bars
y_55min = 2 # plot55_population_on = 5
y_55max = 9 # plot55_population_on = 5

y_60min = 0.5  #  Temperature in °C y axis left mode
y_60max = 2.5  #  Temperature in °C y axis left mode
y_61min = 0  #  also for figure 404  EEI in W/m2 y axis left mode
y_61max = 2  #   also for figure 404  EEI in W/m2 y axis left mode

y_62min = 0  # EEA in ZJ
y_62max = 400  # EEA in ZJ

y_64min = -1.6  # in W/m2
y_64max = 2  # in W/m2
y_65min = 239.5  # ASR in W/m2
y_65max = 243.5  # 242.8  # ASR in W/m2

y_66min = 239.5  # OLR in W/m2
y_66max = 243.5 # 242.8  # OLR in W/m2

y_67min = 0.2936  # 0.294 albedo in %
y_67max = 0.2862  # 0.286 albedo in %
y_67min = 0.296  # Hansen no swap albedo in %
y_67max = 0.286   # Hansen no swap albedo in %

y_68min = 0.5  # for era5 Temperature
y_68max = 2.5 # for era5 Temperature 

y_69min = 1.6   # albedo anomaly in W/m2 
y_69max = -1.6  # albedo anomaly in W/m2
#y_69min = 1.3   # albedo anomaly in W/m2 
#y_69max = -1.5  # albedo anomaly in W/m2

y_Tmin = 0
y_Tmax = 2.5 # 1.7
y_71min = 0
y_71max = 3 # 1.7
y_72min = 0
y_72max = 6 # 
y_73min = 0
y_73max = 6 # 
y_74min = 0.5  # for GIS Temperature 
y_74max = 2.5  # 1.6 for GIS Temperature 
y_75min = 0.5 #  Temperature  
y_75max = 2.5   #  Temperature 
y_76min = 0 #  Temperature  
y_76max = 4   #  Temperature 
y_77min = 0 #  Temperature  
y_77max = 2.5 #  Temperature 
y_78min = 1.9 #  for Tom Harris Temperature 
y_78max = 2.1 #  for Tom Harris Temperature

# YLO, YHI = 5, 40
x_303min = 200   # 125  figure303 CO2 x axis 
x_303max = 600  # 1500 figure303 CO2 x axis 
y_303min = 10  # 5 13 figure303 Temperature y axis left
y_303max = 25 # 30 17 figure303 Temperature y axis left
y_504min = 1.44 # manimum 0°C
y_504max = 1.64 # maximum 4°C
y_505min = 0 # manimum 0°C
y_505max = 3 # maximum 4°C


box303_3Ma = 5 # in figure 304 line 5 print 400 ppm resulted in 3C warming in the Pliocene, 3-4 million years ago
cbox303Ma="#94dd2d"
cbox303Maedge="#16b426"
box304_16Ma = 6 # in figure 304 line 6 print 400 ppm resulted in 5C warming in the Pliocene, 16 million years ago
cbox304Ma="#ffcccc"
cbox304Maedge="red"
plot304_450ppm_blue_band = 0 # 0 , 1 = plot

x_anf = 1970   # 2005   2000
x_end = 2055   # 2028   2065

# XLO, XHI = 125, 1500

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
tr5y = -.47  # -.47    -.46  Text position
tr6y = -.53  # -.53    -.51  Text position
tr7y = -.59  # -.57  Text position
trs = 20

# Legend line positions
lr2x1 = 0.065
lr2x2 = 0.085
lr1y = 0.248
lr2y = 0.211
lr3y = 0.168
lr4y = 0.129
lr5y = 0.092 # 0.092   0.095 Legend line position
lr6y = 0.054 # 0.054   0.064 Legend line position
lr7y = 0.034


# Figure size
scale_mode = 10 # other values are not used
print_debug = 10 # print some items 




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

# 111.1 overwrite config values 

if figure100 == 102:
   # used in Substack: Global Warming EEI sets the World on Fire #28
   text100 = "Figure 2: Global Warming ... possible Temperature in 2050 = 2.5°C with  Hansen linear fit +0.4°C"

   plot74_GIS_T = 2 # Hansen GISS temperature
   text74 = "measured Temperature in °C from  giss.nasa.gov   Hansen+0.3°C                             74"  
   c74 =  "#2EDF1B90"
   c74 =  "green"
   y_74min = -0.5  # for GIS Temperature 
   y_74max = 3  # 1.6 for GIS Temperature 

   linear_41_75 = 3
   text75 = "James Hansen:   linear 0.4°C   warming  every  10  years    -  doted  green               75"  # Added for linear_41_75
   c75 = "#226C12CC"
   y_75min = -0.5 #  Temperature  
   y_75max = 3   #  Temperature 

   line4_play = 0
   play_60_T_E = 0
   plot_T_78 = 0 # 3 , 4 , 5 Tom Harris
   plot29_ETq = 0 #  EEI simulates T quadratic  add 0.00208°C for every 1 W/m²/month 
   plot28_E_T = 0 # linear EEI increase in line 5

   x_anf = 1880   # 2005
   x_end = 2065   # 2028   2065

   if print_debug > 9:
      # print(f"config__433  {plot28_E_T}", text28)
      print(f"config__460  {figure100}", text100)

elif figure100 == 104:
   # used in Substack: Global Warming EEI sets the World on Fire #28
   text100 = "Figure 4: Global Warming ... possible Temperature in 2050 = 2.6°C using Tom Harris quadratic fit"

   plot74_GIS_T = 2 # Hansen GISS temperature
   text74 = "measured Temperature in °C from  giss.nasa.gov   Hansen+0.3°C                             74"  
   c74 =  "#2EDF1B90"
   c74 =  "green"
   y_74min = 0.5  # for GIS Temperature 
   y_74max = 3  # 1.6 for GIS Temperature 

   linear_41_75 = 3
   text75 = "James Hansen:   linear 0.4°C   warming  every  10  years    -  doted  green               75"  # Added for linear_41_75
   c75 = "#226C12CC"
   y_75min = 0.5 #  Temperature  
   y_75max = 3   #  Temperature 

   plot_T_78 = 4 # 3 , 4 , 5 Tom Harris
   text78 = "Temperature in °C   quadratic       Tom Harris   T = 0.0004x²  + 0.0019x + 0.5079      78" 
   text78 = "Temperature in °C      Tom Harris  quadratic   T = 0.0004 x²  + 0.0019 x + 0.5079      78" 
   y_78min = 0.5 #  for Tom Harris Temperature 
   y_78max = 3 #  for Tom Harris Temperature

   plot29_ETq = 0 
   line4_play = 0
   play_60_T_E = 0

   if print_debug > 9:
      # print(f"config__433  {plot28_E_T}", text28)
      print(f"config__492  {figure100}", text100)


elif figure100 == 105:
   # used in Substack: Global Warming EEI sets the World on Fire #28
   text100 = "Figure 5: Global Warming calculated with linear EEI increase.   Result = 2.7°C in the year 2050"

   plot74_GIS_T = 2 # Hansen GISS temperature
   text74 = "measured Temperature in °C from  giss.nasa.gov   Hansen+0.3°C                             74"  
   c74 =  "#2EDF1B90"
   c74 =  "green"
   y_74min = 0.5  # for GIS Temperature 
   y_74max = 3  # 1.6 for GIS Temperature 

   linear_41_75 = 3
   text75 = "James Hansen:  linear 0.4°C warming  every  10  years      =  2.4°C in year 2050      75"  # Added for linear_41_75
     
   c75 = "#226C12CC"
   y_75min = 0.5 #  Temperature  
   y_75max = 3   #  Temperature 

   play_60_T_E = 48   # 2=no average 12 , 24 , 48 add 0.00208°C for every 1 W/m²/month    Piers Forster 1 W/m² in 1month warmes 0.00208°C 
   text60 = "the measured EEI - CERES satellites -  warmed the earth 1.5°C in the year 2025       60"  # Added for linear_41_75
      
   a60_start = 2005   # 2015 starting year of play_60_T_E
   a60_offset = 1.01 
   line4_play = 60
   y_60min = 0.5  #  Temperature in °C y axis left mode
   y_60max = 3  #  Temperature in °C y axis left mode

   plot28_E_T = 5 # linear EEI increase in line 5
   text28 = "Global Warming  in  °C  calculated  with  -> linear  EEI = 0.04788 x  +  0.408              28"
   y_28min = 0.5  #  Temperature in °C y axis left mode
   y_28max = 3  #  Temperature in °C y axis left mode

   plot29_ETq = 0 #  EEI simulates T quadratic  add 0.00208°C for every 1 W/m²/month 
   a29_start = 2026.5   # 2015 starting year of play_60_T_E
   a29_offset = 1.5  
   y_29min = 0.5  #  Temperature in °C y axis left mode
   y_29max = 3  #  Temperature in °C y axis left mode

   plot_T_78 = 0 # 3 , 4 , 5 Tom Harris

   if print_debug > 9:
      # print(f"config__433  {plot28_E_T}", text28)
      print(f"config__534  {figure100}", text100)

elif figure100 == 106:
   # used in Substack: Global Warming EEI sets the World on Fire #28
   text100 = "Figure 6: Global Warming Temperature  calculated with EEI quadratic increase in 2050 = 3°C  "

   plot74_GIS_T = 2 # Hansen GISS temperature
   text74 = "measured Temperature in °C from  giss.nasa.gov   Hansen+0.3°C                             74"  
   c74 =  "#2EDF1B90"
   c74 =  "green"
   y_74min = 0.5  # for GIS Temperature 
   y_74max = 3  # 1.6 for GIS Temperature 

   linear_41_75 = 3
   text75 = "James Hansen:   linear 0.4°C   warming  every  10  years    -  dotted  green              75"  # Added for linear_41_75
   c75 = "#226C12CC"
   y_75min = 0.5 #  Temperature  
   y_75max = 3   #  Temperature 

   play_60_T_E = 48   # 2=no average 12 , 24 , 48 add 0.00208°C for every 1 W/m²/month    Piers Forster 1 W/m² in 1month warmes 0.00208°C 
   a60_start = 2005   # 2015 starting year of play_60_T_E
   a60_offset = 1.01 
   line4_play = 60
   y_60min = 0.5  #  Temperature in °C y axis left mode
   y_60max = 3  #  Temperature in °C y axis left mode

   plot29_ETq = 5 #  EEI simulates T quadratic  add 0.00208°C for every 1 W/m²/month 
   a29_start = 2026.5   # 2015 starting year of play_60_T_E
   a29_offset = 1.5  
   y_29min = 0.5  #  Temperature in °C y axis left mode
   y_29max = 3  #  Temperature in °C y axis left mode

   plot_T_78 = 0 # 3 , 4 , 5 Tom Harris

   if print_debug > 9:
      # print(f"config__433  {plot28_E_T}", text28)
      print(f"config__534  {figure100}", text100)

elif figure100 == 107:
   # used in Substack: Global Warming EEI sets the World on Fire #28
   text100 = "Figure 7: Global Warming Temperature  calculated with constant EEI = 1.5 W/m²  in 2050 = 2.4°C  "

   plot74_GIS_T = 2 # Hansen GISS temperature
   text74 = "measured Temperature in °C from  giss.nasa.gov   Hansen+0.3°C                             74"  
   c74 =  "#2EDF1B90"
   c74 =  "green"
   y_74min = 0.5  # for GIS Temperature 
   y_74max = 3  # 1.6 for GIS Temperature 

   linear_41_75 = 3
   text75 = "James Hansen:   linear 0.4°C   warming  every  10  years    -  doted  green               75"  # Added for linear_41_75
   c75 = "#226C12CC"
   y_75min = 0.5 #  Temperature  
   y_75max = 3   #  Temperature 

   play_60_T_E = 48   # 2=no average 12 , 24 , 48 add 0.00208°C for every 1 W/m²/month    Piers Forster 1 W/m² in 1month warmes 0.00208°C 
   a60_start = 2005   # 2015 starting year of play_60_T_E
   a60_offset = 1.01 
   line4_play = 60
   y_60min = 0.5  #  Temperature in °C y axis left mode
   y_60max = 3  #  Temperature in °C y axis left mode

   plot30_c = 5 #  EEI =1.5W T linear add 0.00208°C for every 1 W/m²/month 
   a30_start = 2026.5   # 2015 starting year of play_60_T_E
   a30_offset = 1.5  
   a30_value = 1.5 # const value  W/m²
   y_30min = 0.5  #  Temperature in °C y axis left mode
   y_30max = 3  #  Temperature in °C y axis left mode 

   plot29_ETq = 0 #  EEI simulates T quadratic  add 0.00208°C for every 1 W/m²/month 
   
   plot_T_78 = 0 # 3 , 4 , 5 Tom Harris

   if print_debug > 9:
      # print(f"config__433  {plot28_E_T}", text28)
      print(f"config__614  {figure100}", text100)


if figure100 == 110:
   # used in Substack: Global Warming EEI sets the World on Fire #28
   text100 = "Figure 10: Global Warming ... possible Temperatures in ..2050...  EEI, Hansen..."

   plot74_GIS_T = 2 # Hansen GISS temperature
   text74 = "measured Temperature in °C from  giss.nasa.gov   Hansen+0.3°C                             74"  
   c74 =  "#2EDF1B90"
   c74 =  "green"
   y_74min = 0.5  # for GIS Temperature 
   y_74max = 3  # 1.6 for GIS Temperature 

   linear_41_75 = 3
   text75 = "James Hansen:  linear 0.4°C warming every 10  years.        The year 2050 result = 2.4°C"  # Added for linear_41_75
      
   c75 = "#226C12CC"
   y_75min = 0.5 #  Temperature  
   y_75max = 3   #  Temperature 

   text78 = "Temperature in °C using Tom Harris quadratic formula.        The year 2050 result = 2.6°C" 
   plot_T_78 = 4 # 3 , 4 , 5 Tom Harris
   y_78min = 0.5 #  for Tom Harris Temperature 
   y_78max = 3 #  for Tom Harris Temperature

   line5_play = 60 
   play_60_T_E = 48

   plot28_E_T = 5 # linear EEI increase in line 5
   text28 = "Global Warming in °C  using linear increasing EEI.              The year 2050 result = 2.7°C" 
   y_28min = 0.5  #  Temperature in °C y axis left mode
   y_28max = 3  #  Temperature in °C y axis left mode

   plot29_ETq = 6 #  EEI simulates T quadratic  add 0.00208°C for every 1 W/m²/month 
   text29 = "Global Warming in °C  using quadratic increasing EEI.        The year 2050 result =  3  °C" 
   y_29min = 0.5  #  Temperature in °C y axis left mode
   y_29max = 3  #  Temperature in °C y axis left mode

   y_60min = 0.5  #  Temperature in °C y axis left mode
   y_60max = 3  #  Temperature in °C y axis left mode

   x_anf = 2005   # 2005
   x_end = 2065   # 2028   2065

   if print_debug > 9:
      # print(f"config__433  {plot28_E_T}", text28)
      print(f"config__450  {figure100}", text100)

elif figure100 == 111:
   text100 = "Figure 111: Global Warming calculated with EEI constant & linear & quadratic   in 2050 = 2.4...3°C  "

   plot74_GIS_T = 2 # Hansen GISS temperature
   text74 = "measured Temperature in °C from  giss.nasa.gov   Hansen+0.3°C                             74"  
   c74 =  "#2EDF1B90"
   c74 =  "green"
   y_74min = 0  # for GIS Temperature 
   y_74max = 3  # 1.6 for GIS Temperature 

   linear_41_75 = 3
   text75 = "James Hansen:   linear 0.4°C   warming  every  10  years    -  doted  green               75"  # Added for linear_41_75
   c75 = "#226C12CC"
   y_75min = 0 #  Temperature  
   y_75max = 3   #  Temperature 

   plot30_c = 3 #  EEI =1.5W T linear add 0.00208°C for every 1 W/m²/month 
   a30_start = 2026.5   # 2015 starting year of play_60_T_E
   a30_offset = 1.5  
   a30_value = 1.5 # const value  W/m²
   y_30min = 0  #  Temperature in °C y axis left mode
   y_30max = 3  #  Temperature in °C y axis left mode 

   play_60_T_E = 48   # 2=no average 12 , 24 , 48 add 0.00208°C for every 1 W/m²/month    Piers Forster 1 W/m² in 1month warmes 0.00208°C 
   a60_start = 2005   # 2015 starting year of play_60_T_E
   a60_offset = 1.01 
   line4_play = 60
   y_60min = 0  #  Temperature in °C y axis left mode
   y_60max = 3  #  Temperature in °C y axis left mode

   plot28_E_T = 5 #  EEI simulates T linear add 0.00208°C for every 1 W/m²/month 
   a28_start = 2026.5   # 2015 starting year of play_60_T_E
   a28_offset = 1.5  
   y_28min = 0  #  Temperature in °C y axis left mode
   y_28max = 3  #  Temperature in °C y axis left mode
   
   plot29_ETq = 6 #  EEI simulates T quadratic  add 0.00208°C for every 1 W/m²/month 
   a29_start = 2026.5   # 2015 starting year of play_60_T_E
   a29_offset = 1.5  
   y_29min = 0  #  Temperature in °C y axis left mode
   y_29max = 3  #  Temperature in °C y axis left mode
   
   plot_T_78 = 0 # 3 , 4 , 5 Tom Harris

   if print_debug > 9:
      # print(f"config__433  {plot28_E_T}", text28)
      print(f"config__699  {figure100}", text100)


elif figure100 == 112:
   text100 = "Figure 112: Global Warming calculated with EEI and Temperature   in 2050 = 2.4...3°C  "

   plot74_GIS_T = 2 # Hansen GISS temperature
   text74 = "measured Temperature in °C from  giss.nasa.gov   Hansen+0.3°C                             74"  
   c74 =  "#2EDF1B90"
   c74 =  "green"
   y_74min = 0  # for GIS Temperature 
   y_74max = 3  # 1.6 for GIS Temperature 

   linear_41_75 = 3
   text75 = "James Hansen:   linear 0.4°C   warming  every  10  years    -  doted  green               75"  # Added for linear_41_75
   c75 = "#226C12CC"
   y_75min = 0 #  Temperature  
   y_75max = 3   #  Temperature 

   plot30_c = 3 #  EEI =1.5W T linear add 0.00208°C for every 1 W/m²/month 
   a30_start = 2026.5   # 2015 starting year of play_60_T_E
   a30_offset = 1.5  
   a30_value = 1.5 # const value  W/m²
   y_30min = 0  #  Temperature in °C y axis left mode
   y_30max = 3  #  Temperature in °C y axis left mode 

   play_60_T_E = 48   # 2=no average 12 , 24 , 48 add 0.00208°C for every 1 W/m²/month    Piers Forster 1 W/m² in 1month warmes 0.00208°C 
   a60_start = 2005   # 2015 starting year of play_60_T_E
   a60_offset = 1.01 
   line4_play = 60
   y_60min = 0  #  Temperature in °C y axis left mode
   y_60max = 3  #  Temperature in °C y axis left mode

   plot28_E_T = 5 #  EEI simulates T linear add 0.00208°C for every 1 W/m²/month 
   a28_start = 2026.5   # 2015 starting year of play_60_T_E
   a28_offset = 1.5  
   y_28min = 0  #  Temperature in °C y axis left mode
   y_28max = 3  #  Temperature in °C y axis left mode
   
   plot29_ETq = 6 #  EEI simulates T quadratic  add 0.00208°C for every 1 W/m²/month 
   a29_start = 2026.5   # 2015 starting year of play_60_T_E
   a29_offset = 1.5  
   y_29min = 0  #  Temperature in °C y axis left mode
   y_29max = 3  #  Temperature in °C y axis left mode
   
   plot_T_78 = 7 # 3 , 4 , 5 Tom Harris
   text78 = "Temperature in °C      Tom Harris  quadratic   T = 0.0004 x²  + 0.0019 x + 0.5079      78" 
   y_78min = 0 #  for Tom Harris Temperature 
   y_78max = 3 #  for Tom Harris Temperature

   if print_debug > 9:
      # print(f"config__433  {plot28_E_T}", text28)
      print(f"config__757  {figure100}", text100)
   
# substack #28 uses 102 , 104 , 105 , 106 , 107 , 110 , 409 Global Warming EEI sets the World on Fire #28 Published 20. Nov
if figure404 == 409:  
   figure404 = 48
   text400 = "Figure 409: Global Warming ... possible Temperatures in ..2050...  EEI, Hansen..."

   plot28_E_T = 5 # linear EEI increase in line 5
   text28 = "Global Warming  in  °C  calculated  with  -> linear  EEI = 0.04788 x  +  0.408              28"
   y_28min = 0.5  #  Temperature in °C y axis left mode
   y_28max = 3  #  Temperature in °C y axis left mode

   plot29_ETq = 6 #  EEI simulates T quadratic  add 0.00208°C for every 1 W/m²/month 
   y_29min = 0.5  #  Temperature in °C y axis left mode
   y_29max = 3  #  Temperature in °C y axis left mode

   y_60min = 0.5  #  Temperature in °C y axis left mode
   y_60max = 3  #  Temperature in °C y axis left mode

   x_anf = 2005   # 2005
   x_end = 2028   # 2028   2065

   if print_debug > 9:
      # print(f"config__433  {plot28_E_T}", text28)
      print(f"config__450  {figure404}", text400)



def apply_figure100_settings(figure_id):
   """Apply and return the settings for a supported Figure 100 variant."""
   shared_settings = {
       "figure100": figure_id,
       "plot74_GIS_T": 2,
       "text74": "measured Temperature in °C from  giss.nasa.gov   Hansen+0.3°C                             74",
       "c74": "green",
       "y_74min": 0.5,
       "y_74max": 2.5,
       "linear_41_75": 3,
       "c75": "#226C12CC",
       "y_75min": 0.5,
       "y_75max": 2.5,
       "plot29_ETq": 0,
       "plot28_E_T": 0,
       "line5_play": 60,
       "y_28min": 0.5,
       "y_28max": 2.5,
       "y_29min": 0.5,
       "y_29max": 2.5,
       "y_60min": 0.5,
       "y_60max": 2.5,
       "x_anf": 2005,
       "x_end": 2050,
   }
   if figure_id == 102:
       shared_settings.update({
           "text100": "Figure 2: James Hansen linear fit +0.4°C passes 2°C in the year 2038",
           "y_74min": -0.5,
           "y_75min": -0.5,
           "text75": "James Hansen: linear 0.4°C warming every 10 years passes the 2°C in the year 2038.5", # col 115
           "plot_T_78": 0,
           "line4_play": 0,
           "play_60_T_E": 0,
           "plot28_E_T": 0,
           "plot29_ETq": 0,
           "x_anf": 1880,
       })
   elif figure_id == 103:
       shared_settings.update({
           "text100": "Figure 3: Tom Harris quadratic fit passes 2°C in the year 2038 - same as Hansen ",
           "text75": "James Hansen: linear 0.4°C warming every 10 years passes the 2°C in the year 2038.5",
           "plot_T_78": 4,
           "text78": "Temperature in °C  Tom Harris  T = 0.0004 x²  + 0.0019 x + 0.5079 = 2°C in 2038.75",
           "y_78min": 0.5,
           "y_78max": 2.5,
           "line4_play": 0,
           "play_60_T_E": 0,
       })
   elif figure_id == 105:
       shared_settings.update({
           "text100": "Figure 5: Warming calculated with linear EEI increase. Result: 2°C is passed in year 2038 ",
           "text75": "James Hansen:  linear 0.4°C warming  every  10  years      =  2.4°C in year 2050      75",
           "plot_T_78": 0,
           "play_60_T_E": 48,
           "text60": "the measured EEI - CERES satellites -  warmed the earth 1.5°C in the year 2025       60",
           "a60_start": 2005,
           "a60_offset": 1.01,
           "line4_play": 60,
           "plot28_E_T": 5,
           "text28": "Global Warming  in  °C  calculated  with  -> linear  EEI = 0.04789 x  +  0.408              28",
           "a29_start": 2026.5,
           "a29_offset": 1.5,
       })
   elif figure_id == 106:
       shared_settings.update({
           "text100": "Figure 6: Warming calculated with quadratic EEI increase. Result: 2°C is passed in year 2037",
           "text75": "James Hansen:   linear 0.4°C   warming  every  10  years    -  dotted  green              75",
           "play_60_T_E": 48,
           "a60_start": 2005,
           "a60_offset": 1.01,
           "line4_play": 60,
           "plot29_ETq": 5,
           "a29_start": 2026.5,
           "a29_offset": 1.5,
           "plot_T_78": 0,
       })
   elif figure_id == 110:
       shared_settings.update({
           "text100": "Figure 10: Global Warming ... possible Temperatures in ..2050...  EEI, Hansen...",
           "text75": "James Hansen:  linear 0.4°C warming every 10  years.        The year 2050 result = 2.4°C",
           "text78": "Temperature in °C using Tom Harris quadratic formula.        The year 2050 result = 2.6°C",
           "plot_T_78": 4,
           "y_78min": 0.5,
           "y_78max": 2.5,
           "line5_play": 60,
           "play_60_T_E": 48,
           "text60": "the measured EEI - CERES satellites -  warmed the earth 1.5°C in the year 2025       60",
           "a60_start": 2005,
           "a60_offset": 1.01,
           "line4_play": 60,
           "plot28_E_T": 5,
           "text28": "Global Warming in °C  using linear increasing EEI.              The year 2050 result = 2.7°C",
           "plot29_ETq": 6,
           "text29": "Global Warming in °C  using quadratic increasing EEI.        The year 2050 result =  3  °C",
           "a29_start": 2026.5,
           "a29_offset": 1.5,
       })
   else:
       raise ValueError(f"Unsupported Figure 100 variant: {figure_id}")

   globals().update(shared_settings)
   if print_debug > 9:
       print(f"config: applied Figure {figure_id} settings")
   return shared_settings
   