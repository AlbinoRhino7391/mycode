#!/usr/bin/env python3

import requests
import shutil

def main():
    pokenum = input("Pick a number between 1 and 151!\n>")
    pokeapi = requests.get("https://pokeapi.co/api/v2/pokemon/" + pokenum).json()

    # Get the URL to "front_default" sprite image
    sprite_url = pokeapi["sprites"]["front_default"]

    # Download the sprite image
    response = requests.get(sprite_url, stream=True)
    if response.status_code == 200:
        # Save the image to /home/student/static
        save_path = f"/home/student/static/pokemon_{pokenum}.png"
        with open(save_path, "wb") as file:
            response.raw.decode_content = True
            shutil.copyfileobj(response.raw, file)
        print("Sprite image has been downloaded and saved.")
    else:
        print("Failed to download the sprite image.")

    # Print out the names of all the selected Pokemon's "moves"
    print("\nMoves:")
    for move in pokeapi["moves"]:
        print(move["move"]["name"])

    # Count the total number of games this Pokemon character appeared in
    total_games = len(pokeapi["game_indices"])

    # Print the count of how many games the selected Pokemon has appeared in
    print("\nTotal number of games:", total_games)

if __name__ == "__main__":
    main()

