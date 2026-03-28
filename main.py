# main.py 5a1
# part 1 configure 
v = "5a6" # based on /42_CO2_T.py  based on /42v1_CO2_T.py 
# bug EEI 11 is goodnot shown
# ok line linear_41_75 = 3 is not displayed
# ok left y axis
# ok right y axis
# bug line 6 is not shown text6 = f"Left Y axis is the " # 
#   text6 = text6 + f"EEI = {y_Emin}" # y_max number inside string
#   text6 = text6 + f" ... {y_Emax} W/m²" # y_max number inside string
# ok horizontal 1.8°C line is T value

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



import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
import sys

# Import modules
from config import *
from data_processing import *
from plotting import *
from data_processing import *
from text_annotations import *

def get_active_temperature_axis(ax1):
    """Find which temperature axis is active"""
    if plot71_temperature > 0:
        return ax1.twinx()
    elif plot72_AESS_T > 0:
        return ax1.twinx()
    elif plot73_ECS_T > 0:
        return ax1.twinx()
    elif plot74_GIS_T > 0:
        return ax1.twinx()
    elif linear_41_75 > 0:
        return ax1.twinx()
    return None







def process_ceres_data():
    """Process CERES data based on configuration"""
    if part41_ceres_eei > 10:
        df41a = convert_ceres_to_csv('csv/csv41/csv41a_in_CERES.txt', 
                                      'csv/csv41/csv41b_ceres.csv')
    
    if part41_ceres_eei == 12:
        df_with_12avg = create_running_average('csv/csv41/csv41b_ceres.csv', 
                                               'csv/csv41/csv41d12_ceres.csv',
                                               window_months=12)
    
    elif part41_ceres_eei == 48:
        df_with_48avg = create_running_average('csv/csv41/csv41b_ceres.csv', 
                                               'csv/csv41/csv41d48_ceres.csv',
                                               window_months=48)
    
    elif part41_ceres_eei == 50:
        df_with_48avg = create_running_average('csv/csv41/csv41b_ceres.csv', 
                                               'csv/csv41/csv41d50_ceres.csv',
                                               window_months=48, center=False)
    
    # Process part44_ceres_eei
    if part44_ceres_eei > 13:
        out = f"csv/csv44/csv44d_EEI_{part44_ceres_eei}_month.csv"
        
        if part44_ceres_eei % 2 == 0:
            use_center = True
            min_periods = part44_ceres_eei // 2
            avg_type = "CENTERED"
        else:
            use_center = False
            min_periods = part44_ceres_eei
            avg_type = "TRAILING"
        
        df_with_avg = create_running_average('csv/csv44/csv44b_ceres.csv', 
                                            "csv/csv44/csv44d_out.csv",
                                            window_months=part44_ceres_eei,
                                            min_periods=min_periods,
                                            center=use_center,
                                            column_name='EEI')
        
        print(f"{avg_type} average for {part44_ceres_eei}-month window")

def create_temperature_plots(ax1):
    """Create temperature plots based on configuration"""
    temp_axes = {}
    
    if plot71_temperature > 0:
        years = np.arange(x_anf, x_end + 1)
        values = T_model71(years)
        ax = ax1.twinx()
        ax.plot(years, values, '--', color=c71, linewidth=3)
        temp_axes['71'] = configure_right_y_axis(ax, y_Tmin, y_Tmax, c71, 
                                                   "Δ Temperature in °C 71")
    
    if plot72_AESS_T > 0:
        years = np.arange(x_anf, x_end + 1)
        values = T_model72(years)
        ax = ax1.twinx()
        ax.plot(years, values, '--', color=c72, linewidth=3)
        temp_axes['72'] = configure_right_y_axis(ax, y_Tmin, y_Tmax, c72, 
                                                   "Δ Temperature calc72 in °C")
    
    if plot73_ECS_T > 0:
        years = np.arange(x_anf, x_end + 1)
        values = T_model73(years)
        ax = ax1.twinx()
        ax.plot(years, values, '--', color=c73, linewidth=3)
        temp_axes['73'] = configure_right_y_axis(ax, y_Tmin, y_Tmax, c73, 
                                                   "Δ Temperature in °C (ECS = 4.5°C)")
    
    if plot74_GIS_T > 0:
        df = pd.read_csv("csv/csv7/csv_74_gis_temperature.csv")
        ax = ax1.twinx()
        ax.plot(df["Year74"], df["GIS_temp"] + 0.3, '-', color=c74, linewidth=3)
        temp_axes['74'] = configure_right_y_axis(ax, y_Tmin, y_Tmax, c74, 
                                                   "Δ GIS Temperature in °C 74")
    
    if linear_41_75 > 0:
        df = pd.read_csv("csv/csv7/csv_75_hansen.csv")
        ax = ax1.twinx()
        ax.plot(df["Year75"], df["temp"] + 0.1, '--', color=c75, linewidth=2)
        temp_axes['75'] = configure_right_y_axis(ax, y_Tmin, y_Tmax, c75, 
                                                   "Hansen linear fit 75")
    
    return temp_axes


