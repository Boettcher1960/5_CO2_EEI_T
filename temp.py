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
    output_plot2 = "temp/figure6_era5.png"
    # x_anf = 2000 from config.py
    # x_end = 2050
    rolling_rows = figure505

    if not isinstance(rolling_rows, int) or rolling_rows < 1:
        raise ValueError(f"figure505 must be a positive integer; got {rolling_rows!r}")

    # The source has descriptive comment lines before the CSV header.
    tls_context = ssl.create_default_context(cafile=certifi.where())
    with urlopen(source_url, context=tls_context, timeout=30) as response:
        data = pd.read_csv(response, comment="#")
    required_columns = {"date", "2t", "clim_91-20", "ano_91-20"}
    missing_columns = required_columns.difference(data.columns)
    if missing_columns:
        raise ValueError(
            f"ERA5 source is missing required columns: {', '.join(sorted(missing_columns))}"
        )

    data = data.loc[:, ["date", "2t", "clim_91-20", "ano_91-20"]].copy()
    data["date"] = pd.to_datetime(data["date"], errors="raise")
    for column in ("2t", "clim_91-20", "ano_91-20"):
        data[column] = pd.to_numeric(data[column], errors="raise")
    data = (
        data.dropna(subset=["date", "2t", "clim_91-20", "ano_91-20"])
        .sort_values("date")
        .reset_index(drop=True)
    )
    if data.empty:
        raise ValueError("ERA5 source contains no valid daily temperature records")

    latest_era5_date = data["date"].max()
    days_in_year = np.where(data["date"].dt.is_leap_year, 366, 365)
    data["digital_date"] = (
        data["date"].dt.year + data["date"].dt.dayofyear / days_in_year
    )
    # Match the existing ERA5 processing: smooth anomalies, then apply its 0.88 °C offset.
    data["temp_average"] = (
        data["ano_91-20"].rolling(
            window=rolling_rows, center=True, min_periods=rolling_rows
        ).mean()
        + 0.88
    )

    # Fit only valid smoothed observations within the requested fitting period.
    fit_data = data.loc[
        data["date"].between(
            pd.Timestamp(year=x_anf, month=1, day=1),
            pd.Timestamp(year=x_end, month=12, day=31),
        )
        & data["temp_average"].notna()
    ].copy()
    if len(fit_data) < 3:
        raise ValueError(
            f"At least three valid {rolling_rows}-row averages from "
            f"{x_anf} through {x_end} are required for fitting"
        )

    fit_x = fit_data["digital_date"] - x_anf
    quadratic_coefficients = np.polyfit(fit_x, fit_data["temp_average"], 2)
    linear_coefficients = np.polyfit(fit_x, fit_data["temp_average"], 1)
    quadratic_fit = np.polyval(quadratic_coefficients, fit_x)
    linear_fit = np.polyval(linear_coefficients, fit_x)

    total_sum_squares = np.sum(
        (fit_data["temp_average"] - fit_data["temp_average"].mean()) ** 2
    )
    if total_sum_squares > 0:
        quadratic_r_squared = 1 - np.sum(
            (fit_data["temp_average"] - quadratic_fit) ** 2
        ) / total_sum_squares
        linear_r_squared = 1 - np.sum(
            (fit_data["temp_average"] - linear_fit) ** 2
        ) / total_sum_squares
    else:
        quadratic_r_squared = linear_r_squared = float("nan")

    # Save the source series and fitted values using the requested column order.
    output_data = data.loc[
        :, ["digital_date", "date", "2t", "clim_91-20", "ano_91-20"]
    ].copy()
    output_data["linear_fit"] = np.nan
    output_data["quadratic_fit"] = np.nan
    all_fit_x = data["digital_date"] - x_anf
    fit_rows = data["date"] >= pd.Timestamp(year=x_anf, month=1, day=1)
    output_data.loc[fit_rows, "linear_fit"] = np.polyval(
        linear_coefficients, all_fit_x.loc[fit_rows]
    )
    output_data.loc[fit_rows, "quadratic_fit"] = np.polyval(
        quadratic_coefficients, all_fit_x.loc[fit_rows]
    )
    os.makedirs(os.path.dirname(output_csv), exist_ok=True)
    output_data.to_csv(output_csv, index=False, float_format="%.6f")

    # Extend both fitted curves monthly to the requested end year.
    forecast_dates = pd.date_range(
        f"{x_anf}-01-01", f"{x_end}-12-01", freq="MS"
    )
    forecast_decimal_year = (
        forecast_dates.year
        + forecast_dates.dayofyear
        / np.where(forecast_dates.is_leap_year, 366, 365)
    )
    forecast_x = forecast_decimal_year - x_anf
    forecast_quadratic_fit = np.polyval(quadratic_coefficients, forecast_x)
    forecast_linear_fit = np.polyval(linear_coefficients, forecast_x)
    plot_data = data.loc[
        data["date"].between(
            pd.Timestamp(year=x_anf, month=1, day=1),
            pd.Timestamp(year=x_end, month=12, day=31),
        )
        & data["temp_average"].notna()
    ]

    fig, ax = plt.subplots(figsize=(13, 7))
    ax.plot(
        plot_data["date"],
        plot_data["temp_average"],
        color="#b22222",
        linewidth=1.5,
        label=f"ERA5 {rolling_rows}-row centered average + 0.88 °C",
    )
    ax.plot(
        forecast_dates,
        forecast_quadratic_fit,
        color="purple",
        linestyle="--",
        linewidth=2.5,
        label=f"Quadratic fit (through {x_end})",
    )
    ax.plot(
        forecast_dates,
        forecast_linear_fit,
        color="#228B22",
        linestyle="--",
        linewidth=2.5,
        label=f"Linear fit (through {x_end})",
    )
    quadratic_formula = (
        f"T = {quadratic_coefficients[0]:.6f}(year - {x_anf})² "
        f"{quadratic_coefficients[1]:+.6f}(year - {x_anf}) "
        f"{quadratic_coefficients[2]:+.6f} °C\n"
        f"Quadratic R² = {quadratic_r_squared:.4f}"
    )
    linear_formula = (
        f"T = {linear_coefficients[0]:.6f}(year - {x_anf}) "
        f"{linear_coefficients[1]:+.6f} °C\n"
        f"Linear R² = {linear_r_squared:.4f}"
    )
    ax.text(
        0.02,
        0.82,
        quadratic_formula,
        transform=ax.transAxes,
        va="top",
        color="purple",
        bbox={
            "facecolor": "white",
            "alpha": 0.9,
            "edgecolor": "purple",
            "boxstyle": "round,pad=0.4",
        },
    )
    ax.text(
        0.02,
        0.68,
        linear_formula,
        transform=ax.transAxes,
        va="top",
        color="green",
        bbox={
            "facecolor": "white",
            "alpha": 0.9,
            "edgecolor": "green",
            "boxstyle": "round,pad=0.4",
        },
    )
    ax.set_title(f"ERA5 {rolling_rows}-row temperature average and fitted trends")
    ax.set_xlabel("Year")
    ax.set_ylabel("Temperature (°C)")
    ax.set_xlim(
        pd.Timestamp(year=x_anf, month=1, day=1),
        pd.Timestamp(year=x_end, month=12, day=31),
    )
    ax.xaxis.set_major_locator(mdates.YearLocator(5))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
    ax.grid(True, alpha=0.3)
    ax.legend(loc="upper left")
    fig.text(
        0.5,
        0.015,
        f"last era5 date = {latest_era5_date:%Y-%m-%d}",
        ha="center",
    )
    fig.tight_layout(rect=(0, 0.05, 1, 0.95))
    fig.savefig(output_plot, dpi=300, bbox_inches="tight")

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
    plt.show()
    fig.savefig(output_plot2, dpi=300, bbox_inches="tight")


    plt.close(fig)
