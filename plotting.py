# plotting.py
# version 5c99
# plot_1_axe ,  for: 22  plot22_CO2_Mauna_Loa = 2                             ,  line  121
# plot_5_left_y_axe(ax1, x_anf, x_end, y_min, y_max  line 115
# plot_6_remove_axe1(axes,yr6_delete): line 365
# plot8_right_y_axe_for_ppm_22  plot22_CO2_Mauna_Loa                         ,   line  374
# plot8_right_y_axe_for_C_31 ,  plot31_CO2_emission , cumulative CO2 emissions , line  402
# plot8_right_y_axe_for_eei_42  plot42_EEI_48month   Earth Energy Imbalance     ,  line  450
# plot8_right_y_axe_for_eei_43  plot43_eei_12month   Earth Energy Imbalance     ,  line  460
# plot8_right_y_axe_for_delta_ppm_increase_52      plot52_delta_CO2_red_bars  ,  line  397
# plot8_160_right_y_axe_55                         plot55_population_on       ,  line  412
# plot8_right_y_axe_for_T_71 ,  plot71_temperature                            ,  line  525
# plot8_right_y_axe_for_T_74 ,     plot74_GIS_T  ,   GISS Temperature         ,  line  501
# plot8_right_y_axe_for_T_75 ,     linear_41_75  ,   Hansen 0.41°C            ,  line  581
# plot8_right_y_axe_for_T_77 ,     plot_T_77    ,   my quadratic              ,  line  604
# plot_9_create_all_plots(ax1, data): line 400 600
# plot25_long_CO2,  NOAA 800_000 year ice data,      plot_9_create_all_plots() ,  line 447
# plot31_CO2_emission summed  co2_cumul.csv   Entity,Code,Year,Cumula           , line 603
# plot42_EEI_48month, running average over 48 months,  plot_9_create_all_plots() ,  line 601
# plot52_delta_CO2_red_bars,   Mauna Loa delta    ,  plot_9_create_all_plots() ,  line 630
# plot74_GIS_T,  GIS temperature add 0.3°C Hansen ,  plot_9_create_all_plots() ,  line 750

import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
from mpl_toolkits.axes_grid1 import make_axes_locatable
import matplotlib.pyplot as plt

# Import modules
from config import *
from data_processing import *
from data_processing import *
from text import *
from config import play_62_CERES
from config import plot34_CO2_emission

if print_debug > 12:
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



def configure_right_y_axis(ax, y_Tmin, y_Tmax, color, label):
    """Configure a right y-axis for temperature"""

    ax.tick_params(axis="y", labelcolor=color, labelsize=20)
    ax.set_ylim(y_Tmin, y_Tmax)
    ax.yaxis.set_major_locator(MultipleLocator(0.5))
    ax.yaxis.set_minor_locator(MultipleLocator(0.1))
    ax.set_ylabel(label, color=color, fontsize=20, labelpad=10)
    print("plot_ 50: right axis ",label, "-")
    return ax
    # end 




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
            ax.axhspan(y_min, y_max, color="#B3D9FF87", alpha=0.2, zorder=0)

def add_vertical_bands(ax1, C280):
    """Add vertical bands for CO2 levels"""
    ax1.axhspan(4 * C280 - 2, 4 * C280 + 2, color="#4554A8C6", alpha=0.25, zorder=0)
    ax1.axhspan(2 * C280 - 2, 2 * C280 + 2, color="#4554A8C6", alpha=0.3, zorder=0)

def add_year_band(ax1, year_start=2025, year_end=2027):
    """Add vertical band for current year"""
    ax1.axvspan(year_start, year_end, color="#B3D9FF", alpha=0.5, zorder=0)


