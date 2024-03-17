import pywifi
import time

def connect_to_wifi(ssid, password):
    try:
        # Interface selection
        wifi = pywifi.PyWiFi()
        iface = wifi.interfaces()[0]  # Replace with the index of your WiFi interface if needed

        # Connect to a specific network
        profile = pywifi.Profile()
        profile.ssid = ssid
        profile.auth = pywifi.const.AUTH_ALG_OPEN  # Change if required (e.g., AUTH_ALG_WPA2PSK)
        profile.akm.append(pywifi.const.AKM_TYPE_WPA2PSK)  # Add AKM type for WPA2 networks
        profile.cipher = pywifi.const.CIPHER_TYPE_CCMP  # Set cipher type
        profile.key = password

        iface.remove_all_network_profiles()
        tmp_profile = iface.add_network_profile(profile)
        iface.connect(tmp_profile)

        # Check connection status
        time.sleep(5)  # Wait for a few seconds before checking
        if iface.status() == pywifi.const.IFACE_CONNECTED:
            print("Connected to WiFi successfully!")
        else:
            print("Connection failed.")

    except Exception as e:
        print(f"Error connecting to WiFi: {e}")

# Example Usage (replace with your credentials)
ssid = "MyServoControl"
password = "12345678"
connect_to_wifi(ssid, password)

# Wait for some time
time.sleep(5)

# New credentials
new_ssid = "127.0.0.1"
new_password = "hehe1234"
connect_to_wifi(new_ssid, new_password)
