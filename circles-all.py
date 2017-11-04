# circles-all.py
# Ask how many circles to draw, and repeat.  This program uses most of the techniques
# in the textbook - importing, use of functions, input, looping, lists, breaking out of
# loops and conditional statements.  It also uses exception handling when the input is
# not as expected.

import turtle

color_list = ["red", "green", "blue", "magenta", "cyan", "yellow"]
index = 0

number_circles_str = input("How many circles? ")

try:
    number_circles = int(number_circles_str)
except:
    # User didn't type in an integer - just set it to a 100
    number_circles = 100
    
window_size = 750

turtle.setup(window_size, window_size)
turtle.speed(0)
turtle.pensize(5)

radius = window_size / 5
angle = 360 / number_circles

while True:
    for num in range(number_circles):
        turtle.pencolor(color_list[index])
        turtle.circle(radius)
        turtle.left(angle)

        index = index + 1
        if index >= len(color_list):
            index = 0
            
    answer = input("Another turn, y/n? ")
    if answer.upper() == "N":
        print("Bye for now.")
        break
    
    turtle.clear()
    angle = -angle  # Let's turn the other way next time
