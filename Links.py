# split the file into several parts.
# example main, part4 and part 9
# 42_CO2_T.py 
v = "42v1" #  plot 44 displays 77month(input) run mean average
# Thomas Boettcher
# part 1 configure 
# part 2.2 plot CO2 Mauna Loa
# part 2.3 plot23_Glen_CO2 
# part 2.5 plot25_long_CO2  -800 000 years ppm CO2 file
#
# part 3.4 plot34_CO2_emission summed
#
# part 4 EEI CERES data
# part41_ceres_eei = 3 # print EEI 12 month running mean. Info in line 3 below the plot
# part42_ceres_eei = 4 # print EEI 48 month running mean. Info in line 4 below the plot
# part44_ceres_eei = 77 #  print EEI 77 month running mean. Info in line 5 below the plot
#
# part 5.2 plot52_delta_CO2_red_bars
# part 5.3 plot53_CO2_orange2025
# part 5.4 plot54_Glen_delta_on
# part 5.5 plot55_population_on human earth population 
#
# part 71 plot quadratic temperature with right y axis
# part 72 plot temperature ECS = 8°C with right y axis
# part 73 plot temperature ECS = 4.5°C with right y axis
# part 74 plot Hansen GIS temperature 1880 2027
# part 75      Hansen 2015 .41°C linear fit
# part 76  my  T 
# part 77 deepseek.com 
#
# part 8 print headline, axis numbers. around figue
# 8.2 print the headline above the plot
# 8.3 print the left y axis 
# 8.4 
# 8.5 configure the right y axis legend  
# 8.6 print the vertical lines CO2=constant
# 8.7 print the right y axis
# 8.8 print the x axis 
# 8.9 print the horizontal lines year 2026

# yl_mode = 2 ppm CO2 y axis left mode
# yl_mode = 3 Gt CO2 y axis left mode
# yl_mode = 4 EEI in W/m2 y axis left mode
# yl_mode = 5 delta ppm CO2 y axis left mode
# yl_mode = 7 Temperature in °C y axis left mode

# part 9 print line 1 to 5 below the figure 

# -----------------------------
# part 1 configure  variables
# -----------------------------
# 1.1 imports
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from matplotlib.lines import Line2D
from matplotlib.ticker import MultipleLocator
import os
import sys

# 1.2 Parameter decide which curves to plot
plot22_CO2_Mauna_Loa = 0 # 1, 2 print in line 2 # 0 no plot CO2 # 1 Mauna Loa 
c22 = "blue" # plot1 color
plot23_Glen_CO2 = 0 # 2, 3 print in line 2, 3, 0 keine Kurve Glen , 1 = 0.013t² - 51t + 49,536 in dark blue  
c23 = "#4554A8C6"   # c23 = "#4B3FD1"

plot25_long_CO2 = 0 #  3 4 print -800 000 years ppm CO2 file
c25 = "#A8349DC5" 
c25 = "green"
# https://ourworldindata.org/grapher/co2-long-term-concentration?overlay=download-data

plot34_CO2_emission = 0 # 33 # 43, 34 row3 mode 4, 42 row 4 mode 2   cumulative CO2 emissions 1750 to 2024
c34 = "purple"
c34 = "#942296C5" 
# no part 4
part41_ceres_eei = 3 # print EEI 12 month running mean
     # 3,5,12,47,48,50,84 convert txt to csv runnig 12 month avg , 48 convert txt to csv runnig 48 month avg
c41                 = "#289C1684" # plot41 color
part42_ceres_eei = 4 # print EEI 12 month running mean
c42 = "purple"
part43_ceres_eei = 0 
c43 =   "#13DF2F84" # plot41 color

part44_ceres_eei = 11 # 5,12,47,48,50,84 convert txt to csv runnig 12 month avg ,
                      #  48 =>Centered: True 
                      #  47 =>Centered: False with 48 moving average makes plot 43 csv
                      # 11 makes plot 43 csv
c44 =   "#6513DF84" # plot41 color
c44 = "blue"


plot52_delta_CO2_red_bars = 0 # 8 0 7 4 keine delta_CO2 , 1 = delta_CO2 in rot , 7,8 mit Beschriftung   
plot53_CO2_orange2025 = 0 # 3, 4, 0 orange Glen , 1 = 0.013t² - 51t + 49,536 in rot 3 works plot53_CO2_orange2025
plot54_Glen_delta_on = 0 #  4, 0 print row 4 # green Glen diff print in line 4
plot55_population_on = 0 # 4, 5 row 5 # 0=no print , 1 = population in green
# no part 6
plot71_temperature = 0 # 4,5, 0 quadratic T
plot72_AESS_T = 0      # 4,5,0 apparent Earth system sensitivity (AESS=7.7°C)
plot73_ECS_T  = 0       # 6,5 #  Earth Climate sensitivity (ECS=4.5°C)
plot74_GIS_T  = 2 #
c74                  = "#E8125984" # plot74 color
c74 = "red"
linear_41_75  = 3 # part 75    Hansen 2015 .41°C linear fit
c75                 = "#371EA484" # plot75 color
plot76_my_T  =  0 #
c76                  = "#CB4949C5" # plot76 color
c76 = "red"
plot_T_77 = 0
parameter84_save_png = 8 # save png


c71 = "red" # plot71 color c71 = "green" 
if plot71_temperature < 1:    c72 = "red" # plot72 color
else:                         c72 = "#DD3646A3" # plot72 color
if plot71_temperature < 1 and plot72_AESS_T < 1:
   c73 = "red" # plot73 color 
else:   
   c73 = "#B9184E84" # plot73 color
   c73 = "orange"

C280=280 # CO2 concentration 1750 275 ppm

# 1.3.1 scale the left Y axis
y_min = 250 # 300 # min value 280
y_max = 500 # 1300 # min value 440 70

# 1.3.2 scale the right Y axis
y_Tmin = 0 # min value °C
y_Tmax = 2.5 # 2.5.1.6 4 # max value C

# 1.3.3 scale the right Y axis
y_Emin = 0 # 0 min value W/m² 
y_Emax = 2 # 5, 1.6 4 # max value  W/m² 

x_anf = 2000 # 1960 2000 -33000
x_end = 2026 # 2200 2026 

# 1.4.5 scale the text rows below the plot field
tr1x = -0.09 # text row 1 x value -.3...1 -0.12
tr2x = 0.01 # text row 2 x value -.3...1 -0.08

tr1y = -.19 # text row 1 y end value -.3...1 -.15
tr2y = -.26 # text row 2 y end value -.3...1 -.24
# 1.5 scale the text rows below the plot field
tr3y = -.33 # text row 1 y end value -.3...1 -.32
tr4y = -.40 # text row 1 y end value -.3...1 -.40
tr5y = -.46 # text row 1 y end value -.3...1 -.48
tr6y = -.57 # text row 1 y end value -.3...1 -.56
trs = 20 # trs = 16 # fontsize=14

# 1.6 scale the legend lines below the plot field
lr2x1 = 0.065 # line row 2 x value begin 0.065
lr2x2 = 0.085 # line row 2 x value end 0.085
lr1y = 0.248 # line row 1 y value begin 
lr2y = 0.211 # line row 2 y value begin 0.215
lr3y = 0.168 # line row 3 y value begin 0.17
lr4y = 0.129 # line row 4 y value begin 0.124
lr5y = 0.095 # line row 5 y value begin 0.08
lr6y = 0.034 # line row 6 y value begin 0.08

# 1.7 Plot (x-width, y-width) Size of the figure in inches
scale_mode = 10 # 10 inches high. 13 inches wide
if scale_mode == 7:
   fig, ax1 = plt.subplots(figsize=(13, 7))
elif scale_mode == 8:
   fig, ax1 = plt.subplots(figsize=(13, 8))
elif scale_mode == 10:
   fig, ax1 = plt.subplots(figsize=(13, 10))
else:
   fig, ax1 = plt.subplots(figsize=(13, 7))

# yr1 = int(yr1+0.49) # cast to integer result = 2 (int)

# 1.8 Parameter strig
header_parameter = f"{plot22_CO2_Mauna_Loa}" # 1960 number inside string
header_parameter = header_parameter + f"{plot23_Glen_CO2}" # 
header_parameter = header_parameter + f"{plot25_long_CO2}" # 
header_parameter = header_parameter + f"{plot34_CO2_emission} " # 

header_parameter = header_parameter + f"4({part41_ceres_eei}" # 
header_parameter = header_parameter + f"{part42_ceres_eei}" # 
header_parameter = header_parameter + f"{part43_ceres_eei}" # 
header_parameter = header_parameter + f"{part44_ceres_eei} " # 

header_parameter = header_parameter + f"5({plot52_delta_CO2_red_bars}" # plot52_delta_CO2_red_bars number inside string
header_parameter = header_parameter + f"{plot53_CO2_orange2025}" # plot53_CO2_orange2025 number inside string
header_parameter = header_parameter + f"{plot54_Glen_delta_on}" # plot54_Glen_delta_on number inside string
header_parameter = header_parameter + f"{plot55_population_on}" # plot55_population_on number inside string

header_parameter = header_parameter + f" 7({plot71_temperature}" 
header_parameter = header_parameter + f"{plot72_AESS_T}" 
header_parameter = header_parameter + f"{plot73_ECS_T}" 
header_parameter = header_parameter + f"{plot74_GIS_T}"
header_parameter = header_parameter + f"{linear_41_75} "
header_parameter = header_parameter + f"{plot76_my_T} "
# header_parameter = header_parameter + f"{parameter84_save_png} " 

# 1.9 left Y axis is in ppm CO2 per default.
yl_mode = 4 # 4 EEI in W/m2 y axis left mode
# 2 ppm CO2 y axis left mode
yr_mode = 7 # ppm CO2 y axis right mode
# yl_mode = 3 Gt CO2 y axis left mode
# yl_mode = 4 EEI in W/m2 y axis left mode
# yl_mode = 5 delta ppm CO2 y axis left mode
# yl_mode = 7 # Temperature in °C y axis left mode
# yr_mode = 7 # Temperature in °C y axis right mode
# end part 1



# -----------------------------
#  part 2   plot CO2 
#  part 2.2 plot CO2 Mauna Loa
blue22_text="blue dots: CO2 measured at Mauna Loa ( 2025 = 427.35 ppm ) 22"
# -----------------------------
# 2.2.1 years 1960–2025 x_years_22_list = [1960, 1961, 1962, ..., x_end - 1]
if x_end > 1961:
   x_years_22_list = list(range(1960, x_end+1)) # list of years 1960...
else:
   x_years_22_list = list(range(1960, 2026)) # list of years 1960...

# 2.2.2 Select only 2018–2025
if x_anf < 1960:
   start_of_x_index = x_years_22_list.index(1960)
else:
   start_of_x_index = x_years_22_list.index(x_anf)    
if x_end > 2026:
   end_of_x_index = x_years_22_list.index(2025)
elif x_end < 1960:
   end_of_x_index = 1
else:
   end_of_x_index = x_years_22_list.index(x_end)

x_years_22_list_subset = x_years_22_list[start_of_x_index:end_of_x_index]
# -----------------------------
# 2.2.3 Kurve1 CO₂ Daten https://gml.noaa.gov/webdata/ccgg/trends/co2/co2_annmean_mlo.txt
# https://gml.noaa.gov/ccgg/trends/mlo.html
# https://gml.noaa.gov/ccgg/trends/global.html
# -----------------------------
co2_values22 = [
316.91, 317.64, 318.45, 318.99, 319.62, 320.04, 321.38, 322.16, 323.04, 324.62, # 1960–1969
325.68, 326.32, 327.46, 329.68, 330.19, 331.13, 332.03, 333.84, 335.41, 336.84, # 1970–1979
338.76, 340.12, 341.48, 343.15, 344.87, 346.35, 347.61, 349.31, 351.69, 353.20, # 1980–1989
354.45, 355.70, 356.54, 357.21, 358.96, 360.97, 362.74, 363.88, 366.84, 368.54, # 1990–1999
369.71, 371.32, 373.45, 375.98, 377.70, 379.98, 382.09, 384.02, 385.83, 387.64, # 2000–2009
390.10, 391.85, 394.06, 396.74, 398.81, 401.01, 404.41, 406.76, 408.72, 411.66, # 2010–2019
414.24, # 2020
416.41, # 2021
418.53, # 2022
421.08, # 2023
424.61, # 2024
427.35  # 2025 = 427.35  ppm
]
# 2.2.4 Kurve1 CO₂ 
#  https://gml.noaa.gov/webdata/ccgg/trend_of_x_indexs/co2/co2_annmean_mlo.txt
# 2.2.4 Mauna_Loa 13.3.2026
# plot22_CO2_Mauna_Loa https://gml.noaa.gov/ccgg/trends/global.html
# 2.2.5 subset skip the old years
co2_values22_subset = co2_values22[start_of_x_index:end_of_x_index]
df2 = pd.DataFrame({  # make a DataFrame with two columns:"x_22_years" → years (x-axis) "y_22_CO2_ppm" → CO₂ values (y-axis)
     "x_22_years": x_years_22_list_subset,
     "y_22_CO2_ppm": co2_values22_subset })
# 2.2.6 add more space below plot
fig.subplots_adjust(bottom=0.30) # 0.25 = 25% margin at bottom
# end part 2.2 Mauna Loa CO2 measurements


# -----------------------------
# 2.3 plot23_Glen_CO2 = 0.013t² - 51t + 49,536 in dark blue 
# source a plot with the formula explained in a thread
# source https://x.com/Gergyl/status/1810632238230589564
# -----------------------------
text_plot23_Glen="calculated CO2 dashed blue line = 0.0132251t² - 51.0337t + 49,536 ppm 23"
# CO₂ function CO2 = 0.013t² - 51t + 49,536
def co3_ppm(t):
   return 0.0132251 * t**2 - 51.0337 * t + 49536.7
# 2.3.2 years as x values 1960 to 3000
years23 = np.arange(x_anf, x_end +1 )
co23_values = co3_ppm(years23)
# 2.3.3. Create DataFrame for convenience
df23 = pd.DataFrame({
      "Year3": years23,
      "Modeled3": co23_values
       })
# 2.3.4 assign ax1  
if plot22_CO2_Mauna_Loa > 0:
   ax1.plot(df2["x_22_years"], df2["y_22_CO2_ppm"], marker="o", markersize=5, color="blue", linewidth=2, label=" ")
   print("line 260 plot22_CO2_Mauna_Loa does not show ")
   ax1.set_ylim(y_min, y_max) # scale
elif plot23_Glen_CO2 > 0:
   ax1.plot(df23["Year3"], df23["Modeled3"], '--', label="Glen formula CO2= 0.0132t² - 51t + 49,536 K6", color=c23, linewidth=3)
# 2.3.7
if plot23_Glen_CO2 > 0:
   ax23 = ax1.twinx()
   ax23.spines.right.set_position(("outward", 90))
   ax23.spines["right"].set_visible(False) # remove right y-Achse
   ax23.tick_params(right=False, labelright=False) # remove Zahlen
# 2.3.8
if plot23_Glen_CO2 > 0:
   ax23.plot(df23["Year3"], df23["Modeled3"], '--', label="Glen formula CO2= 0.0132t² - 51t + 49,536 K6", color=c23, linewidth=3)
   ax23.tick_params(axis="y", labelcolor="green")
   ax23.set_ylim(y_min, y_max) # scale
   ax23.spines.right.set_position(("outward", 60))
# end part 2.3 CO2


# plot25_long_CO2 = 3 # 2, 3 print -800 000 years ppm CO2 file
# https://ourworldindata.org/grapher/co2-long-term-concentration?overlay=download-data
# Data sources: NOAA Global Monitoring Laboratory - Trends in Atmospheric Carbon Dioxide (2026)EPA 
# based on various sources (2022) – with major processing by Our World in Data
# -----------------------------
#  part 2.5 plot CO2 Mauna Loa
blue25_text="green: CO2 NOAA 800_000 year ice data 25"
if plot25_long_CO2 > 0:
      df25 = pd.read_csv("csv_25_ppm_long.csv") # our world in data file
      long_co25 = (
         df25[df25["Entity"] == "World"][["Year25", "ppm25"]]
         .query("-10 <= Year25 <= 2026")
         .sort_values("Year25")
         .reset_index(drop=True)
         )
      ax25 = ax1.twinx()
      ax25.spines.right.set_position(("outward", 90))
      ax25.spines["right"].set_visible(False) # remove right y-Achse
      ax25.tick_params(right=False, labelright=False) # remove Zahlen

      ax25.plot(df25["Year25"], df25["ppm25"], '--', label="Glen formula CO2= 0.0132t² - 51t + 49,536 K6", color=c25, linewidth=3)
      ax25.tick_params(axis="y", labelcolor=c25)
      ax25.set_ylim(y_min, y_max) # scale
      ax25.spines.right.set_position(("outward", 60))
      # print(long_co25.head(5))