# plot_1_axe ,  for: 22  plot22_CO2_Mauna_Loa = 2                             ,  line  121
def plot_1_axe(ax1):
    """Configure the axes based on selected mode"""
    plt.xlim(x_anf, x_end)
    ax1.grid(True)

    if plot22_CO2_Mauna_Loa == 2:  # 22.5 y axe left 
        ax1.set_ylim(y_min, y_max)
        ax1.set_ylabel("Mauna Loa CO₂ in ppm  (plot128) ", color=c22, fontsize=20)
        ax1.tick_params(axis="y", labelcolor=c22, labelsize=20)
        y_mayor_ticks = 50 if (y_max - y_min) > 200 else 20
        y_minor_ticks = 10
        ax1.yaxis.set_major_locator(MultipleLocator(y_mayor_ticks))
        ax1.yaxis.set_minor_locator(MultipleLocator(y_minor_ticks))
    elif plot23_Glen_CO2 == 2:  # 23.5 y axe left 
        # ax42.spines.right.set_position(("outward", outward_right))
        ax1.spines.left.set_position(("outward", 10))
        ax1.set_ylim(y_min, y_max)
        ax1.set_ylabel(" CO₂ in ppm  (plot137) ", color=c22, fontsize=20)
        ax1.tick_params(axis="y", labelcolor=c23, labelsize=20)
        y_mayor_ticks = 50 if (y_max - y_min) > 200 else 20
        y_minor_ticks = 10
        ax1.yaxis.set_major_locator(MultipleLocator(y_mayor_ticks))
        ax1.yaxis.set_minor_locator(MultipleLocator(y_minor_ticks))
    elif plot25_long_CO2 == 2:  # 23.5 y axe left 
        # ax42.spines.right.set_position(("outward", outward_right))
        ax1.spines.left.set_position(("outward", 3))
        ax1.set_ylim(y_min, y_max)
        ax1.set_ylabel(" CO₂ in ppm  (plot149) ", color=c25, fontsize=20)
        ax1.tick_params(axis="y", labelcolor=c25, labelsize=20)
        y_mayor_ticks = 50 if (y_max - y_min) > 200 else 20
        y_minor_ticks = 10
        ax1.yaxis.set_major_locator(MultipleLocator(y_mayor_ticks))
        ax1.yaxis.set_minor_locator(MultipleLocator(y_minor_ticks))
    elif plot31_CO2_emission == 2:  # 31.5 y axe left 
        # ax42.spines.right.set_position(("outward", outward_right))
        ax1.spines.left.set_position(("outward", 0))
        ax1.set_ylim(y_31Gmin, y_31Gmax)
        ax1.set_ylabel("cumulative CO₂ emission in GtCO₂ ", color=c31, fontsize=20)
        ax1.tick_params(axis="y", labelcolor=c31, labelsize=20)
        y_mayor_ticks = 500 
        y_minor_ticks = 100
        ax1.yaxis.set_major_locator(MultipleLocator(y_mayor_ticks))
        ax1.yaxis.set_minor_locator(MultipleLocator(y_minor_ticks))
    elif plot32_CO2_emission == 2:  # 32.5 y axe left 
        # ax42.spines.right.set_position(("outward", outward_right))
        ax1.spines.left.set_position(("outward", 0))
        ax1.set_ylim(y_32min, y_32max)
        ax1.set_ylabel("cumulative CO₂ emissions in GtC    ", color=c32, fontsize=20)
        ax1.tick_params(axis="y", labelcolor=c32, labelsize=20)
        y_mayor_ticks = 100 
        y_minor_ticks = 50
        ax1.yaxis.set_major_locator(MultipleLocator(y_mayor_ticks))
        ax1.yaxis.set_minor_locator(MultipleLocator(y_minor_ticks))
    elif plot42_EEI_48month == 2:  # 43.5 y axe left 
        # ax42.spines.right.set_position(("outward", outward_right))
        ax1.spines.left.set_position(("outward", 0))
        ax1.set_ylim(y_Emin, y_Emax)
        ax1.set_ylabel("Earth Energy Imbalance EEI in W/m² (plot180)  ", color=c42, fontsize=20)
        ax1.tick_params(axis="y", labelcolor=c42, labelsize=20)
        y_mayor_ticks = 0.500 
        y_minor_ticks = 0.100
        if (y_Emax - y_Emin) > 5:
           y_mayor_ticks = 5
           y_minor_ticks = 1
        ax1.yaxis.set_major_locator(MultipleLocator(y_mayor_ticks))
        ax1.yaxis.set_minor_locator(MultipleLocator(y_minor_ticks))

    elif plot43_eei_12month == 2:  # 43.5 y axe left 
        # ax42.spines.right.set_position(("outward", outward_right))
        ax1.spines.left.set_position(("outward", 3))
        ax1.set_ylim(y_Emin, y_Emax)
        ax1.set_ylabel("Earth energy Imbalance EEI in W (plot168)  ", color=c43, fontsize=20)
        ax1.tick_params(axis="y", labelcolor=c43, labelsize=20)
        y_mayor_ticks = 0.500 
        y_minor_ticks = 0.100
        ax1.yaxis.set_major_locator(MultipleLocator(y_mayor_ticks))
        ax1.yaxis.set_minor_locator(MultipleLocator(y_minor_ticks))
    elif plot71_temperature == 2:  # 71.5 y axe left  red quadratic Temperature = 0.000618t² - 2.459 t + 2446.0579 in °C 71
        # ax42.spines.right.set_position(("outward", outward_right))
        ax1.spines.left.set_position(("outward", 3))
        ax1.set_ylim(y_Tmin, y_Tmax)
        ax1.set_ylabel("quadratic Temperature in °C      71  (plot178)  ", color=c71, fontsize=20)
        ax1.tick_params(axis="y", labelcolor=c71, labelsize=20)
        y_mayor_ticks = 0.500 
        y_minor_ticks = 0.100
        ax1.yaxis.set_major_locator(MultipleLocator(y_mayor_ticks))
        ax1.yaxis.set_minor_locator(MultipleLocator(y_minor_ticks))
    elif plot72_AESS_T == 2:  # 72.5 y axe left  red quadratic Temperature = 0.000618t² - 2.459 t + 2446.0579 in °C 71
        # ax42.spines.right.set_position(("outward", outward_right))
        ax1.spines.left.set_position(("outward", 3))
        ax1.set_ylim(y_Tmin, y_Tmax)
        ax1.set_ylabel(" Temperature in °C      72  (plot188)  ", color=c72, fontsize=20)
        ax1.tick_params(axis="y", labelcolor=c72, labelsize=20)
        y_mayor_ticks = 1 
        y_minor_ticks = 0.5
        ax1.yaxis.set_major_locator(MultipleLocator(y_mayor_ticks))
        ax1.yaxis.set_minor_locator(MultipleLocator(y_minor_ticks))
    elif plot73_ECS_T == 2:  # 73.5 y axe left  red 
        # a
        ax1.spines.left.set_position(("outward", 3))
        ax1.set_ylim(y_Tmin, y_Tmax)
        ax1.set_ylabel(" Temperature in °C      73  (plot200)  ", color=c73, fontsize=20)
        ax1.tick_params(axis="y", labelcolor=c73, labelsize=20)
        y_mayor_ticks = 1 
        y_minor_ticks = 0.5
        ax1.yaxis.set_major_locator(MultipleLocator(y_mayor_ticks))
        ax1.yaxis.set_minor_locator(MultipleLocator(y_minor_ticks))
    elif plot74_GIS_T == 2:  # 74.5 y axe left  red 
        # a Temperature in °C giss.nasa.gov Hansen+0.3°C 74 
        ax1.spines.left.set_position(("outward", 0))
        ax1.set_ylim(y_Tmin, y_Tmax)
        ax1.set_ylabel(" Temperature in °C  giss  74  ", color=c74, fontsize=20)
        ax1.tick_params(axis="y", labelcolor=c74, labelsize=20)
        y_mayor_ticks = 0.5 
        y_minor_ticks = 0.1
        ax1.yaxis.set_major_locator(MultipleLocator(y_mayor_ticks))
        ax1.yaxis.set_minor_locator(MultipleLocator(y_minor_ticks))
    elif plot76_my_T == 2:  # 76.5 y axe left  red 
        # my76_text="guessed quadratic temperature  my_T   76 "
        ax1.spines.left.set_position(("outward", 3))
        ax1.set_ylim(y_Tmin, y_Tmax)
        ax1.set_ylabel(" Temperature in °C  myguess  76  ", color=c76, fontsize=20)
        ax1.tick_params(axis="y", labelcolor=c76, labelsize=20)
        y_mayor_ticks = 0.5 
        y_minor_ticks = 0.1
        ax1.yaxis.set_major_locator(MultipleLocator(y_mayor_ticks))
        ax1.yaxis.set_minor_locator(MultipleLocator(y_minor_ticks))



    else:    
        ax1.set_ylim(y_min, y_max)
        ax1.set_ylabel(" else generic y axe CO₂ in ppm  (plot146) ", color=c22, fontsize=20)
        ax1.tick_params(axis="y", labelcolor=c23, labelsize=20)
        y_mayor_ticks = 50 if (y_max - y_min) > 200 else 20
        y_minor_ticks = 10
        ax1.yaxis.set_major_locator(MultipleLocator(y_mayor_ticks))
        ax1.yaxis.set_minor_locator(MultipleLocator(y_minor_ticks))


    

    return ax1 
    # end plot_1_axe




