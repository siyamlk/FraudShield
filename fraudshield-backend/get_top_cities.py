import json

with open("city_reference.json") as f:
    data = json.load(f)

top = sorted(data.items(), key=lambda x: x[1]["transaction_count"], reverse=True)[:30]

for city, info in top:
    print(f'{{ name: "{city}, {info["state"]}" }},')