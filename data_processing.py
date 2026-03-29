# data_processing.py
# version 5a53
import pandas as pd
import numpy as np
print_debug_DP = 10 # global variable print_debug = 10

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
    if print_debug_DP > 9:
        print(f"DataP_32: Successfully converted {len(df)} records to {output_file}")
    return df

def create_running_average(input_csv, 
                           output_csv, 
                           window_months, 
                          min_periods=None, 
                          center=True, 
                          keep_original=True,
                          column_name='EEI'):
    """Create running average for specified window size"""
    df = pd.read_csv(input_csv)
    df['date'] = pd.to_datetime(df['date'])
    df = df.sort_values('date').reset_index(drop=True)
    
    if min_periods is None:
        # min_periods = window_months // 2
        min_periods = window_months
   
    df[column_name] = df['toa_net_flux_w_m2'].rolling(
        window=window_months, 
        center=center,
        min_periods=min_periods
    ).mean()
    
    output_columns = ['date', 'year', 'month', 'decimal_year']
    if keep_original:
        output_columns.append('toa_net_flux_w_m2')
    output_columns.append(column_name)
    
    df_output = df[output_columns].copy()
    df_output.to_csv(output_csv, index=False, float_format='%.6f')
    
    valid_records = df_output[column_name].notna().sum()
    #print(f"{window_months}-month running average saved to {output_csv}")
    #print(f"Valid records: {valid_records} out of {len(df_output)}")
    if print_debug_DP > 9:
        print(f"DataP_71: Valid records: {valid_records} out of {len(df_output)}")
        print(f"DataP_72: {window_months}-month running average saved to {output_csv} ")
    return df_output

def load_co2_mauna_loa(x_anf, x_end):
    """Load Mauna Loa CO2 data"""
    co2_values = [
        316.91, 317.64, 318.45, 318.99, 319.62, 320.04, 321.38, 322.16, 323.04, 324.62,
        325.68, 326.32, 327.46, 329.68, 330.19, 331.13, 332.03, 333.84, 335.41, 336.84,
        338.76, 340.12, 341.48, 343.15, 344.87, 346.35, 347.61, 349.31, 351.69, 353.20,
        354.45, 355.70, 356.54, 357.21, 358.96, 360.97, 362.74, 363.88, 366.84, 368.54,
        369.71, 371.32, 373.45, 375.98, 377.70, 379.98, 382.09, 384.02, 385.83, 387.64,
        390.10, 391.85, 394.06, 396.74, 398.81, 401.01, 404.41, 406.76, 408.72, 411.66,
        414.24, 416.41, 418.53, 421.08, 424.61, 427.35
    ]
    
    years = list(range(1960, 2026))
    df = pd.DataFrame({"year": years, "co2_ppm": co2_values})
    df = df[(df['year'] >= x_anf) & (df['year'] <= x_end)]
    return df

def load_gis_temperature():
    """Load GIS temperature data"""
    return pd.read_csv("read_csv/csv_74_gis_temperature.csv")