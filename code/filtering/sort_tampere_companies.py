import pandas as pd
import json


try:
    with open("full_company_data.json", "r", encoding="utf-8-sig") as file:
        data = json.load(file)
except UnicodeDecodeError:
    with open("full_company_data.json", "r", encoding="ISO-8859-1") as file:
        data = json.load(file)


companies = data.get("companies", [])


df = pd.DataFrame(
    [
        {
            "businessId": company["businessId"]["value"],
            "registrationDate": company["businessId"]["registrationDate"],
            "city": next(
                (
                    post_office["city"]
                    for address in company.get("addresses", [])
                    if "postOffices" in address
                    for post_office in address["postOffices"]
                    if post_office["city"].upper() == "TAMPERE"
                ),
                None,
            ),
            "mainBusinessLineType": company.get("mainBusinessLine", {}).get(
                "type", None
            ),
            "companyFormType": (
                company["companyForms"][0]["type"]
                if "companyForms" in company and company["companyForms"]
                else None
            ),
        }
        for company in companies
    ]
)


df_tampere = df[df["city"] == "TAMPERE"]


df_tampere.to_csv("tampere_companies.csv", index=False)

print("Filtered companies located in Tampere saved to 'tampere_companies.csv'")
