import random

# Global range for the guessing game
min_num = 1
max_num = 100

def show_feedback_guide():
    """Displays a helpful guide to what the guess feedback means."""
    print("\n**Important Note: You can type 'q' at any time to quit the game.**")
    print("\nFeedback Guide:")
    print("After each guess, you'll get a hint about how close you are:")
    print("Super hot  - You're very, very close to the number (within 2).")
    print("Hot        - You're close (within 5).")
    print("Warm       - You're not far off (within 10).")
    print("Cool       - You're getting warmer, but still off (within 20).")
    print("Cold       - You're far away from the number (more than 20).")
    print("You can also type 'exit' anytime to quit the game.")
    print("You'll be told if your guess is too high or too low.\n")


def guess_number(min_num, max_num):
    rand_num = random.randint(min_num, max_num)
    attempts = 0

    print(f"\nI'm thinking of a number between {min_num} and {max_num}. Try to guess it!")
    show_feedback_guide()

    while True:
        user_input = input(f"\nEnter your guess ({min_num}-{max_num}) or type 'q' to quit: ").strip().lower()

        if user_input == 'q':
            print("You chose to exit the game.")
            return

        try:
            guess = int(user_input)
            print ("Your guess is: ", guess)
            attempts += 1

            if not (min_num <= guess <= max_num):
                print("Please guess within the valid range.\n")
                continue

            if guess == rand_num:
                print(f"Correct! You got it in {attempts} attempts.")
                break
            else:
                diff = abs(rand_num - guess)

                # guess feedback
                if diff <= 2:
                    print("Super hot! You're very, very close.\n")
                elif diff <= 5:
                    print("Hot! Almost there.\n")
                elif diff <= 10:
                    print("Warm.")
                elif diff <= 20:
                    print("Cool. Getting warmer.\n")
                else:
                    print("Cold.\n")

                # Directional feedback
                if guess < rand_num:
                    print("Your guess is too low. Try a higher number.\n")
                else:
                    print("Your guess is too high. Try a lower number.\n")

        except ValueError:
            print("Invalid input. Please enter a whole number or 'q' to quit.")

def play_game():
    while True:
        guess_number(min_num, max_num)
        play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if play_again not in ['yes', 'y']:
            print("Thanks for playing. Goodbye.")
            break

# Start the game
play_game()