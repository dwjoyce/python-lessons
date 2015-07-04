# polygons.py

import turtle
import random


def draw_polygon(p, x, y, sides, length, pcol, fcol):
    '''Draw one polygon using supplied position, sides, length, etc.'''
    p.up()
    p.goto(x, y)
    p.down()
    p.setheading(random.randint(0, 359))  # random orientation
    p.color(pcol, fcol)  # pen colour, fill colour
    p.begin_fill()  # start shape
    for s in range(sides):
        p.forward(length)
        p.right(360 / sides)
    p.end_fill()    # end shape, so it can be filled in


def draw_number_polygons(p, num_polygons):
    '''Draw a number of polygons using p for pen'''
    for num in range(num_polygons):
        # The position is half the width from the left to right, and half the
        # height from top to bottom. So if window is 400, 300 then it goes
        # from -200 to 200 across and 150 to -150 down.
        width = p.screen.window_width()
        height = p.screen.window_height()
        x = random.randint(-width // 2, width // 2)
        y = random.randint(-height // 2, height // 2)

        sides = random.randint(3, 10)  # from triangles to decagons!
        length = 400 / sides  # make shapes about the same size

        # Random colours - 0.0 to 1.0 for red, green and blue
        pcol = random.random(), random.random(), random.random()
        fcol = random.random(), random.random(), random.random()

        # Finally, draw polygon with all these values supplied
        draw_polygon(p, x, y, sides, length, pcol, fcol)

# Program starts here...

pen = turtle.Pen()
pen.speed(0)

# Draw a 100 polygons using pen variable
draw_number_polygons(pen, 100)

# Call mainloop so that window can be moved
turtle.mainloop()