# part 3.4 plot34_CO2_emission summed
# co2_cumul.csv
# https://ourworldindata.org/grapher/cumulative-co-emissions?country=~OWID_WRL&overlay=download-data
# 3.4.0 Entity,Code,Year,Cumulat
#       World,OWID_WRL,1750,9305937
if plot34_CO2_emission > 0:
   print34_text ="purple dots: cumulative CO2 emissions Carbon Brief 34 mode "
   # plot34_CO2_emission_mode = 1, read self made csv 2000 GtCO2
   # plot34_CO2_emission_mode = 2, read csv 2000 000 000 000 tCO2
   # plot34_CO2_emission_mode = 3, read csv 2000 GtCO2 csv_34a3_cumulative-co-emissions.csv 1750 to 2024
   # plot34_CO2_emission_mode = 4, read csv 2000 GtCO2
   # plot34_CO2_emission_mode = 5
   first_digit = int(str(plot34_CO2_emission)[0]) # print in row
   second_digit = int(str(plot34_CO2_emission)[1])
   plot34_CO2_emission = first_digit
   plot34_CO2_emission_mode = second_digit
   print34_text = print34_text + str(plot34_CO2_emission_mode)
   # 3.4.mode 1 
   if plot34_CO2_emission_mode == 1:
      df34a = pd.read_csv("csv_34a1_co2_world_generated.csv") # processed file
   elif plot34_CO2_emission_mode == 2:   # 3.4.mode 2
      df34b = pd.read_csv("csv_34a2_co2_sum.csv") # our world in data file
      co2_sum_world = (
         df34b[df34b["Entity"] == "World"][["Year34", "Cumulat"]]
         .query("1960 <= Year34 <= 2026")
         .sort_values("Year34")
         .reset_index(drop=True)
         )
      # 3.4.2 in Gt CO2
      co2_sum_world["GCumulat"] = co2_sum_world["Cumulat"] / 1e9
      print("co2_cumul 2  df34b")
      print(co2_sum_world.head(2))
   elif plot34_CO2_emission_mode == 3:  # 3.4.mode 3
      df34b = pd.read_csv("csv_34a3_cumulative-co-emissions.csv") # our world in data file
      co2_sum_world = (
         df34b[df34b["Entity"] == "World"][["Year", "Cumulat"]]
         .query("1750 <= Year <= 2026")
         .sort_values("Year")
         .reset_index(drop=True)
         )
      # 3.4.3 in Gt CO2
      co2_sum_world["GCumulat"] = (co2_sum_world["Cumulat"] / 1e9).astype(int)
      x34years = df34b["Year"]
      cumulative_gt = co2_sum_world["GCumulat"]
   elif plot34_CO2_emission_mode == 4:  # 3.4.mode 5
      df34b = pd.read_csv("csv_34a3_cumulative-co-emissions.csv") # our world in data file
      co2_sum_world = (
         df34b[df34b["Entity"] == "World"][["Year", "Cumulat"]]
         .query("1750 <= Year <= 2026")
         .sort_values("Year")
         .reset_index(drop=True)
         )
      # 3.4.4 in Gt C    round GCumulat to integer
      co2_sum_world["CCumulat"] = (co2_sum_world["Cumulat"] / 1e9 * 12 / 44 )
      x34_year = df34b["Year"]
      y_sum_gt = co2_sum_world["CCumulat"]
   else:  # 3.4.mode 9
      df34b = pd.read_csv("co2_cumul.csv") # our world in data file
      co2_sum_world = (
         df34b[df34b["Entity"] == "World"][["Year34", "Cumulat"]]
         .query("1960 <= Year34 <= 2026")
         .sort_values("Year34")
         .reset_index(drop=True)
         )
      # print("plot34_CO2_emission_mode 0  df34b")
      # print(co2_sum_world.head(10))
      # 3.4.4 in Gt CO2
      co2_sum_world["GCumulat"] = co2_sum_world["Cumulat"] / 1e9
      print(co2_sum_world.head(2))
      #   Year34       Cumulat   GCumulat
      # 0    1960  308396160000  308.39616
      # 1    1961  317811160000  317.81116
      # how to save co2_sum_world with column GCumulat as csv file
      # save CSV
      # co2_sum_world.to_csv("co2_sum_world.csv", index=False)
      #end 3.4

# part 4 EEI CERES data 
# part41_ceres_eei = 4 # 11 convert txt to csv
# #8T44 2 download asci file TOA flux
# CERES_EBAF-TOA_Ed4.2.1 - Global Data Charts
# csv41_CERES_TOA_FluxtoJanuary-2026.txt
# https://ceres-tool.larc.nasa.gov/ord-tool/jsp/EBAFTOA421Selection.jsp
# https://ceres-tool.larc.nasa.gov/ord-tool/srbavg
# https://bsky.app/profile/thomas-boettcher.bsky.social/post/3mhuowkhfq22h
# save file as csv41_CERES_TOA_FluxtoJanuary-2026.txt
# csv41_CERES_TOA_Flux.txt

# 4.1 convert CERES txt to csv 
# https://chat.deepseek.com/a/chat/s/d9a11bdb-f2ce-4c34-b14e-492b673e0a4e
# add column 5 as decimal year 2000.08  2000.16
# 4.1.1 convert_ceres_to_csv calculation: decimal_year = year + (month - 0.5) / 12
def convert_ceres_to_csv(input_file, output_file):
    """
    Convert CERES TOA flux ASCII file to CSV format
    
    Parameters:
    input_file (str): Path to input ASCII file
    output_file (str): Path to output CSV file
    """
    # 4.1.1 Read the data
    data = []
    with open(input_file, 'r') as f:
        lines = f.readlines()
        # Skip header lines (lines starting with # or empty lines)
        for line in lines:
            line = line.strip()
            if not line or line.startswith('#') or line.startswith('CERES'):
                continue
            # Parse each data line
            parts = line.split()
            if len(parts) >= 3:
                try:
                    year = int(parts[0])
                    month = int(parts[1])
                    flux = float(parts[2])
                    data.append([year, month, flux])
                except ValueError:
                    # Skip lines that don't parse correctly
                    continue
    
    # 4.1.1.2 Create DataFrame
    df = pd.DataFrame(data, columns=['year', 'month', 'toa_net_flux_w_m2'])
    
    # 4.1.1.3 Add date column for easier analysis
    df['date'] = pd.to_datetime(df['year'].astype(str) + '-' + df['month'].astype(str) + '-01')
    
    # 4.1.1.4 Add decimal year (column 5)
    # Convert month to decimal fraction of year
    # Using the middle of each month (e.g., Jan = 0.0417, Feb = 0.125, etc.)
    # Formula: decimal_year = year + (month - 0.5) / 12
    df['decimal_year'] = df['year'] + (df['month'] - 0.5) / 12
    
    # 4.1.1.5 Reorder columns with decimal_year as column 5
    df = df[['date', 'year', 'month', 'toa_net_flux_w_m2', 'decimal_year']]
    
    # 4.1.1.6 Save to CSV
    df.to_csv(output_file, index=False, float_format='%.6f')
    
    print(f"part 4.1.1 Successfully converted {len(df)} records to {output_file}")
    print(f"Data range: {df['date'].min()} to {df['date'].max()}")
    print(f"Decimal year range: {df['decimal_year'].min():.4f} to {df['decimal_year'].max():.4f}")
    print(f"Flux range: {df['toa_net_flux_w_m2'].min():.2f} to {df['toa_net_flux_w_m2'].max():.2f} W/m²")
    
    # Show first few rows to verify decimal year calculation
    print("\n4.1.1 First 3 rows of the converted data:")
    print(df.head(3))
    
    return df
    # end 4.1.1 CERES function 1
    # add column 5 as decimal year 2000.08  2000.16


# 4.1.2 CERES function 2 add_running_12month_average
def add_running_12month_average(df):
    """
    Add a column with 12-month running average to the DataFrame
    Parameters:
    df (DataFrame): DataFrame with columns 'date' and 'toa_net_flux_w_m2'
    Returns:
    DataFrame: Original DataFrame with added 'running_12month_avg' column
    """
    # 4.1.2.7 Create a copy to avoid modifying the original
    df_with_avg = df.copy()
    # 4.1.2.8 Sort by date to ensure correct order
    df_with_avg = df_with_avg.sort_values('date')
    # 4.1.2.9 Calculate 12-month running average (centered)
    # Using rolling window with center=True gives centered average
    if (part41_ceres_eei == 1): # end_no_good
       df_with_avg['running_12month_avg'] = df_with_avg['toa_net_flux_w_m2'].rolling(
           window=12, 
           center=True,
           min_periods=6  # Allow partial windows at the edges
       ).mean()
    else:  #  if (part41_ceres_eei == 2): # For trailing 12-month average (uncentered)
       df_with_avg['running_12month_avg'] = df_with_avg['toa_net_flux_w_m2'].rolling(
          window=12, 
          min_periods=12
       ).mean()
    return df_with_avg
    # end 4.1.2 CERES function 2



# 4.1.3 CERES function 3
# save the CERES data to a csv file with running 12 month average
def save_with_12month_average(df, input_filename, output_filename):
    """
    Save CERES data with 12-month running average to CSV
    Parameters:
    df (DataFrame): Original DataFrame
    input_filename (str): Original input filename for reference
    output_filename (str): Output CSV filename
    """
    # 4.1.3.2 Add running average
    df_with_avg = add_running_12month_average(df)
    
    # 4.1.3.3 Save to CSV
    df_with_avg.to_csv(output_filename, index=False)
    
    # 4.1.3.4 Print summary statistics
    print(f"\n4.1.3.4 Saved to {output_filename}")
    print(f"Total records: {len(df_with_avg)}")
    print(f"Records with valid 12-month average: {df_with_avg['running_12month_avg'].notna().sum()}")
    print(f"\nRunning 12-month average statistics:")
    print(f"Min: {df_with_avg['running_12month_avg'].min():.2f} W/m²")
    print(f"Max: {df_with_avg['running_12month_avg'].max():.2f} W/m²")
    print(f"Mean: {df_with_avg['running_12month_avg'].mean():.2f} W/m²")
    return df_with_avg
    # end 4.1.3 CERES function 3





# 4.1.4 CERES function 4 add_running_48month_average
def calculate_48month_running_average(df, value_column='toa_net_flux_w_m2'):
    """
    Calculate 48-month running average for time series data
    
    Parameters:
    df (DataFrame): DataFrame with date and value columns
    value_column (str): Name of the column containing values to average
    
    Returns:
    DataFrame: Original DataFrame with added 'running_48month_avg' column
    """
    # Create a copy to avoid modifying the original
    df_avg = df.copy()
    
    # Ensure data is sorted by date
    df_avg = df_avg.sort_values('date')
    
    # Calculate 48-month (4-year) running average
    # Using center=True gives a centered average (recommended for smoothing)
    df_avg['running_48month_avg'] = df_avg[value_column].rolling(
        window=48, 
        center=True,
        min_periods=24  # Allow partial windows at the edges
    ).mean()
    
    # Also calculate trailing 48-month average (useful for forecasting)
    df_avg['running_48month_avg_trailing'] = df_avg[value_column].rolling(
        window=48, 
        min_periods=48
    ).mean()
    
    return df_avg
    # end 4.1.4 CERES function 4 add_running_48month_average

# 4.1.7 works
def calculate_48month_average(input_csv, output_csv):
    """
    Calculate 48-month running average and save to CSV file
    
    Parameters:
    input_csv (str): Path to input CSV file with CERES data
    output_csv (str): Path to output CSV file with 48-month average
    """
    # Read the input CSV file
    print(f"4.1.7 Reading data from: {input_csv}")
    df = pd.read_csv(input_csv)
    # Display basic information about the data
    print(f"Total records: {len(df)}")
    print(f"Columns: {list(df.columns)}")
    # Ensure date column is in datetime format
    if 'date' in df.columns:
        df['date'] = pd.to_datetime(df['date'])
    else:
        print("Error: No 'date' column found in the CSV file")
        return None
    # Sort by date to ensure correct order
    df = df.sort_values('date').reset_index(drop=True)
    # Calculate 48-month (4-year) running average
    # Using center=True for centered average
    df['running_48month_avg'] = df['toa_net_flux_w_m2'].rolling(
        window=48, 
        center=True,
        min_periods=24  # Allow partial windows at the beginning and end
    ).mean()
    # Also calculate trailing 48-month average (optional)
    df['running_48month_avg_trailing'] = df['toa_net_flux_w_m2'].rolling(
        window=48, 
        min_periods=48
    ).mean()
    # Create a separate DataFrame with only the 48-month average values
    df_48month_avg = df[['date', 'year', 'month', 'decimal_year', 
                          'toa_net_flux_w_m2', 'running_48month_avg']].copy()
    # Save to CSV file
    df_48month_avg.to_csv(output_csv, index=False, float_format='%.6f')
    # Print summary statistics
    print(f"\n{'='*60}")
    print(f"48-MONTH AVERAGE CALCULATION COMPLETE")
    print(f"{'='*60}")
    print(f"Output file: {output_csv}")
    print(f"Total records: {len(df_48month_avg)}")
    print(f"Records with valid 48-month avg: {df_48month_avg['running_48month_avg'].notna().sum()}")
    
    print(f"\nOriginal TOA Net Flux (W/m²):")
    print(f"  Min: {df_48month_avg['toa_net_flux_w_m2'].min():.2f}")
    print(f"  Max: {df_48month_avg['toa_net_flux_w_m2'].max():.2f}")
    print(f"  Mean: {df_48month_avg['toa_net_flux_w_m2'].mean():.2f}")
    print(f"  Std: {df_48month_avg['toa_net_flux_w_m2'].std():.2f}")
    
    print(f"\n48-Month Running Average (W/m²):")
    print(f"  Min: {df_48month_avg['running_48month_avg'].min():.2f}")
    print(f"  Max: {df_48month_avg['running_48month_avg'].max():.2f}")
    print(f"  Mean: {df_48month_avg['running_48month_avg'].mean():.2f}")
    print(f"  Std: {df_48month_avg['running_48month_avg'].std():.2f}")
    
    # Show first few rows
    print(f"\nFirst 10 rows of the output file:")
    print(df_48month_avg.head(10).to_string())
    
    # Show last few rows
    print(f"\n4.1.7 Last 10 rows of the output file:")
    print(df_48month_avg.tail(10).to_string())
    
    return df_48month_avg
    # end 4.1.7 works

# 4.1.8 works well in the middle
# 4.1.8 has big sinus at the beginning
# 4.1.8 has big sinus at the end
def create_simple_48month_average(input_csv, output_csv):
    """
    Simplified version - creates a CSV with just date and 48-month average
    """
    # Read the data
    df = pd.read_csv(input_csv)
    df['date'] = pd.to_datetime(df['date'])
    df = df.sort_values('date').reset_index(drop=True)
    
    # Calculate 48-month average
    df['48month_avg'] = df['toa_net_flux_w_m2'].rolling(
        window=48, 
        center=True,
        min_periods=24
    ).mean()
    
    # Create simplified output with only essential columns
    df_simple = df[['date', 'year', 'month', 'decimal_year', '48month_avg']].copy()
    df_simple = df_simple.dropna()  # Remove rows without 48-month average
    
    # Save to CSV
    df_simple.to_csv(output_csv, index=False, float_format='%.6f')
    
    print(f"\nSimplified 48-month average file created: {output_csv}")
    print(f"Records with valid 48-month average: {len(df_simple)}")
    print(f"Date range: {df_simple['date'].min()} to {df_simple['date'].max()}")
    
    return df_simple
    # end 4.1.8
# make above function with parameter 3, the number of month 12..48

# make a function to append a column named EEE isnstead of running_33month_avg
# 4.1.9 run with part41_ceres_eei = 50
def create_running_average_advanced(input_csv, output_csv, window_months, 
                                    min_periods=None, center=True, keep_original=True):
    """
    Advanced version with more control over the running average calculation
    
    Parameters:
    input_csv (str): Path to input CSV file
    output_csv (str): Path to output CSV file
    window_months (int): Number of months for running average
    min_periods (int): Minimum number of observations required (default: window_months//2)
    center (bool): Whether to center the window (True) or use trailing (False)
    keep_original (bool): Whether to keep original flux column in output
    """
    # Read the data
    df = pd.read_csv(input_csv)
    df['date'] = pd.to_datetime(df['date'])
    df = df.sort_values('date').reset_index(drop=True)
    
    # Set default min_periods if not specified
    if min_periods is None:
        min_periods = window_months // 2
    
    # Calculate running average
    df[f'{window_months}month_avg'] = df['toa_net_flux_w_m2'].rolling(
        window=window_months, 
        center=center,
        min_periods=min_periods
    ).mean()
    
    # Select columns for output
    output_columns = ['date', 'year', 'month', 'year41']
    if keep_original:
        output_columns.append('toa_net_flux_w_m2')
    output_columns.append(f'{window_months}month_avg')
    #output_columns.append('EEI')
    df_output = df[output_columns].copy()
    
    # Save to CSV
    df_output.to_csv(output_csv, index=False, float_format='%.6f')
    
    # Calculate valid records
    valid_records = df_output[f'{window_months}month_avg'].notna().sum()
    #valid_records = df_output'EEI'.notna().sum()

    # Print summary
    print(f"4.1.9\n{'='*60}")
    print(f"{window_months}-MONTH RUNNING AVERAGE")
    print(f"{'='*60}")
    print(f"Window: {window_months} months ({window_months//12} years)")
    print(f"Centered: {center}")
    print(f"Min periods: {min_periods}")
    print(f"Output file: {output_csv}")
    print(f"Valid records: {valid_records} out of {len(df_output)}")
    
    # Show first few valid values
    valid_data = df_output[df_output[f'{window_months}month_avg'].notna()]
    if len(valid_data) > 0:
        print(f"\nFirst 5 valid values:")
        for idx, row in valid_data.head(5).iterrows():
            print(f"  {row['date'].strftime('%Y-%m')}: {row[f'{window_months}month_avg']:.3f} W/m²")
        
        print(f"\n4.1.9 Last 5 valid values:")
        for idx, row in valid_data.tail(5).iterrows():
            print(f"  {row['date'].strftime('%Y-%m')}: {row[f'{window_months}month_avg']:.3f} W/m²")
    
    return df_output
    # end 4.1.9 run with part41_ceres_eei = 50
    # make a function to append a column named EEE isnstead of running_33month_avg

