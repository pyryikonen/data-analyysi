import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
file_path = '../../csv/tampere_companies_filtered.csv'  # Adjust path to your CSV file
df = pd.read_csv(file_path, dtype=str)

# Convert the registration date to datetime format
df['mainBusinessLineRegDate'] = pd.to_datetime(df['mainBusinessLineRegDate'], errors='coerce')

# Filter the DataFrame to include only entries from the year 2000 onwards
df_filtered = df[df['mainBusinessLineRegDate'].dt.year >= 2000]

# Group by postal code and registration year, and count the number of companies
postal_year_counts = df_filtered.groupby(['postCode', df_filtered['mainBusinessLineRegDate'].dt.year]).size().reset_index(name='count')

# Create a cumulative count for each postal code
postal_year_counts['cumulative_count'] = postal_year_counts.groupby('postCode')['count'].cumsum()

# Pivot the table for better structure
postal_year_counts_pivot = postal_year_counts.pivot(index='mainBusinessLineRegDate', columns='postCode', values='cumulative_count').fillna(0)

# Get the top 5 postal codes by total cumulative counts
top_5_postal_codes = postal_year_counts_pivot.max().nlargest(5).index

# Filter the data for the top 5 postal codes
postal_year_counts_top_5 = postal_year_counts_pivot[top_5_postal_codes]

# Create a line diagram for the cumulative counts of the top 5 postal codes
plt.figure(figsize=(14, 8))  # Set the width to 14 and the height to 8
for postal_code in postal_year_counts_top_5.columns:
    plt.plot(postal_year_counts_top_5.index.astype(str), postal_year_counts_top_5[postal_code], marker='o', label=postal_code)

plt.title('Cumulative Count of Companies by Top 5 Postal Codes and Registration Year (From 2000 to 2024)')
plt.xlabel('Registration Year')
plt.ylabel('Cumulative Number of Companies')

# Automatically fit the x-axis limits to the data
plt.autoscale(axis='x', tight=True)

# Optional: Uncomment the following line to automatically fit the layout
# plt.tight_layout()  # Adjust layout for better appearance

plt.legend(title='Postal Code')
plt.grid()
plt.show()
