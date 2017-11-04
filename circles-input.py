# circles-input.py
# Ask user what color to draw the circles and what size they should be

import turtle

color = input("What color to draw the circles? ")
radius = input("What size for each circle? ")
angle = input("What angle between each circle? ")

# Make into integers before using them as such
radius = int(radius)
angle = int(angle)

turtle.speed(0)
turtle.pencolor(color)

turtle.circle(radius)
turtle.left(36)
turtle.circle(radius)
turtle.left(36)
turtle.circle(radius)
turtle.left(36)
turtle.circle(radius)
turtle.left(36)
turtle.circle(radius)
turtle.left(36)
turtle.circle(radius)
turtle.left(36)
turtle.circle(radius)
turtle.left(36)
turtle.circle(radius)
turtle.left(36)
turtle.circle(radius)
turtle.left(36)
turtle.circle(radius)
turtle.left(36)
