
import pandas as pd
import matplotlib.pyplot as plt

# Load the filtered matrix data
filtered_data_no_totals = pd.read_csv('Filtered_Crime_Data_Matrix.csv', index_col=0)

# 1. Increasing Crime Rate by Year
yearly_crime_totals_matrix = filtered_data_no_totals.sum()
plt.figure(figsize=(10, 6))
plt.plot(yearly_crime_totals_matrix.index, yearly_crime_totals_matrix.values, marker='o', linestyle='-')
plt.title('Increasing Crime Rate by Year (Matrix Data)')
plt.xlabel('Year')
plt.ylabel('Total Crimes Against Foreigners')
plt.grid(True)
plt.xticks(yearly_crime_totals_matrix.index)
plt.savefig('visualizations/increasing_crime_rate.png')
plt.show()

# 2. Top 10 Crimes Comparison Year by Year
top_10_crimes = filtered_data_no_totals.sum(axis=1).sort_values(ascending=False).head(10).index
top_10_crimes_data = filtered_data_no_totals.loc[top_10_crimes]
top_10_crimes_data.T.plot(kind='bar', figsize=(14, 8), width=0.8)
plt.title('Top 10 Crimes Comparison Year by Year')
plt.xlabel('Year')
plt.ylabel('Number of Crimes Against Foreigners')
plt.legend(title='Crime Head', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.savefig('visualizations/top_10_crimes_comparison.png')
plt.show()

# 3. Crime Contribution by Year (Donut Charts)
fig, axs = plt.subplots(2, 3, figsize=(20, 12))
axs = axs.flatten()
for i, year in enumerate(filtered_data_no_totals.columns):
    year_data = filtered_data_no_totals[year].dropna()
    wedges, texts, autotexts = axs[i].pie(
        year_data, labels=year_data.index, autopct='%1.1f%%', startangle=140, wedgeprops={'width': 0.3}
    )
    axs[i].set_title(f'Crime Contribution in {year}')
    axs[i].axis('equal')
    axs[i].legend(wedges, year_data.index, title="Crime Head", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
if len(filtered_data_no_totals.columns) < 6:
    fig.delaxes(axs[-1])
plt.tight_layout()
plt.savefig('visualizations/crime_contribution.png')
plt.show()

# 4. Distribution of Crimes Over Time (Area Graph)
ax = filtered_data_no_totals.T.plot(kind='area', stacked=True, figsize=(14, 8), alpha=0.6)
plt.title('Distribution of Crimes Over Time')
plt.xlabel('Year')
plt.ylabel('Number of Crimes Against Foreigners')
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, title='Crime Head', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.savefig('visualizations/distribution_of_crimes_over_time.png')
plt.show()

# 5. Rape Cases Year-wise (Bar Chart)
rape_data = filtered_data_no_totals.loc['Rape']
plt.figure(figsize=(10, 6))
plt.bar(rape_data.index, rape_data.values, color='skyblue')
plt.title('Rape Cases Year-wise')
plt.xlabel('Year')
plt.ylabel('Number of Rape Cases Against Foreigners')
plt.grid(axis='y')
for i, value in enumerate(rape_data.values):
    plt.text(rape_data.index[i], value + 0.1, f'{int(value)}', ha='center', va='bottom', fontsize=10)
plt.tight_layout()
plt.savefig('visualizations/rape_cases_yearwise.png')
plt.show()
