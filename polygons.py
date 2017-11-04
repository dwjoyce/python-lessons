# polygons.py
# Randoming place polygons around the screen, each with
# varying size and number of sides

import turtle
import random

turtle.setup(600, 600)

colors = "red green blue magenta cyan yellow black"
color_list = colors.split()

turtle.up()
turtle.speed(0)

while True:
    for col in color_list:
        x = random.randrange(-300, 300)
        y = random.randrange(-300, 300)
        turtle.goto(x, y)
        
        num_sides = random.randrange(3, 11)
        length = random.randrange(10, 100)

        turtle.fillcolor(col)
        turtle.begin_fill()

        for side in range(num_sides):
            turtle.forward(length)
            turtle.left(360 / num_sides)

        turtle.end_fill()
