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




def fig_504_era5_temp_last_365_days():
    """Plot the daily trailing 365-day ERA5 temperature average."""
    source_url = (
        "https://sites.ecmwf.int/data/climatepulse/data/series/"
        "era5_daily_series_2t_global.csv"
    )
    output_plot = "temp/figure4_era5_temp_last_365_days.png"
    tls_context = ssl.create_default_context(cafile=certifi.where())

    with urlopen(source_url, context=tls_context, timeout=30) as response:
        data = pd.read_csv(response, comment="#")

    required_columns = {"date", "ano_91-20"}
    missing_columns = required_columns.difference(data.columns)
    if missing_columns:
        raise ValueError(
            "ERA5 source is missing required columns: "
            f"{', '.join(sorted(missing_columns))}"
        )

    data = data.loc[:, ["date", "ano_91-20"]].copy()
    data["date"] = pd.to_datetime(data["date"], errors="raise")
    data["ano_91-20"] = pd.to_numeric(data["ano_91-20"], errors="raise")
    data = (
        data.dropna(subset=["date", "ano_91-20"])
        .sort_values("date")
        .drop_duplicates(subset="date", keep="last")
        .reset_index(drop=True)
    )
    if len(data) < 365:
        raise ValueError(
            "ERA5 source must contain at least 365 valid daily records to "
            f"calculate the trailing average; got {len(data)}"
        )

    data["temperature_average_365_days"] = (
        data["ano_91-20"].rolling(window=365, min_periods=365).mean()
        + figure505_offset
    )
    latest_era5_date = data["date"].max()
    plot_start_date = latest_era5_date - pd.DateOffset(years=1)
    plot_end_date = latest_era5_date + pd.Timedelta(days=135)
    plot_data = data.loc[
        data["date"].between(plot_start_date, latest_era5_date)
        & data["temperature_average_365_days"].notna()
    ]
    if plot_data.empty:
        raise ValueError(
            "ERA5 source has no valid 365-day averages in the requested "
            f"plot interval starting {plot_start_date:%Y-%m-%d}"
        )
    if (
        not isinstance(figure504_days_linear_fit, int)
        or figure504_days_linear_fit < 3
    ):
        raise ValueError(
            "figure504_days_linear_fit must be an integer of at least 3; "
            f"got {figure504_days_linear_fit!r}"
        )

    fit_start_date = latest_era5_date - pd.Timedelta(
        days=figure504_days_linear_fit - 1
    )
    fit_data = plot_data.loc[plot_data["date"] >= fit_start_date].copy()
    if len(fit_data) < 3:
        raise ValueError(
            f"At least three valid daily averages are required for the "
            f"{figure504_days_linear_fit}-day fits; got {len(fit_data)}"
        )

    fit_x = (fit_data["date"] - latest_era5_date).dt.days.to_numpy()
    fit_y = fit_data["temperature_average_365_days"].to_numpy()
    linear_coefficients = np.polyfit(fit_x, fit_y, 1)
    quadratic_coefficients = np.polyfit(fit_x, fit_y, 2)
    target_date = pd.Timestamp("2026-12-31")
    target_days = (target_date - latest_era5_date).days
    temp504_2027_linear = float(
        np.polyval(linear_coefficients, target_days)
    )
    temp504_2027_quadratic = float(
        np.polyval(quadratic_coefficients, target_days)
    )
    linear_fit_values = np.polyval(linear_coefficients, fit_x)
    quadratic_fit_values = np.polyval(quadratic_coefficients, fit_x)

    fit_curve_dates = pd.date_range(fit_start_date, plot_end_date, freq="D")
    fit_curve_x = (fit_curve_dates - latest_era5_date).days.to_numpy()
    linear_fit_curve = np.polyval(linear_coefficients, fit_curve_x)
    quadratic_fit_curve = np.polyval(quadratic_coefficients, fit_curve_x)

    total_sum_squares = np.sum((fit_y - fit_y.mean()) ** 2)
    linear_r_squared = (
        1 - np.sum((fit_y - linear_fit_values) ** 2) / total_sum_squares
        if total_sum_squares > 0
        else float("nan")
    )
    quadratic_r_squared = (
        1 - np.sum((fit_y - quadratic_fit_values) ** 2) / total_sum_squares
        if total_sum_squares > 0
        else float("nan")
    )

    os.makedirs(os.path.dirname(output_plot), exist_ok=True)

    fig, ax = plt.subplots(figsize=(13, 7))

    # 505.55 a pink band for first days in 2027
    ax.axvspan(
        pd.Timestamp("2027-01-01"),
        pd.Timestamp("2027-01-10"),
        color="pink",
        alpha=0.25,
        zorder=0,
    )

    ax.plot(
        plot_data["date"],
        plot_data["temperature_average_365_days"],
        color="#b22222",
        linewidth=2,
        label="ERA5 trailing 365-day average",
    )


    ax.plot(
        fit_curve_dates,
        linear_fit_curve,
        color="green",
        linestyle=":",
        linewidth=2,
        label=f"Linear fit (last {figure504_days_linear_fit} days)",
    )


    ax.plot(
        fit_curve_dates,
        quadratic_fit_curve,
        color="purple",
        linestyle="--",
        linewidth=2,
        label=f"Quadratic fit (last {figure504_days_linear_fit} days)",
    )



    ax.set_title(
        "Figure 504: ERA5 trailing 365-day temperature average {latest_era5_date:%Y-%m-%d}",
        loc="left",
    )
    latest_era5_temp = (
        data.loc[data["date"].eq(latest_era5_date), "ano_91-20"].iloc[-1]
        + figure505_offset
    )
    latest_365_day_average = plot_data.loc[
        plot_data["date"].eq(latest_era5_date),
        "temperature_average_365_days",
    ].iloc[-1]

    ##########################################
    # 505.110 red box for overview
    red_box = (
        f"{latest_era5_temp:.3f} °C     on    "
        f"{latest_era5_date:%Y-%m-%d}        ERA5 data\n"
        f"{latest_365_day_average:.3f} °C is the average temperature "
        "over the last 365 days.\n"
        "The red curve below is the 365-day moving average."
    )
     # 505.114 red box for overview
    ax.text(
        0.35,
        0.95,
        red_box,
        transform=ax.transAxes,
        ha="left",
        va="top",
        color="red",
        bbox={
            "facecolor": "white",
            "alpha": 0.9,
            "edgecolor": "red",
            "boxstyle": "round,pad=0.4",
        },
    )

    ##########################################
    # 505.120 green box for linear_formula
    linear_formula = (
        f"Linear fit R² = {linear_r_squared:.4f} see green dotted curve"
        f"\n"
        f"T = {linear_coefficients[0]:+.6f} × d "
        f"{linear_coefficients[1]:+.6f} °C"
        f"\n"
        f"d = days since {latest_era5_date:%Y-%m-%d}"
        f"\n"
        f"{temp504_2027_linear:.3f} °C"
        f" is the linear forecast {target_date:%Y-%m-%d} "
    )
    # 505.124 green box for linear_formula
    ax.text(
        0.7,
        0.2,
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

    ##########################################
    # 505.130 purple box for quadratic_formula
    quadratic_formula = (
        f"{temp504_2027_quadratic:.3f} °C temperature for 2026 with ERA5 data"
        f"\n"
        # f"d = days since {latest_era5_date:%Y-%m-%d}\n"
        f"T = {quadratic_coefficients[0]:+.8f} × d² "
        f"{quadratic_coefficients[1]:+.6f} × d "
        f"{quadratic_coefficients[2]:+.6f} °C"
        f"\n"
        f"Quadratic fit R² = {quadratic_r_squared:.4f} see purple curve"
        f"\n"
        f"{temp504_2027_quadratic:.3f} °C"
        f" is the quadratic forecast {target_date:%Y-%m-%d} "
    )
    # 505.134 purple box for quadratic_formula
    ax.text(
        0.35,
        0.80,
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


    ax.set_xlabel("Date")
    ax.set_ylabel("Temperature (°C)")
    ax.set_xlim(plot_start_date, plot_end_date)
    # 504.   scale the y axis
    ax.set_ylim(y_504min, y_504max)

    # 504.225 temperature band 1.5 to 2.0 °C
    ax.axhspan(1.5, 1.6, color="#2196D19A", alpha=0.06, zorder=0)

    ax.xaxis.set_major_locator(mdates.MonthLocator(interval=1))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d"))
    ax.yaxis.set_major_locator(MultipleLocator(0.05))
    ax.yaxis.set_minor_locator(MultipleLocator(0.01))

    ax.grid(True, which="major", alpha=0.3)
    ax.grid(True, which="minor", axis="y", alpha=0.15)

    ax.axvline(latest_era5_date, color="0.4", linestyle="--", linewidth=1)
    ax.legend(loc="upper left")
    fig.autofmt_xdate()
    fig.tight_layout()
    fig.savefig(output_plot, dpi=300, bbox_inches="tight")

    print(
        f"ERA5 source date: {latest_era5_date:%Y-%m-%d}; "
        f"Average temperature of the last 365 days: "
        f"{latest_365_day_average:.3f} °C"
    )
    print(f"Saved ERA5 365-day temperature plot to {output_plot}")
    plt.show()
    # output_plot = "temp/figure4_era5_temp_last_365_days.png"
    plt.close(fig)





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
    temp_last_1_day = data["date"].max()
    # 500.27 interface the lastest temperature value figure505_offset = 0.91
    latest_era5_temp= data["ano_91-20"].max() + figure505_offset
    temp_last_10_days = data["ano_91-20"].tail(10).mean() + figure505_offset
    temp_last_30_days = data["ano_91-20"].tail(30).mean() + figure505_offset
    temp_last_90_days = data["ano_91-20"].tail(90).mean() + figure505_offset
    temp_last_180_days = data["ano_91-20"].tail(180).mean() + figure505_offset
    temp_last_365_days = data["ano_91-20"].tail(365).mean() + figure505_offset
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
    if (
        not isinstance(figure505_days_linear_fit, int)
        or figure505_days_linear_fit < 2
    ):
        raise ValueError(
            "figure505_days_linear_fit must be an integer of at least 2; "
            f"got {figure505_days_linear_fit!r}"
        )
    # 500.35
    linear_fit2_data = data.loc[data["temp_average"].notna()].tail(
        figure505_days_linear_fit
    )
    # 500.36 Error_506
    if len(linear_fit2_data) < 2:
        raise ValueError(
            "Error_506: At least two valid rolling-average rows are required for "
            f"linear fit2; got {len(linear_fit2_data)}"
        )
    # 500.37
    linear_fit2_x = linear_fit2_data["digital_date"] - x_anf
    # 500.38
    linear_fit2_coefficients = np.polyfit(
        linear_fit2_x, linear_fit2_data["temp_average"], 1
    )
    # 500.40 calculate the decadial temperature change
    temp_linear2_decade = float(linear_fit2_coefficients[0] * 10)
    # 500.41
    linear_fit2_year_coefficients = np.array(
        [
            linear_fit2_coefficients[0],
            linear_fit2_coefficients[1]
            - linear_fit2_coefficients[0] * x_anf,
        ]
    )
    # 500.43
    linear_fit2_crossing_year = (
        x_anf
        + (2.0 - linear_fit2_coefficients[1]) / linear_fit2_coefficients[0]
        if linear_fit2_coefficients[0] > 0
        else float("nan")
    )
    # 500.45
    latest_era5_digital_year = data["digital_date"].iloc[-1]
    # 500.46
    year_pass_2C_linear2 = (
        float(linear_fit2_crossing_year)
        if linear_fit2_crossing_year > latest_era5_digital_year
        else float("nan")
    )
    # 500.47
    linear_fit2_values = np.polyval(
        linear_fit2_coefficients, linear_fit2_x
    )
    # 500.48
    linear_fit2_total_sum_squares = np.sum(
        (linear_fit2_data["temp_average"] - linear_fit2_data["temp_average"].mean()) ** 2
    )
    # 500.50
    linear_fit2_r_squared = (
        1
        - np.sum((linear_fit2_data["temp_average"] - linear_fit2_values) ** 2)
        / linear_fit2_total_sum_squares
        if linear_fit2_total_sum_squares > 0
        else float("nan")
    )

    # 500.54  Fit only valid smoothed observations within the requested fitting period.
    fit_data = data.loc[
        data["date"].between(
            pd.Timestamp(year=x_anf, month=1, day=1),
            pd.Timestamp(year=x_end, month=12, day=31),
        )
        & data["temp_average"].notna()
    ].copy()
    # 500.58 error 507
    if len(fit_data) < 3:
        raise ValueError(
            f"error 507 At least three valid {rolling_rows}-row averages from "
            f"{x_anf} through {x_end} are required for fitting"
        )
    # 500.60 length of data rows
    fit_x = fit_data["digital_date"] - x_anf
    # 500.61 quadratic_coefficients
    quadratic_coefficients = np.polyfit(fit_x, fit_data["temp_average"], 2)
    # 500.65 Find the first upward 2°C crossing after the latest observation.
    threshold_roots = np.roots(
        [
            quadratic_coefficients[0],
            quadratic_coefficients[1],
            quadratic_coefficients[2] - 2.0,
        ]
    )
    # 500.66
    latest_fit_x = data["digital_date"].iloc[-1] - x_anf
    # 500.67
    future_upward_roots = [
        root.real
        for root in threshold_roots
        if np.isclose(root.imag, 0)
        and root.real > latest_fit_x
        and 2 * quadratic_coefficients[0] * root.real
        + quadratic_coefficients[1] > 0
    ]
    # 500.68
    year_pass_2C_quadratic = (
        float(min(future_upward_roots) + x_anf)
        if future_upward_roots
        else float("nan")
    )
    # 500.70
    threshold_roots_1C7 = np.roots(
        [
            quadratic_coefficients[0],
            quadratic_coefficients[1],
            quadratic_coefficients[2] - 1.7,
        ]
    )
    # 500.72
    future_upward_roots_1C7 = [
        root.real
        for root in threshold_roots_1C7
        if np.isclose(root.imag, 0)
        and root.real > latest_fit_x
        and 2 * quadratic_coefficients[0] * root.real
        + quadratic_coefficients[1] > 0
    ]
    # 500.74
    year_pass_1C7_quadratic = (
        float(min(future_upward_roots_1C7) + x_anf)
        if future_upward_roots_1C7
        else float("nan")
    )
    # 500.76
    threshold_roots_2C5 = np.roots(
        [
            quadratic_coefficients[0],
            quadratic_coefficients[1],
            quadratic_coefficients[2] - 2.5,
        ]
    )
    # 500.78
    future_upward_roots_2C5 = [
        root.real
        for root in threshold_roots_2C5
        if np.isclose(root.imag, 0)
        and root.real > latest_fit_x
        and 2 * quadratic_coefficients[0] * root.real
        + quadratic_coefficients[1] > 0
    ]
    # 500.80
    year_pass_2C5_quadratic = (
        float(min(future_upward_roots_2C5) + x_anf)
        if future_upward_roots_2C5
        else float("nan")
    )
    # 500.82 linear_coefficients
    linear_coefficients = np.polyfit(fit_x, fit_data["temp_average"], 1)
    # 500.83
    linear_year_coefficients = np.array(
        [
            linear_coefficients[0],
            linear_coefficients[1] - linear_coefficients[0] * x_anf,
        ]
    )
    # 500.85
    quadratic_year_coefficients = np.array(
        [
            quadratic_coefficients[0],
            quadratic_coefficients[1]
            - 2 * quadratic_coefficients[0] * x_anf,
            quadratic_coefficients[0] * x_anf**2
            - quadratic_coefficients[1] * x_anf
            + quadratic_coefficients[2],
        ]
    )
    # 500.87
    linear_crossing_year = (
        x_anf + (2.0 - linear_coefficients[1]) / linear_coefficients[0]
        if linear_coefficients[0] > 0
        else float("nan")
    )
    # 500.88
    year_pass_2C_linear = (
        float(linear_crossing_year)
        if linear_crossing_year > latest_era5_digital_year
        else float("nan")
    )
    # 500.90 
    quadratic_fit = np.polyval(quadratic_coefficients, fit_x)
    # 500.94
    linear_fit = np.polyval(linear_coefficients, fit_x)
    # 500.95
    total_sum_squares = np.sum(
        (fit_data["temp_average"] - fit_data["temp_average"].mean()) ** 2
    )
    # 500.97
    if total_sum_squares > 0:
        quadratic_r_squared = 1 - np.sum(
            (fit_data["temp_average"] - quadratic_fit) ** 2
        ) / total_sum_squares
        linear_r_squared = 1 - np.sum(
            (fit_data["temp_average"] - linear_fit) ** 2
        ) / total_sum_squares
    else:
        quadratic_r_squared = linear_r_squared = float("nan")

    # 500.100 Save the source series and fitted values using the requested column order.
    output_data = data.loc[
        :, ["digital_date", "date", "2t", "clim_91-20", "ano_91-20"]
    ].copy()
    # 500.103 Export the moving average of the ERA5 anomaly column.
    output_data["T_average"] = data["T_average"]
    # 500.105
    output_data["linear_fit"] = np.nan
    # 500.106
    output_data["quadratic_fit"] = np.nan
    # 500.107
    all_fit_x = data["digital_date"] - x_anf
    # 500.108
    fit_rows = data["date"] >= pd.Timestamp(year=x_anf, month=1, day=1)
    # 500.110
    output_data.loc[fit_rows, "linear_fit"] = np.polyval(
        linear_coefficients, all_fit_x.loc[fit_rows]
    )
    # 500.111
    output_data.loc[fit_rows, "quadratic_fit"] = np.polyval(
        quadratic_coefficients, all_fit_x.loc[fit_rows]
    )
    # 500.113
    os.makedirs(os.path.dirname(output_csv), exist_ok=True)
    # 500.114 write to temp/era5.csv
    output_data.to_csv(output_csv, index=False, float_format="%.6f")

    # 500.115 Extend both fitted curves monthly to the requested end year.
    forecast_dates = pd.date_range(
        f"{x_anf}-01-01", f"{x_end}-12-01", freq="MS"
    )
    # 500.116 
    forecast_decimal_year = (
        forecast_dates.year
        + forecast_dates.dayofyear
        / np.where(forecast_dates.is_leap_year, 366, 365)
    )
    # 500.118
    forecast_x = forecast_decimal_year - x_anf
    # 500.119
    forecast_quadratic_fit = np.polyval(quadratic_coefficients, forecast_x)
    # 500.120
    forecast_linear_fit = np.polyval(linear_coefficients, forecast_x)
    # 500.121
    forecast_fit2_mask = forecast_dates >= linear_fit2_data["date"].iloc[0]
    # 500.122
    forecast_linear_fit2 = np.polyval(
        linear_fit2_coefficients, forecast_x[forecast_fit2_mask]
    )
    # 500.123
    plot_data = data.loc[
        data["date"].between(
            pd.Timestamp(year=x_anf, month=1, day=1),
            pd.Timestamp(year=x_end, month=12, day=31),
        )
        & data["temp_average"].notna()
    ]
    # 500.125
    average_plot_data = data.loc[data["T_average"].notna()]
    
    #######################################################
    # 500.127  size of the figure 13 inch wide  7 inch high
    ########################################################
    fig, ax = plt.subplots(figsize=(13, 7))
    
    # 500.131 upper legend  line1 and text for red curve 1
    ax.plot(
        average_plot_data["date"],
        average_plot_data["T_average"],
        color="#b22222",
        linewidth=3, # for curve and legend
        label=f"Temperature moving average {rolling_rows } ",
    )

    # 500.132  upper legend  line2 and text for purple quadratic_fit
    ax.plot(
        forecast_dates,
        forecast_quadratic_fit,
        color="purple",
        linestyle="--", # dashed
        linewidth=2.5,
        label=f"Quadratic fit ERA5",
    )
    # 500.133  upper legend  line3 and text for green linear_fit
    ax.plot(
        forecast_dates,
        forecast_linear_fit,
        color="#228B22",
        linestyle="--",
        linewidth=2.5,
        label=f"Linear fit ",
    )

    # 500.134  upper legend  line4 and text for orange linear_fit2
    ax.plot(
        forecast_dates[forecast_fit2_mask],
        forecast_linear_fit2,
        color="orange",
        linestyle=":",
        linewidth=2.5,
        label=f"Linear fit ({figure505_days_linear_fit} days)",
    )

    # 500.141  purple quadratic_fit box1 text
    quadratic_formula = (
        f"T = {quadratic_year_coefficients[0]:.5f} * year² "
        f"{quadratic_year_coefficients[1]:+.1f} * year "
        f"{quadratic_year_coefficients[2]:+.1f} °C\n"
        f"Quadratic fit   R² = {quadratic_r_squared:.4f}"
        f"\n"
        f"The quadratic fit breaches 2°C in the year {year_pass_2C_quadratic:.1f}"
    )
    # 500.144   purple quadratic_fit box1 plot
    ax.text(
        0.02, # x value
        0.77, # y value
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

    # 500.151  green linear_formula box2 text
    linear_formula = (
        f"T = {linear_year_coefficients[0]:.4f} * year "
        f"{linear_year_coefficients[1]:+.1f} °C     R² = {linear_r_squared:.4f}\n"
        f"Linear fit all daily ERA5 data since {x_anf} are used"
        f"\n"
        f"The linear fit breaches 2°C in the year {year_pass_2C_linear:.1f}"
    )
    # 500.154  green linear_formula box2 plot
    ax.text(
        0.55, # x value
        0.35, # y value
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
    # 500.161  orange linear2_formula box3 text
    linear_fit2_formula = (
        f"T = {linear_fit2_year_coefficients[0]:.5f} * year "
        f"{linear_fit2_year_coefficients[1]:+.1f} °C   R² = {linear_fit2_r_squared:.4f}"
        f"\n"
        f"Linear fit2 {len(linear_fit2_data)} days => decadial warming = {temp_linear2_decade:.2f}°C"
        f"\n"
        f"The linear fit2 breaches 2°C in the year {year_pass_2C_linear2:.1f}"
    )
    # 500.164  orange linear2_formula box3 plot
    ax.text(
        0.02,
        0.6,
        linear_fit2_formula,
        transform=ax.transAxes,
        fontsize=12,
        va="top",
        color="darkorange",
        bbox={
            "facecolor": "white",
            "alpha": 0.9,
            "edgecolor": "orange",
            "boxstyle": "round,pad=0.4",
        },
    )
    # 500.171  red box4 text ERA5 Temperature moving average
    red_box = (
        # f"ERA5 Temperature moving average over {figure505} days.\n"
        f"{latest_era5_temp:.3f} °C     on    {latest_era5_date:%Y-%m-%d}        ERA5 data"
        f"\n"
        f"{temp_last_365_days:.3f} °C is the average temperature the last 365 days."
        f"\n"
        f"The red curve below is the {figure505} days moving average."
    )
    # 500.172  red box4 plot
    ax.text(
        0.5,
        0.15,
        red_box,
        transform=ax.transAxes,
        fontsize=12,
        va="top",
        color="red",
        bbox={
            "facecolor": "white",
            "alpha": 0.9,
            "edgecolor": "red",
            "boxstyle": "round,pad=0.4",
        },
    )


    ###############################################################
    # 500.190 print the headline 
    ax.set_title(
        f"Figure {figure4_9}: ERA5 Temperature with quadratic and linear fits",
        loc="left",
        x=-0.05,
        fontsize=18,
        pad=20,   # gap between title baseline and top of axes (points)
    )

    # 500.200 x axis
    ax.set_xlabel("Year")
    # 500.160 y axis
    ax.set_ylabel("Temperature (°C)")
    # 500.170 
    ax.set_xlim(
        pd.Timestamp(year=x_anf, month=1, day=1),
        pd.Timestamp(year=x_end, month=12, day=31),
    )
    # 500.174 scale the y axis, as declared in config.py
    ax.set_ylim(y_505min, y_505max)
    
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
    # 500.225 temperature band 1.5 to 2.0 °C
    ax.axhspan(1.5, 2.0, color="#2196D19A", alpha=0.06, zorder=0)

    # 500.230 print the legend (line 1 line 2 line 3)
    ax.legend(loc="upper left")

    ax.axhspan(1.5, 2.0, color="#2196D19A", alpha=0.06, zorder=0)


    # 500.240   print in line 12 below the plot
    fig.text(
        0.08, # x value 0.5 is middle  0.4 center
        0.01,
        f"{latest_era5_date:%Y-%m-%d} "
        # f"  Temperature={latest_era5_temp}°C  10d={temp_last_10_days:.3f}°C   30d={temp_last_30_days:.3f}°C  90d={temp_last_90_days:.3f}°C  from ERA5 + {figure505_offset} ",
        f"  Temperature={latest_era5_temp:.3f}°C  Last 10days={temp_last_10_days:.3f}°C"
        f"  30d={temp_last_30_days:.3f}°C"
        f"  90d={temp_last_90_days:.3f}°C"
        f"  180d={temp_last_180_days:.3f}°C"
        f"  last year={temp_last_365_days:.3f}°C ",
        ha="left",   # ha="center",
        fontsize=12,
    )


    # 500.240   print in line 14 below the plot
    # text_4_add_text(ax, tr2x, tr2y, text68, c68, trs) # from text.py 


   
 
    # text_4_add_text(ax, tr2x, tr2y, text68, c68, trs) # from text.py 

    # 500.250  line 14 (f"-0.4 Source"
    text_below = (f"Source"
                  f" https://sites.ecmwf.int/data/climatepulse/data/series/"
                  f" era5_daily_series_2t_global.csv"
                  f"           last ERA5 entry: {latest_era5_date:%Y-%m-%d}"
                )
    # 500.260  line 14    lry = -0.4     tr2y = -.26  tr4y = -.40
    lry = -0.21
    lrx = -0.06
    ax.text(lrx, lry , text_below, color="black", fontname="Arial", fontsize=12,
            transform=ax.transAxes)


    # 500.250  text_1_print_line(ax)
    # 500.260  text_1_print_line   lry = -0.34     tr2y = -.26  tr4y = -.40
    lry = -0.45
    lrx = -0.06
    # ax.text(lrx, lry , text_below, color="black", fontname="Arial", fontsize=12,
    #        transform=ax.transAxes)




    # 500.350  text_1_print_line(ax)
    text_below = (f"    https://thomas1960.substack.com/ "
                  f"   "
                  f"     https://github.com/Boettcher1960/5_CO2_EEI_T"
                  f"                  version ={v}"
                  f"  ")
    
    # 500.360  text_1_print_line   lry = -0.34     tr2y = -.26  tr4y = -.40
    lry = -0.26
    ax.text(-0.08, lry , text_below, color="black", fontname="Arial", fontsize=12,
            transform=ax.transAxes)







    # 500.270
    # left = 0	Left edge of subplot area at x = 0 (very left of figure)
    # bottom = 0.05	Subplots can't go below 5% from the bottom
    # right = 1	Right edge at x = 1 (very right of figure)
    # top = 0.95	Subplots can't go above 95% from the bottom (5% margin at top)
    # fig.tight_layout(rect=(0, 0.08, 1, 0.94))
    # fig.savefig(output_plot, dpi=300, bbox_inches="tight")
    print(f"Last ERA5 source date: {latest_era5_date:%Y-%m-%d}")
    print(f"Average temperature of the last   1 day : {latest_era5_temp:.3f} °C")
    print(f"Average temperature of the last  10 days: {temp_last_10_days:.3f} °C")
    print(f"Average temperature of the last  30 days: {temp_last_30_days:.3f} °C")
    print(f"Average temperature of the last  90 days: {temp_last_90_days:.3f} °C")
    print(f"Average temperature of the last 180 days: {temp_last_180_days:.3f} °C")
    print(f"Average temperature of the last 365 days: {temp_last_365_days:.3f} °C")
    print()
    print(
        "Figure 505 quadratic fit: "
        f"T = {quadratic_year_coefficients[0]:.9f} year^2 "
        f"{quadratic_year_coefficients[1]:+.9f} year "
        f"{quadratic_year_coefficients[2]:+.9f}; R² = {quadratic_r_squared:.6f}"
    )
    print(f"Figure 505 quadratic formula: {quadratic_formula.replace(chr(10), '; ')}")
    print(f"year_pass_1C7_quadratic: {year_pass_1C7_quadratic:.3f}")
    print(f"year_pass_2C_quadratic: {year_pass_2C_quadratic:.3f}")
    print(f"year_pass_2C5_quadratic: {year_pass_2C5_quadratic:.3f}")
    print()           

    print(f"Figure 505 linear formula: {linear_formula.replace(chr(10), '; ')}")
    print(
        "Figure 505 linear fit: "
        f"T = {linear_year_coefficients[0]:.9f} year "
        f"{linear_year_coefficients[1]:+.9f}; R² = {linear_r_squared:.6f}"
    )
    print(f"year_pass_2C_linear: {year_pass_2C_linear:.3f}")
    
    print(
        f"Figure 505 linear fit2 ({len(linear_fit2_data)} rows): "
        f"T = {linear_fit2_year_coefficients[0]:.9f} year "
        f"{linear_fit2_year_coefficients[1]:+.9f}; "
        f"R² = {linear_fit2_r_squared:.6f}"
    )
     # calculate the decadial temperature change
    print(f"temp_linear2_decade: {temp_linear2_decade:.3f} °C per decade")
    print(f"year_pass_2C_linear2: {year_pass_2C_linear2:.3f}")
    print()

    print(f"Saved ERA5 fit data to {output_csv}")
    print(f"Saved ERA5 temperature plot to {output_plot}")

    fig.savefig(output_plot, dpi=300, bbox_inches="tight")

    plt.show()
    save_png5(fig)
    plt.close(fig)
