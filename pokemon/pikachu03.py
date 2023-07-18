#!/usr/bin/python3

## for accepting arguments from the cmd line
import argparse

## for making HTTP requests
## python3 -m pip install requests
import requests

## for working with data in lots of formats
## python3 -m pip install pandas
import pandas

ITEMURL = "http://pokeapi.co/api/v2/item/"
POKEMONURL = "https://pokeapi.co/api/v2/pokemon/"

def fetch_all_pokemon():
    # Make HTTP GET request to get all Pokemon data
    all_pokemon = requests.get(f"{POKEMONURL}?limit=1000")
    all_pokemon = all_pokemon.json()

    # Extract the list of Pokemon names
    pokemon_list = [pokemon.get("name") for pokemon in all_pokemon.get("results")]

    return pokemon_list

def main():
    # ... (existing code)

    # Fetch all Pokemon data
    all_pokemon = fetch_all_pokemon()

    # Export Pokemon data to plaintext
    with open("pokemon.txt", "w") as txt_file:
        txt_file.write("\n".join(all_pokemon))

    # Export Pokemon data to JSON
    with open("pokemon.json", "w") as json_file:
        json_file.write(f'{{ "pokemon": {all_pokemon} }}')

    # Export Pokemon data to Excel
    pokemon_data = {"pokemon": all_pokemon}
    pokemon_df = pandas.DataFrame(pokemon_data)
    pokemon_df.to_excel("pokemon.xlsx", index=False)

    # ... (existing code)

if __name__ == "__main__":
    # ... (existing code)
    main()

