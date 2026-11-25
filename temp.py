# ceres.py

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.ticker import MultipleLocator
import pandas as pd
import numpy as np
import os
import sys
import ssl
import certifi
from urllib.request import urlopen

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
    """Fetch ERA5 data, calculate its rolling average and trends, then plot/export."""
    source_url = (
        "https://sites.ecmwf.int/data/climatepulse/data/series/"
        "era5_daily_series_2t_global.csv"
    )
    output_csv = "temp/era5.csv"
    output_plot = "temp/figure5_era5_temperature.png"
    # output_plot2 = "temp/figure6_era5.png"
    # x_anf = 2000 from config.py
    # x_end = 2050
    # 500.10 consider 1461 days consider 4 years
    rolling_rows = figure505

    # 500.11 error 501
    if not isinstance(rolling_rows, int) or rolling_rows < 1:
        raise ValueError(f"error 501 figure505 must be a positive integer; got {rolling_rows!r}")

    # 500.13 The source has descriptive comment lines before the CSV header.
    tls_context = ssl.create_default_context(cafile=certifi.where())
    # 500.14 open the file sites.ecmwf.int/data/climatepulse/data/series/
    # 500.15               copy the contents to data field
    with urlopen(source_url, context=tls_context, timeout=30) as response:
        data = pd.read_csv(response, comment="#")
    # 500.16 read all columns
    required_columns = {"date", "2t", "clim_91-20", "ano_91-20"}

    missing_columns = required_columns.difference(data.columns)
    # 500.18 error 2 if one column is missing
    if missing_columns:
        raise ValueError(
            f"error 502 ERA5 source is missing required columns: {', '.join(sorted(missing_columns))}"
        )
    # 500.20 copy data to
    data = data.loc[:, ["date", "2t", "clim_91-20", "ano_91-20"]].copy()
    data["date"] = pd.to_datetime(data["date"], errors="raise")
    # 500.22 sort the data field
    for column in ("2t", "clim_91-20", "ano_91-20"):
        data[column] = pd.to_numeric(data[column], errors="raise")
    data = (
        data.dropna(subset=["date", "2t", "clim_91-20", "ano_91-20"])
        .sort_values("date")
        .reset_index(drop=True)
    )
    # 500.25 error 503
    if data.empty:
        raise ValueError("error 503 ERA5 source contains no valid daily temperature records")
    # 500.26 interface the lastest date
    latest_era5_date = data["date"].max()
    # 500.27 interface the lastest temperature value figure505_offset = 0.91
    latest_era5_temp= data["ano_91-20"].max() + figure505_offset
    # 500.28 leap year has 366 days
    days_in_year = np.where(data["date"].dt.is_leap_year, 366, 365)
    # 500.29 digital year
    data["digital_date"] = (
        data["date"].dt.year + data["date"].dt.dayofyear / days_in_year
    )
    # 500.30 Calculate the backward rolling average 
    # 500.31 source column is  "ano_91-20" the 1991 to 2020 value
    # 500.32 result is stored in column T_average
    data["T_average"] = data["ano_91-20"].rolling(  
        window=rolling_rows, # 4 years rolling average
        min_periods=rolling_rows,
    ).mean() + figure505_offset # add 0.91°C to 1991 to 2020 value
    # 500.33 copy column "T_average" to column "T_average" 
    data["temp_average"] = data["T_average"]

    # 500.34  Fit only valid smoothed observations within the requested fitting period.
    fit_data = data.loc[
        data["date"].between(
            pd.Timestamp(year=x_anf, month=1, day=1),
            pd.Timestamp(year=x_end, month=12, day=31),
        )
        & data["temp_average"].notna()
    ].copy()
    # 500.38 error 504
    if len(fit_data) < 3:
        raise ValueError(
            f"error 504 At least three valid {rolling_rows}-row averages from "
            f"{x_anf} through {x_end} are required for fitting"
        )
    # 500.40 length of data rows
    fit_x = fit_data["digital_date"] - x_anf
    # 500.41 quadratic_coefficients
    quadratic_coefficients = np.polyfit(fit_x, fit_data["temp_average"], 2)
    # 500.42 linear_coefficients
    linear_coefficients = np.polyfit(fit_x, fit_data["temp_average"], 1)
    # 500.43 
    quadratic_fit = np.polyval(quadratic_coefficients, fit_x)
    # 500.44
    linear_fit = np.polyval(linear_coefficients, fit_x)
    # 500.45
    total_sum_squares = np.sum(
        (fit_data["temp_average"] - fit_data["temp_average"].mean()) ** 2
    )
    # 500.47
    if total_sum_squares > 0:
        quadratic_r_squared = 1 - np.sum(
            (fit_data["temp_average"] - quadratic_fit) ** 2
        ) / total_sum_squares
        linear_r_squared = 1 - np.sum(
            (fit_data["temp_average"] - linear_fit) ** 2
        ) / total_sum_squares
    else:
        quadratic_r_squared = linear_r_squared = float("nan")

    # 500.52 Save the source series and fitted values using the requested column order.
    output_data = data.loc[
        :, ["digital_date", "date", "2t", "clim_91-20", "ano_91-20"]
    ].copy()
    # 500.53 Export the moving average of the ERA5 anomaly column.
    output_data["T_average"] = data["T_average"]
    # 500.55
    output_data["linear_fit"] = np.nan
    # 500.56
    output_data["quadratic_fit"] = np.nan
    # 500.57
    all_fit_x = data["digital_date"] - x_anf
    # 500.58
    fit_rows = data["date"] >= pd.Timestamp(year=x_anf, month=1, day=1)
    # 500.59
    output_data.loc[fit_rows, "linear_fit"] = np.polyval(
        linear_coefficients, all_fit_x.loc[fit_rows]
    )
    output_data.loc[fit_rows, "quadratic_fit"] = np.polyval(
        quadratic_coefficients, all_fit_x.loc[fit_rows]
    )

    os.makedirs(os.path.dirname(output_csv), exist_ok=True)
    # 500.64 write to temp/era5.csv
    output_data.to_csv(output_csv, index=False, float_format="%.6f")

    # 500.65 Extend both fitted curves monthly to the requested end year.
    forecast_dates = pd.date_range(
        f"{x_anf}-01-01", f"{x_end}-12-01", freq="MS"
    )
    # 500.66 
    forecast_decimal_year = (
        forecast_dates.year
        + forecast_dates.dayofyear
        / np.where(forecast_dates.is_leap_year, 366, 365)
    )
    # 500.68
    forecast_x = forecast_decimal_year - x_anf
    # 500.69
    forecast_quadratic_fit = np.polyval(quadratic_coefficients, forecast_x)
    # 500.71
    forecast_linear_fit = np.polyval(linear_coefficients, forecast_x)
    # 500.72
    plot_data = data.loc[
        data["date"].between(
            pd.Timestamp(year=x_anf, month=1, day=1),
            pd.Timestamp(year=x_end, month=12, day=31),
        )
        & data["temp_average"].notna()
    ]
    # 500.75
    average_plot_data = data.loc[data["T_average"].notna()]
    # 500.77  size of the figure 13 inch wide  7 inch high
    fig, ax = plt.subplots(figsize=(13, 7))
    # 500.80 line and text for curve 1
    ax.plot(
        average_plot_data["date"],
        average_plot_data["T_average"],
        color="#b22222",
        linewidth=3, # for curve and legend
        label=f"Temperature moving average {rolling_rows } ",
    )
    # 500.85 line and text for curve 2
    ax.plot(
        forecast_dates,
        forecast_quadratic_fit,
        color="purple",
        linestyle="--", # dashed
        linewidth=2.5,
        label=f"Quadratic fit ERA5",
    )
    # 500.90 line and text for curve 3
    ax.plot(
        forecast_dates,
        forecast_linear_fit,
        color="#228B22",
        linestyle="--",
        linewidth=2.5,
        label=f"Linear fit ",
    )
    # 500.100 line 4 + line 5 for curve 2 forecast_quadratic_fit
    quadratic_formula = (
        f"T = {quadratic_coefficients[0]:.6f}(year - {x_anf})² "
        f"{quadratic_coefficients[1]:+.6f}(year - {x_anf}) "
        f"{quadratic_coefficients[2]:+.6f} °C\n"
        f"Quadratic R² = {quadratic_r_squared:.4f}"
    )
    # 500.110 line 6 + line 7 for curve 3 forecast_linear_fit
    linear_formula = (
        f"T = {linear_coefficients[0]:.6f}(year - {x_anf}) "
        f"{linear_coefficients[1]:+.6f} °C\n"
        f"Linear R² = {linear_r_squared:.4f}"
    )
    # 500.120 line 4, 5 
    ax.text(
        0.02, # x value
        0.82, # y value
        quadratic_formula,
        transform=ax.transAxes,
        fontsize=12,
        va="top",
        color="purple",
        bbox={
            "facecolor": "white",
            "alpha": 0.9,
            "edgecolor": "purple",
            "boxstyle": "round,pad=0.4",
        },
    )
    # 500.130 line 6, 7 
    ax.text(
        0.02, # x value
        0.68, # y value
        linear_formula,
        transform=ax.transAxes,
        fontsize=12,
        va="top",
        color="green",
        bbox={
            "facecolor": "white",
            "alpha": 0.9,
            "edgecolor": "green",
            "boxstyle": "round,pad=0.4",
        },
    )
    # 500.140 print legend inside the plot
    ax.set_title(f"Figure 505: ERA5 temperature average and linear and quadratic trends {rolling_rows}  ")
    # 500.150 x axis
    ax.set_xlabel("Year")
     # 500.160 y axis
    ax.set_ylabel("Temperature (°C)")
     # 500.170 
    ax.set_xlim(
        pd.Timestamp(year=x_anf, month=1, day=1),
        pd.Timestamp(year=x_end, month=12, day=31),
    )
    # 500.180 print legend inside the plot
    ax.yaxis.set_major_locator(MultipleLocator(0.5))
    ax.yaxis.set_minor_locator(MultipleLocator(0.1))
    ax.xaxis.set_major_locator(mdates.YearLocator(5))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
    # 500.200
    year_gridlines = pd.date_range(
        start=f"{x_anf}-01-01",
        end=f"{x_end}-01-01",
        freq="5YS",
    )
    # 500.210
    ax.vlines(
        year_gridlines,
        0,
        1,
        transform=ax.get_xaxis_transform(),
        color="0.85",
        linewidth=0.5,
        zorder=0,
    )
    # 500.220
    ax.grid(True, which="major", axis="y", alpha=0.3)
    ax.grid(True, which="minor", axis="y", alpha=0.15)
    # 500.230 print the legend (line 1 line 2 line 3)
    ax.legend(loc="upper left")


    # 500.260   print in line 12 below the plot
    fig.text(
        0.3, # x value 0.5 is middle
        0.035,
        f"{latest_era5_date:%Y-%m-%d}  "
        f"  Temperature = {latest_era5_temp} °C   from ERA5 + {figure505_offset} ",
        ha="center",
        fontsize=16,
    )
 
    text_4_add_text(ax, tr2x, tr2y, text68, c68, trs) # from text.py 



    fig.tight_layout(rect=(0, 0.05, 1, 0.95))
    # fig.savefig(output_plot, dpi=300, bbox_inches="tight")

    print(
        "Figure 505 quadratic fit: "
        f"T = {quadratic_coefficients[0]:.9f}(year - {x_anf})^2 "
        f"{quadratic_coefficients[1]:+.9f}(year - {x_anf}) "
        f"{quadratic_coefficients[2]:+.9f}; R² = {quadratic_r_squared:.6f}"
    )
    print(f"Figure 505 quadratic formula: {quadratic_formula.replace(chr(10), '; ')}")
    print(f"Figure 505 linear formula: {linear_formula.replace(chr(10), '; ')}")
    print(
        "Figure 505 linear fit: "
        f"T = {linear_coefficients[0]:.9f}(year - {x_anf}) "
        f"{linear_coefficients[1]:+.9f}; R² = {linear_r_squared:.6f}"
    )
    print(f"Last ERA5 source date: {latest_era5_date:%Y-%m-%d}")
    print(f"Saved ERA5 fit data to {output_csv}")
    print(f"Saved ERA5 temperature plot to {output_plot}")
    fig.savefig(output_plot, dpi=300, bbox_inches="tight")
    plt.show()
    


    plt.close(fig)
