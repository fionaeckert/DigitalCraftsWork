# A low-level implementation of the classic game “Mastermind”. 
# We need to write a program that generates a four-digit random code 
# and the user needs to guess the code in 10 tries or less. If any digit 
# out of the guessed four-digit code is wrong, the computer should print out “B”.
# If the digit is correct but at the wrong place, the computer should print “Y”. 
# If both the digit and position is correct, the computer should print “R”.

# Correct Digit: 5348 -> User Guess: 5182 -> RBYB
import random
import unittest
# compInteger = '1234'
# userInput = (input('Please guess an integer: '))


# def mastermind(userInput:str)->str:
#     compResponse = ''
#     # iteration = 1
#     # while iteration <= 1:
#     for x in userInput:
#         for j in compInteger:
#            if x == j:
#                 compResponse = 'R'
#                 print(compResponse)
#             # elif x in compInteger:
#             #     compResponse = 'Y'




# mastermind(userInput)


# Step 1: create a function that generates a random 4 digit number
# Step 2: prompt user to enter value and store it
# Step 3: compare answer to guess, create hint based on the guess
# Step 4: have the game run until the user enters right or 10 turns have been used
def mastermind():
    answer = generateNumber()
    turns = 0
    win = False
    print('Welcome to Mastermind!')
    while turns <= 10 and win == False:
        guess = input('Enter an integer: ')
        if checkGuess(guess,answer) == True:
            win = True
            print("You've won :D The answer was ",answer)
        turns += 1
    if turns >= 10:
        print("You've lost :( The answer was ", answer)
    print('Answer: ',answer)
    print('Guess: ',guess)

def generateNumber() ->str:
     # Generate each number individually then concatenate them
    number = ''
    for num in range(0,4):
        number += str(random.randint(0,9))
    return number

def checkGuess(guess:str,answer:str)->bool:
    hint = ''
    for i in range(0,4):
        # if the guess at this index is the same as the answer at this index, add an R
        if guess[i] == answer[i]:
            hint += 'R'
        # check if answer contains the guessed number
        elif guess[i] in answer:
            hint += 'Y'
        # if the number is not in the answer at all, add a B
        else:
            hint += 'B'
    print(hint)
    return hint == 'RRRR'
# print(checkGuess('1122','0123'))
mastermind()

