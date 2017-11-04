# rockpaperscissors.py
# paper, rock, scissors game where program will randomly choose one of the
# choices, and matches it against the user"s choice.

import random

possible_choices = ["paper", "rock", "scissors"]

while True:
    user_choice = input("What's your choice: rock, paper or scissors (or quit)? ")
    
    if user_choice == "quit":  # break out of loop
        break

    computer_choice = random.choice(possible_choices)

    if not user_choice in possible_choices:
        print("Sorry, don't understand that choice. Let's try again!")
    elif user_choice == computer_choice:
        print("I choose", computer_choice, "too, let's try again!")
    else:
        print("I choose " + computer_choice + ". ", end="")
        
        if (user_choice == "paper" and computer_choice == "rock"     or
            user_choice == "rock" and computer_choice == "scissors"  or
            user_choice == "scissors" and computer_choice == "paper"):           
            print("You win!")
        else:
            print("I win!")

        print("Let's play again!")

    print()