# 4.1.11
def create_running_average(input_csv, output_csv, window_months, 
                                    min_periods=None, center=True, keep_original=True,
                                    column_name='EEI'):
    """
    Advanced version with more control over the running average calculation
    
    Parameters:
    input_csv (str): Path to input CSV file
    output_csv (str): Path to output CSV file
    window_months (int): Number of months for running average
    min_periods (int): Minimum number of observations required (default: window_months//2)
    center (bool): Whether to center the window (True) or use trailing (False)
    keep_original (bool): Whether to keep original flux column in output
    column_name (str): Name of the output column (default: 'EEI')
    """
    # Read the data
    df = pd.read_csv(input_csv)
    df['date'] = pd.to_datetime(df['date'])
    df = df.sort_values('date').reset_index(drop=True)
    
    # Set default min_periods if not specified
    if min_periods is None:
        min_periods = window_months // 2
    
    # Calculate running average and store in EEI column
    df[column_name] = df['toa_net_flux_w_m2'].rolling(
        window=window_months, 
        center=center,
        min_periods=min_periods
    ).mean()
    
    # Select columns for output (only EEI, not the window-specific name)
    output_columns = ['date', 'year', 'month', 'decimal_year']
    if keep_original:
        output_columns.append('toa_net_flux_w_m2')
    output_columns.append(column_name)
    
    df_output = df[output_columns].copy()
    
    # Save to CSV
    df_output.to_csv(output_csv, index=False, float_format='%.6f')
    
    # Save to same CSV
    output_csv2 = "csv/csv44/csv44d_out.csv"
    df_output.to_csv(output_csv2, index=False, float_format='%.6f')
    # Calculate valid records
    valid_records = df_output[column_name].notna().sum()
    
    # Print summary
    print(f"4.1.11\n{'='*60}")
    print(f"{window_months}-MONTH RUNNING AVERAGE (saved as '{column_name}')")
    print(f"{'='*60}")
    print(f"Window: {window_months} months ({window_months//12} years)")
    print(f"--44---Centered: {center}")
    print(f"Min periods: {min_periods}")
    print(f"Output file: {output_csv}")
    print(f"Valid records: {valid_records} out of {len(df_output)}")
    print(f"Column name: {column_name}")
    
    # Show first few valid values
    valid_data = df_output[df_output[column_name].notna()]
    if len(valid_data) > 0:
        print(f"\nFirst 5 valid values:")
        for idx, row in valid_data.head(5).iterrows():
            print(f"  {row['date'].strftime('%Y-%m')}: {row[column_name]:.3f} W/m²")
        
        print(f"\n4.1.11 Last 5 valid values:")
        for idx, row in valid_data.tail(5).iterrows():
            print(f"  {row['date'].strftime('%Y-%m')}: {row[column_name]:.3f} W/m²")
    
    return df_output
    # end 4.1.11





# step1 download # https://ceres-tool.larc.nasa.gov/ord-tool/srbavg
# copy to csv/csv41/csv41a_in_CERES.txt
# step 3 convert to csv
# 4.1.20 convert txt to csv
if part41_ceres_eei > 10:
   df41a = convert_ceres_to_csv('csv/csv41/csv41a_in_CERES.txt', 'csv/csv41/csv41b_ceres.csv')
   # step 4 add 12 running mean convert to csv
if part41_ceres_eei == 12:   
   df_with_12avg = save_with_12month_average(
       df41a, 
       'csv41a_in_CERES.txt', 
       'csv/csv41/csv41d12_ceres.csv'
)
elif part41_ceres_eei == 47:   
   df_with_48avg = create_simple_48month_average(
       'csv/csv41/csv41b_ceres.csv', 
       'csv/csv41/csv41d47_ceres.csv'
      )
elif part41_ceres_eei == 48:   # works
   df_with_48avg = calculate_48month_average(
       'csv/csv41/csv41b_ceres.csv', 
       'csv/csv41/csv41d48_ceres.csv'
      )
elif part41_ceres_eei == 50:   # works
   df_with_48avg = create_running_average_advanced(
       'csv/csv41/csv41b_ceres.csv', 
       'csv/csv41/csv41d50_ceres.csv',
       window_months=48 ,
       min_periods=30 ,
       center=False ,
       keep_original=True
      )
elif part41_ceres_eei == 84:   # works
   df_with_48avg = create_running_average_advanced(
       'csv/csv41/csv41b_ceres.csv', 
       'csv/csv41/csv41d84_ceres.csv',
       window_months=84 ,
       min_periods=30 ,
       center=False ,
       keep_original=True
      )
elif part41_ceres_eei == 17:   # 
   out = f"csv/csv41/csv41d_ceres_{part41_ceres_eei}month.csv"
   
   df_with_48avg = create_running_average_advanced(
       'csv/csv41/csv41c_ceres.csv', 
       out,
       window_months=part41_ceres_eei ,
       min_periods=30 ,
       center=False ,
       keep_original=True
      )
if part41_ceres_eei > 13:
    out = f"csv/csv41/csv41d_EEI_{part41_ceres_eei}_month.csv"
    df_with_avg = create_running_average(
        'csv/csv41/csv41b_ceres.csv', 
        out,
        window_months=part41_ceres_eei,
        min_periods=30,
        center=False,
        keep_original=True,
        column_name='EEI'  # This will create a column named 'EEI'
    )

# 4.1.30 plot_48month_running_average in df41
if part41_ceres_eei > 0:
   p41_text ="Earth Energy Imbalance  W/m² moving average 12 month 41"
   # eckig df41 = pd.read_csv("csv/csv41/csv41f46_ceres.csv") # 
   # ok df41 = pd.read_csv("csv/csv41/csv41f47_ceres.csv") 
   df41 = pd.read_csv("csv/csv44/_plot_41_41g12.csv") 
   # df41 = pd.read_csv("csv/csv41/csv41g50_ceres.csv") 
   # print(df41.head(22)) csv41g48_ceres
   ax41 = ax1.twinx()  # twinx(): Shares the same x-axis Adds a new y-axis on the right
   # part 7.4.6 add 0.3°C same as Hansen to GIS
   ax41.plot(df41["year41"], df41["EEI"], '-', label="EEI  K41", color=c41, linewidth=2)
   ax41.tick_params(axis="y", labelcolor=c41)
   ax41.set_ylim(y_Emin, y_Emax) # scale
   # end 4.1.30

# 4.2 plot_48month_running_average in df41
if part42_ceres_eei > 0:
   p42_text ="Earth Energy Imbalance  W/m² moving average 48 month 42"
   df42 = pd.read_csv("csv/csv44/_plot_42_41g50.csv") 
   # print(df41.head(22)) csv41g48_ceres
   ax42 = ax1.twinx()  # twinx(): Shares the same x-axis Adds a new y-axis on the right
   # part 7.4.6 add 0.3°C same as Hansen to GIS
   ax42.plot(df42["year41"], df42["EEI"], '-', label="EEI  K42", color=c42, linewidth=2)
   ax42.tick_params(axis="y", labelcolor=c42)
   ax42.set_ylim(y_Emin, y_Emax) # scale
# 4.3 plot_84 month_running_average in df43
if part43_ceres_eei > 0:
   p43_text ="Earth Energy Imbalance  W/m² moving average 84 month 43"
   # df43 = pd.read_csv("csv/csv41/csv43g.csv") 
   df43 = pd.read_csv("csv/csv41/csv41d_out.csv") 
   
   # print(df41.head(22)) csv41g48_ceres
   ax43 = ax1.twinx()  # twinx(): Shares the same x-axis Adds a new y-axis on the right
   # part 7.4.6 add 0.3°C same as Hansen to GIS
   ax43.plot(df43["decimal_year"], df43["EEI"], '-', label="EEI  K43", color=c43, linewidth=2)
   ax43.tick_params(axis="y", labelcolor=c43)
   ax43.set_ylim(y_Emin, y_Emax) # scale

# step1 download # https://ceres-tool.larc.nasa.gov/ord-tool/srbavg
# copy to csv/csv44/csv44a_in_CERES.txt
# step 3 convert to csv
# 4.1.20 convert txt to csv
if part44_ceres_eei > 0:    # call 4.1.1 convert_ceres_to_csv
   df44a = convert_ceres_to_csv('csv/csv44/csv44a_in_CERES.txt', 'csv/csv44/csv44b_ceres.csv')
   # step 4 add 12 running mean convert to csv
   # how to put integer part44_ceres_eei in the middle center=False,center=True
if part44_ceres_eei > 0:
    out = f"csv/csv44/csv44d_EEI_{part44_ceres_eei}_month.csv"
    # out not used as csv44d_out.csv is needed for display
    output_csv2 = "csv/csv44/csv44d_out.csv"

    # Configure based on even/odd
    if part44_ceres_eei % 2 == 0:
        # Even: Centered average with standard min_periods
        use_center = True
        min_periods = part44_ceres_eei // 2  # Use half the window size
        avg_type = "CENTERED"
    else:
        # Odd: Trailing average with full window requirement
        use_center = False
        part44_ceres_eei = part44_ceres_eei + 1 # 47 will be 48
        min_periods = part44_ceres_eei  # Require full window for trailing
        avg_type = "TRAILING"
    
    df_with_avg = create_running_average(
        'csv/csv44/csv44b_ceres.csv', 
        "csv/csv44/csv44d_out.csv",
        window_months=part44_ceres_eei,
        min_periods=min_periods,
        center=use_center,
        keep_original=True,
        column_name='EEI'
    )
    
    print(f"{avg_type} average for {part44_ceres_eei}-month window")
    print(f"Min periods: {min_periods}")
    print(f"Output: {out}")


if part44_ceres_eei > 0:
   p44_text = f"Earth Energy Imbalance -{part44_ceres_eei}-month moving average 44"
   df44 = pd.read_csv("csv/csv44/csv44d_out.csv") 
   # print(df44.head(22)) csv41g48_ceres
   ax44 = ax1.twinx()  # twinx(): Shares the same x-axis Adds a new y-axis on the right
   ax44.plot(df44["decimal_year"], df44["EEI"], '-', label="EEI  K44", color=c44, linewidth=2)
   ax44.tick_params(axis="y", labelcolor=c44)
   ax44.set_ylim(y_Emin, y_Emax) # scale


# -----------------------------
# part 5.2 plot52_delta_CO2_red_bars
# part 5.3 plot53_CO2_orange2025
# part 5.4 plot54_Glen_delta_on
# part 5.5 plot55_population_on human earth population 
# -----------------------------
# part 5.2 plot52_delta_CO2_red_bars
# 5.2.2 ΔCO₂ berechnen (per pandas) Balken
# df2["CO2"].diff() Calculates the difference between consecutive CO₂ values
# -----------------------------
if plot52_delta_CO2_red_bars > 0:
   df2["Delta_CO2"] = df2["CO2"].diff().fillna(0)  
   # This line creates a new column in your DataFrame called Delta_CO2.
   ax52 = ax1.twinx()  # twinx(): Shares the same x-axis Adds a new y-axis on the right
# growth data is different https://gml.noaa.gov/webdata/ccgg/trends/co2/co2_gr_mlo.txt

# part 5.3 plot53_CO2_orange2025
# part 5.3.1 -- Quadratic model function
def co53_model(t):
   return 0.0132251 * t**2 - 51.0337 * t + 49536.7

# 5.3.2 Kurve4 . Real Mauna Loa CO₂ annual data 1960–2023
# 2025 = 424.61 + 3.69 ppm = 428.26
data53 = {
1960: 316.91, 1961: 317.64, 1962: 318.45, 1963: 318.99, 1964: 319.62,
1965: 320.04, 1966: 321.37, 1967: 322.18, 1968: 323.05, 1969: 324.62,
1970: 325.68, 1971: 326.32, 1972: 327.46, 1973: 329.68, 1974: 330.19,
1975: 331.12, 1976: 332.03, 1977: 333.84, 1978: 335.41, 1979: 336.84,
1980: 338.76, 1981: 340.12, 1982: 341.48, 1983: 343.15, 1984: 344.85,
1985: 346.35, 1986: 347.61, 1987: 349.31, 1988: 351.69, 1989: 353.20,
1990: 354.45, 1991: 355.70, 1992: 356.54, 1993: 357.21, 1994: 358.96,
1995: 360.97, 1996: 362.74, 1997: 363.88, 1998: 366.84, 1999: 368.54,
2000: 369.71, 2001: 371.32, 2002: 373.45, 2003: 375.98, 2004: 377.70,
2005: 379.98, 2006: 382.09, 2007: 384.02, 2008: 385.83, 2009: 387.64,
2010: 390.10, 2011: 391.85, 2012: 394.06, 2013: 396.74, 2014: 398.87,
2015: 401.01, 2016: 404.41, 2017: 406.76, 2018: 408.72, 2019: 411.66, 
2020: 414.24, 2021: 416.41, 2022: 418.53, 2023: 421.08, 2024: 424.61 , 2025: 427.35 
}
years53 = np.array(list(data53.keys()))
# 5.3.4
co53_actual = np.array(list(data53.values()))
co53_modeled = co53_model(years53)
# 5.3.5 Calculate difference (actual minus model)
difference53 = co53_actual - co53_modeled
# 5.3.6 Create DataFrame for convenience
df53 = pd.DataFrame({
"Year": years53,
"Actual": co53_actual,
"Modeled": co53_modeled,
"Difference": difference53
})
# 5.3.7
if plot53_CO2_orange2025 > 0:
   ax53 = ax1.twinx()
   ax53.tick_params(labelright=False) # removes the right-side numbers
   ax53.set_ylabel("") # removes the axis label
# 5.3.8 Legende oben links
if plot53_CO2_orange2025 > 0:
   ax53.plot(df53["Year"], df53["Modeled"], '--', label="Glen *parabola* ( 0.0132t² - 51t + 49,536) K4", color="orange", linewidth=3)
   ax53.set_ylim(y_min, y_max) # scale glen curve same as Mauna loa
   ax53.spines.right.set_position(("outward", 90))

# part 5.4 plot54_Glen_delta_on
# 5.4 difference Mauna Loa minus Glen_CO2
# 5.4.2 print y axis 5 on right side Twin axis for difference
if plot54_Glen_delta_on > 0:
   ax54 = ax1.twinx()
   ax54.bar(df53["Year"], df53["Difference"], color="green", alpha=0.4, label="Diff (Actual − Model)")
   ax54.set_ylabel(
      "Difference Mauna Loa - Glen-parabol (ppm)  (plot 54)",
      color="green",
      fontsize=14,
      labelpad=-4   # smaller = closer to axis
      )
   ax54.tick_params(axis="y", labelcolor="green")
   #ax54.set_ylim(-1, 13) # scale
   ax54.set_ylim(0, 4) # scale
   if plot54_Glen_delta_on > 2:
      ax54.spines.right.set_position(("axes", 1))
   # end 5.4


# part 5.5 plot55_population_on human earth population 
# 5.5.1 population up to 2023 (UN WPP 2024 via OWID)
# url = "https://ourworldindata.org/grapher/population.csv"
# population4.csv
# -----------------------------
# 5.5.2 population 2023 to 2026 
# https://www.worldometers.info/world-population/world-population-by-year/
# 2026	8,300,678,395	0.84%	69,065,325	56
# 2025	8,231,613,070	0.85%	69,640,498	55
# 2024	8,161,972,572	0.87%	70,237,642	55
# 2023	8,091,734,930	0.88%	70,327,738	54
# 5.5.3 read csv_55_population.csv
if plot55_population_on > 0:
   green55_text="Green line: Earth Population in billion"
   df55 = pd.read_csv("csv/csv55/csv_55_population.csv")
   pop_world = (
         df55[df55["Entity"] == "World"][["Year", "Population"]]
         .query("1960 <= Year <= 2026")
         .sort_values("Year")
         .reset_index(drop=True)
      )
   # 5.5.4 in Milliarden
   pop_world["Population_Mrd"] = pop_world["Population"] / 1e9
# 5.5.5 plot55_population_on=1
if plot55_population_on > 0:
   ax55 = ax1.twinx()
   #end 5.5. plot55_population_on

# no part 6

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
df7 = pd.DataFrame({
      "Year71": years71,
      "Modeled71": T_71values })