# plot_5_left_y_axe(ax1, x_anf, x_end, y_min, y_max  line 115
def plot_5_left_y_axe(ax1, x_anf, x_end, y_min, y_max, y_Emin, y_Emax, 
                   y_Tmin, y_Tmax, print_debug, c22, c42, c74):
    """Configure the axes based on selected mode"""
    plt.xlim(x_anf, x_end)
    ax1.grid(True)
    
    # 8.5 configure the left y axis legend 
    #if print_debug == 10:  # EEI mode
      

    if print_debug == 4:  # 
        c4l = "blue" # color of left yaxis for print_debug == 4 EEI mode
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
    # print_debug = 6 # TOA energy in W/m2 y axis left mode
    elif print_debug == 6:  # TOA energy in W/m2 y axis left mode
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
    elif print_debug == 7:  # Temperature mode
        ax1.set_ylim(y_Tmin, y_Tmax)
        ax1.set_ylabel("Temperature in °C", color=c74, fontsize=20)
        ax1.tick_params(axis="y", labelcolor=c74, labelsize=20)
        
        # Set temperature tick spacing
        y_Tmayor_ticks = 0.5 if (y_Tmax - y_Tmin) > 2 else 0.2
        y_Tminor_ticks = 0.1
        ax1.yaxis.set_major_locator(MultipleLocator(y_Tmayor_ticks))
        ax1.yaxis.set_minor_locator(MultipleLocator(y_Tminor_ticks))
    elif print_debug == 3:  #  Gt CO2 y axis left mode
        ax1.set_ylim(y_Gmin, y_Gmax)
        ax1.set_ylabel("cummulative CO₂ emissions in Gt  plot 218", color=c22, fontsize=20)
        ax1.tick_params(axis="y", labelcolor=c22, labelsize=20)
        
        # Set CO2 tick spacing
        if (y_Gmax - y_Gmin) < 200:
            y_Gmayor_ticks = 50
            y_Gminor_ticks = 10
        elif (y_Gmax - y_Gmin) < 2002:
            y_Gmayor_ticks = 500
            y_Gminor_ticks = 100
        else:
            y_Gmayor_ticks = 500
            y_Gminor_ticks = 200
        ax1.yaxis.set_major_locator(MultipleLocator(y_Gmayor_ticks))
        ax1.yaxis.set_minor_locator(MultipleLocator(y_Gminor_ticks))
    elif print_debug == 2:  # CO2 mode (default)
        ax1.set_ylim(y_min, y_max)
        ax1.set_ylabel("Mauna Loa CO₂ in ppm  (plot233) ", color=c21, fontsize=20)
        ax1.tick_params(axis="y", labelcolor=c21, labelsize=20)
        
        # Set CO2 tick spacing
        y_mayor_ticks = 50 if (y_max - y_min) > 200 else 20
        y_minor_ticks = 10
        ax1.yaxis.set_major_locator(MultipleLocator(y_mayor_ticks))
        ax1.yaxis.set_minor_locator(MultipleLocator(y_minor_ticks))
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
    # end plot_5_left_y_axe(ax1, x_anf, x_end, y_min, y_max  line 115



# plot_6_remove_axe1(axes,yr6_delete): line 365
def plot_6_remove_axe1(axes,yr6_delete):
    for i, ax in enumerate(plt.gcf().get_axes()):
        ylabel = ax.get_ylabel()
        print(f"plot_369: Axis {i}: yaxis side = {ax.yaxis.get_ticks_position()}, label = '{ylabel}'")
    if yr6_delete == 9:
       print("plot_371: no right y axes in figure")
       for i in range(1, len(axes)): # remove Axis 3, 4
           axes[i].yaxis.set_ticks([])  # Remove tick numbers
           axes[i].set_yticklabels([])  # Remove tick labels
           axes[i].spines['right'].set_visible(False)
           axes[i].set_ylabel('') # Remove any label
        # return
    elif yr6_delete == 1:
       i = yr6_delete
       print("plot_407: remove ", i, len(axes))
       axes[i].yaxis.set_ticks([])  # Remove tick numbers
       axes[i].set_yticklabels([])  # Remove tick labels
       axes[i].spines['right'].set_visible(False)
       axes[i].set_ylabel('') # Remove any label
    elif yr6_delete == 2:
       i = yr6_delete
       print("plot_415: remove ", i, len(axes))
       axes[i].yaxis.set_ticks([])  # Remove tick numbers
       axes[i].set_yticklabels([])  # Remove tick labels
       axes[i].spines['right'].set_visible(False)
       axes[i].set_ylabel('') # Remove any label
    elif yr6_delete == -1:
       print("plot_390: no x axe removed ", i, len(axes)) 

