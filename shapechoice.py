# shapechoice.py
# Turtle program to ask user which shape to draw (rectangle/circle/triangle/star),
# and then draw shape centred

import turtle

# First get the type of shape, the size and color
choice = input("Would you like a circle, rectangle, triangle or star (c/r/t/s)? ")
size_str = input("How big? ")
color = input("What color? ")

size = int(size_str)

# Create the window and set the shape color
turtle.setup(500, 500)
turtle.fillcolor(color)

# Start filling and then draw shape

turtle.begin_fill()

if choice == "c":        # Circle
    turtle.circle(size)
elif choice == "r":      # Rectangle
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(size)
elif choice == "t":      # Triangle
    turtle.forward(size)
    turtle.left(120)
    turtle.forward(size)
    turtle.left(120)
    turtle.forward(size)
elif choice == "s":      # Star
    turtle.forward(size)
    turtle.right(144)
    turtle.forward(size)
    turtle.left(72)
    turtle.forward(size)
    turtle.right(144)
    turtle.forward(size)
    turtle.left(72)
    turtle.forward(size)
    turtle.right(144)
    turtle.forward(size)
    turtle.left(72)
    turtle.forward(size)
    turtle.right(144)
    turtle.forward(size)
    turtle.left(72)
    turtle.forward(size)
    turtle.right(144)
    turtle.forward(size)
else:
    print("Sorry, couldn't understand that shape!")

# Finish shape by filling it in
turtle.end_fill()
