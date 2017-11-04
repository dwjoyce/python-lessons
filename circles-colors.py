# circles-colors.py
# Use the colors as defined in a list, using an index that returns to the start
# once the end is reached.

import turtle

color_list = ["red", "green", "blue", "magenta", "cyan", "yellow"]
index = 0

number_circles_str = input("How many circles? ")
number_circles = int(number_circles_str)

turtle.speed(0)

for num in range(number_circles):
    turtle.pencolor(color_list[index])
    turtle.circle(100)
    turtle.left(360 / number_circles)

    index = index + 1
    if index >= len(color_list):
        index = 0
