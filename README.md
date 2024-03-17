# Python Scripts Repository

This repository contains a collection of Python scripts for various purposes, including connecting to Wi-Fi networks, fetching and processing sensor and GPS data, and interacting with APIs.

## Scripts

### 1. Geolocation Script

This script uses the Geoapify Geocoding API to get the address corresponding to a given latitude and longitude. It also demonstrates how to connect to a Wi-Fi network using the provided SSID and password.

### 2. Sensor Data Collection and Display System

This script fetches sensor and GPS data from a specific URL, processes the fetched data, and then pushes the data to a Supabase database. It also includes an example usage of the `connect_to_wifi` function with specific SSID and password.

### 3. CSV Data Pusher

This script reads data from a CSV file and pushes each row to a Supabase database.

### 4. Sensor and GPS Data Fetcher

This script continuously fetches sensor and GPS data from a specific URL, processes the fetched data, and stores the data in a CSV file.

### 5. Wi-Fi Connector

This script demonstrates how to connect to a Wi-Fi network using the provided SSID and password. It also attempts to connect to a new Wi-Fi network with a different SSID and password.

## Libraries Used

- `requests`
- `pywifi`
- `time`
- `csv`
- `re`

## Installation

To use these scripts, you need to install the required Python libraries. You can do this using pip:

```bash
pip install requests pywifi
