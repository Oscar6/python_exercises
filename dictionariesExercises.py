# Dictionary Exercises

# Exercise 1

# phonebook_dict = { 
#     #contact[0]
#         'Alice': '703-493-1834', 
#         'Bob': '857-384-1234', 
#         'Elizabeth': '484-584-2923'
#     }

# 1. Print Elizabeth's phone number.
# nameContact = phonebook_dict[0]['Elizabeth']
# print(nameContact)


# 2. Add a entry to the dictionary: Kareem's number is 938-489-1234.
# phonebook_dict['Kareem'] = '484-584-2923'
# print(phonebook_dict)

# 3. Delete Alice's phone entry.
# del phonebook_dict['Alice']
# print(phonebook_dict)

# 4. Change Bob's phone number to '968-345-2345'.
# phonebook_dict['Bob'] = '968-345-2345'
# print(phonebook_dict)


# 5. Print all the phone entries.
# print(phonebook_dict)

# ///////////////////////// ## ///////////////////////// #

# Exercise 2

# ramit = { 
#   'name': 'Ramit', 
#   'email': 'ramit@gmail.com', 
#   'interests': ['movies', 'tennis'], 
#   'friends': [ 
#      { 
#        'name': 'Jasmine', 
#        'email': 'jasmine@yahoo.com', 
#        'interests': ['photography', 'tennis']
#      }, 
#      { 
#         'name': 'Jan', 
#         'email': 'jan@hotmail.com', 
#         'interests': ['movies', 'tv'] 
#      } 
#     ] 
# }

# 1. Write a python expression that gets the email address of Ramit.
# print("Ramit's email:", ramit['email'])

# 2. Write a python expression that gets the first of Ramit's interests.
# print("Ramit likes:", ramit['interests'][0])

# 3. Write a python expression that gets the email address of Jasmine.
# print("Jasmine's email:", ramit['friends'][0]["email"])

# 4. Write a python expression that gets the second of Jan's two interests.
# print("Jan likes:", ramit['friends'][1]["interests"][1])

# ///////////////////////// ## ///////////////////////// #

# Letter Summary

# letter_histogram = input("Enter a word: ")

# counts = {}

# for char in letter_histogram:
#     if char not in counts:
#         counts[char] = 1
#     else:
#         counts[char] += 1

# print(counts)

 # Word Summary
word_histogram = input("Enter a paragraph: ")

word_list = word_histogram.split()
word_lib = {}

for word in word_list:
    if word not in word_lib:
        word_lib[word] = 1
    else:
        word_lib[word] += 1

print(word_lib)