def hide_other_right_axes(ax1, keep_axis):
    """Hide all right y-axes except the one we want to keep"""
    # Get all axes in the figure
    all_axes = ax1.get_figure().get_axes()
    
    for ax in all_axes:
        if ax != ax1 and ax != keep_axis:
            # Check if this is a right y-axis (has a spine on the right)
            if ax.spines['right'].get_visible():
                ax.spines["right"].set_visible(False)
                ax.tick_params(right=False, labelright=False)


def load_plot_data():
    """Load all data needed for plotting"""
    data = {}
    
    # Load CO2 data if needed
    if plot22_CO2_Mauna_Loa > 0:
        data['co2'] = load_co2_mauna_loa(x_anf, x_end)
    
    # Load GIS temperature data
    if plot74_GIS_T > 0:
        data['gis_temp'] = load_gis_temperature()
    
    # Load CERES data
    if part41_ceres_eei > 0:
        data['ceres_12'] = pd.read_csv("csv/csv44/_plot_41_41g12.csv")
    
    if part42_ceres_eei > 0:
        data['ceres_48'] = pd.read_csv("csv/csv44/_plot_42_41g50.csv")
    
    if part44_ceres_eei > 0:
        data['ceres_custom'] = pd.read_csv("csv/csv44/csv44d_out.csv")
    
    return data

def create_plots(ax1, data):
    """Create all plots based on configuration"""
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
    
    if part44_ceres_eei > 0 and 'ceres_custom' in data:
        ax44 = ax1.twinx()
        ax44.plot(data['ceres_custom']["decimal_year"], data['ceres_custom']["EEI"], '-', 
                  label="EEI K44", color=c44, linewidth=2)
        ax44.tick_params(axis="y", labelcolor=c44)
        ax44.set_ylim(y_Emin, y_Emax)
    
    # Plot GIS temperature
    if plot74_GIS_T > 0 and 'gis_temp' in data:
        ax74 = ax1.twinx()
        ax74.plot(data['gis_temp']["Year74"], data['gis_temp']["GIS_temp"]+0.3, '-', 
                  label="T GIS K74", color=c74, linewidth=3)
        ax74.tick_params(axis="y", labelcolor=c74)
        ax74.set_ylim(y_Tmin, y_Tmax)

def add_text_annotations(fig, ax1, header_parameter):
    """Add all text annotations to the plot"""
    filename = os.path.basename(sys.argv[0])
    
    # Add header
    add_header(ax1, x_anf, x_end, yl_mode)
    
    # Add bottom text
    add_bottom_text(fig, ax1, filename, v, header_parameter, tr1y, tr2x)
    
    # Add legend lines for active plots
    if plot74_GIS_T == 2:
        add_legend_line(fig, lr2x1, lr2x2, lr2y, c74)
        add_text_row(ax1, tr2x, tr2y, 
                    "Temperature in °C giss.nasa.gov Hansen+0.3°C 74", 
                    c74, trs)


    if part41_ceres_eei == 3:
        add_legend_line(fig, lr2x1, lr2x2, lr3y, c41)
        add_text_row(ax1, tr2x, tr3y, 
                    "Earth Energy Imbalance W/m² moving average 12 month 41", 
                    c41, trs)
    
    if part42_ceres_eei == 4:
        add_legend_line(fig, lr2x1, lr2x2, lr4y, c42)
        add_text_row(ax1, tr2x, tr4y, 
                    "Earth Energy Imbalance W/m² moving average 48 month 42", 
                    c42, trs)
    
    if part44_ceres_eei > 0:
        add_legend_line(fig, lr2x1, lr2x2, lr5y, c44)
        p44_text = f"Earth Energy Imbalance {part44_ceres_eei}-month moving average 44"
        add_text_row(ax1, tr2x, tr5y, p44_text, c44, trs)

