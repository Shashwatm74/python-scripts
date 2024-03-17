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
        supabase_url = "https://xzesgzaoewbtbiivxcal.supabase.co/rest/v1/ranking"
        headers = {
            "apikey": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Inh6ZXNnemFvZXdidGJpaXZ4Y2FsIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTA1MjE3ODksImV4cCI6MjAyNjA5Nzc4OX0.D5II1tvD3grGOoNwMkDsibaFBR1TvitYz5J5b8RIi7k",
            "Content-Type": "application/json",
        }
        response = requests.post(supabase_url, headers=headers, json=data)
        if response.status_code == 201:
            print(f"Pushed data to Supabase: {data}")
        else:
            print(f"Failed to push data to Supabase: {response.content}")
