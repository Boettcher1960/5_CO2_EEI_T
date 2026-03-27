# main.py
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
    
    # Process CERES data
    process_ceres_data()
    
    # Setup figure
    fig, ax1 = setup_figure(scale_mode)
    
    # Load data
    data = load_plot_data()
    
    # Configure axes
    ax1 = configure_axes(ax1, x_anf, x_end, y_min, y_max, y_Emin, y_Emax,
                         y_Tmin, y_Tmax, yl_mode, c22, c42)
    
    # Create plots
    create_plots(ax1, data)
    
    # Add grid lines
    add_grid_lines(ax1)
    
    # Add vertical bands
    add_vertical_bands(ax1, C280)
    
    # Add temperature band if temperature plots are active
    if plot71_temperature > 0 or plot72_AESS_T > 0 or plot73_ECS_T > 0 or plot74_GIS_T > 0:
        # Find the active temperature axis
        for ax in [ax1] + ax1.get_figure().get_axes():
            if hasattr(ax, 'get_ylabel') and 'Temperature' in ax.get_ylabel():
                add_temperature_band(ax)
                break
    
    # Add text annotations
    add_text_annotations(fig, ax1, header_parameter)
    
    # Add x-axis label
    ax1.set_xlabel("year", fontsize=20)
    plt.xticks(fontsize=20)
    ax1.tick_params(axis="x", labelcolor="black", labelsize=20)
    
    # Adjust layout
    fig.tight_layout()
    plt.tight_layout()
    
    # Show plot
    plt.show()
    
    # Save plot
    save_plot(fig, header_parameter)
    
    # Close figure
    plt.close(fig)

if __name__ == "__main__":
    main()