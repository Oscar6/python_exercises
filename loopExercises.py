# 1. 1 to 10
# for i in range(11):
#     print(i)

# 2. n to m
# start = int(input('Type start: '))
# end = int(input('Type end: '))
# for i in range(start, end + 1):
#     print(i)

# 3. Odd Numbers
# for x in range(1, 10):
#     if(x % 2 != 0):
#         print(x)
        
# 4. Print a Square
# sqr = 5
# for i in range(sqr):
#     print ('*' * sqr)

# 5. Print a Square II
# sqr = int(input('How big is the square?: '))
# for i in range(sqr):
#     print ('*' * sqr)

# 6. Print a Box
# boxW = int(input('Width?: '))
# boxH = int(input('Height?: '))

# for i in range(boxW):
#     for j in range(boxH):
#         print('*' if i in [0, boxW-1] or j in [0, boxH-1] else ' ', end='')
#     print()

# 7. Print a Triangle
# def tri(i, x=0):
#     if i == 0:
#         return 0
#     else:
#         print(' ' * ( i + 1 ) + '*' * ( x * 2 + 1 ))
#         return tri( i - 1, x + 1 )

# tri(4)

# 8. Print a Triangle II
# height = int(input("Height of triangle: "))
# count = 0

# for i in range(height-1):
#     print('*' + ' ' * count + '*')
#     count += 1

# print('*' * height)

# 9. Multiplication Table
# for x in range(1, 11):
#     for y in range(1, 11):
#         print(x, " x ", y , " = ", x * y)
