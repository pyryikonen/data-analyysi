import pandas as pd
from scipy.stats import pearsonr


df = pd.read_csv("../../csv/tampere_companies_filtered.csv")


total_counts = df["postCode"].value_counts().reset_index()
total_counts.columns = ["postCode", "totalBusinesses"]


description = "Ohjelmistojen suunnittelu ja valmistus"
filtered_df = df[df["mainBusinessLineDescription"] == description]
specific_counts = filtered_df["postCode"].value_counts().reset_index()
specific_counts.columns = ["postCode", "specificBusinesses"]


merged_counts = pd.merge(
    total_counts, specific_counts, on="postCode", how="left"
).fillna(0)


correlation, p_value = pearsonr(
    merged_counts["totalBusinesses"], merged_counts["specificBusinesses"]
)


print("Merged Counts by Postal Code:")
print(merged_counts)
print(f"\nCorrelation between total businesses and specific businesses: {correlation}")
print(f"P-value for the correlation: {p_value}")