# 7.1.4 plot71_temperature
if plot71_temperature > 0:
   ax71 = ax1.twinx()  # twinx(): Shares the same x-axis Adds a new y-axis on the right
   ax71.plot(df7["Year71"], df7["Modeled71"], '--', label="T formula CO2=  K6", color=c71, linewidth=3)
   ax71.tick_params(axis="y", labelcolor=c71)
   ax71.set_ylim(y_Tmin, y_Tmax) # scale
# end 7.1 


# plot72_AESS_T= 4 # apparent Earth system sensitivity (AESS=7.7°C)
red72_text="AESS_T Apparent Earth System Sensitivity = 8°C * log2(CO2/C0) 72"
# 7.2 plot72_AESS_T # dT=ECS*log2(C/C0) # T560ppm=AESS*log2(560/280) 
# AESS=7.7°C  # (Judd 2024)
# https://www.science.org/doi/10.1126/science.adk3705) 
# 2025
# https://www.annualreviews.org/content/journals/10.1146/annurev-earth-032320-064209
#
def T_model72(t):
   CO2= 0.0132251 * t**2 - 51.0337 * t + 49536.7 # Glen formula
   log2_value = np.log2(CO2/C280)
   AESS=8 # apparent Earth system sensitivity (AESS=7.7°C)
   temp72=AESS * log2_value
   return temp72
# 7.2.2 years scale x axis
years72 = np.arange(x_anf, x_end + 1 )
T_72values = T_model72(years72)
# 7.2.3. Create DataFrame for convenience
df72 = pd.DataFrame({
       "Year72":      years72,
       "Modeled72": T_72values })
# 7.2.4 plot72_temperature
if plot72_AESS_T > 0:
   ax72 = ax1.twinx()  # twinx(): Shares the same x-axis Adds a new y-axis on the right
   ax72.plot(df72["Year72"], df72["Modeled72"], '--', label="T formula CO2=  K72", color=c72, linewidth=3)
   ax72.tick_params(axis="y", labelcolor=c72)
   ax72.set_ylim(y_Tmin, y_Tmax) # scale
   # end 7.2 plot72_AESS_T


# plot73_ECS_T Earth Climate sensitivity 
# 7.3  dT=ECS*log2(C/C0) # T560ppm=ECS*log2(560/280) 
def T_model73(t):
   CO2= 0.0132251 * t**2 - 51.0337 * t + 49536.7 # Glen formula
   log2_value = np.log2(CO2/C280)
   ECS = 4.5
   temp73 = ECS * log2_value
   return temp73
# 7.3.2 years scale x axis
years73 = np.arange(x_anf, x_end + 1 )
T_73values = T_model73(years73)
# 7.3.4. Create DataFrame for convenience
df73 = pd.DataFrame({
       "Year73": years73,
       "Modeled73": T_73values })
# 7.3.6 plot_ax73_temperature
if plot73_ECS_T > 0:
   ax73 = ax1.twinx()  # twinx(): Shares the same x-axis Adds a new y-axis on the right
   ax73.plot(df73["Year73"], df73["Modeled73"], '--', label="T formula CO2=  K73", color=c73, linewidth=3)
   ax73.tick_params(axis="y", labelcolor=c73)
   ax73.set_ylim(y_Tmin, y_Tmax) # scale
   # end 7.3


# part part 74 plot NASA GIS temperature
# csv_74_gis_temperature.csv
# https://data.giss.nasa.gov/gistemp/zonal_means/
# https://data.giss.nasa.gov/tmp/gistemp/ltmap/tmp.4_ob4LOTI_E5_12_1880_2027_1951_1980-0/global.txt
# 7.4.2 Year74,GIS_temp
if plot74_GIS_T > 0:
   print74_text ="Temperature in °C giss.nasa.gov Hansen+0.3°C 74 n"
   df74 = pd.read_csv("csv/csv7/csv_74_gis_temperature.csv") # our world in data file
   # print(df74.head(2))
   ax74 = ax1.twinx()  # twinx(): Shares the same x-axis Adds a new y-axis on the right
   # part 7.4.6 add 0.3°C same as Hansen to GIS
   ax74.plot(df74["Year74"], df74["GIS_temp"]+0.3, '-', label="T GIS  K74", color=c74, linewidth=3)
   ax74.tick_params(axis="y", labelcolor=c74)
   ax74.set_ylim(y_Tmin, y_Tmax) # scale
   # end 7.4 part 74 plot NASA GIS temperature

# part 75 plot 2015 .41°C linear fit
# linear_41_75  = 4 # part 75    Hansen 2015 .41°C linear fit
# https://www.columbia.edu/~jeh1/mailings/2026/ElNino.2026.02.06.pdf
# 7.5.2 Year75,GIS_temp
if linear_41_75 > 0:
   print75_text ="Hansen linear fit from 2015 +0.41°C     75"
   df75 = pd.read_csv("csv/csv7/csv_75_hansen.csv") # our world in data file
   #print(df75.head(2))
   ax75 = ax1.twinx()  # twinx(): Shares the same x-axis Adds a new y-axis on the right
   # part 7.4.6 add 0.3°C same as Hansen to GIS
   ax75.plot(df75["Year75"], df75["temp"]+0.1, '--', label="T GIS  K75", color=c75, linewidth=2)
   ax75.tick_params(axis="y", labelcolor=c75)
   ax75.set_ylim(y_Tmin, y_Tmax) # scale
   # end 7.5

# plot76_my_T
my76_text="guessed quadratic temperature  my_T   76 "
# 7.6.1 0.3999999999999999   1950
# 1.10686   2013
# 1.46726   2023
# 1.58864   2026
# 1.6729600000000002   2028
def T_model76(t): # my best try
    x = t - 2000
    return 0.00034 * x**2 + 0.0238 * x + 0.74

def T_model77(t):
    # https://chat.deepseek.com/a/chat/s/d9a11bdb-f2ce-4c34-b14e-492b673e0a4e
    # Define the three points
    #t1, y1 = 1980, 0.5  # 
    t1, y1 = 1950, 0.2 
    t2, y2 = 2013, 1.0
    t3, y3 = 2023, 1.5
    # Lagrange interpolation
    term1 = y1 * ((t - t2) * (t - t3)) / ((t1 - t2) * (t1 - t3))
    term2 = y2 * ((t - t1) * (t - t3)) / ((t2 - t1) * (t2 - t3))
    term3 = y3 * ((t - t1) * (t - t2)) / ((t3 - t1) * (t3 - t2))
    
    return term1 + term2 + term3




# 7.6.2 years scale x axis
years76 = np.arange(x_anf, x_end + 1 )
T_76values = T_model76(years76)
#print(T_76values)
# 7.6.3. Create DataFrame for convenience
df76 = pd.DataFrame({
       "Year76":      years76,
       "Modeled76": T_76values })
# 7.6.4 plot76_temperature
# print(df76.head(2))
#print(T_model76(1950) ,"  1950")  # 0.2
#print(T_model76(2013) ,"  2013")  # 1.0
#print(T_model76(2023) ,"  2023")
#print(T_model76(2026) ,"  2026")  # 1.5
#print(T_model76(2028) ,"  2028")  # 1.5
if plot76_my_T > 0:
   ax76 = ax1.twinx()  # twinx(): Shares the same x-axis Adds a new y-axis on the right
   ax76.plot(df76["Year76"], df76["Modeled76"], '--', label="T formula CO2=  K76", color=c76, linewidth=3)
   ax76.tick_params(axis="y", labelcolor=c76)
   ax76.set_ylim(y_Tmin, y_Tmax) # scale
   # end 7.6 plot76_my_T



# part 8
# 8.1 scale the plot area
# 8.2 print the headline above the plot
# 8.3 print the left y axis 
# 8.4 configure the left y axis legend  
# 8.5 configure the right y axis legend  
# 8.6 print the vertical lines CO2=constant
# 8.7 print the right y axis
# 8.8 print the x axis 
# 8.9 print the horizontal lines year 2026

# 8.1 scale the plot area
# 8.1.2 scale the x axis
plt.xlim(x_anf, x_end)
# 8.1.4 enable grid
ax1.grid(True)

# 8.2 print the headline above the plot
# 8.2.1 blue headline part
trs = 20
# header_black = f"CO2 concentration in the atmosphere {x_anf}" # 1960 number inside string

# yl_mode = 7 Temperature in °C y axis left mode
# yl_mode = 4 # 4 EEI in W/m2 y axis left mode
if ( yl_mode == 7 ): # left Y axis is °C 
   header = f"Temperature in °C  year {x_anf}" # 1960 number inside string
   # header = header + f" Temperature in °C NASA GIS  " # 1960 number inside string
   header = header + f" to year {x_end} " # 2026 number inside string
   # 8.2.8 plot the headline
   plt.text(-0.1, 1.05, header, color="black", fontname="Arial", fontsize=20,
            transform=plt.gca().transAxes)
elif ( yl_mode == 4 ): # yl_mode = 4 # 4 EEI in W/m2 y axis left mode
   header = f"Earth Energy Imbalance     CERES_EBAF-TOA_Ed4.2.1   Jan. 2026 data.   Plot {x_anf}" # 1960 number inside string
   # header = header + f" Temperature in °C NASA GIS  " # 1960 number inside string
   header = header + f" to {x_end}." # 2026 number inside string
   # 8.2.8 plot the headline
   plt.text(-0.1, 1.05, header, color="black", fontname="Arial", fontsize=20,
            transform=plt.gca().transAxes)

elif plot71_temperature > 0: # one temperature active
   # 8.2.3 plot the headline
   # plt.text(-0.1, 1.05, header, color="blue", fontname="Arial", fontsize=18, transform=plt.gca().transAxes)
   plt.text(-0.1, 1.05,
     f"{x_anf}   CO2 Mauna Loa",    # f"More CO2 in atmosphere", 
     color="blue", fontname="Arial", fontsize=trs, transform=plt.gca().transAxes )
   plt.text(0.24, 1.05,
     f"- - CO2 quadratic",
     color=c23, fontname="Arial", fontsize=trs, transform=plt.gca().transAxes )
   plt.text(0.48, 1.05,
     f"--> Δ Temperature calculated °C year {x_end}",
    color=c71, fontname="Arial", fontsize=trs, transform=plt.gca().transAxes )
else:   
   header = f"CO2 measured at Mauna Loa up to 2025. Print {x_anf}" # 1960 number inside string
   header = header + f" to {x_end} " # 2026 number inside string
   # 8.2.8 plot the headline
   plt.text(-0.1, 1.05, header, color="black", fontname="Arial", fontsize=18,
            transform=plt.gca().transAxes)
            # end 8.2


# 8.3 print the left y axis 
# 8.3.1 scale the Y axis for 280 ppm CO2
# yl_mode = 2 ppm CO2 y axis left mode
if y_max - y_min < 11:
   y_mayor_ticks = 2
   y_minor_ticks = 0.2
elif y_max - y_min < 21:
   y_mayor_ticks = 5
   y_minor_ticks = 1
elif y_max - y_min < 50:
   y_mayor_ticks = 10
   y_minor_ticks = 2
elif y_max - y_min < 101:
   y_mayor_ticks = 20
   y_minor_ticks = 2
elif y_max - y_min < 201:
   y_mayor_ticks = 40
   y_minor_ticks = 5
elif y_max - y_min < 500:
   y_mayor_ticks = 50
   y_minor_ticks = 10
elif y_max - y_min < 1100:
   y_mayor_ticks = 100
   y_minor_ticks = 20
   y_minor_grid  = 10
elif y_max - y_min < 3100:
   y_mayor_ticks = 500
   y_minor_ticks = 100
   y_minor_grid  = 10
elif y_max - y_min < 5100:
   y_mayor_ticks = 1000
   y_minor_ticks = 200
else: 
   y_mayor_ticks = 200 # Hauptstriche y axis
   y_minor_ticks = 50
   # yl_mode = 2 ppm CO2 y axis left mode

# 8.3.2 scale the Y axis for -10°C to 1°C  temperature 
# yl_mode = 7 Temperature in °C y axis left mode
y_Tmayor_ticks = 5
y_Tminor_ticks = 1
if y_Tmax - y_Tmin < 0.5:
   y_Tmayor_ticks = 0.2
   y_Tminor_ticks = 0.1
elif y_Tmax - y_Tmin < 1.1:
   y_Tmayor_ticks = 0.2
   y_Tminor_ticks = 0.05
elif y_Tmax - y_Tmin < 2.1:
   y_Tmayor_ticks = 0.2
   y_Tminor_ticks = 0.1
elif y_Tmax - y_Tmin < 3.1:
   y_Tmayor_ticks = 0.5
   y_Tminor_ticks = 0.1
elif y_Tmax - y_Tmin < 5.1:
   y_Tmayor_ticks = 0.5
elif y_Tmax - y_Tmin < 7:
   y_Tmayor_ticks = 1
   y_Tminor_ticks = 0.2
elif y_Tmax - y_Tmin < 11:
   y_Tmayor_ticks = 2
   y_Tminor_ticks = 0.2
elif y_Tmax - y_Tmin < 21:
   y_Tmayor_ticks = 5
   y_Tminor_ticks = 1
else:
   y_Tmayor_ticks = 20
   y_Tminor_ticks = 10
   # yl_mode = 7 Temperature in °C y axis left mode




# 8.4 configure the left y axis legend             
# yl_mode = 7 Temperature in °C y axis left mode
if ( yl_mode == 7 ):   # 8.4.7 left Y axis in °C for plot74_GIS_T elif
   # 8.4.7.1 scale the y axis temperature
   ax1.set_ylim(y_Tmin, y_Tmax)
   ###ax1.set_ylim(y_min, y_max)
   cyl = "red" # color y axis left
   # 8.4.7.2 "Temperature in °C GIS " left Axis upwards
   ax1.set_ylabel("Temperature in °C GIS", color=cyl, fontsize=20) # y achse links
   # 8.4.7.3 write the numbers left of plot field
   ax1.tick_params(axis="y", labelcolor=cyl, labelsize=20) # Achsenbeschriftung
   # 8.4.7.4 scale the Y axis 1°C main items
   ax1.yaxis.set_major_locator(MultipleLocator(y_Tmayor_ticks))   # y axis ticks
   ax1.tick_params(axis='y', which='major', length=12, width=1.5)
   # 8.4.7.5 scale the Y axis 10ppm minor items
   ax1.yaxis.set_minor_locator(MultipleLocator(y_Tminor_ticks))   # 10 Nebenstriche
   ax1.tick_params(axis='y', which='minor', length=6,  width=1, color='blue')
   # end 8.4.7. left Y axis in °C 
if ( yl_mode == 4 ):   # 8.4.7 left Y axis in °C for plot74_GIS_T elif
   # 8.4.7.1 scale the y axis temperature
   ax1.set_ylim(y_Emin, y_Emax)
   ###ax1.set_ylim(y_min, y_max)
   cyl = c42 # color y axis left
   # 8.4.7.2 "Temperature in °C GIS " left Axis upwards
   ax1.set_ylabel("Earth Energy Imbalance in  W/m² ", color=cyl, fontsize=20) # y achse links
   # 8.4.7.3 write the numbers left of plot field
   ax1.tick_params(axis="y", labelcolor=cyl, labelsize=20) # Achsenbeschriftung
   # 8.4.7.4 scale the Y axis 1°C main items
   ax1.yaxis.set_major_locator(MultipleLocator(y_Tmayor_ticks))   # y axis ticks
   ax1.tick_params(axis='y', which='major', length=12, width=1.5)
   # 8.4.7.5 scale the Y axis 10ppm minor items
   ax1.yaxis.set_minor_locator(MultipleLocator(y_Tminor_ticks))   # 10 Nebenstriche
   ax1.tick_params(axis='y', which='minor', length=6,  width=1, color='blue')
   # end 8.4.7. left Y axis in °C 



#elif ( yl_mode  == 2 ): # yl_mode = 2 ppm CO2 y axis left 
else: # 8.4.2 configure the left y axis for ppm CO2 
   # 8.4.2.1 scale the y axis for ppm CO2
   ax1.set_ylim(y_min, y_max)
   # 8.4.2.2 write "CO₂ in ppm" left Axis upwards
   ax1.set_ylabel("CO₂ in ppm", color=c22, fontsize=20) # y achse links
   # 8.4.2.3 write the numbers left of plot field
   ax1.tick_params(axis="y", labelcolor=c22, labelsize=20) # Achsenbeschriftung
   # 8.4.2.4 scale the Y axis 50ppm main items
   ax1.yaxis.set_major_locator(MultipleLocator(y_mayor_ticks))   # 50 Hauptstriche
   ax1.tick_params(axis='y', which='major', length=12, width=1.5)
   # 8.4.2.5 scale the Y axis 10ppm minor items
   ax1.yaxis.set_minor_locator(MultipleLocator(y_minor_ticks))   # 10 Nebenstriche
   ax1.tick_params(axis='y', which='minor', length=6,  width=1, color='blue')
   # end 8.4.2 

# 8.5 configure the right y axis legend  



# 8.6 print the vertical lines CO2=constant
# 8.6.1 horizontal line at 1120 ppm
ax1.axhspan(4 * C280 -2, 4 * C280 +2, color=c23, alpha=0.25, zorder=0)      # 1120 ppm horicontal stripe
# 8.6.2 horizontal line at 560 ppm
ax1.axhspan(2 * C280 -2, 2 * C280 +2, color=c23, alpha=0.3, zorder=0)        # 560 ppm horicontal stripe
# 8.6.3 horizontal major grid all 50ppm
for line in ax1.get_ygridlines():    # horizontal lines
       line.set_color('blue')           # horizontal color
       line.set_alpha(0.5)
       line.set_linestyle('-')          # optional
       line.set_linewidth(1.1)   # <-- thickness
