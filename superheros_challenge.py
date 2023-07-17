#!/usr/bin/env python3
import random

classinfo = {
    "all": [
        {
            "name": "Ariana",
            "skill level": "wondrous",
            "spirit animal": "Alpaca",
            "super power": "Structure Weakening",
        },
        {
            "name": "Lily",
            "skill level": "admirable",
            "spirit animal": "Shark",
            "super power": "Super Strength",
        },
        {
            "name": "Eric",
            "skill level": "amazing",
            "spirit animal": "Goat",
            "super power": "Weather Control",
        },
        {
            "name": "Exxon",
            "skill level": "astonishing",
            "spirit animal": "Banana",
            "super power": "Flight",
        },
        {
            "name": "Jason",
            "skill level": "awesome",
            "spirit animal": "Horse",
            "super power": "X-ray Vision",
        },
        {
            "name": "James",
            "skill level": "brilliant",
            "spirit animal": "Eagle",
            "super power": "Helicopter Propulsion",
        },
        {
            "name": "Kevin",
            "skill level": "cool",
            "spirit animal": "Rabbit",
            "super power": "Invisibility",
        },
        {
            "name": "Michael",
            "skill level": "enjoyable",
            "spirit animal": "Water buffalo",
            "super power": "Immobility",
        },
        {
            "name": "Raylan",
            "skill level": "excellent",
            "spirit animal": "Chicken",
            "super power": "Immutability",
        },
        {
            "name": "Richard",
            "skill level": "fabulous",
            "spirit animal": "Duck",
            "super power": "Invulnerability",
        },
        {
            "name": "Joseph",
            "skill level": "fantastic",
            "spirit animal": "Goose",
            "super power": "Jet Propulsion",
        },
        {
            "name": "Josia",
            "skill level": "fine",
            "spirit animal": "Pigeon",
            "super power": "Matter Ingestion",
        },
        {
            "name": "Kendra",
            "skill level": "incredible",
            "spirit animal": "Turkey",
            "super power": "Mobile Invulnerability",
        },
        {
            "name": "Tito",
            "skill level": "magnificent",
            "spirit animal": "Aardvark",
            "super power": "Muscle Manipulation",
        },
        {
            "name": "Ryan",
            "skill level": "marvelous",
            "spirit animal": "Aardwolf",
            "super power": "Nail Manipulation",
        },
        {
            "name": "Sabin",
            "skill level": "outstanding",
            "spirit animal": "Elephant",
            "super power": "Needle Projection",
        },
        {
            "name": "Sheraz",
            "skill level": "pleasing",
            "spirit animal": "Alligator",
            "super power": "Sonic Voice",
        },
        {
            "name": "Sunny",
            "skill level": "remarkable",
            "spirit animal": "Alpaca",
            "super power": "Hydrokinesis",
        },
    ]
}

# Part 1. Find your name in the classinfo dictionary below. Write code that prints your first name from the classinfo data shown here.
# Convert the name to lowercase to match the case in the dictionary
my_name = input("Enter your name: ").lower()

# Iterate through the "all" list to find the matching name
for student in classinfo["all"]:
    if student["name"].lower() == my_name:
        print("My name is:", student["name"])
        print("\n")
        break
else:
    print("Name not found in the classinfo dictionary.\n")

# Part 2. Find your name in the classinfo dictionary below. Write a script that outputs ONE of the following using the classinfo dictionary below. (fill in the blank!):
""" My name is ______ and my spirit animal is _______.

    My name is ______ and my skills are _______.

    My name is ______ and my super power is _______."""  
# Function to randomly choose one of the output formats and corresponding attribute
def get_random_output_format():
    output_formats = [
        ("My name is {} and my spirit animal is {}.\n", "spirit animal"),
        ("My name is {} and my skills are {}.\n", "skill level"),
        ("My name is {} and my super power is {}.\n", "super power")
    ]
    return random.choice(output_formats)

# Find the data for "Eric" in the classinfo dictionary
eric_data = next((student for student in classinfo["all"] if student["name"].lower() == "eric"), None)

if eric_data:
    # Fill in the blanks with the data for "Eric" and corresponding attribute
    output_format, attribute = get_random_output_format()
    output = output_format.format(eric_data["name"], eric_data[attribute])

    # Print the final output
    print(output)
else:
    print("Eric's information not found in the classinfo dictionary.")



# Part 3. Write a script that loops through the entire classinfo dictionary. Have it output the following for every person in class:
""" Mario, a <wondrous> <alpaca> of a programmer, possesses a <structure weakening> factor for moonlighting as a superhero!

    Luigi, an <admirable> <donkey> of a programmer, possesses a <super strength> factor for moonlighting as a superhero!"""
for person in classinfo["all"]:
    name = person["name"]
    skill_level = person["skill level"]
    spirit_animal = person["spirit animal"]
    super_power = person["super power"]

    output = f"{name}, a {skill_level} {spirit_animal} of a programmer, possesses a {super_power} factor for moonlighting as a superhero!"
    print(output)