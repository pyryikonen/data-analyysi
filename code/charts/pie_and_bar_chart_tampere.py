import pandas as pd
import matplotlib.pyplot as plt


file_path = "../../csv/tampere_companies_filtered.csv"
df = pd.read_csv(file_path, dtype=str)


business_line_counts = df["mainBusinessLineDescription"].value_counts()


business_line_counts = business_line_counts[business_line_counts >= 100]


if not business_line_counts.empty:
    plt.figure(figsize=(10, 6))
    plt.pie(
        business_line_counts,
        labels=business_line_counts.index,
        autopct="%1.1f%%",
        startangle=140,
    )
    plt.title("Distribution of Main Business Line Descriptions (100 or more companies)")
    plt.axis("equal")
    plt.show()


if not business_line_counts.empty:
    plt.figure(figsize=(10, 6))
    business_line_counts.plot(kind="barh")
    plt.title("Counts of Main Business Line Descriptions (100 or more companies)")
    plt.ylabel("Main Business Line Description")
    plt.xlabel("Count")
    plt.xticks(rotation=30, ha="right")
    plt.tight_layout()
    plt.show()
else:
    print("No business line descriptions with 10 or more companies to visualize.")
