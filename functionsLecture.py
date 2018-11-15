# def f(x):
#     return 2 * x + 1
# def g(x):
#     return x + 1

# for x in range(-3, 5):
#     print("f({x}) = {y} ".format(x=x,  y=f(x)))


# def sampleFunction(a, b, c):
#     print("{a} {b} {c}".format(a=a, b=b, c=c))

# sampleFunction(1, 2, 3)

# from math import sqrt

# def quadratic(a, b, c):
#     x1 = -b / (2*a)
#     x2 = sqrt(b**2 - 4*a*c) / (2*a)
#     return (x1 + x2), (x1 - x2)

# print(quadratic(31, 93, 62))

# import matplotlib
# matplotlib.use("Agg")
# from matplotlib import pyplot

# xrange = list(range(2, 10))
# yrange = list(range(2, 10))

# pyplot.plot(xrange, yrange)
# pyplot.savefig('samplePlot.png')

# pyplot.close()

# f_output = []
# g_output = []

# x_list = list(range(-3, 5))

# def f(x):
#     return 2 * x + 1
# def g(x):
#     return x + 1

# for x in x_list:
#     f_output.append(f(x))
#     g_output.append(g(x))

# pyplot.plot(x_list, f_output , x_list, g_output)
# pyplot.savefig('myplot.png')
# pyplot.close()

from turtle import *
pencolor('orange')
width(10)
circle(180)

# move into position
up()
forward(50)
left(90)
forward(50)
left(90)
down()
# draw the square
forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
forward(100)

mainloop()