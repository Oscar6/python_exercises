# 1. Hello, you!
# name = input('What is your name? ')

# print("Hello " + name + "!")

# 2. HELLO, YOU!
# name = input('WHAT IS YOUR NAME? ')
# print('Hello '.upper() + name.upper() + '!')

# name = 'oscar'
# print('YOUR NAME HAS', len(name), 'LETTERS IN IT!')

# 3. Madlib
# print('Please fill in the blanks below: \n ____(name)____\'s favorite sport is ____(sport)____.')
# name = input('What is your name? ')
# sport = input('What is your favorite sport? ')
# print(name + '\'s favorite sport is ' + sport + '.')

# 4. Day of the Week
# day = int(input('Enter your favorite Day of the week (0-6)? '))
# if (day == 0):
#     print("Sunday")
# if (day == 1):
#     print("Monday")
# if (day == 2):
#     print("Tuesday")
# if (day == 3):
#     print("Wednesday")
# if (day == 4):
#     print("Thursday")
# if (day == 5):
#     print("Friday")
# if (day == 6):
#     print("Saturday")

# 5. Work or Sleep In?
# day = int(input('Enter your Day of the week (0-6)? '))
# if (day == 0):
#     print("It's Sunday. Sleep or watch football")
# elif (day == 1):
#     print("It's Monday. Go to work.")
# elif (day == 2):
#     print("It's Tuesday. Go to work.")
# elif (day == 3):
#     print("It's Wednesday, but that much closer to the weekend. Go to work.")
# elif (day == 4):
#     print("It's Thursday. Almost there. Go to work.")
# elif (day == 5):
#     print("It's Friday. Go to work for 8 hours and you're free.")
# elif (day == 6):
#     print("It's Saturday. If you were out late, sleep in.")

# 6. Celsius to Fahrenheit
# Celsius = int(input('Please enter a temperature in C? '))
# Fahrenheit = Celsius * 1.8 + 32
# print(Fahrenheit, 'F')

# 7. Tip Calculator
# bill = float(input("Total bill amount? "))
# print("Level of service?")
# service = input("Please choose good, fair, or bad: ")
# if service == 'good':
#     tip = (bill * 0.20)
#     total = (bill + tip)

# elif service == 'fair':
#     tip = (bill * 0.15)
#     total = (bill + tip)

# elif service == 'bad':
#     tip = (bill * 0.10)
#     total = (bill + tip)

# print("Tip amount: $" + "{:.2f}".format(tip))
# print("Total amount: $" + "{:.2f}".format(total))

# 8. Tip Calculator
# bill = float(input("Total bill amount? "))
# print("Level of service?")
# service = input("Please choose good, fair, or bad: ")
# split = float(input("Split how many ways? "))
# if service == 'good':
#     tip = (bill * 0.20)
#     total = (bill + tip)
#     person = (total / split)
# elif service == 'fair':
#     tip = (bill * 0.15)
#     total = (bill + tip)
#     person = (total / split)
# elif service == 'bad':
#     tip = (bill * 0.10)
#     total = (bill + tip)
#     person = (total / split)

# print("Tip amount: $" + "{:.2f}".format(tip))
# print("Total amount: $" + "{:.2f}".format(total))
# print("Amount per person: $" + "{:.2f}".format(person))

# 9. 1 to 10
# i = 1
# while i < 11:
#   print(i)
#   i += 1

# 10. How many coins?
# coins = 0
# print("You have {} coins.".format(coins))
# while True:
#     switch = input("Do you want another? (yes/no) ")
#     if switch == 'yes':
#         coins += 1
#         print("You have {} coins.".format(coins))
#     elif switch == 'no':
#         print("Bye")
#         break