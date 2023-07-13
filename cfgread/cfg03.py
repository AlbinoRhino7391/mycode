#!/usr/bin/env python3

# Prompt the user for the filename
filename = input("Enter the name of the file to load: ")

# Open the file in "r"ead mode
with open(filename, "r") as configfile:
    # Read the file line by line and create a list
    configlist = configfile.readlines()

# Each item of the list now has the "\n" characters included
print(configlist)

# Count the number of lines
line_count = len(configlist)

# Print the number of lines on the screen
print("Number of lines in", filename, ":", line_count)
