import requests

# Replace 'YOUR_GEOAPIFY_API_KEY' with your actual API key
api_key = 'c8588b6778b94c1da71c7c90926bccf4'

def get_address(latitude, longitude):
    url = f'https://api.geoapify.com/v1/geocode/reverse?lat={latitude}&lon={longitude}&apiKey={api_key}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if 'features' in data and data['features']:
            address = data['features'][0]['properties']['formatted']
            return address
    return None

# Example usage
latitude = 12.838671026976279
longitude = 80.15468784834857
address = get_address(latitude, longitude)
if address:
    print(f"Address: {address}")
else:
    print("Failed to fetch address.")
