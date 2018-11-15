# 1. Sum the Numbers
# numbers = [10, 12, 9, 1, 8, 2]
# sum = 0
# for x in numbers:
#     sum += x
# print(sum)

# 2. Largest Number
# largest = [10, 12, 9, 1, 8, 2]
# print(max(largest))

# 3. Smallest Number
# smallest = [10, 12, 9, 1, 8, 2]
# print(min(smallest))

# 4. Even Numbers
# evenNum = [10, 12, 9, 1, 8, 2]
# for i in evenNum:
#     if i % 2 == 0:
#         print(i)

# 5. Positive Numbers
# pos = [10, -12, 9, -1, 8, -2, 0]
# for num in pos:
#     if num >= 0:
#         print(num)

#  6. Positive Numbers II
# numbers = [10, -12, 9, -1, 8, -2, 0]
# posOnly = [n for n in numbers if n > 0]
# print(posOnly)

# 7. Multiply a list
# l1 = [10, -12, 9, -1, 8, -2, 0]
# l2 = []
# for i in l1:
#     l2.append(i * 2)

# print(l2)

# 8. Multiply Vectors
# l1 = [8, 10, 12, 14]
# l2 = [9, 11, 13, 15]
# l3 = []          
# for i in range(0, len(l1)):
#      l3.append(l1[i]*l2[i])
# print(l3)

# 9. Matrix Addition
# x=[[2, -2]]
# y=[[5, 3]]
# z=[[0, 0]]
# for i in range(len(x)):
#     for j in range(len(x[0])):
#         z[i][j] = x[i][j] + y[i][j]
# for matrix in z:
#     print(matrix)

# 10. Matrix Addition II

# 11. De-dup
# deDupe = [1, 2, 2, 3, 4, 12, 12, 42, 42]
# deDupe = list(set(deDupe))
# print(deDupe)

# Bonus: Matrix Multiplication
# x=[[5, 10]]
# y=[[10, 20]]
# z=[[0, 0]]
# for i in range(len(x)):
#     for j in range(len(x[0])):
#         z[i][j] = x[i][j] * y[i][j]
# for matrix in z:
#     print(matrix)