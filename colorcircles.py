# colorcircles.py
# Ask for a number of circles, and then draw that number on the screen all varying
# in size, placement and color

import turtle
import random

num_str = input("How many circles? ")
num = int(num_str)

turtle.speed(0)
turtle.setup(600, 600)
turtle.colormode(255)

counter = 0
while counter < num:
    x = random.randrange(-300, 300)
    y = random.randrange(-300, 300)
    turtle.up()
    turtle.goto(x, y)
    turtle.down()

    red = random.randrange(256)
    green = random.randrange(256)
    blue = random.randrange(256)

    turtle.fillcolor(red, green, blue)
    
    turtle.begin_fill()
    radius = random.randrange(5, 200)
    turtle.circle(radius)
    turtle.end_fill()
    
    counter = counter + 1
