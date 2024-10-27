import requests
import json


base_url = "https://avoindata.prh.fi/opendata-ytj-api/v3/companies?location=Tampere"


output_file = "tampere_companies.json"


all_companies = {"totalResults": 0, "companies": []}


page = 1

while True:

    response = requests.get(f"{base_url}&page={page}")

    print("hello")

    if response.status_code != 200:
        print(f"Error fetching page {page}: {response.status_code}")
        break

    data = response.json()
    total_results = data["totalResults"]
    companies = data["companies"]

    if total_results == 0:
        break

    all_companies["companies"].extend(companies)
    all_companies["totalResults"] += len(companies)

    print(f"Fetched page {page} with {len(companies)} companies.")
    page += 1


with open(output_file, "w", encoding="utf-8") as f:
    json.dump(all_companies, f, ensure_ascii=False, indent=4)

print(
    f"Data fetching complete. Total companies collected: {len(all_companies['companies'])}."
)
