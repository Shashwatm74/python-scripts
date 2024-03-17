import csv
import requests

with open("payl.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip the header row
    for row in reader:
        # Push each row to Supabase
        latitude, longitude, timestamp = row
        data = {
            "latitude": latitude,
            "longitude": longitude,
            "timestamp": timestamp,
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
