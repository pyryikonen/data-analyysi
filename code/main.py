import pandas as pd
import json


with open("tampere_companies.json", "r", encoding="utf-8") as file:
    data = json.load(file)


companies = data.get("companies", [])


df = pd.DataFrame(
    [
        {
            "businessId": company["businessId"]["value"],
            "name": next(
                (
                    name["name"]
                    for name in company.get("names", [])
                    if name.get("type") == "1"
                ),
                None,
            ),
            "mainBusinessLineType": company.get("mainBusinessLine", {}).get("type"),
            "mainBusinessLineDescription": next(
                (
                    desc["description"]
                    for desc in company.get("mainBusinessLine", {}).get(
                        "descriptions", []
                    )
                    if desc["languageCode"] == "1"
                ),
                None,
            ),
            "mainBusinessLineRegDate": company.get("mainBusinessLine", {}).get(
                "registrationDate"
            ),
            "postCode": next(
                (
                    address.get("postCode")
                    for address in company.get("addresses", [])
                    if address.get("type") == 2
                ),
                None,
            ),
        }
        for company in companies
    ]
)


df["mainBusinessLineRegDate"] = pd.to_datetime(
    df["mainBusinessLineRegDate"], errors="coerce"
)


print(df)


df.to_csv("tampere_companies_extracted.csv", index=False)
