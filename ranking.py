import csv
import requests

with open("smart.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip the header row
    for row in reader:
        # Push each row to Supabase
        cities, aqi, transportation, waste, qualityoflife = row
        data = {
            "cities": cities,
            "aqi": aqi,
            "transportation": transportation,
            "waste": waste,
            "qualityoflife": qualityoflife,
        }
        supabase_url = ""
        headers = {
            "apikey": "",
            "Content-Type": "application/json",
        }
        response = requests.post(supabase_url, headers=headers, json=data)
        if response.status_code == 201:
            print(f"Pushed data to Supabase: {data}")
        else:
            print(f"Failed to push data to Supabase: {response.content}")
