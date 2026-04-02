# plotting.py
# version 5b56
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
from mpl_toolkits.axes_grid1 import make_axes_locatable
import matplotlib.pyplot as plt

# Import modules
from config import *
from data_processing import *
from data_processing import *
from text_annotations import *


from config import y_TOAmin
from config import y_TOAmax
from config import play_61_CERES
from config import play_62_CERES
from config import plot34_CO2_emission # = 2  # 34.1

print("plotting: TOA", y_TOAmin, y_TOAmax, plot34_CO2_emission, play_61_CERES)


color_left = "blue" # color of left y axis

def setup_figure(scale_mode=10):
    """Setup the figure with appropriate size"""
    #if scale_mode == 7:
    #    fig, ax1 = plt.subplots(figsize=(13, 7))
    #elif scale_mode == 8:
    #    fig, ax1 = plt.subplots(figsize=(13, 8))
    #elif scale_mode == 10:
    fig, ax1 = plt.subplots(figsize=(13, 10))
    #else:
    #    fig, ax1 = plt.subplots(figsize=(13, 7))
    
    fig.subplots_adjust(bottom=0.30)
    return fig, ax1

def configure_axes(ax1, x_anf, x_end, y_min, y_max, y_Emin, y_Emax, 
                   y_Tmin, y_Tmax, yl_mode, c22, c42, c74):
    """Configure the axes based on selected mode"""
    plt.xlim(x_anf, x_end)
    ax1.grid(True)
    
    # 8.5 configure the left y axis legend 
    if yl_mode == 4:  # EEI mode
        c4l = "blue" # color of left yaxis for yl_mode == 4 EEI mode
        ax1.set_ylim(y_Emin, y_Emax)
        ax1.set_ylabel("Earth Energy Imbalance in W/m²", color=color_left, fontsize=20)
        ax1.tick_params(axis="y", labelcolor=color_left, labelsize=20)
        
        # Set EEI tick spacing       
        if (y_Emax - y_Emin) < 1:
            y_Emayor_ticks = 0.2 
            y_Eminor_ticks = 0.1
        elif (y_Emax - y_Emin) < 2.1:
            y_Emayor_ticks = 0.5 
            y_Eminor_ticks = 0.1
        elif (y_Emax - y_Emin) < 21:
            y_Emayor_ticks = 5 
            y_Eminor_ticks = 1
        else:
            y_Emayor_ticks = 100 
            y_Eminor_ticks = 20
        ax1.yaxis.set_major_locator(MultipleLocator(y_Emayor_ticks))
        ax1.yaxis.set_minor_locator(MultipleLocator(y_Eminor_ticks))
    # yl_mode = 6 # TOA energy in W/m2 y axis left mode
    elif yl_mode == 6:  # TOA energy in W/m2 y axis left mode
        c6l = "green" # color of left yaxis for TOA energy in W/m2 y axis left mode
        #y_TOAmin = 99.15   # bug the global config.py line 101 does not work
        #y_TOAmax = 99.3  # bug the global config.py line 102 does not work
        ax1.set_ylim(y_TOAmin, y_TOAmax)
        ax1.set_ylabel("TOA Energy in W/m²", color=color_left, fontsize=20)
        ax1.tick_params(axis="y", labelcolor=color_left, labelsize=20)
        # Set EEI tick spacing   y_TOAmin    
        if (y_TOAmax - y_TOAmin) < 0.2:
            y_TEmayor_ticks = 0.02
            y_TEminor_ticks = 0.01
        elif (y_TOAmax - y_TOAmin) < 0.5:
            y_TEmayor_ticks = 0.1 
            y_TEminor_ticks = 0.02
        elif (y_TOAmax - y_TOAmin) < 1.1:
            y_TEmayor_ticks = 0.1 
            y_TEminor_ticks = 0.02
        elif (y_TOAmax - y_TOAmin) < 2:
            y_TEmayor_ticks = 2 
            y_TEminor_ticks = 0.2
        elif (y_TOAmax - y_TOAmin) < 5:
            y_TEmayor_ticks = 1 
            y_TEminor_ticks = 0.1
        elif (y_TOAmax - y_TOAmin) < 10:
            y_TEmayor_ticks = 2 
            y_TEminor_ticks = 0.4
        elif (y_TOAmax - y_TOAmin) < 30:
            y_TEmayor_ticks = 2 
            y_TEminor_ticks = 1
        else:
            y_TEmayor_ticks = 100 
            y_TEminor_ticks = 20
        ax1.yaxis.set_major_locator(MultipleLocator(y_TEmayor_ticks))
        ax1.yaxis.set_minor_locator(MultipleLocator(y_TEminor_ticks))
    elif yl_mode == 7:  # Temperature mode
        ax1.set_ylim(y_Tmin, y_Tmax)
        ax1.set_ylabel("Temperature in °C", color=c74, fontsize=20)
        ax1.tick_params(axis="y", labelcolor=c74, labelsize=20)
        
        # Set temperature tick spacing
        y_Tmayor_ticks = 0.5 if (y_Tmax - y_Tmin) > 2 else 0.2
        y_Tminor_ticks = 0.1
        ax1.yaxis.set_major_locator(MultipleLocator(y_Tmayor_ticks))
        ax1.yaxis.set_minor_locator(MultipleLocator(y_Tminor_ticks))
        
    else:  # CO2 mode (default)
        ax1.set_ylim(y_min, y_max)
        ax1.set_ylabel("CO₂ in ppm", color=c22, fontsize=20)
        ax1.tick_params(axis="y", labelcolor=c22, labelsize=20)
        
        # Set CO2 tick spacing
        y_mayor_ticks = 50 if (y_max - y_min) > 200 else 20
        y_minor_ticks = 10
        ax1.yaxis.set_major_locator(MultipleLocator(y_mayor_ticks))
        ax1.yaxis.set_minor_locator(MultipleLocator(y_minor_ticks))
    
    return ax1

