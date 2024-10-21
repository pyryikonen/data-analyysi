import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
file_path = '../../csv/tampere_companies_filtered.csv'  # Adjust path to your CSV file
df = pd.read_csv(file_path, dtype=str)

# Count occurrences of each mainBusinessLineDescription
business_line_counts = df_filtered['mainBusinessLineDescription'].value_counts()

# Filter out descriptions with fewer than 10 companies
business_line_counts = business_line_counts[business_line_counts >= 100]

# Create a pie chart if there are sufficient descriptions
if not business_line_counts.empty:
    plt.figure(figsize=(10, 6))
    plt.pie(business_line_counts, labels=business_line_counts.index, autopct='%1.1f%%', startangle=140)
    plt.title('Distribution of Main Business Line Descriptions (100 or more companies)')
    plt.axis('equal')  # Equal aspect ratio ensures the pie chart is circular.
    plt.show()

# Create a horizontal bar chart if there are sufficient descriptions
if not business_line_counts.empty:
    plt.figure(figsize=(10, 6))
    business_line_counts.plot(kind='barh')  # Switch to horizontal bar chart
    plt.title('Counts of Main Business Line Descriptions (100 or more companies)')
    plt.ylabel('Main Business Line Description')  # Y-axis label is now the description
    plt.xlabel('Count')  # X-axis label is now the count
    plt.xticks(rotation=30, ha='right')
    plt.tight_layout()  # Adjust layout for better appearance
    plt.show()
else:
    print('No business line descriptions with 10 or more companies to visualize.')
