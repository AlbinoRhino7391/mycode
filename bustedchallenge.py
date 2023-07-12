#!/usr/env python3

def main():
    words = {1: "great",
             2: "fabulous",
             3: "super"}

    while True: #fixed typo
        name = input("What is your name?\n>")
        num = input("Pick a number between 1 and 3: ")

        #changed the input validation to check both name and num
        if name and num in map(str, words.keys()):
            #added parentesis to .capitalize
            #converted num to an int
            #fixed typo, brake to break
            print("Hi " + name.capitalize() + "! Have a " + words[int(num)] + " day!")
            break
        else:
            print("Come on, follow directions. Try again.")
            continue

# Call the main function to start the program
if __name__ == "__main__":
    main()