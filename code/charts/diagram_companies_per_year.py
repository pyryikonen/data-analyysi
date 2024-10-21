import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
file_path = '../../csv/tampere_companies_filtered.csv'  # Adjust path to your CSV file
df = pd.read_csv(file_path, dtype=str)

# Convert the registration date to datetime format
df['mainBusinessLineRegDate'] = pd.to_datetime(df['mainBusinessLineRegDate'], errors='coerce')

# Filter the DataFrame to include only entries from the year 2000 onwards
df_filtered = df[df['mainBusinessLineRegDate'].dt.year >= 2000]

# Group by postal code and registration date, and count the number of companies
postal_date_counts = df_filtered.groupby(['postCode', df_filtered['mainBusinessLineRegDate'].dt.to_period('M')]).size().reset_index(name='count')

# Create a cumulative count for each postal code
postal_date_counts['cumulative_count'] = postal_date_counts.groupby('postCode')['count'].cumsum()

# Pivot the table for better structure
postal_date_counts_pivot = postal_date_counts.pivot(index='mainBusinessLineRegDate', columns='postCode', values='cumulative_count').fillna(0)

# Create a line diagram for the cumulative counts
plt.figure(figsize=(12, 6))
for postal_code in postal_date_counts_pivot.columns:
    plt.plot(postal_date_counts_pivot.index.astype(str), postal_date_counts_pivot[postal_code], marker='o', label=postal_code)

plt.title('Cumulative Count of Companies by Postal Code and Registration Date (From 2000 Onwards)')
plt.xlabel('Registration Date (Year-Month)')
plt.ylabel('Cumulative Number of Companies')
plt.xticks(rotation=45)  # Rotate dates for better visibility
plt.legend(title='Postal Code')
plt.grid()
plt.tight_layout()  # Adjust layout for better appearance
plt.show()
