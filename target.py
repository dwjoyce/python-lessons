import turtle

window_size = 500

turtle.setup(window_size, window_size)
turtle.up()
turtle.speed(0)

num = 11
width = window_size / num / 2.25  # thickness of each circle

while num > 0:
    turtle.goto(0, -num * width)
    if (num % 2) == 0:
        turtle.fillcolor("white")
    else:
        turtle.fillcolor("red")

    turtle.begin_fill()
    turtle.circle(num * width)
    turtle.end_fill()
    
    num = num - 1

input()

