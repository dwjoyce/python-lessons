# stars.py
# Python program to display a star on the turtle window using a random size,
# colour and position.

import turtle
import random

p = turtle.Pen()

p.reset()
p.speed(0)

width, height = p.screen.window_width(), p.screen.window_height()

while True:
    p.up()
    x = random.randint(-width // 2, width // 2)
    y = random.randint(-height // 2, height // 2)
    p.goto(x, y)
    p.down()

    length = random.randint(10, 100)

    p.fillcolor(random.random(), random.random(), random.random())
    p.begin_fill()
    for side in range(10):
        p.forward(length)
        if side % 2:
            p.right(144)
        else:
            p.left(72)
    p.end_fill()
