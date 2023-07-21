#!/usr/bin/env python3
"""
This script demonstrates sending a GET request to a Flask API hosted on 'http://localhost:5000/json-data'.
The API endpoint returns JSON data representing a list of people with their names and ages.

The script 'alta3research-requests02.py' sends a GET request to the API, receives the JSON response,
and normalizes the data into a simple format for easy understanding.

To run this script, make sure the Flask API ('alta3research-flask01.py') is running in another terminal.

Prerequisites:
- Python 3 and the 'requests' library installed.
"""

import requests

def normalize_json(json_data):
    """
    This function takes JSON data as input and normalizes it into a list of strings, where each string represents a person with their name and age.

    Args:
        json_data (list): List of dictionaries containing person data (name and age).

    Returns:
        list: List of strings representing each person with their name and age.
    """
    normalized_data = []
    for item in json_data:
        normalized_data.append(f"Name: {item['name']}, Age: {item['age']}")
    return normalized_data

if __name__ == '__main__':
    # Replace 'http://localhost:5000' with the URL of your Flask API if it's hosted on a different server, we are using local host for dem purposes.
    api_url = 'http://localhost:5000/json-data'
    
    response = requests.get(api_url)
    
    if response.status_code == 200:
        json_data = response.json()
        normalized_data = normalize_json(json_data)
        for item in normalized_data:
            print(item)
    else:
        print(f"Failed to get data. Status code: {response.status_code}")

