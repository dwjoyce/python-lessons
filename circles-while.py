# circles-while.py
# Draw a number of circles around a point, this time using a while loop

import turtle

number_circles = input("How many circles to draw? ")
color = input("What color to draw the circles? ")
radius = input("What size for each circle? ")

number_circles = int(number_circles)
radius = int(radius)

turtle.speed(0)
turtle.pencolor(color)

num = 0
while num < number_circles:
    turtle.circle(100)
    turtle.left(360 / number_circles)

    num = num + 1
