import pandas as pd
import matplotlib.pyplot as plt


file_path = "../../csv/tampere_companies_filtered.csv"
df = pd.read_csv(file_path, dtype=str)


df["mainBusinessLineRegDate"] = pd.to_datetime(
    df["mainBusinessLineRegDate"], errors="coerce"
)


df_filtered = df[df["mainBusinessLineRegDate"].dt.year >= 2000]


postal_year_counts = (
    df_filtered.groupby(["postCode", df_filtered["mainBusinessLineRegDate"].dt.year])
    .size()
    .reset_index(name="count")
)


postal_year_counts["cumulative_count"] = postal_year_counts.groupby("postCode")[
    "count"
].cumsum()


postal_year_counts_pivot = postal_year_counts.pivot(
    index="mainBusinessLineRegDate", columns="postCode", values="cumulative_count"
).fillna(0)


top_5_postal_codes = postal_year_counts_pivot.max().nlargest(5).index


postal_year_counts_top_5 = postal_year_counts_pivot[top_5_postal_codes]


plt.figure(figsize=(14, 8))
for postal_code in postal_year_counts_top_5.columns:
    plt.plot(
        postal_year_counts_top_5.index.astype(str),
        postal_year_counts_top_5[postal_code],
        marker="o",
        label=postal_code,
    )

plt.title(
    "Cumulative Count of Companies by Top 5 Postal Codes and Registration Year (From 2000 to 2024)"
)
plt.xlabel("Registration Year")
plt.ylabel("Cumulative Number of Companies")


plt.autoscale(axis="x", tight=True)


plt.legend(title="Postal Code")
plt.grid()
plt.show()
