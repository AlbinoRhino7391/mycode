#!/usr/bin/env python3
"""Number guessing game! User has 5 chances to guess a number between 1 and 100!"""

import random #to fix the call to get a random int

def main():
    num = random.randint(1, 100)
    rounds = 0

    while rounds < 5:
        guess = input("Guess a number between 1 and 100: ")

        if guess.isdigit():
            guess = int(guess)
        else:
            #handle error of non-numeric value and continue the game
            print("Invalid input. Please enter a valid number.")
            continue

        if guess > num:
            print("Too high!")
            #fixed to increment the rounds
            rounds += 1

        #Used elif instead of multiple if statements for checking if the guess is too low or too high. This ensures that only one message is printed per guess.
        elif guess < num:
            print("Too low!")
            rounds += 1

        else:
            print("Correct!")
            #Added a break statement to exit the loop when the guess is correct.
            break

    #Included an additional if statement after the loop to display a message when the user runs out of rounds without guessing the correct number.
    if guess != num:
        print("You ran out of rounds. The number was", num)

# Call the main function to start the game
if __name__ == "__main__":
    main()