# plot8_right_y_axe_for_ppm_22  plot22_CO2_Mauna_Loa                         ,   line  415
def plot8_right_y_axe_for_ppm_22(ax22,right22): # 22.4 line 375
    if print_debug > 9:
          print(f"plot_452: plot8_right_y_axe_for_ppm_22  22.3 ={plot22_CO2_Mauna_Loa} parameter 2 {right22}")
    if right22 > 0:
        outward_right = right22
    else:
        outward_right =  ( plot22_CO2_Mauna_Loa * yr_60 ) - yr_150
    if print_debug > 9:
          print(f"plot_425: plot8_right_y_axe_for_ppm_22  22.3 ={plot22_CO2_Mauna_Loa} parameter 2 {outward_right}")
    ax22.spines.right.set_position(("outward", outward_right))
    ax22.set_ylabel("CO2_Mauna_Loa in ppm             plot460                  22", color=c22, fontname="Arial",fontsize=16)
    ax22.tick_params(axis="y", labelcolor=c22)
    ax22.set_ylim(y_min, y_max) #8

# plot8_right_y_axe_for_C_31 ,  plot31_CO2_emission , cumulative CO2 emissions , line  402
def plot8_right_y_axe_for_C_31(ax31,right52): # 31.6 
    if right52 > 0:
        outward_right = right52
    else:
        outward_right =  ( plot31_CO2_emission * yr_60 ) - yr_150
    ax31.spines.right.set_position(("outward", outward_right))
    ax31.set_ylabel("cumulative CO2 emissions in Gt  plot410     31", color=c31, fontname="Arial",fontsize=18)
    ax31.tick_params(axis="y", labelcolor=c31)






# Earth Energy Imbalance W/m² moving average 48 month 
# plot8_right_y_axe_for_eei_42  plot42_EEI_48month   Earth Energy Imbalance     ,  line  383
def plot8_right_y_axe_for_eei_42(ax42,rightv): # 42.5
    outward_right =  ( plot42_EEI_48month *  yr_60 ) - yr_150
    ax42.spines.right.set_position(("outward", outward_right))
    #ax42.spines.right.set_position(("outward", 120))
    ax42.set_ylabel("Earth Energy Imbalance  in W/m²     plot470            42", color=c42, fontname="Arial",fontsize=18)
    ax42.tick_params(axis="y", labelcolor=c42)
    ax42.set_ylim(y_Emin, y_Emax) #

# Earth Energy Imbalance W/m² moving average 12 month 
# plot8_right_y_axe_for_eei_43  plot43_eei_12month   Earth Energy Imbalance     ,  line  460
def plot8_right_y_axe_for_eei_43(ax43,rightv): # 43.5
    outward_right =  ( plot43_eei_12month *  yr_60 ) - yr_150
    ax43.spines.right.set_position(("outward", outward_right))
    #ax43.spines.right.set_position(("outward", 120))
    ax43.set_ylabel("Earth Energy Imbalance  in W/m²     plot470            43", color=c43, fontname="Arial",fontsize=18)
    ax43.tick_params(axis="y", labelcolor=c43)
    ax43.set_ylim(y_Emin, y_Emax) #



# plot8_right_y_axe_for_eei_42  plot42_EEI_48month   Earth Energy Imbalance     ,  line  383
# plot8_right_y_axe_for_delta_ppm_increase_52      plot52_delta_CO2_red_bars  ,  line  397
def plot8_right_y_axe_for_delta_ppm_increase_52(ax52, df52,right52): # 52.4
    # growth data is different https://gml.noaa.gov/webdata/ccgg/trends/co2/co2_gr_mlo.txt
    if right52 > 0:
        outward_right = right52
    else:
        outward_right =  ( plot52_delta_CO2_red_bars * yr_60 ) - yr_150
    ax52.spines.right.set_position(("outward", outward_right))
    # ax52.spines.right.set_position(("outward", right55))
    # bars = ax52.bar(df52["x_52_years"], df52["Delta_CO2"], width=0.7, alpha=0.5, color="red")
    ax52.bar(df52["x_52_years"], df52["Delta_CO2"], width=0.6, alpha=0.01, color=c52)
    ax52.set_ylabel("green bars: CO2 increase in ppm   p488      ", color=c52, fontname="Arial",fontsize=18) # fontweight="bold"
    ax52.tick_params(axis="y", labelcolor=c52, labelsize=12)
    ax52.set_ylim(y_52min, y_52max) # scale y axis3 right red   
    # end plot8_right_y_axe_for_delta_ppm_increase_52
  
# plot8_160_right_y_axe_55                         plot55_population_on       ,  line  412
def plot8_160_right_y_axe_55(ax55,pop_world): # 55.4 line 356
    ax55.spines.right.set_position(("outward", 210))
    ax55.plot(pop_world["Year"], pop_world["Population_Mrd"], marker="s", color=c55, label="Earth Population in Billion K2")
    ax55.set_ylabel("Earth Population in Billion  (plot359)   55", color=c55)
    ax55.tick_params(axis="y", labelcolor="green")
    ax55.set_ylim(y_55min, y_55max) #8
    # ax55.set_ylim(4, 9)
    #end plot8_160_right_y_axe_55  

# plot8_right_y_axe_for_C_63(ax63,0) # 63.5 line 460
def plot8_right_y_axe_for_C_63(ax63,right52): # 63.5
     if right52 > 0:
        outward_right = right52
     else:
        outward_right =  ( play_63_CB * yr_60 ) - yr_150
     ax63.spines.right.set_position(("outward", outward_right))
     ax63.set_ylabel("cummulative CO2 values   plot475     63", color=c63, fontname="Arial",fontsize=18)
     ax63.tick_params(axis="y", labelcolor=c63)


# plot8_right_y_axe_for_T_71 ,  plot71_temperature                            ,  line  525
def plot8_right_y_axe_for_T_71(ax71,right52): # 71.6 plot71_temperature
    if right52 > 0:
        outward_right = right52
    else:
        outward_right =  ( plot71_temperature * yr_60 ) - yr_150
    ax71.spines.right.set_position(("outward", outward_right))
    ax71.set_ylabel("Temperature in °C           plot532               71", color=c71, fontname="Arial",fontsize=18)
    ax71.tick_params(axis="y", labelcolor=c71)
    # ax71.set_ylim(y_Tmin, y_Tmax) #8

