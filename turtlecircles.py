# turtlecircles.py
# Program to draw a number of circles, panning out from the centre,
# then turn, and drawing another line of circles.  Continue this forever!

import turtle

colors = ["red", "green", "blue", "yellow", "cyan", "magenta", "brown", "purple", "orange", "black"]
number_turns = 8
step = 5

turtle.setup(600, 600)
turtle.speed(0)
turtle.pensize(2)

color_index = 0

while True:
    for size in range(10, 200, step):
        turtle.pencolor(colors[color_index])
        turtle.circle(size)

    color_index = color_index + 1
    if color_index >= len(colors):
        color_index = 0
    turtle.left(360 / number_turns)
