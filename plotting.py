# plotting.py
# version 5b13
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
from mpl_toolkits.axes_grid1 import make_axes_locatable
import matplotlib.pyplot as plt


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
        y_TOAmin = 99.15   # bug the global config.py line 101 does not work
        y_TOAmax = 99.3  # bug the global config.py line 102 does not work
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
            y_TEmayor_ticks = 2 
            y_TEminor_ticks = 0.2
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