#!/usr/bin/env python3

# imports always go at the top of your code
import requests
import json

# Define our "base" API
API = "https://api.magicthegathering.io/v1/" # this will never change regardless of the lookup we perform

def main():
    """Run time code"""

    setcode = input("What is the code of the set you are trying to lookup (see mtgsets.index for a list of codes)? ").lower()   # collect user input for MTG card set to lookup

    # create resp, which is our request object
    resp = requests.get(f"{API}cards?set={setcode}")   # this "f" string reads: API + "cards/" + setcode
    cards_data = resp.json()

    #create a file name based on the setcode
    filename = f"{setcode}_cards.set"

    #write the data to the file in a human-readable form
    with open(filename, "w") as file:
        json.dump(cards_data, file, indent=2)

    print(f"Data has been written to {filename}.")

if __name__ == "__main__":
    main()

