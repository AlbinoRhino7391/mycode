#!/usr/bin/env python3
"""This is to practice reading and writing from files"""
def main():
    input_filename = "dracula.txt"
    output_filename = "vampytimes.txt"

    vampire_lines = []  # To store lines containing the word "vampire"

    with open(input_filename, "r") as input_file:
        for line in input_file:
            if "vampire" in line.lower():
                vampire_lines.append(line)  # Append the line to the list

                # Print the line
                print(line.rstrip())

    # Count the number of lines containing the word "vampire"
    line_count = len(vampire_lines)
    print("Number of lines containing 'vampire':", line_count)

    # Write the vampire lines to the output file
    with open(output_filename, "w") as output_file:
        output_file.writelines(vampire_lines)

    print("Vampire lines have been written to", output_filename)


if __name__ == "__main__":
    main()
