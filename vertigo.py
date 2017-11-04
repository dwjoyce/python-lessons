# vertigo.py
# Draw lines in a spiral shape

import turtle
import random

# Define the colors we will use below
colors = ["red", "green", "blue", "magenta", "cyan", "yellow"]

# Set the pen size, color and drawing speed
turtle.pensize(2)
turtle.speed(0)

# Start with a length of 5, and increase as we draw
length = 5

# Draw 300 lines, changing the color and length as we progress
for i in range(300):
    new_color = random.choice(colors)
    turtle.pencolor(new_color)
    turtle.forward(length)
    turtle.right(91)
    length = length + 3
