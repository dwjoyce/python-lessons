# boxes.py
# Program to draw a number boxes, increasing in size and angled each time

import turtle
import random

colors = ["red", "green", "blue", "magenta", "yellow", "cyan"]

turtle.speed(0)
turtle.up()
turtle.goto(100, -100)
turtle.down()

length = 20

for box in range(12):
    turtle.pencolor(random.choice(colors))
    turtle.pensize(5)
    for s in range(4):
    	turtle.forward(length)
    	turtle.left(90)
    length += 20
    turtle.left(8)
