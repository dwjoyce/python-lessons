# guessing.py
# Store a random number between 1 and 100, and then repeatedly ask the user to guess what
# this number is.  Allow up the 6 tries, and then print out the answer if it wasn't guessed.

import random

secret_number = random.randint(1, 100)

number_tries = 0
while number_tries < 6:  # give them 6 tries maximum
    guess = input("What is your guess (between 1 and 100)? ")
    guess = int(guess)

    if guess == secret_number:
        break
    elif guess < secret_number:
        print("Too low!")
    else:
        print("Too high!")

    number_tries = number_tries + 1

if guess == secret_number:
    print("You got it right!")
else:
    print("Wrong! The number was:", secret_number)
