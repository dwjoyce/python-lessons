# battleship.py
# Program to store coordinates (row and column), and then give the user 5 guesses to
# correctly guess both of them

import random

map_size = 5

ship_row = random.randrange(1, map_size + 1)
ship_col = random.randrange(1, map_size + 1)

guesses = 0
while guesses < 5:
    user_row = int(input("Where is my ship, row? "))
    user_col = int(input("Where is my ship, col? "))

    if user_row == ship_row and user_col == ship_col:
        print("You sunk my battleship!")
        break
    elif (user_row < 1 or user_row > map_size or
          user_col < 1 or user_col > map_size):
        print("That\"s not even on the map!")
    elif user_row == ship_row:
        print("Missed, but the row was correct!")
    elif user_col == ship_col:
        print("Missed, but the column was correct!")
    else:
        print("Wrong!  My ship survives to fight another day!")

    guesses = guesses + 1

if guesses == 5:
    print("Ha! Out of guesses!")
