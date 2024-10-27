import pandas as pd
import plotly.graph_objects as go

file_path = "../../csv/tampere_companies_filtered.csv"
df = pd.read_csv(file_path, dtype=str)

business_line_counts = df["mainBusinessLineDescription"].value_counts()

business_over_50 = business_line_counts[business_line_counts > 50]
business_under_50 = business_line_countsbusiness_under_50 = business_line_counts[
    (business_line_counts <= 50) & (business_line_counts > 10)
]

fig_over_50 = go.Figure()
fig_over_50.add_trace(
    go.Bar(
        y=business_over_50.index,
        x=business_over_50.values,
        name="Over 50 Companies",
        orientation="h",
    )
)
fig_over_50.update_layout(
    title="Business Line Descriptions (Over 50 Companies)",
    yaxis_title="Main Business Line Description",
    xaxis_title="Count",
    height=1200,
    margin=dict(l=50, r=20, t=40, b=150),
)

fig_under_50 = go.Figure()
fig_under_50.add_trace(
    go.Bar(
        y=business_under_50.index,
        x=business_under_50.values,
        name="50 or Fewer Companies",
        orientation="h",
    )
)

fig_under_50.update_layout(
    title="Business Line Descriptions (50 or Fewer Companies)",
    yaxis_title="Main Business Line Description",
    xaxis_title="Count",
    height=1200,
    margin=dict(l=50, r=20, t=40, b=150),
)


fig_over_50.show()
fig_under_50.show()
