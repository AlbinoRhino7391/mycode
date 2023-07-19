# client.py - Contains the client code

import requests

BASE_URL = "http://localhost:2224"

def make_fast_requests(num_requests):
    for _ in range(num_requests):
        response = requests.get(f"{BASE_URL}/fast")
        print(f"Status Code: {response.status_code}, Response: {response.text}")

if __name__ == "__main__":
    num_lookups = 51
    make_fast_requests(num_lookups)