def save_plot(fig, header_parameter):
    """Save the plot if configured"""
    if parameter84_save_png > 0:
        filename = os.path.basename(__file__)[:parameter84_save_png]
        filename = f"{filename}_{header_parameter}{x_end}"
        path = f"/Users/thomasboettcher/Desktop/{filename}"
        fig.savefig(path, dpi=300, bbox_inches="tight")
        
        path = "/Users/thomasboettcher/documents/Python/5_CO2_EEI_T/42_CO2_T.png"
        fig.savefig(path, dpi=300, bbox_inches="tight")








def main():
    """Main execution function"""
    # Create header parameter string
    header_parameter = (f"{plot22_CO2_Mauna_Loa}{plot23_Glen_CO2}{plot25_long_CO2}"
                       f"{plot34_CO2_emission} 4({part41_ceres_eei}{part42_ceres_eei}"
                       f"{part43_ceres_eei}{part44_ceres_eei}) 5({plot52_delta_CO2_red_bars}"
                       f"{plot53_CO2_orange2025}{plot54_Glen_delta_on}{plot55_population_on})"
                       f"7({plot71_temperature}{plot72_AESS_T}{plot73_ECS_T}{plot74_GIS_T}"
                       f"{linear_41_75}{plot76_my_T})")
    
    # Setup figure
    fig, ax1 = setup_figure(scale_mode)
    
    # Configure left axes
    ax1 = configure_axes(ax1, x_anf, x_end, y_min, y_max, y_Emin, y_Emax,
                         y_Tmin, y_Tmax, yl_mode, c22, c42, c74)
    
    # Create temperature plots (these create right y-axes)
    temp_axes = create_temperature_plots(ax1)
    
    # Find the primary temperature axis to keep visible
    primary_axis = None
    if plot74_GIS_T > 0 and '74' in temp_axes:
        primary_axis = temp_axes['74']
    elif linear_41_75 > 0 and '75' in temp_axes:
        primary_axis = temp_axes['75']
    elif temp_axes:
        primary_axis = list(temp_axes.values())[0]
    
    # Hide other right y-axes to avoid clutter
    if primary_axis:
        hide_other_right_axes(ax1, primary_axis)
    
    # Add temperature band only to temperature axes
    if primary_axis:
        add_temperature_band(primary_axis, 1.5, 2.0)
    
    # Add grid lines
    add_grid_lines(ax1)
    
    # Add vertical bands
    add_vertical_bands(ax1, C280)
    add_year_band(ax1, 2025, 2027)
    
    # Add x-axis label
    ax1.set_xlabel("year", fontsize=20)
    plt.xticks(fontsize=20)
    ax1.tick_params(axis="x", labelcolor="black", labelsize=20)
    
    # Add header
    add_header(ax1, x_anf, x_end, yl_mode)
    
    # Add bottom text (line 1)
    filename = os.path.basename(sys.argv[0])
    add_bottom_text(fig, ax1, filename, v, header_parameter, tr1y)
    
    # Add axis info (line 6)
    add_axis_info_line(ax1, yl_mode, y_Emin, y_Emax, y_Tmin, y_Tmax, 
                       y_min, y_max, header_parameter, tr6y, c42)
    
    # Add legend lines for active plots (lines 2-5)
    # This is a simplified version - you can expand based on your needs
    
    # Adjust layout
    fig.tight_layout()
    plt.tight_layout()
    
    # Show plot
    plt.show()
    
    # Save plot
    if parameter84_save_png > 0:
        filename = os.path.basename(__file__)[:parameter84_save_png]
        filename = f"{filename}_{header_parameter}{x_end}"
        path = f"/Users/thomasboettcher/Desktop/{filename}"
        fig.savefig(path, dpi=300, bbox_inches="tight")
        
        path = "/Users/thomasboettcher/documents/Python/5_CO2_EEI_T/42_CO2_T.png"
        fig.savefig(path, dpi=300, bbox_inches="tight")
    
    # Close figure
    plt.close(fig)

if __name__ == "__main__":
    main()
