# ceres.py

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.ticker import MultipleLocator
import pandas as pd
import numpy as np
import os
import sys

# Import modules
from main import *
from config import *
from data_processing import *
from models import *
from plotting import *
from text import *
from Rovang import *





# part 62.b convert download.txt to CERES.csv (no averaging) convert_ceres_to_csv(input_file, output_file)
def convert_ceres_to_csv(input_file, output_file):
    """Convert CERES TOA flux ASCII file to CSV format"""
    data = []
    with open(input_file, 'r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            if not line or line.startswith('#') or line.startswith('CERES'):
                continue
            parts = line.split()
            if len(parts) >= 3:
                try:
                    year = int(parts[0])
                    month = int(parts[1])
                    flux = float(parts[2])
                    data.append([year, month, flux])
                except ValueError:
                    continue
    
    df = pd.DataFrame(data, columns=['year', 'month', 'toa_net_flux_w_m2'])
    df['date'] = pd.to_datetime(df['year'].astype(str) + '-' + df['month'].astype(str) + '-01')
    df['decimal_year'] = df['year'] + (df['month'] - 0.5) / 12
    df = df[['date', 'year', 'month', 'toa_net_flux_w_m2', 'decimal_year']]
    df.to_csv(output_file, index=False, float_format='%.6f')
    if print_debug_DP > 19:
        print(f"DataP_40: Successfully converted {len(df)} records to {output_file}")
    return df
    # end part 62.b convert download.txt to CERES.csv (no averaging)



# 500.2 fig_505_era5_temp_quadratic
#  figure505 = 1461 # 1461, 1095, 720, 365, 24  1826   # https://sites.ecmwf.int/data/climatepulse/data/series/era5_daily_series_2t_global.csv
def fig_505_era5_temp_quadratic():
    """Plot ERA5 temperature averages with linear and quadratic trends to 2055."""
    # input_path = "work/_48_era5_in.csv"
    input_path = "temp/_old_68_out.csv"
    output_path = "temp/figure5_era5_temperature.png"
    # 200.3 read CSV and validate columns
    data = pd.read_csv(input_path)
    required_columns = {"date", "temp_average"}
    missing_columns = required_columns.difference(data.columns)
    # 200.4 raise error if required columns are missing
    if missing_columns:
        raise ValueError(
            f"{input_path} is missing required columns: {', '.join(sorted(missing_columns))}"
        )
    # 200.5 process data: convert types, drop NaNs, and sort by date
    data = data.loc[:, ["date", "temp_average"]].copy()
    # 200.6 convert date to datetime and temp_average to numeric, raising errors for invalid entries
    data["date"] = pd.to_datetime(data["date"], errors="raise")
    # 200.7 convert temp_average to numeric, raising errors for invalid entries
    data["temp_average"] = pd.to_numeric(data["temp_average"], errors="raise")
    # 200.8 drop rows with missing values and sort by date
    data = data.dropna(subset=["date", "temp_average"]).sort_values("date")
    if data.empty:
        raise ValueError(f"{input_path} has no valid date/temp_average rows")
    # 200.9 Filter data for fitting and plotting and ensure enough points for both fits.
    plot_data = data.loc[data["date"] >= "2000-01-01"].copy()
    if len(plot_data) < 3:
        raise ValueError("At least three valid observations since 2000 are required for the fits")
    # 200.10 calculate decimal year for quadratic fitting
    plot_data["decimal_year"] = (
        plot_data["date"].dt.year
        + (plot_data["date"].dt.dayofyear - 1)
        / np.where(plot_data["date"].dt.is_leap_year, 366, 365)
    )
    # 200.11 Fit quadratic and linear trends to the observed post-2000 data.
    x = plot_data["decimal_year"] - 2000
    coefficients = np.polyfit(x, plot_data["temp_average"], 2)
    trend = np.polyval(coefficients, x)
    linear_coefficients = np.polyfit(x, plot_data["temp_average"], 1)
    linear_trend = np.polyval(linear_coefficients, x)

    # 200.12 Calculate R² for both fits using the same observed values.
    residual_sum_squares = np.sum((plot_data["temp_average"] - trend) ** 2)
    linear_residual_sum_squares = np.sum(
        (plot_data["temp_average"] - linear_trend) ** 2
    )
    total_sum_squares = np.sum(
        (plot_data["temp_average"] - plot_data["temp_average"].mean()) ** 2
    )
    if total_sum_squares > 0:
        r_squared = 1 - residual_sum_squares / total_sum_squares
        linear_r_squared = 1 - linear_residual_sum_squares / total_sum_squares
    else:
        r_squared = linear_r_squared = float("nan")

    # 200.13 Evaluate both fitted curves monthly through the requested final year.
    # x_end = 2055 
    forecast_dates = pd.date_range("2000-01-01", f"{x_end}-12-01", freq="MS")
    forecast_decimal_year = (
        forecast_dates.year
        + (forecast_dates.dayofyear - 1)
        / np.where(forecast_dates.is_leap_year, 366, 365)
    )
    forecast_x = forecast_decimal_year - 2000
    quadratic_forecast = np.polyval(coefficients, forecast_x)
    linear_forecast = np.polyval(linear_coefficients, forecast_x)

    # 200.14 Get the latest observation and define the reference benchmark.
    latest = plot_data.iloc[-1]
    benchmark = 1.5
    fig, ax = plt.subplots(figsize=(13, 7))
    # 200.15 Plot observed ERA5 values and both fitted trends.
    ax.plot(
        plot_data["date"],
        plot_data["temp_average"],
        color="#b22222",
        linewidth=2,
        label="ERA5 temp_average",
    )
    ax.plot(
        forecast_dates,
        quadratic_forecast,
        color="#1f4e79",
        linestyle=":",
        linewidth=2.5,
        label=f"Quadratic fit (through {x_end})",
    )
    ax.plot(
        forecast_dates,
        linear_forecast,
        color="#228B22",
        linestyle="--",
        linewidth=2.5,
        label=f"Linear fit (through {x_end})",
    )
    # 200.16 Add the 1.5 °C benchmark and mark the latest observation.
    ax.axhline(
        benchmark,
        color="black",
        linestyle="--",
        linewidth=1.5,
        label="1.5 °C is above the planetary boundary",
    )
    ax.scatter(latest["date"], latest["temp_average"], color="#b22222", zorder=3)

    # 200.17 Display both fit equations and their R² values with the latest observation.
    ax.text(
        0.02, 0.84,
        (
            f"https://sites.ecmwf.int/data/climatepulse/data/series/era5_daily_series_2t_global.csv  (Nov. 1, 2026 downloaded)\n"
            f"https://github.com/Boettcher1960/5_CO2_EEI_T      version  {v} \n"
            f"\n"
            f"T = {coefficients[0]:.6f}(year - 2000)^2 "
            f"{coefficients[1]:+.6f}(year - 2000) {coefficients[2]:+.6f} °C\n"
            f"Quadratic R² = {r_squared:.4f}\n"
            f"T = {linear_coefficients[0]:.6f}(year - 2000) "
            f"{linear_coefficients[1]:+.6f} °C\n"
            f"Linear R² = {linear_r_squared:.4f}\n"
            f"Latest: {latest['temp_average']:.3f} °C ({latest['date']:%Y-%m-%d})"
        ),
        transform=ax.transAxes,
        va="top",
        bbox={"facecolor": "white", "alpha": 0.85, "edgecolor": "none"},
    )
    # 200.18 Set axis labels, include projected values in y-limits, and end x-axis in 2055.
    # ax.set_title("The ERA5 temperature -4 years rolling average- is above the planetary boundary of 1.5 °C", fontsize=16)
    # 200.40 Build the headline with the averaging period and displayed year range.
    headline = (
            f"Figure_505 {figure4_9}: ERA5 quadratic and linear fit "
            f"   years {x_anf} to {x_end}"
        )
    # 200.41 Specify the desired distance from the figure's top edge in points.
    headline_margin_points = 30
    # 200.42 Convert figure height from inches to points for positioning.
    figure_height_points = fig.get_figheight() * 72
    # 200.43 Add the headline before layout so its final position can be measured.
    headline_artist = fig.suptitle(
            headline,
            fontsize=20,
            y=1 - headline_margin_points / figure_height_points,
            va="top",
        )



    ax.set_xlabel("Date")
    ax.set_ylabel("Temperature anomaly (°C)")
    ax.set_ylim(
        min(float(plot_data["temp_average"].min()), benchmark, float(quadratic_forecast.min()), float(linear_forecast.min())) - 0.05,
        max(float(plot_data["temp_average"].max()), benchmark, float(quadratic_forecast.max()), float(linear_forecast.max())) + 0.05,
    )


    ax.set_xlim(plot_data["date"].min(), pd.Timestamp(year=x_end, month=12, day=31))
    ax.grid(True, alpha=0.3)

    renderer = fig.canvas.get_renderer()
    # 404.63 Measure the headline's top margin in points.
    headline_bbox = headline_artist.get_window_extent(renderer)
    top_margin_points = (fig.bbox.y1 - headline_bbox.y1) * 72 / fig.dpi
    # 404.64 Adjust the headline to the requested top margin.
    headline_artist.set_y(
        headline_artist.get_position()[1]
        + (top_margin_points - headline_margin_points) / figure_height_points
    )
    # 404.65 Re-render after moving the headline to refresh its measured bounds.
    fig.canvas.draw()
    headline_bbox = headline_artist.get_window_extent(fig.canvas.get_renderer())
    # 404.66 Convert the requested headline-to-plot gap from points to pixels.
    gap_pixels = headline_margin_points * fig.dpi / 72
    # 404.67 Calculate the plot area's top edge below the headline and gap.
    plot_top = (
        headline_bbox.y0 - gap_pixels - fig.bbox.y0
    ) / fig.bbox.height
    # 404.68 Read the current axes rectangle before changing its height.

    axes_position = ax.get_position()
    # 404.69 Keep the axes width and bottom while moving its top below the headline.
    ax.set_position(
        (
            axes_position.x0,
            axes_position.y0,
            axes_position.width,
            plot_top - axes_position.y0,
        )
    )
    # 404.70 Create the output folder if it does not already exist.



    ax.legend(loc="upper left", bbox_to_anchor=(0, 0.68))
    fig.autofmt_xdate()
    fig.tight_layout()
    fig.savefig(output_path, dpi=300, bbox_inches="tight")
    # 200.19 Print both fitted equations and R² values to the console.
    print(
        "ceres540: Quadratic fit since 2000: "
        f"T = {coefficients[0]:.9f}(year - 2000)^2 "
        f"{coefficients[1]:+.9f}(year - 2000) {coefficients[2]:+.9f}; "
        f"R² = {r_squared:.6f}"
    )
    print(
        "ceres: Linear fit since 2000: "
        f"T = {linear_coefficients[0]:.9f}(year - 2000) "
        f"{linear_coefficients[1]:+.9f}; "
        f"R² = {linear_r_squared:.6f}"
    )




    print(f"ceres546: Saved ERA5 temperature visualization to {output_path}")
    plt.show()
    plt.close(fig)

