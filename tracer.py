import random
import turtle

steps = int(input("How many steps? "))

options = ["left", "right", "none"]

turtle.speed(0)

counter = 0
while counter < steps:
    turtle.forward(10)

    dir = random.choice(options)
    if dir == "left":
        turtle.left(90)
    elif dir == "right":
        turtle.right(90)

    counter = counter + 1

input()
