import json

output_file = "post_codes_tampere.json"


with open("post_codes_finland.json", "r", encoding="utf-8") as file:
    data = json.load(file)


sorted_data = sorted(data, key=lambda x: x["municipalityCode"])

with open(output_file, "w", encoding="utf-8") as f:
    json.dump(sorted_data, f, ensure_ascii=False, indent=4)
