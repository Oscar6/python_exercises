from turtle import *

pencolor('red')
bgcolor('black')
width(6)

for i in range(5):
    right(144)
    forward(100)
    left(72)
    forward(100)
penup()

for i in range(5):
    goto(-4, 10)
    pendown()
    forward(100)
    right(144)

mainloop()