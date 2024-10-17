import pandas as pd

# Load the CSV file
file_path = r'tampere_companies_extracted.csv'
df = pd.read_csv(file_path, dtype=str)

df_filtered = df[df['mainBusinessLineType'].astype(str) != '68202']

# Save the filtered DataFrame to a new CSV file
filtered_file_path = r'tampere_companies_filtered.csv'
df_filtered.to_csv(filtered_file_path, index=False)

print(f'Filtered data saved to: {filtered_file_path}')
