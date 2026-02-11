# #Project 1: Number Guessing Game (Core Logic Project)
# Problem Statement
# Build a game where:
# Computer selects a random number between 1 and 100.
# User keeps guessing.
# Program tells:
# “Too High”
# “Too Low”
# “Correct”
# Count number of attempts.
# Stop when correct.
# 🔥 Bonus (Intermediate Level)
# Limit attempts to 5
# Ask user if they want to play again
# Handle invalid input

import random

name = input("Enter ur name: ").title()
print(f"Hey {name}, do u want to play a number guessing game?")
startgame = input("Enter Yes to start the Game and No to quit: ").lower()

if startgame == "yes":
    print("Let's start! I'm thinking of a number between 1 and 100.")
    computer_generated = random.randint(1, 100)
    user_chances = 1

    while user_chances <= 5:
        try:
            user_number = int(input(f"Attempt {user_chances}/5 - Enter a number: "))

            if user_number > computer_generated:
                print("You are guessing too high!")
            elif user_number < computer_generated:
                print("You are guessing too low!")
            else:
                print(f"🎉🤩 Awesome, {name}! You guessed it right!")
                break  

            user_chances += 1

        except ValueError:
            print("❌ Invalid input! Please enter a whole number (integer).")

    else:
        print(
            f"😢 Sorry {name}, your chances are over. The number was {computer_generated}."
        )

else:
    print("We are sorry to let u go. Have a great day!")
