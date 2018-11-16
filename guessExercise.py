# Step 1
# guessNumber = 5
# guess = int(input("Guess a number between 1 - 5: "))
# while guess != guessNumber:
#     print("Guess again")
#     guess = int(input("Guess a number between 1 - 5: "))
# if guess == guessNumber:
#     print("You guessed correctly")

# Step 2
# guessNumber = 5
# guess = int(input("Guess a number between 1 - 5: "))
# while guess != guessNumber:
#     if guess > guessNumber:
#         print(guess, "is too high. Guess again")
#         guess = int(input("Guess a number between 1 - 5: "))
        
#     elif guess < guessNumber:
#         print(guess, "is too low. Guess again")
#         guess = int(input("Guess a number between 1 - 5: "))


# if guess == guessNumber:
#     print("You guessed correctly")

# Step 3
# import random 
# ranNum = random.randint(1, 10)

# guess = int(input("Guess a number between 1 - 5: "))
# while guess != ranNum:
#     if guess > ranNum:
#         print(guess, "is too high. Guess again")
#         guess = int(input("Guess a number between 1 - 5: "))
        
#     elif guess < ranNum:
#         print(guess, "is too low. Guess again")
#         guess = int(input("Guess a number between 1 - 5: "))


# if guess == ranNum:
#     print("You guessed correctly")

# Step 4
# import random 
# ranNum = random.randint(1, 10)

# count = 0
# guess = int(input("Guess a number between 1 - 5: "))
# while guess != ranNum:
#     count += 1
#     if count == 5:
#         print("You are out of guesses.")
#         break

#     elif guess > ranNum:
#         print(guess, "is too high. Guess again")
#         guess = int(input("Guess a number between 1 - 5: "))
        
#     elif guess < ranNum:
#         print(guess, "is too low. Guess again")
#         guess = int(input("Guess a number between 1 - 5: "))

# if guess == ranNum:
#     print("You guessed correctly")

# Bonus: Play Again (Incomplete)
import random 
ranNum = random.randint(1, 10)

count = 0
guess = int(input("Guess a number between 1 - 5: "))
while guess != ranNum:
    count += 1
    if count == 5:
        print("You are out of guesses.")

    elif guess < ranNum:
            print(guess, "is too low. Guess again")
            guess = int(input("Guess a number between 1 - 5: "))

    elif guess > ranNum:
        print(guess, "is too high. Guess again")
        guess = int(input("Guess a number between 1 - 5: "))
    
    switch = input("Do you want another try? (yes/no) ")
    if switch == 'yes':
        guess = int(input("Guess a number between 1 - 5: "))
    elif switch == 'no':
        print("Bye")
        break

if guess == ranNum:
    print("You guessed correctly")
    switch = input("Do you want to play again? (yes/no) ")
    if switch == 'yes':
         guess = int(input("Guess a number between 1 - 5: "))
    elif switch == 'no':
        print("Bye")
        