import requests
from time import sleep
import csv
import re


# Define the target URL for sensor and GPS data
url = "http://192.168.4.1/"

while True:
  try:
    # Send a GET request to the sensor data URL
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for unsuccessful requests

    # Get the webpage content
    content = response.text

    # Extract sensor distances and GPS data using regular expressions (unchanged)
    sensor1_match = re.search(r"Distance \(Sensor 1\): (\d+) cm", content)
    sensor2_match = re.search(r"Distance \(Sensor 2\): (\d+) cm", content)
    latitude_match = re.search(r"Latitude: ([\d.-]+)", content)  # Capture latitude with decimals
    longitude_match = re.search(r"Longitude: ([\d.-]+)", content)  # Capture longitude with decimals

    if sensor1_match and sensor2_match and latitude_match and longitude_match:
      sensor1_distance = int(sensor1_match.group(1))
      sensor2_distance = int(sensor2_match.group(1))
      latitude = float(latitude_match.group(1))
      longitude = float(longitude_match.group(1))

      # Process and utilize the data (sensor distances and GPS coordinates)
      print(f"Latitude: {latitude}")
      print(f"Longitude: {longitude}")
      print(f"Sensor 1 Distance: {sensor1_distance} cm")
      print(f"Sensor 2 Distance: {sensor2_distance} cm")

      # Optional: Save data to CSV (modify as needed)
      with open("sensor_data.csv", "a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([latitude, longitude, sensor1_distance, sensor2_distance])

    else:
      print("Error: Could not extract data from the webpage content.")

  except requests.exceptions.RequestException as e:
    print(f"Error scraping webpage: {e}")

  # Wait 10 seconds before the next request
  sleep(10)
