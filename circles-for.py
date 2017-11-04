# circles-for.py
# Draw a number of circles around a point, this time using a for loop

import turtle

number_circles = input("How many circles to draw? ")
color = input("What color to draw the circles? ")
radius = input("What size for each circle? ")

number_circles = int(number_circles)
radius = int(radius)

turtle.speed(0)
turtle.pencolor(color)

for num in range(number_circles):
    turtle.circle(100)
    turtle.left(360 / number_circles)

