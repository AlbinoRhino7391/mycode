#!/usr/bin/python3
"""Alta3 Research - Exploring OpenAPIs with requests"""
# documentation for this API is at
# https://anapioficeandfire.com/Documentation

import requests
import pprint

AOIF_CHAR = "https://www.anapioficeandfire.com/api/characters/"

def main():
    ## Ask user for input
    got_charToLookup = input("Pick a number between 1 and 1000 to return info on a GoT character! ")

    ## Send HTTPS GET to the API of ICE and Fire character resource
    gotresp = requests.get(AOIF_CHAR + got_charToLookup)

    ## Decode the response
    got_dj = gotresp.json()

    ## Extract house(s) affiliated with the character
    affiliated_houses = got_dj['allegiances']
    if affiliated_houses:
        print("Affiliated House(s):")
        for house_url in affiliated_houses:
            house_response = requests.get(house_url)
            house_data = house_response.json()
            print(f"- {house_data['name']}")

    ## Extract list of books the character appears in
    appeared_in_books = got_dj['books']
    if appeared_in_books:
        print("Appears in Books:")
        for book_url in appeared_in_books:
            book_response = requests.get(book_url)
            book_data = book_response.json()
            print(f"- {book_data['name']}")

if __name__ == "__main__":
    main()