# 8.6.4 horizontal minor grid all 10ppm
ax1.grid(True, which="minor", axis="y", color="lightblue", alpha=0.94)   # horizontal
# 8.6.5 draw blue 1.5°C bar
if plot71_temperature > 0:
   ax71.axhspan(1.5, 2.0, color="#B3D9FF", alpha=0.5, zorder=0) # color="lightblue" 2°C streifen
elif plot72_AESS_T > 0:
   ax72.axhspan(1.5, 2.0, color="#B3D9FF", alpha=0.5, zorder=0) # color="lightblue" 2°C streifen
elif plot73_ECS_T > 0:
   ax73.axhspan(1.5, 2.0, color="#B3D9FF", alpha=0.5, zorder=0) # color="lightblue" 2°C streifen
elif plot74_GIS_T > 0:
   ax74.axhspan(1.5, 2.0, color="#B3D9FF", alpha=0.5, zorder=0) # color="lightblue" 2°C streifen


# 8.7 print the right y axis
# yr_mode = 2 # ppm CO2 y axis right mode
# yl_mode = 3 Gt CO2 y axis left mode
# yl_mode = 4 EEI in W/m2 y axis left mode
# yl_mode = 5 delta ppm CO2 y axis left mode
# yl_mode = 7 # Temperature in °C y axis left mode
# yr_mode = 7 # Temperature in °C y axis right mode

# 8.7.1 plot71 Achse und Beschriftung
if yr_mode == 7: # Temperature
   ax74.tick_params(axis="y", labelcolor=c74)
   ax74.set_ylim(y_Tmin, y_Tmax) # scale
   if plot71_temperature < 1: # make y axis right only if not exist
      ax74.yaxis.set_major_locator(MultipleLocator(y_Tmayor_ticks))   # Hauptstriche
      ax74.yaxis.set_minor_locator(MultipleLocator(y_Tminor_ticks))   # Nebenstriche
      ax74.tick_params(axis='y', labelsize=20) # numbers on right y axis size 20
      ax74.set_ylabel (
         "Δ GIS Temperature in °C   74 ",
         color=c74,
         fontname="Arial",fontsize=20,
         labelpad=10   # smaller = closer to y axis
       )
   if part41_ceres_eei > 0: # delete second y axis
      ax41.spines["right"].set_visible(False)
      ax41.tick_params(right=False, labelright=False)    
   if part42_ceres_eei > 0: # delete second y axis
      ax42.spines["right"].set_visible(False)
      ax42.tick_params(right=False, labelright=False)  
   if part43_ceres_eei > 0: # delete second y axis
      ax43.spines["right"].set_visible(False)
      ax43.tick_params(right=False, labelright=False)   
   if part44_ceres_eei > 0: # delete second y axis
      ax44.spines["right"].set_visible(False)
      ax44.tick_params(right=False, labelright=False)   
   if linear_41_75 > 0: # delete second y axis
      ax75.spines["right"].set_visible(False)
      ax75.tick_params(right=False, labelright=False)  
elif plot71_temperature > 0:
   if plot54_Glen_delta_on > 2:
      ax71.spines.right.set_position(("outward", 50))
   else:
      ax71.spines.right.set_position(("outward", 5))
   ax71.set_ylabel (
         "Δ Temperature in °C 71",
         color=c71,
         fontname="Arial",fontsize=20,
         labelpad=10   # smaller = closer to y axis
          )
   ax71.tick_params(axis="y", labelcolor=c71, labelsize=20)
# 8.7.2 plot72
elif plot72_AESS_T > 0 and plot71_temperature < 1:
   if plot54_Glen_delta_on > 2:
      ax72.spines.right.set_position(("outward", 50))
   else:
      ax72.spines.right.set_position(("outward", 5))
   ax72.set_ylabel (
         "Δ Temperature calc72 in  °C ",
         color=c72,
         fontname="Arial",fontsize=20,
         labelpad=10   # smaller = closer to y axis
         )
   ax72.tick_params(axis="y", labelcolor=c72, labelsize=20)
# 8.7.3 plot73
elif plot73_ECS_T > 0:
   ax73.plot(df73["Year73"], df73["Modeled73"], '--', label="T formula CO2=  K73", color=c73, linewidth=3)
   ax73.tick_params(axis="y", labelcolor=c73)
   ax73.set_ylim(y_Tmin, y_Tmax) # scale
   if plot71_temperature < 1: # make y axis right only if not exist
      #ax73.yaxis.set_major_locator(MultipleLocator(y_Tmayor_ticks))   # Hauptstriche
      #ax73.yaxis.set_minor_locator(MultipleLocator(y_Tminor_ticks))   # Nebenstriche
      # ax73.minorticks_off()
      ax73.tick_params(axis='y', labelsize=20) # numbers on right y axis size 20
      ax73.set_ylabel (
         "Δ Temperature in °C (ECS = 4.5°C)73",
         color=c71,
         fontname="Arial",fontsize=20,
         labelpad=10   # smaller = closer to y axis
       )
elif plot74_GIS_T > 0:
   # ax74.plot(df73["Year73"], df73["Modeled73"], '--', label="T formula CO2=  K73", color=c73, linewidth=3)
   ax74.tick_params(axis="y", labelcolor=c74)
   ax74.set_ylim(y_Tmin, y_Tmax) # scale
   if plot71_temperature < 1: # make y axis right only if not exist
      ax74.yaxis.set_major_locator(MultipleLocator(y_Tmayor_ticks))   # Hauptstriche
      ax74.yaxis.set_minor_locator(MultipleLocator(y_Tminor_ticks))   # Nebenstriche
      ax74.tick_params(axis='y', labelsize=20) # numbers on right y axis size 20
      ax74.set_ylabel (
         "Δ GIS Temperature in °C  1095  74",
         color=c74,
         fontname="Arial",fontsize=20,
         labelpad=10   # smaller = closer to y axis
       )      
elif plot52_delta_CO2_red_bars > 0:
   ax52.spines.right.set_position(("outward", 20))
   bars = ax52.bar(df2["x_22_years"], df2["Delta_CO2"], width=0.7, alpha=0.5, color="red")
   ax52.bar(df2["x_22_years"], df2["Delta_CO2"], width=0.7, alpha=0.5, color="red")
   ax52.set_ylabel("red bars Mauna Loa CO2 increase in ppm", color="red", fontname="Arial",fontsize=16) # fontweight="bold"
   ax52.tick_params(axis="y", labelcolor="red", labelsize=16)
   ax52.set_ylim(y_Tmin, y_Tmax) # scale y axis3 right red   
   # 5.2.8 Add numbers on top of delta CO2 bars
   if plot52_delta_CO2_red_bars > 6:
      ax52.bar_label(bars, fontsize=8, fontname="Arial",padding=1, color="black")
elif plot34_CO2_emission > 0:
   ax34 = ax1.twinx()

   # Left axis 2: GtC
   if plot73_ECS_T > 0:
      ax34.spines["left"].set_position(("outward", 60))  # move outward from ax1
      ax34.spines["left"].set_visible(True)
      ax34.spines["right"].set_visible(False)
      ax34.yaxis.set_label_position("left")
      ax34.yaxis.tick_left()
   else:
      ax34.spines.right.set_position(("outward", 4))
      ax34.set_ylabel("CO2 cumulative emission in GtCO2  34", color=c34,
                   fontname="Arial",fontsize=20,
                   labelpad=1   # smaller = closer to y axis
                   )
   if plot34_CO2_emission_mode == 1:       # df34a = pd.read_csv("co2_sum_world.csv")
      ax34.plot(df34a["Year34"], df34a["GCumulat"], marker="o",  color=c34, label="plot34_CO2_emission")
      ax34.tick_params(axis="y", labelcolor=c34)
      ax34.set_ylim(0, 2000) # best scaling 2000 GtCO2
   elif plot34_CO2_emission_mode == 2:
      ax34.plot(df34b["Year34"], df34b["Cumulat"], marker="o",  color=c34, label="plot34_CO2_emission")
      ax34.tick_params(axis="y", labelcolor=c34)
      ax34.set_ylim(0, 2000000000000) #8
   elif plot34_CO2_emission_mode == 3:
      ax34.plot(co2_sum_world["Year"], co2_sum_world["GCumulat"], marker="o",  color=c34, label="plot34_CO2_emission")
      ax34.tick_params(axis="y", labelcolor=c34)
      ax34.set_ylim(300, 800) # best scaling 2000 GtCO2
   elif plot34_CO2_emission_mode == 4:
      ax34.set_ylabel("cumulative emission in GtC  34 mode 4", color=c34,
                   fontname="Arial",fontsize=20,
                   labelpad=1   # smaller = closer to y axis
                   )
      ax34.plot(co2_sum_world["Year"], co2_sum_world["CCumulat"], marker="o",  color=c34, label="plot34_CO2_emission")
      ax34.tick_params(axis="y", labelcolor=c34)
      ax34.set_ylim(0, 800) # best scaling 500 GtC
      ax34.set_ylim(0, 1000) # best scaling 500 GtC
      
   else:
      ax34.plot(df34b["Year"], df34b["Cumulat"], marker="o",  color=c34, label="plot34_CO2_emission")
      ax34.tick_params(axis="y", labelcolor=c34)
      ax34.set_ylim(0, 2000000000000) #8

# 8.7.9 
elif plot55_population_on > 0:
   ax55.spines.right.set_position(("outward", 80))
   ax55.set_ylabel("Earth Population in Billion", color="green")
   ax55.plot(pop_world["Year"], pop_world["Population_Mrd"], marker="s", color="green", label="Earth Population in Billion K2")
   ax55.set_ylabel("Earth Population in Billion", color="green")
   ax55.tick_params(axis="y", labelcolor="green")
   ax55.set_ylim(1, 9) #8
   # ax55.set_ylim(4, 9)
   #end print_y2=1 - print population


# 8.8 print the x axis 
# 8.8.1 print year below the year numbers 
ax1.set_xlabel("year", fontsize=20 )
plt.xticks(fontsize=20)
ax1.tick_params(axis="x", labelcolor="black", labelsize=20) # 1960 2020 Achsenbeschriftung
# 8.8.2 scale the x axis major 20 years
if x_end - x_anf < 5:
   x_mayor_ticks = 1
   x_minor_ticks = 0.5
elif x_end - x_anf < 11:
   x_mayor_ticks = 1
   x_minor_ticks = 0.5
elif x_end - x_anf < 21:
   x_mayor_ticks = 5
   x_minor_ticks = 1
elif x_end - x_anf < 70:
   x_mayor_ticks = 10
   x_minor_ticks = 2
elif x_end - x_anf < 120:
   x_mayor_ticks = 20
   x_minor_ticks = 5
elif x_end - x_anf < 220:
   x_mayor_ticks = 50
   x_minor_ticks = 10
elif x_end - x_anf < 320:
   x_mayor_ticks = 100
   x_minor_ticks = 20
elif x_end - x_anf < 520:
   x_mayor_ticks = 100
   x_minor_ticks = 50
elif x_end - x_anf < 1020:
   x_mayor_ticks = 200
   x_minor_ticks = 20
elif x_end - x_anf < 2020:
   x_mayor_ticks = 200
   x_minor_ticks = 50
elif x_end - x_anf < 4020:
   x_mayor_ticks = 500
   x_minor_ticks = 100
elif x_end - x_anf < 10020:
   x_mayor_ticks = 1000
   x_minor_ticks = 500
elif x_end - x_anf < 25060:
   x_mayor_ticks = 5000
   x_minor_ticks = 2000
elif x_end - x_anf < 50020:
   x_mayor_ticks = 10000
   x_minor_ticks = 2000
elif x_end - x_anf < 150020:
   x_mayor_ticks = 10000
   x_minor_ticks = 2000
elif x_end - x_anf < 1000020:
   x_mayor_ticks = 100000
   x_minor_ticks = 20000
else:
   x_mayor_ticks = 100000
   x_minor_ticks = 20000
# 8.8.8 scale the x axis major 20 years
ax1.xaxis.set_major_locator(MultipleLocator(x_mayor_ticks))  # works
ax1.tick_params(axis='x', which='major', length=10, width=2) # all 20 years
# 8.8.9 scale the x axis minor 5 years
ax1.xaxis.set_minor_locator(MultipleLocator(x_minor_ticks))   # no work
ax1.tick_params(axis='x', which='minor', length=7,  width=1)
  
# 8.9 print the horizontal lines year 2026
# 8.9.1 vertical major grid all 20 years
for line in ax1.get_xgridlines():   # vertical lines
       line.set_color('black')          # vertical color
       line.set_alpha(0.5)
       line.set_linestyle('--')        # optional '--'
       line.set_linewidth(1.9)   # <-- thickness
# 8.9.2 vertical minorlines all 5 years        
ax1.grid(True, which="minor", axis="x", color="purple", alpha=0.64)   # work vertical 5 years
# 8.9.3 vertical line at year 2026
ax1.axvspan(2025, 2027, color="#B3D9FF", alpha=0.5, zorder=0) # vertical bar'
# 8.9.4
ax1.axvspan(2065, 2066, color=c23, alpha=0.4, zorder=0) # vertical bar'
ax1.axvspan(2174, 2175, color=c23, alpha=0.25, zorder=0) # vertical bar'


# end part 8





# 9 part 9 print information below the plot field
# 9 part 9 print information below the plot field
trs = 20
# 9 part 9 print information below the plot field
# 9.1.1 print line 1 the text below the figure tr1x = -0.09 # tr1y = -.16 
filename = os.path.basename(sys.argv[0])
if plot22_CO2_Mauna_Loa == 1: #  legende world data plot22_CO2_Mauna_Loa
   line22 = Line2D([lr2x1, lr2x2], [lr1y, lr1y], # x coords in figure space (0–1)
   transform=fig.transFigure,
   marker="o", markersize=5, color=c22, linewidth=2)
   # 9.1.1 plot the blue text
   plt.text(tr2x, tr1y, blue22_text, color=c22, fontname="Arial", fontsize=trs,
   transform=plt.gca().transAxes)
   fig.add_artist(line22)
else:
   text_below1 = ""
   # 9.1.2 text_below1 = text_below1 + header_parameter
   text_below1 = text_below1 + "Figure from "
   text_below1 = text_below1 + filename
   text_below1 = text_below1 + " v "
   text_below1 = text_below1 + v
   text_below1 = text_below1 + "  https://github.com/Boettcher1960/co2_python       Parameter "
   text_below1 = text_below1 + header_parameter
   plt.text(-0.1, tr1y, text_below1, color="black", fontname="Arial", fontsize=12,
         transform=plt.gca().transAxes)

# 9.2 print line 2 blue Mauna Loa data below the figure
# 9.2.2 print line 22 below the plot explainations
if plot22_CO2_Mauna_Loa == 2: #  legende world data plot22_CO2_Mauna_Loa
   line22 = Line2D([lr2x1, lr2x2], [lr2y, lr2y], # x coords in figure space (0–1)
   transform=fig.transFigure,
   marker="o", markersize=5, color=c22, linewidth=2)
   # 9.2.2.5 plot the blue text
   plt.text(tr2x, tr2y, blue22_text, color=c22, fontname="Arial", fontsize=trs,
   transform=plt.gca().transAxes)
   fig.add_artist(line22)
# 9.2.3 print line 23 below the plot explainations
elif plot23_Glen_CO2 == 2: # 
   line23 = Line2D([lr2x1, lr2x2], [lr2y, lr2y], # y from 0 to 1
   transform=fig.transFigure,
   marker="o", markersize=3, color=c23, linewidth=2)
   fig.add_artist(line23)
   plt.text(tr2x, tr2y, text_plot23_Glen, color=c23, fontname="Arial", fontsize=trs,
   transform=plt.gca().transAxes)
   fig.add_artist(line23)
elif plot34_CO2_emission == 2: # 
   line34 = Line2D([lr2x1, lr2x2], [lr2y, lr2y], # y from 0 to 1
   transform=fig.transFigure,
   marker="o", markersize=3, color=c34, linewidth=2)
   fig.add_artist(line34)
   plt.text(tr2x, tr2y, print34_text, color=c34, fontname="Arial", fontsize=trs,
   transform=plt.gca().transAxes)
   fig.add_artist(line34)
elif plot74_GIS_T == 2:
   line74 = Line2D([lr2x1, lr2x2], [lr2y, lr2y], # y from 0 to 1
   transform=fig.transFigure,
   marker="o", markersize=3, color=c73, linewidth=2)
   fig.add_artist(line74)        
   plt.text(tr2x, tr2y, print74_text, color=c74, fontname="Arial", fontsize=trs,
   transform=plt.gca().transAxes)
elif plot22_CO2_Mauna_Loa == 3: #  legende world data plot22_CO2_Mauna_Loa
   K1_text=" 2 new text )"
   plt.text(tr2x, tr2y, K1_text, color=c22, fontname="Arial", fontsize=18,
   transform=plt.gca().transAxes)
   fig.add_artist(line22)
