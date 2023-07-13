#!/usr/bin/env python3

# Prompt the user to enter the number of bottles of beer to count down from
num_bottles = int(input("Enter the number of bottles of beer to count down from (1-100): "))

# Define the main function
def main():
    # Call the sing_99_bottles function with the user's input as the argument
    sing_99_bottles(num_bottles)

# Define the sing_99_bottles function
def sing_99_bottles(num_bottles):
    # Check if the number of bottles is more than 100
    if num_bottles > 100:
        print("Sorry, you cannot count down from more than 100 bottles of beer.")
        return

    # Loop through the range from num_bottles down to 1 (exclusive), decreasing by 1 in each iteration
    for i in range(num_bottles, 0, -1):
        # Print the current number of bottles on the wall and remaining bottles
        print(f"{i} bottles of beer on the wall, {i} bottles of beer.")
        # Print the instruction to take one down and pass it around, and the updated number of bottles on the wall
        print(f"Take one down, pass it around, {i-1} bottles of beer on the wall.\n")

    # Print the last two lines of the song when there are no more bottles left
    print("No more bottles of beer on the wall, no more bottles of beer.")
    print("Go to the store and buy some more, 99 bottles of beer on the wall.")

# Check if the script is being run directly
if __name__ == "__main__":
    # Start the game by calling the main function
    main()
