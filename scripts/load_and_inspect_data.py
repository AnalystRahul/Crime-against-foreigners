
import pandas as pd

# Define file paths
file_paths = {
    2021: 'data/NCRB-2021_Table_13A.2.csv',
    2020: 'data/NCRB_CII-2020_Table.No-13A.2.csv',
    2019: 'data/NCRB_CII-2019_Table_13A.2.csv',
    2018: 'data/NCRB_CII_2018_State_Table13A.2.csv',
    2016: 'data/Table_13A.2_2016.csv'
}

# Load and standardize column names
data_frames = {}
for year, path in file_paths.items():
    df = pd.read_csv(path)
    df['Year'] = year
    if year == 2021 or year == 2020 or year == 2019:
        df.columns = ['Sl. No', 'Category', 'Crime Head', 'Foreign Tourists', 'Other Foreigners', 'Total Foreigners', 'Year']
    elif year == 2018:
        df.columns = ['Sl. No', 'Category', 'Crime Head', 'Foreign Tourists', 'Other Foreigners', 'Total Foreigners', 'Year']
    elif year == 2016:
        df.columns = ['Category', 'Crime Head', 'Foreign Tourists', 'Other Foreigners', 'Total Foreigners', 'Year']
    data_frames[year] = df[['Category', 'Crime Head', 'Foreign Tourists', 'Other Foreigners', 'Total Foreigners', 'Year']]