# plot8_right_y_axe_for_T_74 ,     plot74_GIS_T  ,   GISS Temperature         ,  line  421
def plot8_right_y_axe_for_T_74(ax74,right52): # 74.6 
    # ax74.spines.right.set_position(("outward", rightv))
    if right52 > 0:
        outward_right = right52
    else:
        outward_right =  ( plot74_GIS_T * yr_60 ) - yr_150
    ax74.spines.right.set_position(("outward", outward_right))
    ax74.set_ylabel("Temperature in °C   GISS     74 ", color=c74, fontname="Arial",fontsize=18)
    ax74.tick_params(axis="y", labelcolor=c74)
 
# plot8_right_y_axe_for_T_75 ,     linear_41_75  ,   Hansen 0.41°C         ,  line  581
def plot8_right_y_axe_for_T_75(ax75,right52): # 75.6 
    # ax75.spines.right.set_position(("outward", rightv))
    if right52 > 0:
        outward_right = right52
    else:
        outward_right =  ( linear_41_75 * yr_60 ) - yr_150
    ax75.spines.right.set_position(("outward", outward_right))
    if plot74_GIS_T == 2: # T axis already on the left
        print(f"plot 474: no need for second T axis linear_41_75 ={linear_41_75} ")
        ax75.yaxis.set_ticks([])
        ax75.spines['right'].set_visible(False)
    else:    
       ax75.set_ylabel("Temperature in °C        plot589          75", color=c75, fontname="Arial",fontsize=18)
       ax75.tick_params(axis="y", labelcolor=c75)
   

# plot8_right_y_axe_for_T_76 ,     plot76_my_T  ,   my quadratic   ,  line  584
def plot8_right_y_axe_for_T_76(ax76,right52): # 76.6 
    # ax76.spines.right.set_position(("outward", rightv))
    if right52 > 0:
        outward_right = right52
    else:
        outward_right =  ( plot76_my_T * yr_60 ) - yr_150
    ax76.spines.right.set_position(("outward", outward_right))
    ax76.set_ylabel("Temperature in °C        plot559          76", color=c76, fontname="Arial",fontsize=18)
    ax76.tick_params(axis="y", labelcolor=c76)
    
# plot8_right_y_axe_for_T_77 ,     plot_T_77    ,   my quadratic   ,  line  604
def plot8_right_y_axe_for_T_77(ax77,right52): # 77.6 
    if right52 > 0:
        outward_right = right52
    else:
        outward_right =  ( plot_T_77 * yr_60 ) - yr_150
    ax77.spines.right.set_position(("outward", outward_right))
    if plot74_GIS_T == 2: # T axis already on the left
        print(f"plot 496: no need for second T axis on the right ax77 ={plot_T_77} {'='*2}")
        ax77.yaxis.set_ticks([])
        ax77.spines['right'].set_visible(False)
    else:    
       ax77.set_ylabel("Temperature in °C        plot570          77", color=c77, fontname="Arial",fontsize=18)
       ax77.tick_params(axis="y", labelcolor=c77)
       


