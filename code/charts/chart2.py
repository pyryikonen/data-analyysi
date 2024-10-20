import pandas as pd
import plotly.graph_objects as go

# Load the CSV file
file_path = '../csv/tampere_companies_extracted.csv'  # Adjust path to your CSV file
df = pd.read_csv(file_path, dtype=str)

# Convert mainBusinessLineType to string and filter out rows with '68202'
df_filtered = df[df['mainBusinessLineType'] != '68202']

# Save the filtered DataFrame to a new CSV file
filtered_file_path = '../csv/tampere_companies_filtered.csv'  # Save path for the filtered file
df_filtered.to_csv(filtered_file_path, index=False)
print(f'Filtered data saved to: {filtered_file_path}')

# Count occurrences of each mainBusinessLineDescription
business_line_counts = df_filtered['mainBusinessLineDescription'].value_counts()

# Create two separate DataFrames for descriptions based on the count
business_over_50 = business_line_counts[business_line_counts > 50]
business_under_50 = business_line_countsbusiness_under_50 = business_line_counts[(business_line_counts <= 50) & (business_line_counts > 10)]


# Create the horizontal bar chart for business descriptions over 50 companies
fig_over_50 = go.Figure()
fig_over_50.add_trace(go.Bar(
    y=business_over_50.index,  # Main Business Line Descriptions on y-axis
    x=business_over_50.values,  # Counts on x-axis
    name='Over 50 Companies',
    orientation='h'  # Set orientation to horizontal
))
fig_over_50.update_layout(
    title='Business Line Descriptions (Over 50 Companies)',
    yaxis_title='Main Business Line Description',  # Update titles accordingly
    xaxis_title='Count',
    height=1200,
    margin=dict(l=50, r=20, t=40, b=150)  # Adjust margins
)

# Create the horizontal bar chart for business descriptions under or equal to 50 companies
fig_under_50 = go.Figure()
fig_under_50.add_trace(go.Bar(
    y=business_under_50.index,  # Main Business Line Descriptions on y-axis
    x=business_under_50.values,  # Counts on x-axis
    name='50 or Fewer Companies',
    orientation='h'  # Set orientation to horizontal
))
fig_under_50.update_layout(
    title='Business Line Descriptions (50 or Fewer Companies)',
    yaxis_title='Main Business Line Description',  # Update titles accordingly
    xaxis_title='Count',
    height=1200,
    margin=dict(l=50, r=20, t=40, b=150)  # Adjust margins
)

# Show both figures
fig_over_50.show()
fig_under_50.show()
