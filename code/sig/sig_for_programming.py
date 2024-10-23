import pandas as pd
from scipy.stats import pearsonr

# Load the CSV
df = pd.read_csv('../../csv/tampere_companies_filtered.csv')

# Step 1: Count total businesses by postal code (all descriptions)
total_counts = df['postCode'].value_counts().reset_index()
total_counts.columns = ['postCode', 'totalBusinesses']

# Step 2: Count the number of businesses for the specific description
description = "Ohjelmistojen suunnittelu ja valmistus"
filtered_df = df[df['mainBusinessLineDescription'] == description]
specific_counts = filtered_df['postCode'].value_counts().reset_index()
specific_counts.columns = ['postCode', 'specificBusinesses']

# Step 3: Merge the two counts on postCode
merged_counts = pd.merge(total_counts, specific_counts, on='postCode', how='left').fillna(0)

# Step 4: Calculate correlation and p-value
correlation, p_value = pearsonr(merged_counts['totalBusinesses'], merged_counts['specificBusinesses'])

# Display the merged counts, correlation, and p-value
print("Merged Counts by Postal Code:")
print(merged_counts)
print(f"\nCorrelation between total businesses and specific businesses: {correlation}")
print(f"P-value for the correlation: {p_value}")
