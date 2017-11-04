# checkboard.py
# Ask the user how many squares the checkboard should be drawn with, and then draw
# the checkerboard

import turtle

# Set the number of squares across and down
number_squares = int(input('Please enter the number of squares across: '))

WINDOW_SIZE = 500

# Set square turtle window
turtle.setup(WINDOW_SIZE, WINDOW_SIZE)
turtle.speed(0)

# Save width and calculate side as a proportion of the window
left_side = -WINDOW_SIZE / 2
top_side = WINDOW_SIZE / 2
square_size = WINDOW_SIZE / number_squares

# Step through a number columns
for col in range(number_squares):
    # Set initial colour, depending on whether it is an even column or odd
    if col % 2 == 0:
        square_color = "white"
    else:
        square_color = "black"
    
    # Draw the squares down the screen
    for square in range(number_squares):
        turtle.up()
        turtle.goto(left_side + col * square_size, top_side - square * square_size)
        turtle.down()
        
        # Draw a square
        turtle.fillcolor(square_color)
        turtle.begin_fill()
        for side in range(4):
            turtle.forward(square_size)
            turtle.right(90)
        turtle.end_fill()
        
        # Flip color
        if square_color == "black":
            square_color = "white"
        else:
            square_color = "black"