def configure_right_y_axis(ax, y_Tmin, y_Tmax, color, label):
    """Configure a right y-axis for temperature"""
    ax.tick_params(axis="y", labelcolor=color, labelsize=20)
    ax.set_ylim(y_Tmin, y_Tmax)
    ax.yaxis.set_major_locator(MultipleLocator(0.5))
    ax.yaxis.set_minor_locator(MultipleLocator(0.1))
    ax.set_ylabel(label, color=color, fontsize=20, labelpad=10)
    return ax

def right_T_y_axis(ax, y_Tmin, y_Tmax, color, label):
    """Configure the first right y-axis for temperature"""
    ax2 = ax.twinx()
    ax2.tick_params(axis='y', labelcolor='r')
    ax2.tick_params(axis="y", labelcolor=color, labelsize=20)
    ax2.set_ylim(y_Tmin, y_Tmax)
    ax2.yaxis.set_major_locator(MultipleLocator(0.5))
    ax2.yaxis.set_minor_locator(MultipleLocator(0.1))
    ax2.set_ylabel(label, color=color, fontsize=20, labelpad=10)
    return ax2

# bug ax6 = right_EEI_y_axis(ax1, y_Emin, y_Emax, c74, label)
def right_EEI_y_axis(ax, y_Emin, y_Emax, color, label):
    """Configure the first right y-axis for temperature"""
    ax2 = ax.twinx()

    # Create a third y-axis offset by 60 points to the right
    divider = make_axes_locatable(ax2)
    # Create new axis with offset (60 points = 60/72 inches if using points)
    ax3 = divider.append_axes("right", size="5%", pad=0.6)  # pad is in inches, 0.6 inches ≈ 43 points
    # For exact 60 points: 60/72 = 0.8333 inches
    ax3 = divider.append_axes("right", size="5%", pad=0.8333)

    # Or use points directly
    ax3 = divider.append_axes("right", size="5%", pad=60/72)  # 60 points in inches
    return ax3
    # bug ax6 = right_EEI_y_axis(ax1, y_Emin, y_Emax, c74, label)



def add_grid_lines(ax1):
    # mayor grid lines vertical lines inside the plot to better read the y value
    for line in ax1.get_ygridlines():
        # line.set_color('green')  # major lines
        line.set_color('blue')
        line.set_alpha(0.5)
        line.set_linestyle('-')
        line.set_linewidth(1.1)
    
    ax1.grid(True, which="minor", axis="y", color="lightblue", alpha=0.94)

