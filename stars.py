# stars.py
# Python program to display a star on the turtle window using a random size,
# colour and position.

import turtle
import random

window_size = 600

turtle.setup(window_size, window_size)
turtle.speed(0)

while True:
    turtle.up()
    x = random.randint(-window_size // 2, window_size // 2)
    y = random.randint(-window_size // 2, window_size // 2)
    turtle.goto(x, y)
    turtle.down()

    length = random.randint(10, 100)

    turtle.fillcolor(random.random(), random.random(), random.random())
    turtle.begin_fill()
    for side in range(10):
        turtle.forward(length)
        # Depending on whether the side is even or odd, turn right or left
        if (side % 2) == 0:
            turtle.right(144)
        else:
            turtle.left(72)
    turtle.end_fill()