else: # 9.2.2 draw bue line as legend
   line22 = Line2D([lr2x1, lr2x2], [lr2y, lr2y], # x coords in figure space (0–1)
   transform=fig.transFigure,
   marker="o", markersize=5, color=c22, linewidth=2)
   # 9.2.3 draw bue line as legend
   fig.add_artist(line22)
   plt.text(tr2x, tr2y, "707 no item for line 2", color=c22, fontname="Arial", fontsize=18,
            transform=plt.gca().transAxes)
# end line 2

# 9.3 print line 3 below the plot explainations
# 9.3.3  print line red Glen 
if plot22_CO2_Mauna_Loa == 3: #  legende world data plot22_CO2_Mauna_Loa
   line22 = Line2D([lr2x1, lr2x2], [lr3y, lr3y], # x coords in figure space (0–1)
   transform=fig.transFigure,
   marker="o", markersize=5, color=c22, linewidth=2)
   # 9.2.2.5 plot the blue text
   plt.text(tr2x, tr3y, blue22_text, color=c22, fontname="Arial", fontsize=trs,
   transform=plt.gca().transAxes)
   fig.add_artist(line22)
elif plot23_Glen_CO2 == 3: # print in line 3
   line23 = Line2D([lr2x1, lr2x2], [lr3y, lr3y], # y from 0 to 1
   transform=fig.transFigure,
   marker="o", markersize=3, color=c23, linewidth=2)
   # 9.3.3 draw bue line as legend
   fig.add_artist(line23)
   # 9.3.3 write blue text
   plt.text(tr2x, tr3y, text_plot23_Glen, color=c23, fontname="Arial", fontsize=trs,
   transform=plt.gca().transAxes)
elif plot25_long_CO2 == 3: # 
   line25 = Line2D([lr2x1, lr2x2], [lr3y, lr3y], # y from 0 to 1
   transform=fig.transFigure,
   marker="o", markersize=3, color=c34, linewidth=2)
   fig.add_artist(line25)
   plt.text(tr2x, tr3y, blue25_text, color=c25, fontname="Arial", fontsize=trs,
   transform=plt.gca().transAxes)
   fig.add_artist(line25)

# 9.3.4 print line 3 green Glen data below the figure marker="_", markersize=5, color="green", linewidth=8)
elif plot34_CO2_emission == 3: # 
   line34 = Line2D([lr2x1, lr2x2], [lr3y, lr3y], # y from 0 to 1
   transform=fig.transFigure,
   marker="o", markersize=3, color=c34, linewidth=2)
   fig.add_artist(line34)
   plt.text(tr2x, tr3y, print34_text, color=c34, fontname="Arial", fontsize=trs,
   transform=plt.gca().transAxes)
   fig.add_artist(line34)
elif part41_ceres_eei == 3: #  legende world data plot22_CO2_Mauna_Loa
   line41 = Line2D([lr2x1, lr2x2], [lr3y, lr3y], # x coords in figure space (0–1)
   transform=fig.transFigure,
   marker="s", markersize=5, color=c41, linewidth=2)
   # 9.5.2 draw bue line as legend
   fig.add_artist(line41)
   # 9.5.4 write green text
   plt.text(tr2x, tr3y, p41_text, color=c41, fontname="Arial", fontsize=trs,
   transform=plt.gca().transAxes)
elif plot52_delta_CO2_red_bars == 3 or plot52_delta_CO2_red_bars == 7:
   line4 = Line2D([lr2x1, lr2x2], [lr3y, lr3y], # y from 0 to 1
   transform=fig.transFigure,
   marker="_", markersize=5, color="red", linewidth=8)
   # 9.3.4 draw bue line as legend
   fig.add_artist(line4)
   # 9.3.4 write red text
   text4="red bars: Mauna Loa yearly CO2 increase //see right larger ppm scaling"
   # 9.3.4 plot the red text
   plt.text(tr2x, tr3y, text4, color="red", fontname="Arial", fontsize=trs,
   transform=plt.gca().transAxes)
# 9.3.5 print line 3 orange Glen data below the figure
elif plot53_CO2_orange2025 == 3: # print in line 3 up to 2025
   line3 = Line2D([lr2x1, lr2x2], [lr3y, lr3y], # y from 0 to 1
   transform=fig.transFigure,
   marker="o", markersize=3, color="orange", linewidth=2)
   # 9.3.5 draw bue line as legend
   fig.add_artist(line3)
   # 9.3.5 write blue text
   red53_text="Orange dashed line: Glen parabol formula ppm = 0.0132251t² - 51.0337t + 49,536"
   # 9.3.5 plot the blue text
   plt.text(tr2x, tr3y, red53_text, color="orange", fontname="Arial", fontsize=trs,
   transform=plt.gca().transAxes)
   # 9.3.5 print line 4 green Glen data below the figure marker="_", markersize=5, color="green", linewidth=8)
# 9.3.6  print line 3 green Glen 
elif plot54_Glen_delta_on == 3: # print in line4
   line4 = Line2D([lr2x1, lr2x2], [lr3y, lr3y], # y from 0 to 1 lr3y
   transform=fig.transFigure,
   marker="_", markersize=5, color="green", linewidth=8)
   # 9.3.6 draw bue line as legend
   fig.add_artist(line4)
   # 9.3.6 write blue text
   green_text="Green bars: Difference Mauna Loa - Glen quadratic t² //see right larger ppm scaling"
   # 9.3.6 plot the green text
   plt.text(tr2x, tr3y, green_text, color="green", fontname="Arial", fontsize=trs,
   transform=plt.gca().transAxes)
   # 9.3.6_ print line 3 red Glen data below the figure
# 9.3.7 print line 3 plot55_population_on marker="s"
elif plot55_population_on == 3: #  legende world data plot22_CO2_Mauna_Loa
   line55 = Line2D([lr2x1, lr2x2], [lr3y, lr3y], # x coords in figure space (0–1)
   transform=fig.transFigure,
   marker="s", markersize=5, color="green", linewidth=2)
   # 9.3.7 draw bue line as legend
   fig.add_artist(line55)
   # 9.3.7 write green text
   plt.text(tr2x, tr3y, green55_text, color="green", fontname="Arial", fontsize=trs,
   transform=plt.gca().transAxes)
elif plot73_ECS_T == 3:
   line73 = Line2D([lr2x1, lr2x2], [lr3y, lr3y], # y from 0 to 1
   transform=fig.transFigure,
   marker="o", markersize=3, color=c73, linewidth=2)
   # 9.5.8 draw line72 as legend
   fig.add_artist(line73)
   # 9.5.8 write  text         
   red73_text="ECS Earth Climate sensitivity= 4.5°C * log2(CO2/C0) 73"
   plt.text(tr2x, tr3y, red73_text, color=c73, fontname="Arial", fontsize=trs,
   transform=plt.gca().transAxes)
elif plot74_GIS_T == 3:
   line74 = Line2D([lr2x1, lr2x2], [lr3y, lr3y], # y from 0 to 1
   transform=fig.transFigure,
   marker="o", markersize=3, color=c74, linewidth=2)
   fig.add_artist(line74)    
   plt.text(tr2x, tr3y, print74_text, color=c74, fontname="Arial", fontsize=trs,
   transform=plt.gca().transAxes)

   # 9.3 end print line 3 below the plot explainations


# 9.4 print line 4 below the plot explainations
# 9.4 print line 4 below the plot explainations
# 9.4.3_ print line 3 red Glen data below the figure
if plot23_Glen_CO2 == 4: # print in line 3
   line4 = Line2D([lr2x1, lr2x2], [lr4y, lr4y], # y from 0 to 1
   transform=fig.transFigure,
   marker="o", markersize=3, color=c23, linewidth=2)
   # 9.4.3 draw bue line as legend
   fig.add_artist(line4)
   plt.text(tr2x, tr4y, text_plot23_Glen, color=c23, fontname="Arial", fontsize=trs,
   transform=plt.gca().transAxes)
elif plot25_long_CO2 == 4: # 
   line25 = Line2D([lr2x1, lr2x2], [lr4y, lr4y], # y from 0 to 1
   transform=fig.transFigure,
   marker="o", markersize=3, color=c34, linewidth=2)
   fig.add_artist(line25)
   plt.text(tr2x, tr4y, blue25_text, color=c25, fontname="Arial", fontsize=trs,
   transform=plt.gca().transAxes)
   fig.add_artist(line25)
elif part42_ceres_eei == 4: #  legende world data plot22_CO2_Mauna_Loa
   line42 = Line2D([lr2x1, lr2x2], [lr4y, lr4y], # x coords in figure space (0–1)
   transform=fig.transFigure,
   marker="s", markersize=5, color=c42, linewidth=2)
   # 9.5.2 draw bue line as legend
   fig.add_artist(line42)
   # 9.5.4 write green text
   plt.text(tr2x, tr4y, p42_text, color=c42, fontname="Arial", fontsize=trs,
   transform=plt.gca().transAxes)
elif plot52_delta_CO2_red_bars == 4 or plot52_delta_CO2_red_bars == 8:
   line4 = Line2D([lr2x1, lr2x2], [lr4y, lr4y], # y from 0 to 1
   transform=fig.transFigure,
   marker="_", markersize=5, color="red", linewidth=8)
   # 9.2.3 draw bue line as legend
   fig.add_artist(line4)
   # 9.2.4 write blue text
   text4="red bars: Mauna Loa yearly CO2 increase //see right larger ppm scaling 52"
   # 9.2.5 plot the blue text
   plt.text(tr2x, tr4y, text4, color="red", fontname="Arial", fontsize=trs,
   transform=plt.gca().transAxes)
# 9.4.4 work_ print line 4 orange Glen data below the figure
elif plot53_CO2_orange2025 == 4: # print in line 3 up to 2025
   line4 = Line2D([lr2x1, lr2x2], [lr4y, lr4y], # y from 0 to 1
   transform=fig.transFigure,
   marker="o", markersize=3, color="orange", linewidth=2)
   # 9.2.3 draw bue line as legend
   fig.add_artist(line4)
   # 9.2.4 write blue text
   red53_text="Orange dashed line: Glen parabol formula ppm = 0.0132251t² - 51.0337t + 49,536"
   # 9.2.5 plot the blue text
   plt.text(tr2x, tr4y, red53_text, color="orange", fontname="Arial", fontsize=trs,
   transform=plt.gca().transAxes)
# 9.4.5 print line 4 green Glen data below the figure marker="_", markersize=5, color="green", linewidth=8)
elif plot54_Glen_delta_on == 4: # print in line4
   line5 = Line2D([lr2x1, lr2x2], [lr4y, lr4y], # y from 0 to 1 lr3y
   transform=fig.transFigure,
   marker="_", markersize=5, color="green", linewidth=8)
   # 9.2.3 draw bue line as legend
   fig.add_artist(line5)
   # 9.2.4 write blue text
   green_text="Green bars: Difference Mauna Loa - Glen quadratic t² //see right larger ppm scaling"
   # 9.2.5 plot the blue text
   plt.text(tr2x, tr4y, green_text, color="green", fontname="Arial", fontsize=trs,
   transform=plt.gca().transAxes)
   # 9.4.2 print line 4 plot55_population_on marker="s"
elif plot34_CO2_emission == 4: # 
   line34 = Line2D([lr2x1, lr2x2], [lr4y, lr4y], # y from 0 to 1
   transform=fig.transFigure,
   marker="o", markersize=3, color=c34, linewidth=2)
   fig.add_artist(line34)
   plt.text(tr2x, tr4y, print34_text, color=c34, fontname="Arial", fontsize=trs,
   transform=plt.gca().transAxes)
   fig.add_artist(line34)
elif plot55_population_on == 4:
   line55 = Line2D([lr2x1, lr2x2], [lr4y, lr4y],
   transform=fig.transFigure,
   marker="s", markersize=5, color="green", linewidth=2)
   fig.add_artist(line55)
   plt.text(tr2x, tr4y, green55_text, color="green", fontname="Arial", fontsize=trs,
   transform=plt.gca().transAxes)
   # 9.4.52 print line 4 green Glen data below the figure marker="_", markersize=5, color="green", linewidth=8)
elif plot71_temperature == 4:
   line7 = Line2D([lr2x1, lr2x2], [lr4y, lr4y], # y from 0 to 1
   transform=fig.transFigure,
   marker="o", markersize=3, color=c71, linewidth=2)
   # 9.4.7 draw bue line as legend
   fig.add_artist(line7)
   # 9.4.7 write  text  0.000617965091650558 * t**2 - 2.45858656778789 * t + 2446.05792853123
   # 9.2.5 plot the blue text
   plt.text(tr2x, tr4y, red71_text, color=c71, fontname="Arial", fontsize=trs,
   transform=plt.gca().transAxes)
elif plot72_AESS_T == 4:
   line72 = Line2D([lr2x1, lr2x2], [lr4y, lr4y], # y from 0 to 1
   transform=fig.transFigure,
   marker="o", markersize=3, color=c72, linewidth=2)
   # 9.5.8 draw line72 as legend
   fig.add_artist(line72)
   # 9.5.8 write  text 
   plt.text(tr2x, tr4y, red72_text, color=c72, fontname="Arial", fontsize=trs,
   transform=plt.gca().transAxes)
elif plot73_ECS_T == 4:
   line73 = Line2D([lr2x1, lr2x2], [lr4y, lr4y], # y from 0 to 1
   transform=fig.transFigure,
   marker="o", markersize=3, color=c73, linewidth=2)
   # 9.5.8 draw line72 as legend
   fig.add_artist(line73)
   # 9.5.8 write  text         
   red73_text="ECS Earth Climate sensitivity= 4.5°C * log2(CO2/C0) 73"
   plt.text(tr2x, tr4y, red73_text, color=c73, fontname="Arial", fontsize=trs,
   transform=plt.gca().transAxes)
elif plot74_GIS_T == 4:
   line74 = Line2D([lr2x1, lr2x2], [lr4y, lr4y], # y from 0 to 1
   transform=fig.transFigure,
   marker="o", markersize=3, color=c74, linewidth=2)
   # 9.4.8 draw line72 as legend
   fig.add_artist(line74)
   # 9.4.8 write  text         
   plt.text(tr2x, tr4y, print74_text, color=c74, fontname="Arial", fontsize=trs,
   transform=plt.gca().transAxes)
elif linear_41_75 == 4:
   # print75_text ="Hansen linear fit from 2015 +0.41°C     75"
   line75 = Line2D([lr2x1, lr2x2], [lr4y, lr4y], # y from 0 to 1
   transform=fig.transFigure,
   marker="o", markersize=3, color=c75, linewidth=2)
   fig.add_artist(line75)
   plt.text(tr2x, tr4y, print75_text, color=c75, fontname="Arial", fontsize=trs,
   transform=plt.gca().transAxes)


# 9.5.2 print line 5 plot55_population_on marker="s"
if part41_ceres_eei == 5: #  legende world data plot22_CO2_Mauna_Loa
   line41 = Line2D([lr2x1, lr2x2], [lr5y, lr5y], # x coords in figure space (0–1)
   transform=fig.transFigure,
   marker="s", markersize=5, color=c41, linewidth=2)
   # 9.5.2 draw bue line as legend
   fig.add_artist(line41)
   # 9.5.4 write green text
   plt.text(tr2x, tr5y, p41_text, color=c41, fontname="Arial", fontsize=trs,
   transform=plt.gca().transAxes)
elif part43_ceres_eei == 5: #  legende 
   line43 = Line2D([lr2x1, lr2x2], [lr5y, lr5y], # x coords in figure space (0–1)
   transform=fig.transFigure,
   marker="s", markersize=5, color=c43, linewidth=2)
   # 9.5.2 draw bue line as legend
   fig.add_artist(line43)
   # 9.5.4 write green text
   plt.text(tr2x, tr5y, p43_text, color=c43, fontname="Arial", fontsize=trs,
   transform=plt.gca().transAxes)   
elif part44_ceres_eei > 3: #  legende world data plot22_CO2_Mauna_Loa
   line44 = Line2D([lr2x1, lr2x2], [lr5y, lr5y], # x coords in figure space (0–1)
   transform=fig.transFigure,
   marker="s", markersize=5, color=c44, linewidth=2)
   fig.add_artist(line44)
   plt.text(tr2x, tr5y, p44_text, color=c44, fontname="Arial", fontsize=trs,
   transform=plt.gca().transAxes)

elif plot55_population_on == 5: #  legende world data plot22_CO2_Mauna_Loa
   line55 = Line2D([lr2x1, lr2x2], [lr5y, lr5y], # x coords in figure space (0–1)
   transform=fig.transFigure,
   marker="s", markersize=5, color="green", linewidth=2)
   # 9.5.2 draw bue line as legend
   fig.add_artist(line55)
   # 9.5.4 write green text
   plt.text(tr2x, tr5y, green55_text, color="green", fontname="Arial", fontsize=trs,
   transform=plt.gca().transAxes)
elif plot71_temperature == 5:
   line7 = Line2D([lr2x1, lr2x2], [lr5y, lr5y], # y from 0 to 1
   transform=fig.transFigure,
   marker="o", markersize=3, color=c71, linewidth=2)
   # 9.5.7 draw bue line as legend
   fig.add_artist(line7)
   plt.text(tr2x, tr5y, red71_text, color=c71, fontname="Arial", fontsize=trs,
   transform=plt.gca().transAxes)
