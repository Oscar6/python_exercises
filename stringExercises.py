# 1. Uppercase a String
# food = 'pizza'
# print(food.upper())

# 2. Capitalize a String
# food = 'pizza'
# print(food.capitalize())

# 3. Reverse a String
# userInput = str(input('Enter text: '))
# string = userInput[::-1]

# print(string) 

######## OR ########

# textUser = input('Enter text: ')
# arrayLength = len(textUser)

# newText = ""
# for i in textUser:
#     index = textUser.index(i)
#     print(index)
#     newText += textUser[arrayLength - 1 - index]
# print(newText)

# 4. Leetspeak
# paragraph = input('Enter some text: ').upper()

# paragraph = paragraph.replace('A', '4')
# paragraph = paragraph.replace('E', '3')
# paragraph = paragraph.replace('G', '6')
# paragraph = paragraph.replace('I', '1')
# paragraph = paragraph.replace('O', '0')
# paragraph = paragraph.replace('S', '5')
# paragraph = paragraph.replace('T', '7')

# print(paragraph)

# 5. Long-long Vowels
# word = input('Enter a long vowel word: ')
# word = word.replace('aa', 'aaaaa')
# word = word.replace('ee', 'eeeee')
# word = word.replace('ii', 'iiiii')
# word = word.replace('oo', 'ooooo')
# word = word.replace('uu', 'uuuuu')

# print(word)

# 6. Caesar Cipher
# from pycipher import Caesar

# answer = Caesar(key=-13).decipher('lbh zhfg hayrnea jung lbh unir yrnearq')
# print(answer)
