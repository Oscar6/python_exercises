from turtle import *

# Equilateral Triangle
def triangle():
    for i in range(3):
        color('red')
        forward(175)
        left(120)

# Square
def square():
    for i in range(2):
        color('blue')
        forward(50)
        left(90)
        forward(50)
        left(90)

# Pentagon
def pentagon():
    for i in range(5):
        color('orange')
        forward(100)
        left(72)

# Hexagon
def hexagon():
    for i in range(6):
        color('yellow')
        forward(100)
        left(60)


# Octagon
def octagon():
    for i in range(8):
        color('green')
        forward(100)
        left(45)

# Star
def star():
    for i in range(5):
        color('black')
        forward(100)
        right(144)

# Circle
def circleS():
    color('yellow')
    width(5)
    circle(100)
    
# circleS()
# mainloop()
