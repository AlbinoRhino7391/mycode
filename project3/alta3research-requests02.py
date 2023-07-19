#!/usr/bin/env python3

import requests

def normalize_json(json_data):
    normalized_data = []
    for item in json_data:
        normalized_data.append(f"Name: {item['name']}, Age: {item['age']}")
    return normalized_data

if __name__ == '__main__':
    # Replace 'http://localhost:5000' with the URL of your Flask API if it's hosted on a different server.
    api_url = 'http://localhost:5000/json-data'
    
    response = requests.get(api_url)
    
    if response.status_code == 200:
        json_data = response.json()
        normalized_data = normalize_json(json_data)
        for item in normalized_data:
            print(item)
    else:
        print(f"Failed to get data. Status code: {response.status_code}")