elif plot72_AESS_T == 5:
   line72 = Line2D([lr2x1, lr2x2], [lr5y, lr5y], # y from 0 to 1
   transform=fig.transFigure,
   marker="o", markersize=3, color=c72, linewidth=2)
   # 9.5.8 draw line72 as legend
   fig.add_artist(line72)
   # 9.5.8 write  text 
   red72_text="AESS_T Apparent Earth Sensitivity=8°C*log2(CO2/C0)"
   plt.text(tr2x, tr5y, red72_text, color=c72, fontname="Arial", fontsize=trs,
   transform=plt.gca().transAxes)
   #else: # 9.5.9 draw bue line as legend
   #plt.text(tr2x, tr5y, "Line 5 -0.48", color="white", fontname="Arial", fontsize=trs,
   #transform=plt.gca().transAxes)
elif plot73_ECS_T == 5:
   line73 = Line2D([lr2x1, lr2x2], [lr5y, lr5y], # y from 0 to 1
   transform=fig.transFigure,
   marker="o", markersize=3, color=c73, linewidth=2)
   # 9.5.8 draw line72 as legend
   fig.add_artist(line73)
   # 9.5.8 write  text 
   if plot72_AESS_T == 5 and plot73_ECS_T == 5:
      red73_text="ECS=4.5°C*log2(CO2/C0)"
      plt.text(0.71, tr5y, red73_text, color=c73, fontname="Arial", fontsize=trs,
      transform=plt.gca().transAxes)
   else:            
       red73_text="ECS Earth Climate sensitivity= 4.5°C * log2(CO2/C0)"
       plt.text(tr2x, tr5y, red73_text, color=c73, fontname="Arial", fontsize=trs,
       transform=plt.gca().transAxes)
elif plot76_my_T == 5:
   line76 = Line2D([lr2x1, lr2x2], [lr5y, lr5y], # y from 0 to 1
   transform=fig.transFigure,
   marker="o", markersize=3, color=c76, linewidth=2)
   fig.add_artist(line76)
   # 9.5.8 write  text 
   if plot76_my_T == 5:
      plt.text(tr2x, tr5y, my76_text, color=c76, fontname="Arial", fontsize=trs,
      transform=plt.gca().transAxes)
   

# 9.5 end print line 5 

# 9.6 print line 6 
if ( yl_mode == 4 ): 
   text6 = f"Left Y axis is the " # 
   text6 = text6 + f"EEI = {y_Emin}" # y_max number inside string
   text6 = text6 + f" ... {y_Emax} W/m²" # y_max number inside string
   plt.text(-0.12, -.56, text6 , color=c42, fontname="Arial", fontsize=trs,
       transform=plt.gca().transAxes)
   text6 = f"    Right Y axis is the" # 
   text6 = text6 + f" Temperature = {y_Tmin}" # y_max number inside string
   text6 = text6 + f" ... {y_Tmax} °C" # y_max number inside string
   
   # text6 = text6 + header_parameter
   # 9.6.2 plot line 6
   plt.text(0.42, -.56, text6 , color="red", fontname="Arial", fontsize=trs,
      transform=plt.gca().transAxes)
   fig.tight_layout()
   plt.tight_layout()

elif plot73_ECS_T < 6:
   text6 = f" CO2_min= {y_min}ppm " # y_max number inside string
   text6 = text6 + f" CO2_max= {y_max} " # y_max number inside string
   text6 = text6 + f"  T_max= {y_Tmax}°C    Parameter=" # y_max number inside string
   text6 = text6 + header_parameter
   # 9.6.2 plot line 6
   plt.text(-0.12, -.56, text6 , color="black", fontname="Arial", fontsize=trs,
       transform=plt.gca().transAxes)
   fig.tight_layout()
   plt.tight_layout()
else: # plot73_ECS_T = 6
   line73 = Line2D([lr2x1, lr2x2], [lr6y, lr6y], # y from 0 to 1
   transform=fig.transFigure,
   marker="o", markersize=3, color=c73, linewidth=2)
   fig.add_artist(line73)
   # 9.6.8 write  text 
   red73_text="ECS Earth Climate sensitivity= 4.5°C * log2(CO2/C0)"
   plt.text(tr2x, tr6y, red73_text, color=c73, fontname="Arial", fontsize=trs,
       transform=plt.gca().transAxes)
   fig.tight_layout()
   plt.tight_layout()

plt.show()

# 9.7 save the plot line 6
if parameter84_save_png > 0:
   filename = ""
   filename2 = os.path.basename(__file__) # "1234test.py"
   # take only the first 5 characters
   first5 = filename2[:parameter84_save_png]
   filename = filename + first5
   filename = filename + "_"
   filename = filename + header_parameter
   filename = filename + str(x_end)
   path = f"/Users/thomasboettcher/Desktop/{filename}"
   fig.savefig(path, dpi=300, bbox_inches="tight")
   path = f"/Users/thomasboettcher/documents/Python/4_Python_CO2/42_CO2_T.png"
   fig.savefig(path, dpi=300, bbox_inches="tight")
# 9.9 close the plotted figure
plt.close(fig)

# 7.9 KurveX – Global annual temperature anomaly (°C, relative to baseline)
dataT79 = {
1880: -0.16, 1881: -0.08, 1882: -0.10, 1883: -0.17, 1884: -0.28,
1885: -0.33, 1886: -0.31, 1887: -0.36, 1888: -0.18, 1889: -0.11,
1890: -0.35, 1891: -0.22, 1892: -0.27, 1893: -0.31, 1894: -0.30,
1895: -0.23, 1896: -0.11, 1897: -0.11, 1898: -0.27, 1899: -0.17,
1900: -0.09,
# …
2000:  0.42, 2001:  0.54, 2002:  0.63, 2003:  0.62, 2004:  0.54,
2005:  0.67, 2006:  0.63, 2007:  0.66, 2008:  0.54, 2009:  0.64,
2010:  0.71, 2011:  0.59, 2012:  0.63, 2013:  0.66, 2014:  0.74,
2015:  0.87, 2016:  1.00, 2017:  0.92, 2018:  0.85, 2019:  0.98,
2020:  1.02, 2021:  0.85, 2022:  0.89, 2023:  1.18
}
yearsT79 = np.array(list(dataT79.keys()))
tempsT79 = np.array(list(dataT79.values()))



# Datenquellen:
# 2.2.2 Mauna_Loa 13.3.2026
# plot22_CO2_Mauna_Loa https://gml.noaa.gov/ccgg/trends/global.html
#
# 3.2 https://ourworldindata.org/grapher/cumulative-co-emissions
# https://github.com/zmlabe 
#
#  split the file into several parts.
# example main, part4 and part 9














# part 1 configure 
# part 2.2 plot CO2 Mauna Loa
# part 2.3 plot23_Glen_CO2 = 3
#
# part 3.4 plot34_CO2_emission summed
#
# part 5.2 plot52_delta_CO2_red_bars
# part 5.3 plot53_CO2_orange2025
# part 5.4 plot54_Glen_delta_on
# part 5.5 plot55_population_on human earth population 
#
# part 71 plot temperature with right y axis
# part 72 plot temperature ECS = 8°C with right y axis
# part 73 plot temperature ECS = 4.5°C with right y axis
#
# part 8 print headline, axis numbers. around figue
# part 9 print line 1 to 5 below the figure 

yl_mode = 2 # y axis left, mode =2 CO2 in ppm
yl_mode = 4 # y axis left, mode =4 EEI in W/m2
yl_mode = 7 # y axis left, mode =7 Temperature in °C


# -----------------------------
# 2.2 Mauna_Loa 13.3.2026
# plot22_CO2_Mauna_Loa data
values for part 2.2 plot22_CO2_Mauna_Loa 
https://gml.noaa.gov/webdata/ccgg/trends/co2/co2_annmean_mlo.txt

