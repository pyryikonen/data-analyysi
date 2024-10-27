import pandas as pd
import plotly.express as px


file_path = "../../csv/tampere_companies_filtered.csv"
df = pd.read_csv(file_path, dtype=str)


df_33100 = df[df["postCode"] == "33520"]


business_line_counts = df_33100["mainBusinessLineDescription"].value_counts()


business_line_counts = business_line_counts[business_line_counts >= 5].nlargest(15)


text_labels = []


for desc, count in business_line_counts.items():
    text_labels.append(f"{desc}: {count}")


if not business_line_counts.empty:
    fig = px.pie(
        names=business_line_counts.index,
        values=business_line_counts.values,
        title="Top 15 Main Business Line Descriptions for Postal Code 33520",
        labels={"names": "Business Line Descriptions", "values": "Counts"},
        template="plotly",
    )

    fig.update_traces(text=text_labels, textinfo="text")

    fig.show()
else:
    print(
        "No main business line description data available for postal code 33100 with 5 or more companies."
    )
