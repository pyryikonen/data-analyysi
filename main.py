import pandas as pd
import json
from datetime import datetime

# Load JSON data
with open('prh_yritys_data.json', 'r') as file:
    data = json.load(file)

# Extract the list of companies from the "companies" key
companies = data.get('companies', [])

# Convert data to a DataFrame
df = pd.DataFrame([
    {
        'businessId': company['businessId']['value'],  # Accessing 'value' inside 'businessId'
        'registrationDate': company['businessId']['registrationDate'],
        'mainBusinessLineType': company['mainBusinessLine']['type'],
        'mainBusinessLineDescription': next(
            (desc['description'] for desc in company['mainBusinessLine']['descriptions'] if desc['languageCode'] == "3"),
            None  # Get the English description (languageCode: 3)
        ),
        'mainBusinessLineRegDate': company['mainBusinessLine']['registrationDate'],
        'companyFormType': company['companyForms'][0]['type'],
        'companyFormDescription': next(
            (desc['description'] for desc in company['companyForms'][0]['descriptions'] if desc['languageCode'] == "3"),
            None  # Get the English form description
        ),
    }
    for company in companies if 'businessId' in company and 'mainBusinessLine' in company and 'companyForms' in company
])

# Convert registrationDate to datetime format
df['registrationDate'] = pd.to_datetime(df['registrationDate'])
df['mainBusinessLineRegDate'] = pd.to_datetime(df['mainBusinessLineRegDate'])

# Display the DataFrame with the English descriptions of the main business line
print(df[['businessId', 'mainBusinessLineType', 'mainBusinessLineDescription', 'mainBusinessLineRegDate']])

# Analysis 1: Business Line count
business_line_count = df['mainBusinessLineType'].value_counts()
print("\nBusiness Line Count:\n", business_line_count)

# Analysis 2: Registration date trends
df['registrationYear'] = df['registrationDate'].dt.year
registration_trends = df['registrationYear'].value_counts().sort_index()
print("\nCompany Registration Trends:\n", registration_trends)

# Analysis 3: Company forms
company_form_count = df['companyFormDescription'].value_counts()
print("\nCompany Forms Count:\n", company_form_count)
