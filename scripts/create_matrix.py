
import pandas as pd

# Pivot the data to create a matrix with years as columns and all crime heads as rows
pivot_data_all_crimes = filtered_data.pivot_table(
    index='Crime Head',
    columns='Year',
    values='Total Foreigners',
    aggfunc='sum'
)

# Remove rows where 'Crime Head' contains the keyword 'Total'
filtered_data_no_totals = pivot_data_all_crimes[~pivot_data_all_crimes.index.str.contains('Total', case=False)]

# Save the matrix to a CSV file
filtered_matrix_csv_path = 'Filtered_Crime_Data_Matrix.csv'
filtered_data_no_totals.to_csv(filtered_matrix_csv_path)
