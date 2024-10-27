import pandas as pd
import json


csv_file_path = "../csv/tampere_companies_extracted.csv"
df = pd.read_csv(csv_file_path, dtype=str)


json_file_path = "../json/post_codes_tampere.json"
with open(json_file_path, "r") as json_file:
    postal_codes_data = json.load(json_file)


postal_codes = [item["postCode"] for item in postal_codes_data]


df_filtered = df[df["postCode"].isin(postal_codes)]


df = df_filtered


filtered_file_path = "../csv/tampere_companies_filtered2.csv"
df.to_csv(filtered_file_path, index=False)
print(f"Filtered data saved to: {filtered_file_path}")
