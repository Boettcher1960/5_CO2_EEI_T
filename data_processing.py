# data_processing.py
# version 5f33
import pandas as pd
import numpy as np
print_debug_DP = 10 # global variable print_debug = 10
# part 62.b  line 12 convert download.txt to CERES.csv (no averaging) convert_ceres_to_csv(input_file, output_file)
# part 62.c  CERES.csv (perform averaging) create_running_average(input_csv, output_csv, 
# part 62.e  line 82 CERES.csv (add averaging column to plotable-csv)
# part 66.b  line 141 convert download.txt to CERES.csv (no averaging) convert66_ceres_to_csv(input_file, output_file)
# part 66.c  line 172 create66_running_average (input_csv, output_csv, 
# part 66.e  line 216 add_66_csv_column   (add averaging column to plotable-csv)


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
    if print_debug_DP > 9:
        print(f"DataP_32: Successfully converted {len(df)} records to {output_file}")
    return df
    # end part 62.b convert download.txt to CERES.csv (no averaging)

# part 62.c  CERES.csv (perform averaging) create_running_average(input_csv, output_csv, 
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
        print(f"DataP_79: Valid records: {valid_records} out of {len(df_output)}")
        print(f"DataP_80: {window_months}-month running average saved to {output_csv} ")
    return df_output
    # end part 62.c  CERES.csv (perform averaging)

