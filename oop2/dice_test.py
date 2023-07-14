#!/usr/bin/python3
"""Creating a slightly more complex dice program utilizing classes."""


# imports from cheadice.py (this is in the local directory)
from cheatdice import Player
from cheatdice import Cheat_Swapper
from cheatdice import Cheat_Loaded_Dice
from cheatdice import Mull_Cheater
from cheatdice import Weighted_Dice_Cheater

def main():
    """run-time code"""

    # create two cheater objects
    cheater1 = Cheat_Swapper() # ability is to change 3rd dice roll to 6
    cheater2 = Cheat_Loaded_Dice() # increase all rolls by +1 provided they are < 6
    cheater3 = Mull_Cheater() # player rerolls if sum is less than nine.
    cheater4 = Weighted_Dice_Cheater() # player cant roll less than a 3

    # all players take turns
    cheater1.roll()
    cheater2.roll()
    cheater3.roll()
    cheater4.roll()

    # all players use their cheat methods
    cheater1.cheat()
    cheater2.cheat()
    cheater3.cheat()
    cheater4.cheat()

    print(f"Cheater 1 rolled {cheater1.get_dice()}")
    print(f"Cheater 2 rolled {cheater2.get_dice()}")
    print(f"Cheater 3 rolled {cheater3.get_dice()}")
    print(f"Cheater 4 rolled {cheater4.get_dice()}")

    # Determine the winner based on the sum of dice rolls
    max_sum = max(sum(cheater1.get_dice()), sum(cheater2.get_dice()), sum(cheater3.get_dice()), sum(cheater4.get_dice()))
    winners = []

    if sum(cheater1.get_dice()) == max_sum:
        winners.append("Cheater 1")
    if sum(cheater2.get_dice()) == max_sum:
        winners.append("Cheater 2")
    if sum(cheater3.get_dice()) == max_sum:
        winners.append("Cheater 3")
    if sum(cheater4.get_dice()) == max_sum:
        winners.append("Cheater 4")

    if len(winners) == 1:
        print(f"{winners[0]} wins!")
    elif len(winners) > 1:
        print("It's a draw between the following players:")
        print(", ".join(winners))
    else:
        print("No winner!")

if __name__ == "__main__":
    main()


