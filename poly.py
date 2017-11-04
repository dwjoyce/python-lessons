# poly.py
# Ask user for number of sides, length of each side, side thickness,
# pen color and fill color, and then draw polygon as specified

import turtle

sides = int(input("How many sides? "))
length = int(input("How long each side? "))
thickness = int(input("How thick should the sides be? "))
pen_color = input("The pen color? ")
fill_color = input("The fill color? ")

turtle.pencolor(pen_color)
turtle.fillcolor(fill_color)
turtle.pensize(thickness)

turtle.begin_fill()

for num in range(sides):
    turtle.forward(length)
    turtle.left(360 / sides)

turtle.end_fill()
