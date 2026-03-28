# plotting.py
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

def setup_figure(scale_mode=10):
    """Setup the figure with appropriate size"""
    if scale_mode == 7:
        fig, ax1 = plt.subplots(figsize=(13, 7))
    elif scale_mode == 8:
        fig, ax1 = plt.subplots(figsize=(13, 8))
    elif scale_mode == 10:
        fig, ax1 = plt.subplots(figsize=(13, 10))
    else:
        fig, ax1 = plt.subplots(figsize=(13, 7))
    
    fig.subplots_adjust(bottom=0.30)
    return fig, ax1


def configure_axes(ax1, x_anf, x_end, y_min, y_max, y_Emin, y_Emax, 
                   y_Tmin, y_Tmax, yl_mode, c22, c42):
    """Configure the axes based on selected mode"""
    plt.xlim(x_anf, x_end)
    ax1.grid(True)
    
    if yl_mode == 4:  # EEI mode
        ax1.set_ylim(y_Emin, y_Emax)
        ax1.set_ylabel("Earth Energy Imbalance in W/m²", color=c42, fontsize=20)
        ax1.tick_params(axis="y", labelcolor=c42, labelsize=20)
    else:  # CO2 mode
        ax1.set_ylim(y_min, y_max)
        ax1.set_ylabel("CO₂ in ppm", color=c22, fontsize=20)
        ax1.tick_params(axis="y", labelcolor=c22, labelsize=20)
    
    return ax1

def add_grid_lines(ax1):
    # mayor grid lines vertical lines inside the plot to better read the y value
    for line in ax1.get_ygridlines():
        # line.set_color('green')  # major lines
        line.set_color('blue')
        line.set_alpha(0.5)
        line.set_linestyle('-')
        line.set_linewidth(1.1)
    
    ax1.grid(True, which="minor", axis="y", color="lightblue", alpha=0.94)

def add_temperature_band(ax48, y_min=1.5, y_max=1.8):
    """Add temperature band to the plot"""
    ax48.axhspan(y_min, y_max, color="#B3D9FF", alpha=0.5, zorder=0)

def add_vertical_bands(ax1, C280):
    """Add vertical bands for CO2 levels"""
    ax1.axhspan(4 * C280 - 2, 4 * C280 + 2, color="#4554A8C6", alpha=0.25, zorder=0)
    ax1.axhspan(2 * C280 - 2, 2 * C280 + 2, color="#4554A8C6", alpha=0.3, zorder=0)