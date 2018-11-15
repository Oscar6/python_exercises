# list

# myShoppingList = ["apples", "oranges", "bananas", "mango"]

# myShoppingList[0]
# myShoppingList[1]
# myShoppingList[2]
# myShoppingList[3]

# print(myShoppingList[0])

# myShoppingList[0] = "grapes"
# l = len(myShoppingList)
# print(myShoppingList[0])

# myShoppingList = ["apples", "oranges", "bananas", "mango"]
# myShoppingList.append("pears")
# print(myShoppingList)
# print(l)

# numbers = [1, 2, 3, 4, 5]

# print(numbers[0:2])

# numbers = [1, 2, 3, 4, 5, 8]

# numbers.insert(1, 56)
# print(len(numbers))

# numbers = [1, 2, 3, 4, 5, 8]
# numbers.append([11, 12, 13, 14])

# print(numbers)

# numbers = [122, 2, 3, 6, 5, 8]
# pv = numbers.pop()

# print(numbers)
# print(pv)
# numbers[1]
# print(numbers.index(1))

# print(numbers.sort())

# newNumbers = numbers.copy()

# print(newNumbers)

# myName = "Oscar"
# print(myName[0])
# print(len(myName))

# sentence = "this is a wonderful life"
# print(sentence.index(' '))

# numbers1 = [122, 2, 3, 6, 5, 8]
# numbers2 = [12, 245, 23, 86, 5, 58]

# print(numbers1 + numbers2)
# print(numbers1 * 3)

# myTuple = (15, 25, 30)
# print(myTuple[0])

# myRange = range(10)
# print(myRange)

# for index in range(1, 11, 2):
    # print("hello world")
    # print(index)

# for outterIndex in range(1, 11):
#     # print("index:", index)
#     for innerIndex in range(1, 11):
#         print(outterIndex, " x ", innerIndex , " = ", outterIndex * innerIndex)

# president = ['George', 'W', 'Bush']

# print(president)

# for name in president:
#     # print(president.index(name))
#     print(president.pop())

# print("my list length", len(president))

# myRange = range(10)
# print(myRange)

# for outterIndex in range(1, 11, 2):
#     # print("index:", index)
#     for innerIndex in range(1, 11, 3):
#         print(outterIndex, " x ", innerIndex , " = ", outterIndex * innerIndex)

# l1 = [1, 5, 3, 6, 7]
# l2 = [3, 6, 9, 10, 2]
# l3 = []
# for i in range(0, len(l1)):
#     while index()
#      l3.append(l1[i]*l2[i])
#      print(l3)

l1 = [1, 5, 3, 6, 7]
l2 = [3, 6, 9, 10, 2]
l3 = []

for x in l1:
    y = 0
    for z in l2:
        y += x * z
    l3.append(y)
print(l3)

# numbers1 = [122, 2, 3, 6, 5, 8]
# numbers2 = [12, 245, 23, 86, 5, 58]

# print(numbers1 + numbers2)
# print(numbers1 * 3)