# part 62.e  CERES.csv (add averaging column to plotable-csv)
def add_62_csv_column(input_csv, 
                      input_EEI_csv, 
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
    
    df2 = pd.read_csv(input_EEI_csv)
    df2['date'] = pd.to_datetime(df2['date'])
    df2 = df2.sort_values('date').reset_index(drop=True)

    df = df.merge(df2[['date', 'EEI']], on='date', how='left')
    # Merge on 'date' column df = df.merge(df2[['date', 'EEI']], on='date', how='left')

    # Create OLR_EEI column (fill NaN with 0 before addition)
    # df['OLR_EEI'] = df['EEI'].fillna(0) + df['LongWave'].fillna(0)


    if min_periods is None:
        # min_periods = window_months // 2
        min_periods = window_months
   
    df[column_name] = df['toa_net_flux_w_m2'].rolling(
        window=window_months, 
        center=center,
        min_periods=min_periods
    ).mean()

    # Merge on 'date' column
    #df = df.merge(df2[['date', 'EEI']], on='date', how='right')

    output_columns = ['date', 'year', 'month', 'decimal_year', 'EEI']
    if keep_original:
        output_columns.append('toa_net_flux_w_m2')
    output_columns.append(column_name)
   
    #output_columns.append('OLR_EEI')
    # Create OLR_EEI column (fill NaN with 0 before addition)
    df['OLR_EEI'] = df['EEI'].fillna(0) + df['LongWave'].fillna(0)
    output_columns.append('OLR_EEI')

    df_output = df[output_columns].copy()
    df_output.to_csv(output_csv, index=False, float_format='%.6f')
    
    valid_records = df_output[column_name].notna().sum()
    #print(f"{window_months}-month running average saved to {output_csv}")
    #print(f"Valid records: {valid_records} out of {len(df_output)}")
    if print_debug_DP > 9:
        print(f"DataP_130: Valid records: {valid_records} out of {len(df_output)}")
        print(f"DataP_131: {window_months}-month running average saved to {output_csv} ")
    return df_output
    # end part 62.e  CERES.csv (add averaging column to plotable-csv)

# part 66.b convert download.txt to CERES.csv (no averaging) convert66_ceres_to_csv(input_file, output_file)
def convert66_txt_to_csv(input_file, 
                           output_file,  #  'work/_66b_OLR_raw.csv',
                           column_name): #  'OLR'
    """Convert CERES TOA flux ASCII file to CSV format"""
    data = []
    # part 66.b.2 open txt file
    with open(input_file, 'r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            if not line or line.startswith('#') or line.startswith('CERES'):
                continue
            # part 66.b.3 read one line of the txt file
            parts = line.split()
            if len(parts) >= 3:
                try:
                    year = int(parts[0])
                    month = int(parts[1])
                    flux = float(parts[2])
                    # part 66.b.4 store values into the data field
                    data.append([year, month, flux])
                except ValueError:
                    continue

    # part 66.b.5 store values into the df field
    df = pd.DataFrame(data, columns=['year', 'month', column_name])
    df['date'] = pd.to_datetime(df['year'].astype(str) + '-' + df['month'].astype(str) + '-01')
    df['decimal_year'] = df['year'] + (df['month'] - 0.5) / 12
    df = df[['date', 'year', 'month', 'decimal_year', column_name]]

    df.to_csv(output_file, index=False, float_format='%.6f')

    if print_debug_DP > 9:
        print(f"DataP_168: convert66_ceres_to_csv {len(df)} records to {output_file}")
    return df
    # end part 66.b convert download.txt to CERES.csv (no averaging)

# part 66.c line182 create66_running_average (input_csv, output_csv, 
def create66_running_average(input_csv,  # 'work/_66b_OLR_raw.csv'
                             output_csv, # 'work/_66c_OLR.csv',
                             column_read,             #  column_name='OLR', 'SW_in'
                             column_average,          #  column_name='OLR48')
                             columnname,              #  column_name='SW_in')
                             window_months, 
                             min_periods=None, 
                             center=True, 
                             keep_original=True,
                             column_name='EEI48'): # not used if main has different parameter
    """Create running average for specified window size"""

    # part 66.c.2 read csv with raw ceres data into data-frame
    df = pd.read_csv(input_csv) # 'work/_66b_OLR_raw.csv' # 'work/_65b_SW_in_raw.csv'

    # part 66.c.3 sort the data-frame
    df['date'] = pd.to_datetime(df['date'])
    df = df.sort_values('date').reset_index(drop=True)

    # part 66.c.4 check the parameters 
    if min_periods is None:
        min_periods = window_months

     # part 66.c.5 mean value (read column OLR)(store in ?)
    df[column_name] = df[column_read].rolling(
        window=window_months, 
        center=center,
        min_periods=min_periods
    ).mean()

    # part 66.c.6 first 4 columns are the date
    output_columns = ['date', 'year', 'month', 'decimal_year']

    # part 66.c.7 columns 5 is ceres txt read value, no average
    if keep_original:
        output_columns.append(column_read)
    # part 66.c.8 columns 6 is the default column_name average
    output_columns.append(column_name)
    # part 66.c.9 columns 7 is the parameter column_average average
    # output_columns.append(column_average)

     # part 66.c.10 copy
    df_output = df[output_columns].copy()
    # part 66.c.11 copy to csv
    df_output.to_csv(output_csv, index=False, float_format='%.6f')
    
    valid_records = df_output[column_name].notna().sum()    
    return df_output
    # end part 66.c  CERES.csv (perform averaging)


# part 67.c line182 create66_running_average (input_csv, output_csv, 
def create67_running_average(input_csv,  # 'work/_66b_OLR_raw.csv'
                             output_csv, # 'work/_66c_OLR.csv',
                             column_read,             #  column_name='ASR'
                             column_average,          #  column_name='ASR48')
                             window_months, 
                             min_periods=None, 
                             center=True, 
                             keep_original=True,
                             column_name='ASR48'): # not used if main has different parameter
    # part 67.c.2 read csv with raw ceres data into data-frame
    df = pd.read_csv(input_csv) # 'work/_66b_OLR_raw.csv' # 'work/_65b_SW_in_raw.csv'

    # part 67.c.3 sort the data-frame
    df['date'] = pd.to_datetime(df['date'])
    df = df.sort_values('date').reset_index(drop=True)

    # part 67.c.4 check the parameters 
    if min_periods is None:
        min_periods = window_months

     # part 67.c.5 mean value (read column OLR)(store in ?)
    df[column_name] = df[column_read].rolling(
        window=window_months, 
        center=center,
        min_periods=min_periods
    ).mean()

    # part 67.c.6 first 4 columns are the date
    output_columns = ['date', 'year', 'month', 'decimal_year']

    # part 67.c.7 columns 5 is ceres txt read value, no average
    if keep_original:
        output_columns.append(column_read)
    # part 67.c.8 columns 6 is the default column_name average
    output_columns.append(column_name)
    # part 67.c.9 columns 7 is the parameter column_average average
    # output_columns.append(column_average)

     # part 67.c.10 copy
    df_output = df[output_columns].copy()
    # part 67.c.11 copy to csv
    df_output.to_csv(output_csv, index=False, float_format='%.6f')
    
    
    return df_output
    # end part 67.c  CERES.csv (perform averaging)




"""
# part 66.e not used line 216 add_66_csv_column   (add averaging column to plotable-csv)
def add_66_csv_column(input_csv, 
                      input_EEI_csv, 
                      output_csv, 
                      window_months, 
                      min_periods=None, 
                      center=True, 
                      keep_original=True,
                      column_name='OLR48'):
    
    df = pd.read_csv(input_csv)
    df['date'] = pd.to_datetime(df['date'])
    df = df.sort_values('date').reset_index(drop=True)
    
    df2 = pd.read_csv(input_EEI_csv)
    df2['date'] = pd.to_datetime(df2['date'])
    df2 = df2.sort_values('date').reset_index(drop=True)

    df = df.merge(df2[['date', 'EEI']], on='date', how='left')
    # Merge on 'date' column df = df.merge(df2[['date', 'EEI']], on='date', how='left')

    # Create OLR_EEI column (fill NaN with 0 before addition)
    # df['OLR_EEI'] = df['EEI'].fillna(0) + df['LongWave'].fillna(0)


    if min_periods is None:
        # min_periods = window_months // 2
        min_periods = window_months
   
    df[column_name] = df['OLR'].rolling(
        window=window_months, 
        center=center,
        min_periods=min_periods
    ).mean()

    # Merge on 'date' column
    #df = df.merge(df2[['date', 'EEI']], on='date', how='right')

    output_columns = ['date', 'year', 'month', 'decimal_year', 'EEI']
    if keep_original:
        output_columns.append('OLR')
    output_columns.append(column_name)
   
    #output_columns.append('OLR_EEI')
    # Create OLR_EEI column (fill NaN with 0 before addition)
    df['OLR_EEI'] = df['EEI'].fillna(0) + df['OLR'].fillna(0)
    output_columns.append('OLR_EEI')

    df_output = df[output_columns].copy()
    df_output.to_csv(output_csv, index=False, float_format='%.6f')
    
    valid_records = df_output[column_name].notna().sum()
    return df_output
    # end part 66.e  CERES.csv (add averaging column to plotable-csv)
    """

 # part 67.1 create work/_CERES_raw.csv with 13 columns
 # https://ceres-tool.larc.nasa.gov/ord-tool/srbavg
 # 67.1 download CERES_EBAF-TOA_Ed4.2.1_TOA_Shortwave_Flux_-_All-Sky_March-2000toJuly-2026.txt
 # 67.2 copy to read_csv/_66_TOA_Shortwave_Flux_All_Sky2026_07.txt'
 # 67.6 download CERES_EBAF-TOA_Ed4.2.1_Incoming_Solar_Flux_March-2000toJuly-2026.txt
 # 67.7 copy to read_csv/_66_TOA_Incoming_Solar_2026_07.txt'
 # 67.10 download CERES_EBAF-TOA_Ed4.2.1_TOA_Net_Flux_-_All-Sky_March-2000toJuly-2026.txt
 # 67.11 copy to 'read_csv/_67_EEI_TOA_Net_Flux_2026_07.txt'
def ceres67_to_csv(
        output_file1,  # work/_67b_sw_out.csv
        output_file2): # work/_CERES.csv'
    
    data  = [] # 67.2 copy to read_csv/_66_TOA_Shortwave_Flux_All_Sky2026_07.txt'
    data2 = [] # 67.7 copy to read_csv/_66_TOA_Incoming_Solar_2026_07.txt'
    data3 = []
    data4 = []

    # part 67.3 read1 txt
    # 67.1 download CERES_EBAF-TOA_Ed4.2.1_TOA_Shortwave_Flux_-_All-Sky_March-2000toJuly-2026.txt
    # 67.2 copy to read_csv/_66_TOA_Shortwave_Flux_All_Sky2026_07.txt'
    # 67.3 read _66_TOA_Shortwave_Flux_All_Sky2026_07.txt' into data
    with open('read_csv/_66_TOA_Shortwave_Flux_All_Sky2026_07.txt', 'r') as f:
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
    # 67.4 copy data into df data field
    df = pd.DataFrame(data, columns=['year', 'month', 'sw_out'])
    df['date'] = pd.to_datetime(df['year'].astype(str) + '-' + df['month'].astype(str) + '-01')
    df['decimal_year'] = df['year'] + (df['month'] - 0.5) / 12
    df = df[['date', 'year', 'month', 'decimal_year', 'sw_out']]

    # part 67.5 write df to  work/_67b_sw_out.csv # may be not used
    df.to_csv(output_file1, index=False, float_format='%.6f')
    if print_debug_DP > 9:
        print(f"DataP387: part 67.5 write df to {output_file1}")

    # part 67.6 read2 txt
    # 67.6 download CERES_EBAF-TOA_Ed4.2.1_Incoming_Solar_Flux_March-2000toJuly-2026.txt
    # 67.7 copy to read_csv/_66_TOA_Incoming_Solar_2026_07.txt'
    #  with open(input_file2, 'r') as f: 
    # 67.8 read _66_TOA_Incoming_Solar_2026_07.txt' into data2
    with open('read_csv/_66_TOA_Incoming_Solar_2026_07.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            if not line or line.startswith('#') or line.startswith('CERES'):
                continue
            parts = line.split()
            if len(parts) >= 3:
                try:
                    year2 = int(parts[0])
                    month2 = int(parts[1])
                    flux2 = float(parts[2])
                    data2.append([year2, month2, flux2])
                except ValueError:
                    continue

    if print_debug_DP > 9:
        print(f"DataP409: read file2  _66_TOA_Incoming_Solar_2026_07.txt to {output_file2}")

    # read3
    # 67.10 download CERES_EBAF-TOA_Ed4.2.1_TOA_Net_Flux_-_All-Sky_March-2000toJuly-2026.txt
    # 67.11 copy to 'read_csv/_67_EEI_TOA_Net_Flux_2026_07.txt'
    # 67.12 read 3 read_csv/_67_EEI_TOA_Net_Flux_2026_07.txt into data3 field
    with open('read_csv/_67_EEI_TOA_Net_Flux_2026_07.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            if not line or line.startswith('#') or line.startswith('CERES'):
                continue
            parts = line.split()
            if len(parts) >= 3:
                try:
                    year3 = int(parts[0])
                    month3 = int(parts[1])
                    flux3 = float(parts[2])
                    data3.append([year3, month3, flux3])
                except ValueError:
                    continue
    # 67.13 print
    if print_debug_DP > 9:
        print(f"DataP434: read file3  _67_EEI_TOA_Net_Flux_2026_07.txt to {output_file2}")

    # 67.14 copy data3 into df3 data field 'EEI_raw'
    df3 = pd.DataFrame(data3, columns=['year', 'month', 'EEI_raw'])

    # read4
    # 67.15 download CERES_EBAF-TOA_Ed4.2.1_TOA_Longwave_Flux_-_All-Sky_March-2000toJuly-2026.txt
    # 67.16 copy to 'read_csv/_67_EEI_TOA_Net_Flux_2026_07.txt'
    # 67.17 read 4 read_csv/_67_TOA_Longwave_Flux_2026_07.txt into data4 field
    with open('read_csv/_67_TOA_Longwave_Flux_2026_07.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            if not line or line.startswith('#') or line.startswith('CERES'):
                continue
            parts = line.split()
            if len(parts) >= 3:
                try:
                    year4 = int(parts[0])
                    month4 = int(parts[1])
                    flux4 = float(parts[2])
                    data4.append([year4, month4, flux4])
                except ValueError:
                    continue
    # 67.18 print
    if print_debug_DP > 9:
        print(f"DataP460: read file4  _67_TOA_Longwave_Flux_2026_07 to {output_file2}")

    # 67.19 copy data4 into df4 data field 'Longwave_out'
    df4 = pd.DataFrame(data4, columns=['year', 'month', 'Longwave_out'])

    # 67.20 copy data2 into df2 data field
    # 67.21 add new column5 'sw_in' to data field df2
    df2 = pd.DataFrame(data2, columns=['year', 'month', 'sw_in'])
    df2['date'] = pd.to_datetime(df2['year'].astype(str) + '-' + df2['month'].astype(str) + '-01')
    df2['decimal_year'] = df2['year'] + (df2['month'] - 0.5) / 12
    
    # 67.22 add new column5 'sw_in' to data field df2
    df2 = df2[['date', 'year', 'month', 'decimal_year', 'sw_in']]
    # 67.22 append new column6 'sw_out' to data field df2
    df2['sw_out'] = df[['sw_out']]
    # 67.23 calculate and append new column7 'albedo' to data field df2
    df2['albedo'] = df2['sw_out'] / df2['sw_in']
    # 67.24 calculate and append new column8 'darkening' to data field df2
    df2['darkening'] = 1 - ( df2['sw_out'] / df2['sw_in'] )


    # part 67.d.7 add a new column 9
    df2['ASR'] = df2['sw_in'] - df2['sw_out']
    # part 67.d.7 add a new column 10
    df2['EEI_raw'] = df3['EEI_raw']
    # part 67.d.7 add a new column 11
    df2['Longwave_out'] = df4['Longwave_out']
    # part 67.d.7 add a new column 12
    df2['EEI_calc'] =  df2['sw_in'] - df2['sw_out']     - df4['Longwave_out']

    # part 67.d.7 add a new column 13
    df2['ASR_calc'] = df2['sw_in'] - df2['sw_out']
    # part 67.d.7 add a new column 14
    df2['toa_net_flux_w_m2'] = df2['sw_out']

    # part 67.d.12 write df2 to  work/_CERES.csv'
    df2.to_csv(output_file2, index=False, float_format='%.6f')

    if print_debug_DP > 9:
        print(f"DataP361: Successfully converted {len(df)} records to {output_file2}")
    return df2






def load_co2_mauna_loa(x_anf, x_end): # 22.2 define the mauna loa CO2 data
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
    return pd.read_csv("read_csv/_74_gis_temperature.csv")



