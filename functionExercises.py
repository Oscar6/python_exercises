# 1. Hello
# def hello(x):
#     print(x, 'Oscar')
 
# hello('Hello')

# 2. y = x + 1
# import matplotlib.pyplot as plot 

# def f(x): 
#      return x + 1

# xs = list(range(-3, 4)) 
# ys = [] 

# for x in xs: 
#      ys.append(f(x)) 

# plot.plot(xs, ys) 
# plot.show()

# 3. Square of x
# import matplotlib.pyplot as plot 

# def f(x): 
#      return x ** 2 + 1

# xs = list(range(-100, 100)) 
# ys = [] 

# for x in xs: 
#      ys.append(f(x)) 

# plot.plot(xs, ys) 
# plot.show()

# 4. Odd or Even
# import matplotlib.pyplot as plot 

# def f(x): 
#     if x % 2:
#         return -1
#     else:
#         return 1

# xs = list(range(-5, 5)) 
# ys = [] 

# for x in xs: 
#      ys.append(f(x)) 

# plot.bar(xs, ys) 
# plot.show()

# 5. Sine
# import matplotlib.pyplot as plot 
# import math

# def f(x): 
#      return math.sin(x)

# xs = list(range(-5, 5)) 
# ys = [] 

# for x in xs: 
#      ys.append(f(x)) 

# plot.plot(xs, ys) 
# plot.show()

# 6. Sine 2
# import matplotlib.pyplot as plot 
# import math
# from numpy import arange

# def f(x): 
#      return math.sin(x)

# xs = arange(-5, 6, 0.1)
# ys = [] 

# for x in xs: 
#      ys.append(f(x)) 

# plot.plot(xs, ys) 
# plot.show()

# 7. Degree Conversion

xs = list(range(0, 0)) 
ys = [] 

for F in xs: 
     ys.append(celsius(F)) 

plot.plot(xs, ys) 
plot.show()