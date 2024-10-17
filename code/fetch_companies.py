import requests
import json

# Base URL for the API
base_url = "https://avoindata.prh.fi/opendata-ytj-api/v3/companies?location=Tampere"

# Output file
output_file = "tampere_companies.json"

# Initialize the list to hold all companies
all_companies = {"totalResults": 0, "companies": []}

# Initialize page counter
page = 1

while True:
    # Construct the URL for the current page
    response = requests.get(f"{base_url}&page={page}")

    print("hello")

    # Check if the response is successful
    if response.status_code != 200:
        print(f"Error fetching page {page}: {response.status_code}")
        break

    # Parse the JSON response
    data = response.json()
    total_results = data["totalResults"]
    companies = data["companies"]

    # If there are no companies, exit the loop
    if total_results == 0:
        break

    # Append the companies to the list
    all_companies["companies"].extend(companies)
    all_companies["totalResults"] += len(companies)

    print(f"Fetched page {page} with {len(companies)} companies.")
    page += 1

# Write the results to the output file
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(all_companies, f, ensure_ascii=False, indent=4)

print(f"Data fetching complete. Total companies collected: {len(all_companies['companies'])}.")
