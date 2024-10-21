import pandas as pd
import plotly.express as px

# Load the CSV file
file_path = '../../csv/tampere_companies_filtered.csv'  # Adjust path to your CSV file
df = pd.read_csv(file_path, dtype=str)

# Count occurrences of each postal code
postal_code_counts = df['postCode'].value_counts()

# Filter out postal codes with counts under 100
postal_code_counts = postal_code_counts[postal_code_counts >= 100]

# Create a new list for displaying text
text_labels = []

# Create text labels based on count conditions
for code, count in postal_code_counts.items():
    text_labels.append(f"{code}: {count}")  # Include count for all remaining codes

# Create a pie chart for postal codes
if not postal_code_counts.empty:
    fig = px.pie(
        names=postal_code_counts.index,
        values=postal_code_counts.values,
        title='Distribution of Postal Codes for All Companies (Count >= 100)',
        labels={'names': 'Postal Codes', 'values': 'Counts'},
        template='plotly'
    )

    # Update the text labels for the pie chart
    fig.update_traces(text=text_labels, textinfo='text')

    # Adjust the size and position of the pie chart
    fig.update_layout(
        width=1000,  # Set desired width
        height=1000,  # Set desired height
        margin=dict(l=20, r=20, t=40, b=20),  # Adjust margins as needed
        showlegend=True  # Show legend for clarity
    )


    fig.show()
else:
    print('No postal code data available for the companies with count >= 100.')
