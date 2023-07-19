#!/usr/bin/env python4
""" Interactive story for lab 48/project1 """

def main():
    # Welcome message and story setup
    print("Welcome to My Interactive Fiction Game!")
    print("Can you Escape!!!")
    print("You wake up in a daze...")
    print("vision is blurry, but things slowly become clear as your eyes adjust to the darkness.")
    print("You find yourself in what seems to be a cave with nothing around you, but you notice in front of you 3 paths...")
    print("Which path do you choose: (L)eft, (C)enter, (R)ight")

    while True:
        #while loop to give the first chance for the story to branch off
        user_choice = input("Please choose a path? (L/C/R) ")

        if user_choice.lower() == "l":
            choose_left_path() 
            break
        elif user_choice.lower() == "c":
            choose_middle_path() 
            break
        elif user_choice.lower() == "r":
            choose_right_path() 
            break
        else:
            print("Invalid choice. Please enter 'L', 'C', or 'R'.")

def choose_left_path():
    #first branch off, if the user chose the left path
    print("You have chosen to take the path on the left.")
    print("While walking this path, You see faint shine from a pile of rubble.")
    print("Instictively you go to investigate, and you find a key buried amongst the rubble.")
    
    while True:
        #while loop to initiate branch off 2
        print("What would you like to do?")
        key_choice = input("1. Take the key\n2. Leave it\n> ")

        if key_choice == "1": #game over
            print("You bend over to  grab the key...")
            print("with a slight pull you hear a slight 'clink'...")
            print("and within the blink of an eye the floor dissappears and you fall into the abysmal darkness.")
            print("your body remains in the depths of the cave for all eternity.")
            print("Game Over")
            game_over()
            break
        elif key_choice == "2": #continue
            print("You leave the key behind and continue onward.")
            left_key_behind()
            break
        else:
            print("Invalid choice. Please enter either '1' or '2'.")

def left_key_behind():
    #continuation of branch 2 leading into final branch
    print("While continuing onward, you find a ladder and a door.")

    while True:
        print("Which one do you choose?")
        door_choice = input("1. Climb the Ladder\n2. Go through the door\n> ")

        if door_choice == "1": #game over
            print("You start your slow descent up the ladder.")
            print("climbing and climbing, seeming to not move an inch from where you started.")
            print("one step up, and the rung of the ladder snaps like a twig.")
            print("you fall to your death.")
            print("game over")
            game_over()
            break
        elif door_choice == "2":#escape
            print("You open the door and see a bright flash of light.")
            print("with that flash of bright light, you suddenly awaken from a deep sleep...")
            print("It was all just a bad dream.")
            print("congratulations, you win")
            game_over()
            break
        else:
            print("Invalid choice. Please enter either '1' or '2'.")

def choose_middle_path():
    #branch off 1 if user chose the middle path.
    print("You start walking down the middle path.")
    print("After walking for what seemed to be hours, youre greeted by a dog.")
    
    while True:
        #while loop to add branch off 2
        print("What do you want to do?")
        pet_choice = input("1. Pet the dog\n2. Ignore the dog\n> ")

        if pet_choice == "1": #continue
            print("You pet the dog, and it wags its tail happily.")
            print("You continue down the path, and the dog gleefully leads you.")
            pet_doggo()
            break
        elif pet_choice == "2": #game over
            print("You ignore the dog and try to walk past it.")
            print("Only making it a few steps past before hearing a low growl behind you.")
            print("You quickly turn around to be met with razor sharp teeth sinking into your neck.")
            print("Game Over.")
            game_over()
            break
        else:
            print("Invalid choice. Please enter either '1' or '2'.")

def pet_doggo():
    #branch off 2 from the middle path
    print("The dog suddenly takes off running.")
    print("Should you follow the dog or let it run off?")

    while True:
        #while loop to lead into final branch off 50/50
        print("Which one do you choose?")
        door_choice = input("1. Follow\n2. Stay> ")

        if door_choice == "1": #escape
            print("You start to run after the dog.")
            print("after a short while, you both come to an opening with a bright light shining through.")
            print("as you approach the light, you vision adjusts and notice you are outside of the cave.")
            print("Congratulations you escaped the cave.")
            game_over()
            break
        elif door_choice == "2":#game over
            print("The dog quickly fades from sight in the dark cave.")
            print("For some reason you get an uneasy feeling, wondering why the dog ran.")
            print("You are suddenly grabbed from behind...")
            print("game over")
            game_over()
            break
        else:
            print("Invalid choice. Please enter either '1' or '2'.")

def choose_right_path():
    #branch off 1 that leads to game over
    print("You start to walk down the path laid on the right.")
    print("After a short while, you step on a rock, that seems to sink.")
    print("Spears drop from the ceiling and impale you.")
    print("Game Over.")
    game_over()

def game_over():
    #game over function that gives the user the ability to play again.
    while True:
        play_again = input("Would you like to play again? (Y/N) ")

        if play_again.lower() == "y":
            main()
            break
        elif play_again.lower() == "n":
            print("Thank you for playing! Goodbye.")
            break
        else:
            print("Invalid choice. Please enter 'Y' to play again or 'N' to exit.")

if __name__ =="__main__":
# Start the game
    main()