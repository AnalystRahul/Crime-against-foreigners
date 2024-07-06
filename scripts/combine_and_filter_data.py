
import pandas as pd

# Combine all dataframes into one
combined_data = pd.concat(data_frames.values(), ignore_index=True)

# Remove rows where 'Crime Head' contains the keyword 'Total'
filtered_data = combined_data[~combined_data['Crime Head'].str.contains('Total', case=False, na=False)]

# Save the combined filtered data to an Excel file for future use
filtered_combined_file_path = 'Filtered_Crime_Data_Combined_All_Years.xlsx'
filtered_data.to_excel(filtered_combined_file_path, index=False)
