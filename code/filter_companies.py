import pandas as pd
import json

# Load the existing CSV file
csv_file_path = '../csv/tampere_companies_extracted.csv'  # Adjust path to your CSV file
df = pd.read_csv(csv_file_path, dtype=str)

# Load the postal codes from the JSON file
json_file_path = '../json/post_codes_tampere.json'  # Adjust path to your JSON file
with open(json_file_path, 'r') as json_file:
    postal_codes_data = json.load(json_file)

# Extract the postal codes into a list
postal_codes = [item['postCode'] for item in postal_codes_data]

# Filter the DataFrame based on the extracted postal codes
df_filtered = df[df['postCode'].isin(postal_codes)]

# Replace the current DataFrame with the filtered one
df = df_filtered

# Save the filtered DataFrame to a new CSV file
filtered_file_path = '../csv/tampere_companies_filtered2.csv'  # Save path for the filtered file
df.to_csv(filtered_file_path, index=False)
print(f'Filtered data saved to: {filtered_file_path}')