# plot_9_create_all_plots(ax1, data): line 436 600
def plot_9_create_all_plots(ax1, data):
    """Create all plots based on configuration"""
    
    # Plot plot22_CO2_Mauna_Loa
    if plot22_CO2_Mauna_Loa > 0: # 22.4 create the plot  ax22.set_ylim(y_min, y_max)
        if print_debug > 19:
          print(f"plot_366: plot22_CO2_Mauna_Loa 22.4 ={plot22_CO2_Mauna_Loa}")
          print(f"plot_367: Last 3 CO2 rows: {data['co2'][-3:] if len(data['co2']) >= 3 else data['co2']}")
        ax22 = ax1.twinx()
        ax22.plot(data['co2']["year"], data['co2']["co2_ppm"], 'o', 
                  label="T GIS K22", color=c22, linewidth=3)
        ax22.tick_params(axis="y", labelcolor=c22)
        ax22.set_ylim(y_min, y_max)
        # plot8_right_y_axe_for_ppm_22  plot22_CO2_Mauna_Loa                         ,   line  415
        plot8_right_y_axe_for_ppm_22( ax22 , 0 ) # 22.4



    # -----------------------------
    # 2.3 plot23_Glen_CO2 = 0.013t² - 51t + 49,536 in dark blue 
    # source a plot with the formula explained in a thread
    # source https://x.com/Gergyl/status/1810632238230589564
    # -----------------------------
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

    # plot25_long_CO2, NOAA 800_000 year ice data,  plot_9_create_all_plots() ,   line 447 
    # plot25_long_CO2 = 3 # 2, 3 print -800 000 years ppm CO2 file
    # https://ourworldindata.org/grapher/co2-long-term-concentration?overlay=download-data
    # Data sources: NOAA Global Monitoring Laboratory - Trends in Atmospheric Carbon Dioxide (2026)EPA 
    # based on various sources (2022) – with major processing by Our World in Data
    # -----------------------------
    # part 2.5 plot CO2 # plot_9 line 453
    blue25_text="green: CO2 NOAA 800_000 year ice data 25"
    if plot25_long_CO2 > 0: # 25.2 plot
      #df25 = pd.read_csv("read_csv/csv_25_ppm_long.csv") # our world in data file
      df25 = pd.read_csv("read_csv/_25_ppm_long.csv") # our world in data file
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

    # plot31_CO2_emission summed  co2_cumul.csv   Entity,Code,Year,Cumula           , line 603
    # https://ourworldindata.org/grapher/cumulative-co-emissions?country=~OWID_WRL&overlay=download-data
    # 3.4.0 Entity,Code,Year,Cumulat
    if plot31_CO2_emission > 0: # 31.7
        ax31 = ax1.twinx()
        # df31 = pd.read_csv("read_csv/_31_co2_carbon_brief.csv")      # processed file from 42_CO2_T.py
        # line 923  world63.to_csv("work/_63b.csv", index=False, float_format='%.6f')
        df31 = pd.read_csv("read_csv/_31_co2_cummulative_GtCO2.csv") 
        # processed file from 5_CO2_EEI_T/main 63play_63_CB=5 cumulative 1750 to 2024 word of data
        # "work/_63b.csv has 5 columns Year,Cumulative CO₂ emissions, GtCO2 and GtC
        print("plot_630: plot31_CO2_emission = ", plot31_CO2_emission) # 31.7 plot 31
        ax31.plot(df31["Year"], df31["GtCO2"], marker="o",  color=c31, label="plot31_CO2_emission")
        ax31.tick_params(axis="y", labelcolor=c31)
        ax31.set_ylim(y_Gmin, y_Gmax) # best scaling 2000 GtCO2
        if plot31_CO2_emission > 2:
            plot8_right_y_axe_for_C_31(ax31,0) # 31.5 line 500
            # plot8_right_y_axe_for_C_31 ,  plot31_CO2_emission , cumulative CO2 emissions , line  402

    # https://ourworldindata.org/grapher/cumulative-co-emissions?country=~OWID_WRL&overlay=download-data
    # 3.4.0 Entity,Code,Year,Cumulat
    if plot32_CO2_emission > 0: # 32.7
        ax32 = ax1.twinx()
        # df31 = pd.read_csv("read_csv/_31_co2_carbon_brief.csv")      # processed file from 42_CO2_T.py
        # line 923  world63.to_csv("work/_63b.csv", index=False, float_format='%.6f')
        df32 = pd.read_csv("read_csv/_31_co2_cummulative_GtCO2.csv") 
        # processed file from 5_CO2_EEI_T/main 63play_63_CB=5 cumulative 1750 to 2024 word of data
        # "work/_63b.csv has 5 columns Year,Cumulative CO₂ emissions, GtCO2 and GtC
        print("plot_650: plot32_CO2_emission = ", plot32_CO2_emission) # 32.7 plot 32
        ax32.plot(df32["Year"], df32["GtC"], marker="o",  color=c32, linewidth=3, label="plot32_CO2_emission")
        ax32.tick_params(axis="y", labelcolor=c32)
        ax32.set_ylim(y_32min, y_32max) # best scaling 2000 GtC
        if plot32_CO2_emission > 2:
            plot8_right_y_axe_for_C_32(ax32,0) # 32.5 line 500
            # plot8_right_y_axe_for_C_32 ,  plot32_CO2_emission , cumulative CO2 emissions , line  402



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
        print34_text = print34_text + str(plot34_CO2_emission_mode)
        # 3.4.mode 1 
        if plot34_CO2_emission_mode == 1: # 34.2   mode 1
           df34a = pd.read_csv("read_csv/csv_34a1_co2_world_generated.csv") # processed file
           print("plot_304: mode 1 plot34_CO2_emission = ", plot34_CO2_emission) # 34.3.1
        elif plot34_CO2_emission_mode == 2:   # 34.2   mode 2
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
        elif plot34_CO2_emission_mode == 3:  # 34.2 .mode 3
           print("plot_318: mode 3 plot34_CO2_emission = ", plot34_CO2_emission) # 34.3.3
           df34b = pd.read_csv("read_csv/csv_34a3_cum_co2.csv") # our world in data file
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
           print(co2_sum_world.tail(5))
           print("plot_332: mode 3 plot34_CO2_emission = ", plot34_CO2_emission) # 34.3
        elif plot34_CO2_emission_mode == 4:  # 3.4.mode 5
           df34b = pd.read_csv("read_csv/csv_34a3_cum_co2.csv") # our world in data file
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
              ax34.set_ylim(y_Gmin, y_Gmax) # best scaling 2000 GtCO2
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



      
    # plot42_EEI_48month, running average over 48 months,  plot_9_create_all_plots() ,   line 601
    # Earth Energy Imbalance W/m² moving average 48 month 
    if plot42_EEI_48month > 0:
        ax42 = ax1.twinx()
        ax42.plot(data['ceres_42']["decimal_year"], data['ceres_42']["EEI"], '-', 
                  label="EEI K42", color=c42, linewidth=4)
        ax42.tick_params(axis="y", labelcolor=c42)
        ax42.set_ylim(y_Emin, y_Emax)
        # plot8_right_y_axe_for_eei_42        plot42_EEI_48month                       ,   line  381
        if plot42_EEI_48month > 2:
           plot8_right_y_axe_for_eei_42( ax42 , 0 ) # 42.4 line 450



    if plot43_eei_12month > 0 and 'ceres_43' in data: # 43.2
        ax43 = ax1.twinx()
        ax43.plot(data['ceres_43']["decimal_year"], data['ceres_43']["EEI"], '-', 
                  label="EEI K41", color=c43, linewidth=2)
        ax43.tick_params(axis="y", labelcolor=c43)
        ax43.set_ylim(y_Emin, y_Emax)
        if print_debug > 19:
           print(f"plot_231: ax43 43.4 ={plot43_eei_12month}")
        # plot8_right_y_axe_for_eei_43  plot43_eei_12month   Earth Energy Imbalance     ,  line  460
        if plot43_eei_12month > 2:
           plot8_right_y_axe_for_eei_43( ax43 , 0 ) # 43.4 line 460




    if part44_ceres_eei > 0 and 'ceres_custom' in data:
        if print_debug > 19:
           print(f"plot_235: ax44 44.7 ={part44_ceres_eei}")

        ax44 = ax1.twinx()
        ax44.plot(data['ceres_custom']["decimal_year"], data['ceres_custom']["EEI"], '-', 
                  label="EEI K44", color=c44, linewidth=2)
        ax44.tick_params(axis="y", labelcolor=c44)
        ax44.set_ylim(y_Emin, y_Emax)
    
    # plot52_delta_CO2_red_bars, Mauna Loa delta ,  plot_9_create_all_plots() ,   line 630

    # part 5.2 plot52_delta_CO2_red_bars
    # part 5.3 plot53_CO2_orange2025
    # part 5.4 plot54_Glen_delta_on
    # -----------------------------
    # part 5.2 plot52_delta_CO2_red_bars
    # 5.2.2 ΔCO₂ berechnen (per pandas) Balken
    # df52["CO2"].diff() Calculates the difference between consecutive CO₂ values
    # -----------------------------
    if plot52_delta_CO2_red_bars > 0: # 52.3    
       # 2.2.1 years 1960–2025 x_years_52_list = [1960, 1961, 1962, ..., x_end - 1]
       if x_end > 1961:
          x_years_52_list = list(range(1960, x_end+1)) # list of years 1960...
       else:
          x_years_52_list = list(range(1960, 2026)) # list of years 1960...
       # 2.2.2 Select only 2018–2025
       if x_anf < 1960:
          start_of_x_index = x_years_52_list.index(1960)
       else:
          start_of_x_index = x_years_52_list.index(x_anf)    
       if x_end > 2026:
          end_of_x_index = x_years_52_list.index(2025)
       elif x_end < 1960:
          end_of_x_index = 1
       else:
          end_of_x_index = x_years_52_list.index(x_end)
       x_years_52_list_subset = x_years_52_list[start_of_x_index:end_of_x_index]
       # -----------------------------
       # 2.2.3 Kurve1 CO₂ Daten https://gml.noaa.gov/webdata/ccgg/trends/co2/co2_annmean_mlo.txt
       # https://gml.noaa.gov/ccgg/trends/mlo.html
       # https://gml.noaa.gov/ccgg/trends/global.html
       # -----------------------------
       co2_values52 = [
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
       co2_values52_subset = co2_values52[start_of_x_index:end_of_x_index]
       df52 = pd.DataFrame({  # make a DataFrame with two columns:"x_52_years" → years (x-axis) "y_52_CO2_ppm" → CO₂ values (y-axis)
            "x_52_years": x_years_52_list_subset,
            "y_52_CO2_ppm": co2_values52_subset })

       df52["Delta_CO2"] = df52["y_52_CO2_ppm"].diff().fillna(0)  
       # This line creates a new column in your DataFrame called Delta_CO2.
       ax52 = ax1.twinx()  # twinx(): Shares the same x-axis Adds a new y-axis on the right
       # growth data is different https://gml.noaa.gov/webdata/ccgg/trends/co2/co2_gr_mlo.txt
       ax52.spines.right.set_position(("outward", 20))
       bars = ax52.bar(df52["x_52_years"], df52["Delta_CO2"], width=0.7, alpha=0.5, color=c52bar)
       plot8_right_y_axe_for_delta_ppm_increase_52(ax52, df52, 0)
       # 5.2.8 Add numbers on top of delta CO2 bars
       if plot52_delta_CO2_red_bars == 3:
          ax52.bar_label(bars, fontsize=12, fontname="Arial",padding=1, color="black")
          # end part 5.2 plot52_delta_CO2_red_bars


    # part 5.5 plot55_population_on human earth population 
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
       green55_text="Green line: Earth Population in billion (plot675) 55"
       df55 = pd.read_csv("read_csv/_55_population.csv")
       pop_world = (
             df55[df55["Entity"] == "World"][["Year", "Population"]]
             .query("1960 <= Year <= 2026")
             .sort_values("Year")
             .reset_index(drop=True)
          )
       # 5.5.4 in Milliarden
       pop_world["Population_Mrd"] = pop_world["Population"] / 1e9
       ax55 = ax1.twinx()
       # plot8_160_right_y_axe_55(ax55,pop_world): # 55 line 358
       plot8_160_right_y_axe_55(ax55,pop_world)    # 55.4 line 358
       # end part 5.5 plot55_population_on human earth population  

    if play_61_CERES > 0:
        ax61 = ax1.twinx()
        ax61.plot(data['ceres_61']["decimal_year"], data['ceres_61']["EEI"], '-', 
                  label="EEI K61", color=c61, linewidth=2)
        ax61.tick_params(axis="y", labelcolor=c61)
        ax61.set_ylim(y_Emin, y_Emax)
        if print_debug > 9:
           print(f"plot_947: ax61 61.8 ={play_61_CERES}")
    if play_62_CERES > 0:
        ax62 = ax1.twinx()
        ax62.plot(data['ceres_62']["decimal_year"], data['ceres_62']["EEI"], '-', 
                  label="EEI K62", color=c62, linewidth=2)
        ax62.tick_params(axis="y", labelcolor=c62)
        ax62.set_ylim(y_TOAmin, y_TOAmax)
        if print_debug > 9:
           print(f"plot_258: ax62 62.8 ={play_62_CERES}")

# play_63_CB    = 3 # carbon brief CO2 values https://ourworldindata.org/grapher/cumulative-co-emissions?country=~OWID_WRL&overlay=download-data
# https://ourworldindata.org/grapher/cumulative-co-emissions?country=~OWID_WRL
# download cumulative-co-emissions.csv displayed data and copy to 
# work/_63a_cumulative-co-emissions.csv with columns  Entity,Code,Year,Cumulative CO₂ emissions

    if play_63_CB > 0: # 63.4
        ax63 = ax1.twinx()
        df63 = pd.read_csv("work/_63a_cumulative-co-emissions.csv")
        if print_debug > 9:
           print(f"plot_888: ax63 63.4 ={play_63_CB}")
        world63 = (
             df63[df63["Entity"] == "World"][["Year", "Cumulative CO₂ emissions"]]
             .query("1750 <= Year <= 2026")    # .query("1750 <= Year <= 2026")
             .sort_values("Year")
             .reset_index(drop=True)
          )
        # in Gt CO2
        world63["GtCO2"] = world63["Cumulative CO₂ emissions"] / 1e9
        world63["Year63"] = world63["Year"] +0.1
        # in GtC
        world63["GtC"] = world63["Cumulative CO₂ emissions"] *12 / ( 1e9 * 44 )
        print(df63.head(3))
        print(f"plot_901: ax63 63.4 ={play_63_CB}")
        print(world63.head(3))
        world63.to_csv("work/_63b.csv", index=False, float_format='%.6f')
        # "work/_63b.csv has 5 columns Year,Cumulative CO₂ emissions, GtCO2 and GtC
        df63b = pd.read_csv("work/_63b.csv") # processed file
        print("plot_906: play_63_CB = ", play_63_CB) # 63.7 
        ax63.plot(world63["Year"], world63["GtCO2"], marker="o",  color=c63, label="play_63_CB")

        ax63.tick_params(axis="y", labelcolor=c63)
        ax63.set_ylim(y_Gmin, y_Gmax) # best scaling 2000 GtCO2
        if play_63_CB > 2:
            plot8_right_y_axe_for_C_63(ax63,1) # 63.5 line 500


    if plot71_temperature > 0 : # 71.4
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
        ax71 = ax1.twinx()
        ax71.plot(df7["Year71"], df7["Modeled71"], '--', label="T formula CO2=  K6", color=c71, linewidth=3)
        ax71.tick_params(axis="y", labelcolor=c71)
        ax71.set_ylim(y_Tmin, y_Tmax) # scale
        # plot8_right_y_axe_for_T_71 ,  plot71_temperature                            ,  line  525
        plot8_right_y_axe_for_T_71(ax71,0) # 71.5 line 35
        # end 7.1 

    if plot72_AESS_T > 0 : # 72.4
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
        ax72 = ax1.twinx()  # twinx(): Shares the same x-axis Adds a new y-axis on the right
        ax72.plot(df72["Year72"], df72["Modeled72"], '--', label="T formula CO2=  K72", color=c72, linewidth=3)
        ax72.tick_params(axis="y", labelcolor=c72)
        ax72.set_ylim(y_Tmin, y_Tmax) # scale
        # end 7.2 plot72_AESS_T


    if plot73_ECS_T > 0 : # 73.4
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
        ax73 = ax1.twinx()  # twinx(): Shares the same x-axis Adds a new y-axis on the right
        ax73.plot(df73["Year73"], df73["Modeled73"], '--', label="T formula CO2=  K73", color=c73, linewidth=3)
        ax73.tick_params(axis="y", labelcolor=c73)
        ax73.set_ylim(y_Tmin, y_Tmax) # scale
        # end 7.3
        # plot8_right_y_axe_for_T_74(ax74,0) # 74.5 line 356

    # plot74_GIS_T,   GIS temperature add 0.3°C like Hansen    ,  plot_9_create_all_plots() ,   line 750
    # Plot GIS temperature
    if plot74_GIS_T > 0 : # 74.4
        ax74 = ax1.twinx()
        ax74.plot(data['gis_temp']["Year74"], data['gis_temp']["GIS_temp"]+0.3, '-', 
                  label="T GIS K74", color=c74, linewidth=5)
        ax74.tick_params(axis="y", labelcolor=c74)
        ax74.set_ylim(y_Tmin, y_Tmax)
        if plot74_GIS_T > 2:
            plot8_right_y_axe_for_T_74(ax74,0) # 74.5 line 500

    # part 75 plot 2015 .41°C linear fit
    # linear_41_75  = 4 # part 75    Hansen 2015 .41°C linear fit
    # https://www.columbia.edu/~jeh1/mailings/2026/ElNino.2026.02.06.pdf
    # 7.5.2 Year75,GIS_temp
    if linear_41_75 > 0:
       print75_text ="Hansen linear fit from 2015 +0.41°C     75"
       df75 = pd.read_csv("read_csv/_75_hansen_41C.csv") # our world in data file
       #print(df75.head(2))
       ax75 = ax1.twinx()  # twinx(): Shares the same x-axis Adds a new y-axis on the right
       # part 7.4.6 add 0.3°C same as Hansen to GIS
       ax75.plot(df75["Year75"], df75["temp"]+0.1, '--', label="T GIS  K75", color=c75, linewidth=2)
       ax75.tick_params(axis="y", labelcolor=c75)
       ax75.set_ylim(y_Tmin, y_Tmax) # scale
       if linear_41_75 > 2:
            plot8_right_y_axe_for_T_75(ax75,0) # 75.5 line 530
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

    def T_model77_old(t):
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

    if plot76_my_T > 0:
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
       ax76 = ax1.twinx()  # twinx(): Shares the same x-axis Adds a new y-axis on the right
       ax76.plot(df76["Year76"], df76["Modeled76"], '--', label="T formula CO2=  K76", color=c76, linewidth=3)
       ax76.tick_params(axis="y", labelcolor=c76)
       ax76.set_ylim(y_Tmin, y_Tmax) # scale
       if print_debug > 9:
            print(f"plot1108: ax76 ={plot76_my_T} {'='*2}")

       if plot76_my_T > 2:
            plot8_right_y_axe_for_T_76(ax76,0) # 76.5 line 540
       # end 7.6 plot76_my_T


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

    if plot_T_77 > 0:
       # 7.6.2 years scale x axis
       years77 = np.arange(x_anf, x_end + 1 )
       T_77values = T_model77(years77)
       #print(T_77values)
       # 7.6.3. Create DataFrame for convenience
       df77 = pd.DataFrame({
             "Year77":      years77,
             "Modeled77": T_77values })
       # 7.6.4 plot77_temperature
       # print(df77.head(2))
       #print(T_model77(1950) ,"  1950")  # 0.2
       #print(T_model77(2013) ,"  2013")  # 1.0
       #print(T_model77(2023) ,"  2023")
       #print(T_model77(2026) ,"  2026")  # 1.5
       #print(T_model77(2028) ,"  2028")  # 1.5
       ax77 = ax1.twinx()  # twinx(): Shares the same x-axis Adds a new y-axis on the right
       ax77.plot(df77["Year77"], df77["Modeled77"], '--', label="T formula CO2=  K77", color=c77, linewidth=3)
       ax77.tick_params(axis="y", labelcolor=c77)
       ax77.set_ylim(y_Tmin, y_Tmax) # scale
       if print_debug > 9:
            print(f"plot1143: no need for second T axis on the right ax77 ={plot_T_77} {'='*2}")
       if plot_T_77 > 2:
            plot8_right_y_axe_for_T_77(ax77,0) # 77.5 line 540
       # end 7.7 plot_T_77




    # end plot_9_create_all_plots(ax1, data):





