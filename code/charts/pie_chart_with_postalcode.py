import pandas as pd
import plotly.express as px


file_path = "../../csv/tampere_companies_filtered.csv"
df = pd.read_csv(file_path, dtype=str)


postal_code_counts = df["postCode"].value_counts()


postal_code_counts = postal_code_counts[postal_code_counts >= 100]


text_labels = []


for code, count in postal_code_counts.items():
    text_labels.append(f"{code}: {count}")


if not postal_code_counts.empty:
    fig = px.pie(
        names=postal_code_counts.index,
        values=postal_code_counts.values,
        title="Distribution of Postal Codes for All Companies (Count >= 100)",
        labels={"names": "Postal Codes", "values": "Counts"},
        template="plotly",
    )

    fig.update_traces(text=text_labels, textinfo="text")

    fig.update_layout(
        width=1000, height=1000, margin=dict(l=20, r=20, t=40, b=20), showlegend=True
    )

    fig.show()
else:
    print("No postal code data available for the companies with count >= 100.")
