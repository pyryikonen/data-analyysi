import pandas as pd
from scipy.stats import pearsonr
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
df = pd.read_csv("../../csv/tampere_companies_filtered.csv")

# Count total businesses by postal code
total_counts = df["postCode"].value_counts().reset_index()
total_counts.columns = ["postCode", "totalBusinesses"]

# Filter data for the specific business category
description = "Asuntojen ja asuinkiinteistöjen hallinta"
filtered_df = df[df["mainBusinessLineDescription"] == description]
specific_counts = filtered_df["postCode"].value_counts().reset_index()
specific_counts.columns = ["postCode", "specificBusinesses"]

# Merge total and specific business counts by postal code
merged_counts = pd.merge(
    total_counts, specific_counts, on="postCode", how="left"
).fillna(0)

# Compute the Pearson correlation and p-value
correlation, p_value = pearsonr(
    merged_counts["totalBusinesses"], merged_counts["specificBusinesses"]
)

# Print the merged data and correlation results
print("Merged Counts by Postal Code:")
print(merged_counts)
print(f"\nCorrelation between total businesses and specific businesses: {correlation}")
print(f"P-value for the correlation: {p_value}")

# Visualization: Scatter plot with regression line
plt.figure(figsize=(10, 6))
sns.regplot(x="totalBusinesses", y="specificBusinesses", data=merged_counts, scatter_kws={'s': 50}, line_kws={'color': 'red'})
plt.title("Scatter Plot: Total Businesses vs Specific Businesses (Property Management)")
plt.xlabel("Total Businesses")
plt.ylabel("Specific Businesses (Property Management)")
plt.show()

# Visualization: Bar plot for total businesses and specific businesses by postal code
plt.figure(figsize=(12, 8))
merged_counts.set_index('postCode')[['totalBusinesses', 'specificBusinesses']].plot(kind='bar', figsize=(12, 8))
plt.title("Total Businesses vs Specific Businesses by Postal Code")
plt.xlabel("Postal Code")
plt.ylabel("Number of Businesses")
plt.legend(["Total Businesses", "Specific Businesses"])
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