( I deleted the https://gml.noaa.gov/ccgg/trends/global.html )
( I deleted https://gml.noaa.gov/webdata/ccgg/trends/co2/co2_annmean_clobal.txt )

# -----------------------------
# 2.3 plot23_Glen_CO2 = 0.013t² - 51t + 49,536 in dark blue 
# https://x.com/Gergyl/status/1810632238230589564
# -----------------------------
# text_plot23_Glen="blue dashed @gergyl.bsky atmosphere ppm = 0.0132251t² - 51.0337t + 49,536"
text_plot23_Glen="calculated CO2 dashed blue line ppm = 0.0132251t² - 51.0337t + 49,536"

# plot25_long_CO2 = 3 # 2, 3 print -800 000 years ppm CO2 file
# https://ourworldindata.org/grapher/co2-long-term-concentration?overlay=download-data
# Data sources: NOAA Global Monitoring Laboratory - Trends in Atmospheric Carbon Dioxide (2026)EPA 
# based on various sources (2022) – with major processing by Our World in Data
# Retrieved from https://gml.noaa.gov/ccgg/trends/gl_data.html
# -----------------------------
#  part 2.5 plot CO2 Mauna Loa
blue25_text="blue: CO2 measured at Mauna Loa ( 2025 = 427.35 ppm ) 22"

Asynchrony between Antarctic temperature and CO2 associated with obliquity over the past 720,000 years
Valérie Masson-Delmotte, csv temperature data
https://www.nature.com/articles/s41467-018-03328-3
https://www.ncei.noaa.gov/access/paleo-search/study/23371

https://www.ncei.noaa.gov/pub/data/paleo/reconstructions/


# part 3.4 plot34_CO2_emission summed
# co2_cumul.csv
# https://ourworldindata.org/grapher/cumulative-co-emissions?country=~OWID_WRL&overlay=download-data
# 3.4.0 Entity,Code,Year,Cumulat
#       World,OWID_WRL,1750,9305937
if plot34_CO2_emission > 0:
   print34_text =" red dots: measured cumulative CO2 emissions by Carbon Brief 34"
   # plot34_CO2_emission_A = 1, read self made csv 2000 GtCO2
   # plot34_CO2_emission_A = 2, read csv 2000 000 000 000 tCO2
   # plot34_CO2_emission_A = 3, read csv 2000 GtCO2
   # plot34_CO2_emission_A = 4, read csv 2000 GtCO2
   # plot34_CO2_emission_A = 5










"""
# Load the annual GISTEMP data
url = "https://datahub.io/core/global-temp/r/annual.csv"
df2 = pd.read_csv(url)

# Inspect the first rows
print(df2.head())

# Plot
plt.figure(figsize=(10,5))
plt.plot(df2["Year"], df2["Mean"], marker="o")
plt.title("Global Annual Temperature Anomalies (GISTEMP)")
plt.xlabel("Year")
plt.ylabel("Temperature Anomaly (°C)")
plt.grid(True)
plt.show()
"""
# 8.4 legende Mauna Loa blau plot22_CO2_Mauna_Loa
if plot22_CO2_Mauna_Loa > 6: # 8.15.1 legende world data plot22_CO2_Mauna_Loa
   K1_text=" Blue: CO2 measured at Mauna Loa ( 2025 = 424.61ppm + 3.69 ppm )"
   plt.text(0.02, 0.95, K1_text, color="blue", fontname="Arial", fontsize=16,
   transform=plt.gca().transAxes)
   ax1.plot([x_anf+1, x_anf +2], [y_max -5, y_max -5], marker="o", markersize=5, color="blue", linewidth=2, label="short line")
# 8.15 plot55_population_on = 1 # 0 keine Bevölkerung , 1 = Bevölkerung in grün
if plot22_CO2_Mauna_Loa > 8:
   if plot55_population_on > 0:
      plt.text(0.02, 0.90,"green: Human Population in billion K2", color="green", fontname="Arial", fontsize=14,
      transform=plt.gca().transAxes)
# 8.16 legende
if plot22_CO2_Mauna_Loa > 8:
   if plot52_delta_CO2_red_bars > 0:
      plt.text(0.02, 0.86," red bars: Mauna Loa yearly increase. //see right larger ppm scaling", color="red", fontname="Arial", fontsize=14,
      transform=plt.gca().transAxes)
      ax1.plot([x_anf+1, x_anf +2], [y_max -21, y_max -21], marker="_", markersize=5, color="red", linewidth=8)
# 8.7 legende '--', label="Glen *parabola* ( 0.0132t² - 51t + 49,536) K4", color="orange", linewidth=3)
if plot22_CO2_Mauna_Loa > 8:
   if plot53_CO2_orange2025 > 0:
      plt.text(0.02, 0.80," orange: Glen formula ppm = 0.0132 t² - 51 t + 49,536 ", color="orange", fontname="Arial", fontsize=14,
      transform=plt.gca().transAxes)
      ax1.plot([x_anf+1, x_anf +2], [y_max -30.5, y_max -30.5], marker="_", markersize=5, color="orange", linewidth=3)
# 8.8 legend in the plot
if plot22_CO2_Mauna_Loa > 8:
   if plot54_Glen_delta_on > 0:
      plt.text(0.02, 0.29," green bars: Difference Mauna Loa - Glen quadratic t² //see right larger ppm scaling", color="green", fontname="Arial", fontsize=14,
      transform=plt.gca().transAxes)
      ax1.plot([x_anf+1, x_anf +2], [y_max -52, y_max -52], marker="_", markersize=5, color="green", linewidth=8)
# 8.9 legend in the plot
if plot22_CO2_Mauna_Loa > 8:
   if plot23_Glen_CO2 > 0:
      plt.text(0.02, 0.85," Red: Glen formula ppm = 0.0132251t² - 51.0337t + 49,536", color="red", fontname="Arial", fontsize=16,
      transform=plt.gca().transAxes)
      ax1.plot([x_anf+1, x_anf +2], [y_max -12, y_max -12], marker="_", markersize=5, color="red", linewidth=3)







Links to github

# Garvin Schmidt (follow up of James Hansen)
# climateofgavin.bsky.social recommends
https://github.com/Climate-REF
https://dashboard.climate-ref.org/

https://wcrp-cmip.org/tools/model-benchmarking-and-evaluation-tools/

# Zack Labe
https://github.com/zmlabe
Zachary Labe Climate Scientist 
https://www.linkedin.com/in/zacharylabe/
https://matplotlib.org/cmocean/
https://chadagreene.com/CDT/CDT_Getting_Started.html
https://www.mathworks.com/matlabcentral/fileexchange/47638-antarctic-mapping-tools/files/coord.m
https://www.ncei.noaa.gov/access/monitoring/monthly-report/global/202602



https://robbieandrew.github.io

https://robbieandrew.github.io/country/?country=DEU


https://matplotlib.org/cmocean/

# CO₂: Mauna-Loa/NOAA Jahresmittel (bis 2023), 2024/2025 vorläufig/Schätzung wie zuvor verwendet.
# https://gml.noaa.gov/webdata/ccgg/trends/co2/co2_annmean_mlo.txt
# ppm CO2 = 0.0132251t² - 51.0337t + 49,536.7
# https://github.com/zmlabe 

co2_cumul.csv
https://ourworldindata.org/grapher/cumulative-co-emissions?country=~OWID_WRL&overlay=download-data
https://ourworldindata.org/grapher/cumulative-co-emissions
https://globalcarbonbudget.org/gcb-2025/


Title	Temperature Vostok and GISP2
Reference	Alley, R.B..  (2004) GISP2 Ice Core Temperature and Accumulation Data
Reference	Jouzel et al. (1987, 1993 and 1996)
Source	
http://www.ncdc.noaa.gov/paleo/indexice.html
File	gisp2_temp_accum_alley2000.txt
File	vostok_deld.txt
Age	Vostok
http://www.climatedata.info/proxies/data-downloads/
https://www.ncei.noaa.gov/products/paleoclimatology



# part 5.2 plot52_delta_CO2_red_bars
# 5.2.2 ΔCO₂ berechnen (per pandas) Balken
# df2["CO2"].diff() Calculates the difference between consecutive CO₂ values
# -----------------------------
if plot52_delta_CO2_red_bars > 0:
   df2["Delta_CO2"] = df2["CO2"].diff().fillna(0)  
   # This line creates a new column in your DataFrame called Delta_CO2.
   ax52 = ax1.twinx()  # twinx(): Shares the same x-axis Adds a new y-axis on the right
# growth data is different https://gml.noaa.gov/webdata/ccgg/trends/co2/co2_gr_mlo.txt
#  2020        2.30        0.11
#  2021        2.35        0.11
#  2022        1.87        0.11
#  2023        3.32   2,55     0.11
#  2024        3.33   3,53     0.11
#  2025        2.23   2.74     0.11
# anual mean data is different https://gml.noaa.gov/webdata/ccgg/trends/co2/co2_annmean_mlo.txt
#  year   noa     my.py  noa  
#  2020   414.21   2,58  2.30
#  2021   416.41   2,17  2.35
#  2022   418.53   2,12  1.87
#  2023   421.08   2,55  3.32
#  2024   424.61   3,53  3.33
#  2025   427.35   2,74  2.23



# part 74 plot NASA GIS temperature
https://data.giss.nasa.gov/gistemp/zonal_means/
https://data.giss.nasa.gov/gistemp/zonal_means/
/4_PYTHON/csv_save/nasa_giss_global.csv
https://data.giss.nasa.gov/tmp/gistemp/ltmap/tmp.4_ob4LOTI_E5_12_1880_2027_1951_1980-0/global.txt
/4_PYTHON/csv_save/csv_74_giss_temperature.txt
https://www.columbia.edu/~jeh1/mailings/2026/ElNino.2026.02.06.pdf 
Hansen adds 0.3K to GIS Temperature in https://www.columbia.edu/~jeh1/mailings/2026/ElNino.2026.02.06.pdf
line ax74.plot(df74["Year74"], df74["GIS_temp"]+0.3, '-', label="T GIS  K74", color=c74, linewidth=3)
# part 7.4.6 add 0.3°C same as Hansen to GIS
   ax74.plot(df74["Year74"], df74["GIS_temp"]+0.3, '-', label="T GIS  K74", color=c74, linewidth=3)
/4_PYTHON/csv_save/74_GIS_temperature/

# part 76 
can you make a quadatic function like the below T_model76(t)
def T_model76(t):
    return 0.00052537 * t**2 - 2.071 * t + 2040.65
which returns 0.2 for t = 1950
which returns 1.0 for t = 2013
which returns 1.5 for t = 2023

def T_model76(t):
    return 0.00052537 * t**2 - 2.071 * t + 2040.65

#can you make a quadatic function like the below T_model71(t) in python
# which returns 0.2 for t = 1950
# which returns 1.0 for t = 2013
# which returns 1.5 for t = 2023
def T_model76b(t):
    return 0.00052537 * t**2 - 2.071 * t + 2040.65
def T_model76c(t):
    return (
        0.000525368248010184 * t**2
        - 2.07099741100324 * t
        + 2040.64663023679
    )
def T_model76d(t):
    x = t - 2000
    return 0.000525368248010184 * x**2 + 0.030377 * x + 0.9027
def T_model71d(t):
   return 0.000617965091650558 * t**2 - 2.45858656778789 * t + 2446.05792853123
# 
def T_model76e(t):
    x = t - 2000
    return 0.000525368248010184 * x**2 + 0.030377 * x + 0.7
def T_model76(t):
    x = t - 2000
    return 0.000525368248010184 * x**2 + 0.030377 * x + 0.7
def T_model71d(t):
   return 0.000617965091650558 * t**2 - 2.45858656778789 * t + 2446.05792853123
def T_model76e(t):
    x = t - 2000
    return 0.000525368248010184 * x**2 + 0.030377 * x + 0.7
def T_model76f(t):
    x = t - 2000
    return 0.000525368248010184 * x**2 + 0.030377 * x + 0.7
def T_model76f(t):
    x = t - 2000
    return 0.000525368248010184 * x**2 + 0.030377 * x + 0.7
def T_model76g(t):
    x = t - 2000
    return 0.0005 * x**2 + 0.02 * x + 0.7
def T_model76(t):
    x = t - 2000
    return 0.0005 * x**2 + 0.02 * x + 0.7
def T_model76f(t):
    x = t - 2000
    return 0.000525368248010184 * x**2 + 0.030377 * x + 0.7
def T_model76g(t):
    x = t - 2000
    return 0.0005 * x**2 + 0.02 * x + 0.7
def T_model76h(t):
    x = t - 2000
    return 0.00035 * x**2 + 0.02 * x + 0.5
def T_model76h2(t):
    x = t - 2000
    return 0.00027 * x**2 + 0.025 * x + 0.6
def T_model76h3(t):
    x = t - 2000
    return 0.00023 * x**2 + 0.027 * x + 0.8
def T_model76h4(t):
    x = t - 2000
    return 0.00021 * x**2 + 0.028 * x + 0.95
def T_model76k(t):
    x = t - 2000
    return 0.00018 * x**2 + 0.025 * x + 0.95
#can you make a quadatic function like the below T_model71(t)
# which returns 0.2 for t = 1950
# which returns 1.0 for t = 2013
# which returns 1.5 for t = 2023
def T_model76m(t):
    x = t - 2000
    return 0.00017 * x**2 + 0.022 * x + 0.85

 def T_model76a(t):
   CO2= 0.0132251 * t**2 - 51.0337 * t + 49536.7 # Glen formula
   #yppm = 440 -340   # scaling left y axis
   #yT   = 1.6 - 0.6  # scaling right y axis
   # scale 1.5°C at 410 ppm 2022: 418.53, 418-280 = 138
   temp76= ( CO2 -280 ) / 99
   temp76= temp76 +0.02
   return temp76   
def T_model76m1(t):
    x = t - 2000
    return 0.00017 * x**2 + 0.022 * x + 0.85
def T_model76m2(t):
    x = t - 2000
    return 0.00016 * x**2 + 0.0207 * x + 0.85
def T_model76m3(t):
    x = t - 2000
    return 0.00016 * x**2 + 0.021 * x + 0.85
def T_model76m4(t):
    x = t - 2000
    return 0.00016 * x**2 + 0.0225 * x + 0.85
    def T_model76m4(t):
    x = t - 2000
    return 0.00016 * x**2 + 0.0225 * x + 0.85
def T_model76m5(t):
    x = t - 2000
    return 0.00017 * x**2 + 0.0233 * x + 0.85
def T_model76m6(t):
    x = t - 2000
    return 0.00018 * x**2 + 0.0233 * x + 0.85
def T_model76m7(t):
    x = t - 2000
    return 0.00023 * x**2 + 0.0233 * x + 0.8
def T_model76m8(t):
    x = t - 2000
    return 0.00025 * x**2 + 0.0233 * x + 0.8
def T_model76m9(t):
    x = t - 2000
    return 0.00033 * x**2 + 0.0236 * x + 0.7
def T_model76m10(t):
    x = t - 2000
    return 0.00034 * x**2 + 0.0238 * x + 0.7
def T_model76(t):
    x = t - 2000
    return 0.00034 * x**2 + 0.0238 * x + 0.7

https://chat.deepseek.com/a/chat/s/d9a11bdb-f2ce-4c34-b14e-492b673e0a4e

def T_model76(t):
    """
    Alternative formulation using polynomial coefficients directly
    (same as above but without solving the system each time)
    """
    # Pre-calculated coefficients (solve once)
    # These were computed by solving the system of equations
    a = 0.00188034188034188
    b = -7.31623931623932
    c = 7130.73076923077
   
    return a * t**2 + b * t + c
homasboettcher@MacBookAir 4_Python_CO2 % /usr/local/bin/python3 /Users/thomasboettcher/Documents/Python/4_Python_CO2/42_CO2_T.py
14.064102564095265   1950
22.604102564096138   2013
25.332307692299764   2023
26.22410256409603    2026
26.837435897428804   2028
print(T_model76(1950) ,"  1950")  # 0.2
print(T_model76(2013) ,"  2013")  # 1.0
print(T_model76(2023) ,"  2023")
print(T_model76(2026) ,"  2026")  # 1.5
print(T_model76(2028) ,"  2028")  # 1.5

correct the formula 
#can you make a quadatic function like the below T_model71(t) in python
# which returns 0.2 for t = 1950
# which returns 1.0 for t = 2013
# which returns 1.5 for t = 2023




https://x.com/rahmstorf/status/2036000186967769338

https://www.jkclimate.fr/InteractiveDashboard2025/dashboard.html

https://library.wmo.int/viewer/69807/download?file=WMO-1391-2025_en.pdf&type=pdf&navigator=1

https://wmo.int/publication-series/state-of-global-climate/state-of-global-climate-2025


https://substack.com/@jimehansen

linear_41_75  = 4 # part 75    Hansen 2015 .41°C linear fit

# yl_mode = 2 ppm CO2 y axis left mode
# yl_mode = 3 Gt CO2 y axis left mode
# yl_mode = 4 EEI in W/m2 y axis left mode
# yl_mode = 5 delta ppm CO2 y axis left mode
# yl_mode = 7 Temperature in °C y axis left mode

which python command makes the scaling on the right y axis?
(note: I have 3 scalings on the right y axis)
https://chat.deepseek.com/a/chat/s/d9a11bdb-f2ce-4c34-b14e-492b673e0a4e

1. Creating Multiple Right Y-Axes (twinx())
python
# Each of these creates a new right y-axis
ax71 = ax1.twinx()  # First right y-axis
ax72 = ax1.twinx()  # Second right y-axis (overlays on right)
ax73 = ax1.twinx()  # Third right y-axis (overlays on right)
2. Positioning Multiple Right Y-Axes
python
# To avoid overlapping, you can offset them:
ax71.spines.right.set_position(("outward", 0))    # Default position
ax72.spines.right.set_position(("outward", 60))   # Offset outward by 60 points
ax73.spines.right.set_position(("outward", 120))  # Offset outward by 120 points

3. Setting Y-Axis Limits (Scaling)
python
# Set the min/max values for each right y-axis
ax71.set_ylim(y_Tmin, y_Tmax)  # e.g., 0 to 2.5°C
ax72.set_ylim(y_Tmin, y_Tmax)  # e.g., 0 to 2.5°C
ax73.set_ylim(y_Tmin, y_Tmax)  # e.g., 0 to 2.5°C

4. Setting Tick Locations (Scale Intervals)
python
# Control the major and minor tick spacing
ax71.yaxis.set_major_locator(MultipleLocator(0.5))  # Major ticks every 0.5°C
ax71.yaxis.set_minor_locator(MultipleLocator(0.1))  # Minor ticks every 0.1°C

ax72.yaxis.set_major_locator(MultipleLocator(0.5))
ax72.yaxis.set_minor_locator(MultipleLocator(0.1))

ax73.yaxis.set_major_locator(MultipleLocator(0.5))
ax73.yaxis.set_minor_locator(MultipleLocator(0.1))

5. Setting Tick Label Size
python
ax71.tick_params(axis="y", labelsize=20)
ax72.tick_params(axis="y", labelsize=20)
ax73.tick_params(axis="y", labelsize=20)

6. Setting Y-Axis Labels
python
ax71.set_ylabel("Δ Temperature in °C 71", color="red", fontsize=20)
ax72.set_ylabel("Δ Temperature calc72 in °C", color="red", fontsize=20)
ax73.set_ylabel("Δ Temperature in °C (ECS = 4.5°C)", color="red", fontsize=20)

7. Controlling Which Axis is Visible
python
# Hide the spine of some axes to avoid clutter
ax72.spines["right"].set_visible(False)
ax72.tick_params(right=False, labelright=False)
# Or only show labels on the outermost axis
ax73.tick_params(axis="y", labelcolor="red", labelsize=20)

Complete Example from Your Code
In your script, the right y-axes are configured in section 8.7:

python
# 8.7 print the right y axis
if yr_mode == 7:  # Temperature mode
    ax74.tick_params(axis="y", labelcolor=c74)
    ax74.set_ylim(y_Tmin, y_Tmax)
    ax74.yaxis.set_major_locator(MultipleLocator(y_Tmayor_ticks))
    ax74.yaxis.set_minor_locator(MultipleLocator(y_Tminor_ticks))
    
elif plot71_temperature > 0:
    ax71.set_ylim(y_Tmin, y_Tmax)
    ax71.yaxis.set_major_locator(MultipleLocator(y_Tmayor_ticks))
    ax71.yaxis.set_minor_locator(MultipleLocator(y_Tminor_ticks))
    
elif plot72_AESS_T > 0:
    ax72.set_ylim(y_Tmin, y_Tmax)
    ax72.yaxis.set_major_locator(MultipleLocator(y_Tmayor_ticks))
    ax72.yaxis.set_minor_locator(MultipleLocator(y_Tminor_ticks))
Key Points for Multiple Right Y-Axes:
Each ax.twinx() creates a new independent y-axis

Use spines.right.set_position() to offset them horizontally

Set ylim() independently for each axis

Use set_major_locator() and set_minor_locator() to control tick spacing

Hide unnecessary axes with set_visible(False) to avoid clutter

The scaling commands that directly control the y-axis range are:

set_ylim(y_min, y_max) - Sets the min/max values

set_major_locator() - Sets the major tick spacing

set_minor_locator() - Sets the minor tick spacing

tick_params() - Controls tick appearance and size

------------ 42t3 ------------- delete y axis left -----------
part41_ceres_eei = 3 # 3,5,12,47,48,50 convert txt to csv runnig 12 month avg , 48 convert txt to csv runnig 48 month avg
part42_ceres_eei = 4 
plot74_GIS_T  = 2 #
linear_41_75  = 3 # part 75    Hansen 2015 .41°C linear fit

------------ 42t4 ------------- run with part41_ceres_eei = 50 -----------


part 4.1.1 Successfully converted 311 records to csv/csv41/csv41b_ceres.csv
Data range: 2000-03-01 00:00:00 to 2026-01-01 00:00:00
Decimal year range: 2000.2083 to 2026.0417
Flux range: -10.49 to 10.67 W/m²

4.1.1 First 3 rows of the converted data:
        date  year  month  toa_net_flux_w_m2  decimal_year
0 2000-03-01  2000      3               5.96   2000.208333
1 2000-04-01  2000      4               1.93   2000.291667
2 2000-05-01  2000      5              -5.93   2000.375000
4.1.9
============================================================
48-MONTH RUNNING AVERAGE
============================================================
Window: 48 months (4 years)
Centered: False
Min periods: 30
Output file: csv/csv41/csv41d50_ceres.csv
Valid records: 282 out of 311

First 5 valid values:
  2002-08: -0.471 W/m²
  2002-09: -0.493 W/m²
  2002-10: -0.397 W/m²
  2002-11: -0.278 W/m²
  2002-12: -0.092 W/m²

4.1.9 Last 5 valid values:
  2025-09: 1.386 W/m²
  2025-10: 1.380 W/m²
  2025-11: 1.373 W/m²
  2025-12: 1.410 W/m²
  2026-01: 1.421 W/m²
thomasboettcher@MacBookAir 4_Python_CO2 % 

------------ 42t5 ------------- run with part41_ceres_eei = 84 -----------

4.1.9
============================================================
84-MONTH RUNNING AVERAGE
============================================================
Window: 84 months (7 years)
Centered: False
Min periods: 30
Output file: csv/csv41/csv41d84_ceres.csv
Valid records: 282 out of 311

First 5 valid values:
  2002-08: -0.471 W/m²
  2002-09: -0.493 W/m²
  2002-10: -0.397 W/m²
  2002-11: -0.278 W/m²
  2002-12: -0.092 W/m²

4.1.9 Last 5 valid values:
  2025-09: 1.326 W/m²
  2025-10: 1.318 W/m²
  2025-11: 1.312 W/m²
  2025-12: 1.319 W/m²
  2026-01: 1.332 W/m²

-------- v = "42t5" #  part 43 84 month average EEI -----------


if part44_ceres_eei > 13:
    out = f"csv/csv44/csv44d_EEI_{part44_ceres_eei}_month.csv"
    df_with_avg = create_running_average(
        'csv/csv44/csv44b_ceres.csv', 
        out,
        window_months=part44_ceres_eei,
        min_periods=30,
        center=True,
        keep_original=True,
        column_name='EEI'  # This will create a column named 'EEI'
    )
    # if part44_ceres_eei is even the above create_running_average call shall be done
    # if part44_ceres_eei is odd the below create_running_average call shall be done
    df_with_avg = create_running_average(
        'csv/csv44/csv44b_ceres.csv', 
        out,
        window_months=part44_ceres_eei,
        min_periods=30,
        center=False,
        keep_original=True,
        column_name='EEI'  # This will create a column named 'EEI'
    )


delete 41 items 
42 is EEI 12 window_months
43 is EEI 48 months
44 produces csv files and diplays 77 months in line 5
45 new CERS cloud data David Ulrich




File Structure
text
climate_analysis/
├── main.py                 # Main execution and configuration
├── config.py               # Configuration parameters
├── data_processing.py      # Data processing functions (CERES, CO2)
├── plotting.py             # Plotting functions
├── temperature_models.py   # Temperature model functions
├── text_annotations.py     # Text annotations and legends
└── utils.py                # Utility functions
1. config.py - Configuration Parameters
python
# config.py
# Configuration parameters for the climate analysis tool

# Version
v = "42u13"

# Plot configuration flags
plot22_CO2_Mauna_Loa = 0
plot23_Glen_CO2 = 0
plot25_long_CO2 = 0
plot34_CO2_emission = 0
part41_ceres_eei = 3
part42_ceres_eei = 4
part43_ceres_eei = 0
part44_ceres_eei = 11
plot52_delta_CO2_red_bars = 0
plot53_CO2_orange2025 = 0
plot54_Glen_delta_on = 0
plot55_population_on = 0
plot71_temperature = 0
plot72_AESS_T = 0
plot73_ECS_T = 0
plot74_GIS_T = 2
linear_41_75 = 3
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
c74 = "red"
c75 = "#371EA484"
c76 = "red"
c71 = "red"

# Axis ranges
y_min = 250
y_max = 500
y_Tmin = 0
y_Tmax = 2.5
y_Emin = 0
y_Emax = 2
x_anf = 2000
x_end = 2026
C280 = 280

# Axis modes
yl_mode = 4  # EEI in W/m2 y axis left mode
yr_mode = 7  # Temperature in °C y axis right mode

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
scale_mode = 10
2. 


Ordner 4_Python_CO2 Alt
5_CO2_EEI_T


