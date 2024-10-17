import pandas as pd
import plotly.express as px

# Load the CSV file
file_path = '../csv/tampere_companies_filtered2.csv'  # Adjust path to your CSV file
df = pd.read_csv(file_path, dtype=str)

# Filter the DataFrame for postal code 33540
df_33100 = df[df['postCode'] == '33540']

# Count occurrences of each main business line description
business_line_counts = df_33100['mainBusinessLineDescription'].value_counts()

# Exclude descriptions with fewer than 5 companies and take the top 15
business_line_counts = business_line_counts[business_line_counts >= 5].nlargest(15)

# Create a new list for displaying text
text_labels = []

# Create text labels based on count conditions
for desc, count in business_line_counts.items():
    text_labels.append(f"{desc}: {count}")  # Include count for all descriptions

# Create a pie chart for business line descriptions in postal code 33100
if not business_line_counts.empty:
    fig = px.pie(
        names=business_line_counts.index,
        values=business_line_counts.values,
        title='Top 15 Main Business Line Descriptions for Postal Code 33540',
        labels={'names': 'Business Line Descriptions', 'values': 'Counts'},
        template='plotly'
    )

    # Update the text labels for the pie chart
    fig.update_traces(text=text_labels, textinfo='text')

    fig.show()
else:
    print('No main business line description data available for postal code 33100 with 5 or more companies.')
