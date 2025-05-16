"""
This app simulates the roll of a die of pre-defined sides
"""
from random import randint

die_min = 1  # The minimum value of the die
die_max = 6  # The maximum value of the die
play = True

print(f"This app simulates the roll of a die of {die_max} sides")  # Print to console

def roll_die():
    roll_outcome = randint(die_min, die_max)  # Randomly generate an integer between die_min - die_max
    print(f"\nThe die rolled {roll_outcome}.")
    # return roll_outcome


def roll_again():
    roll = True
    print("Roll again - (Y)es/(N)o? ")  # Print to console
    while roll:
        roll_again = input("Roll again (Yes/No)? ").lower()  # Get user input
        
        if roll_again == "y" or roll_again == "yes":
            break
        elif roll_again == "n" or roll_again == "no":
            roll = False
        else:
            print(f"\nInvalid choice.\nYou entered {roll_again}\nChoose (Y)es or (N)o.")
        
    else:
        global play  # Declare play as global to break outer while-loop
        play = False

while play:  # play = True
    # Randomly choose a number between die_min - die_max inclusive
    roll_die()

    # Ask if user wants to quit or continue simulation 
    roll_again()

print("\nThanks for rolling - bye!")