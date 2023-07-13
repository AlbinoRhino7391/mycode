#!/usr/bin/env python3

farms = [
    {"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
    {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
    {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}
]

def main():
    # Return all the animals from the NE Farm
    ne_farm_animals = []
    for farm in farms:
        if farm["name"] == "NE Farm":
            ne_farm_animals = farm["agriculture"]

    print("Animals from NE Farm:", ne_farm_animals)

    # Ask the user to choose a farm and return the plants/animals raised on that farm
    chosen_farm = input("Choose a farm (NE Farm, W Farm, or SE Farm): ")
    chosen_farm_plants_animals = []
    for farm in farms:
        if farm["name"] == chosen_farm:
            chosen_farm_plants_animals = farm["agriculture"]

    print("Plants/Animals from", chosen_farm + ":", chosen_farm_plants_animals)

    # Ask the user to choose a farm and return only the animals from that farm
    chosen_farm = input("Choose a farm (NE Farm, W Farm, or SE Farm): ")
    chosen_farm_animals = []
    for farm in farms:
        if farm["name"] == chosen_farm:
            for item in farm["agriculture"]:
                if isinstance(item, str) and item not in ["carrots", "celery"]:
                    chosen_farm_animals.append(item)

    print("Animals from", chosen_farm + ":", chosen_farm_animals)


if __name__ == "__main__":
    # Start the program by calling the main function
    main()
