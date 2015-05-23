import turtle

colours = ['red', 'green', 'blue', 'yellow', 'cyan', 'magenta', 'brown', 'purple', 'orange', 'black']
number_turns = 8
step = 10

p = turtle.Pen()
p.speed('fastest')

colour_index = 0

while True:
    for i in range(number_turns):
        for size in range(10,200,step):
            p.pencolor(colours[colour_index])
            p.circle(size)
        colour_index = colour_index + 1
        if colour_index >= len(colours):
            colour_index = 0
        p.left(360 / number_turns)
