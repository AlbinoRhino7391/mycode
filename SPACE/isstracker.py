import requests
from datetime import datetime
#pip install reverse_geocoder
import reverse_geocoder as rg

def main():
    # Define the API URL
    api_url = "http://api.open-notify.org/iss-now.json"

    # Send a GET request to the API and get the JSON response
    response = requests.get(api_url)
    data = response.json()

    # Extract the timestamp from the JSON response and convert it to human-readable format
    timestamp_epoch = int(data["timestamp"])
    timestamp_readable = datetime.fromtimestamp(timestamp_epoch).strftime('%Y-%m-%d %H:%M:%S')

    # Extract the ISS position
    position = data["iss_position"]
    latitude = float(position["latitude"])
    longitude = float(position["longitude"])

    # Use reverse_geocoder to get the city and country from the latitude and longitude
    results = rg.search((latitude, longitude))
    city = results[0]["name"]
    country = results[0]["cc"]

    # Print the current location of the ISS in a human-readable format
    print("CURRENT LOCATION OF THE ISS:")
    print(f"Timestamp: {timestamp_readable}")
    print(f"Lon: {longitude:.5f}")
    print(f"Lat: {latitude:.5f}")
    print(f"City/Country: {city}, {country}")


if __name__ == "__main__":
    main()