#def add_temperature_band(ax48, y_min=1.5, y_max=1.8):
#    ax48.axhspan(y_min, y_max, color="#B3D9FF", alpha=0.5, zorder=0)
def add_temperature_band(ax, y_min=1.5, y_max=2.0):
    """Add temperature band to the plot (for temperature axes only)"""
    # Only add if this is a temperature axis (not EEI axis)
    if hasattr(ax, 'get_ylabel'):
        ylabel = ax.get_ylabel()
        if 'Temperature' in ylabel or '°C' in ylabel:
            ax.axhspan(y_min, y_max, color="#B3D9FF", alpha=0.5, zorder=0)

def add_vertical_bands(ax1, C280):
    """Add vertical bands for CO2 levels"""
    ax1.axhspan(4 * C280 - 2, 4 * C280 + 2, color="#4554A8C6", alpha=0.25, zorder=0)
    ax1.axhspan(2 * C280 - 2, 2 * C280 + 2, color="#4554A8C6", alpha=0.3, zorder=0)

def add_year_band(ax1, year_start=2025, year_end=2027):
    """Add vertical band for current year"""
    ax1.axvspan(year_start, year_end, color="#B3D9FF", alpha=0.5, zorder=0)

def create_plots(ax1, data):
    """Create all plots based on configuration"""
    
    # Plot plot22_CO2_Mauna_Loa
    if plot22_CO2_Mauna_Loa > 0: # 22.4 create the plot  ax22.set_ylim(y_min, y_max)
        if print_debug > 9:
          print(f"plot_200: plot22_CO2_Mauna_Loa 22.4 ={plot22_CO2_Mauna_Loa}")
          print(f"plot_201: Last 3 CO2 rows: {data['co2'][-3:] if len(data['co2']) >= 3 else data['co2']}")
        ax22 = ax1.twinx()
        ax22.plot(data['co2']["year"], data['co2']["co2_ppm"], '-', 
                  label="T GIS K22", color=c22, linewidth=3)
        ax22.tick_params(axis="y", labelcolor=c22)
        ax22.set_ylim(y_min, y_max)
    # -----------------------------
    # 2.3 plot23_Glen_CO2 = 0.013t² - 51t + 49,536 in dark blue 
    # source a plot with the formula explained in a thread
    # source https://x.com/Gergyl/status/1810632238230589564
    # -----------------------------
    text_plot23_Glen="calculated CO2 dashed blue line = 0.0132251t² - 51.0337t + 49,536 ppm 23"
    # CO₂ function CO2 = 0.013t² - 51t + 49,536
    def co3_ppm(t): # 23.2
        """Glen CO2 model"""
        return 0.0132251 * t**2 - 51.0337 * t + 49536.7

    # 2.3.2 years as x values 1960 to 3000
    if plot23_Glen_CO2 > 0: # 23.4 create the plot  ax22.set_ylim(y_min, y_max)
       years23 = np.arange(x_anf, x_end +1 )
       co23_values = co3_ppm(years23)
       # 2.3.3. Create DataFrame for convenience
       df23 = pd.DataFrame({
          "Year3": years23,
          "Modeled3": co23_values
           })

       # 2.3.7
       ax23 = ax1.twinx()
       ax23.spines.right.set_position(("outward", 90))
       ax23.spines["right"].set_visible(False) # remove right y-Achse
       ax23.tick_params(right=False, labelright=False) # remove Zahlen
       # 2.3.8
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
    if plot25_long_CO2 > 0: # 25.2 plot
      df25 = pd.read_csv("read_csv/csv_25_ppm_long.csv") # our world in data file
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
    plot34_CO2_emission  = 43  # 34.9
    print("plot_272: plot34_CO2_emission bug set = ", plot34_CO2_emission) # 34.7

    if plot34_CO2_emission > 0: # 34.2
        ax34 = ax1.twinx()
        print34_text ="purple dots: cumulative CO2 emissions Carbon Brief 34 mode "
        # plot34_CO2_emission_mode = 1, read self made csv 2000 GtCO2
        # plot34_CO2_emission_mode = 2, read csv 2000 000 000 000 tCO2
        # plot34_CO2_emission_mode = 3, read csv 2000 GtCO2 csv_read/csv_34a3_cumulative-co-emissions.csv 1750 to 2024
        # plot34_CO2_emission_mode = 4, read csv 2000 GtCO2
        # plot34_CO2_emission_mode = 5
        #first_digit = int(str(plot34_CO2_emission)[0]) # print in row
        #second_digit = int(str(plot34_CO2_emission)[1])
        #plot34_CO2_emission = first_digit
        #plot34_CO2_emission_mode = second_digit
        #print34_text = print34_text + str(plot34_CO2_emission_mode)
        # 3.4.mode 1 
        if plot34_CO2_emission_mode == 1:
           df34a = pd.read_csv("read_csv/csv_34a1_co2_world_generated.csv") # processed file
        elif plot34_CO2_emission_mode == 2:   # 3.4.mode 2
           df34b = pd.read_csv("read_csv/csv_34a2_co2_sum.csv") # our world in data file
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
           df34b = pd.read_csv("read_csv/csv_34a3_cumulative-co-emissions.csv") # our world in data file
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
        ax34 = ax1.twinx()
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
        #end 3.4




    # Plot CERES data
    if part41_ceres_eei > 0 and 'ceres_12' in data:
        ax41 = ax1.twinx()
        ax41.plot(data['ceres_12']["year41"], data['ceres_12']["EEI"], '-', 
                  label="EEI K41", color=c41, linewidth=2)
        ax41.tick_params(axis="y", labelcolor=c41)
        ax41.set_ylim(y_Emin, y_Emax)
    
    if part42_ceres_eei > 0 and 'ceres_48' in data:
        ax42 = ax1.twinx()
        ax42.plot(data['ceres_48']["year41"], data['ceres_48']["EEI"], '-', 
                  label="EEI K42", color=c42, linewidth=2)
        ax42.tick_params(axis="y", labelcolor=c42)
        ax42.set_ylim(y_Emin, y_Emax)
    

    if part43_ceres_eei > 0 and 'ceres_43' in data:
        ax43 = ax1.twinx()
        ax43.plot(data['ceres_43']["decimal_year"], data['ceres_43']["EEI"], '-', 
                  label="EEI K41", color=c43, linewidth=2)
        ax43.tick_params(axis="y", labelcolor=c43)
        ax43.set_ylim(y_Emin, y_Emax)
        if print_debug > 19:
           print(f"plot_231: ax43 43.4 ={part43_ceres_eei}")
 
    if part44_ceres_eei > 0 and 'ceres_custom' in data:
        if print_debug > 19:
           print(f"plot_235: ax44 44.7 ={part44_ceres_eei}")

        ax44 = ax1.twinx()
        ax44.plot(data['ceres_custom']["decimal_year"], data['ceres_custom']["EEI"], '-', 
                  label="EEI K44", color=c44, linewidth=2)
        ax44.tick_params(axis="y", labelcolor=c44)
        ax44.set_ylim(y_Emin, y_Emax)
    
    if play_61_CERES > 0 and 'ceres_61' in data:
        ax61 = ax1.twinx()
        ax61.plot(data['ceres_61']["decimal_year"], data['ceres_61']["EEI"], '-', 
                  label="EEI K61", color=c61, linewidth=2)
        ax61.tick_params(axis="y", labelcolor=c61)
        ax61.set_ylim(y_Emin, y_Emax)
        if print_debug > 9:
           print(f"plot_250: ax61 43.8 ={play_61_CERES}")
    if play_62_CERES > 0 and 'ceres_62' in data:
        ax62 = ax1.twinx()
        ax62.plot(data['ceres_62']["decimal_year"], data['ceres_62']["EEI"], '-', 
                  label="EEI K62", color=c62, linewidth=2)
        ax62.tick_params(axis="y", labelcolor=c62)
        ax62.set_ylim(y_TOAmin, y_TOAmax)
        if print_debug > 9:
           print(f"plot_258: ax62 62.8 ={play_62_CERES}")

    # Plot GIS temperature
    if plot74_GIS_T > 0 and 'gis_temp' in data: # 74.4
        ax74 = ax1.twinx()
        ax74.plot(data['gis_temp']["Year74"], data['gis_temp']["GIS_temp"]+0.3, '-', 
                  label="T GIS K74", color=c74, linewidth=3)
        ax74.tick_params(axis="y", labelcolor=c74)
        ax74.set_ylim(y_Tmin, y_Tmax)
    # end create_plots(ax1, data):


