# Write a program to check if the given number is a palindrome number.
# A palindrome number is a number that is same after reverse. For example 545, is the palindrome numbers

userInput = input('Please enter a number > 10: ')
reverseInput = userInput[::-1]

if userInput == reverseInput and int(userInput)>10:
    print('Your number is a palindrome!')
elif userInput != reverseInput or int(userInput)<10:
    print('Your number is not a palindrome!')
elif userInput != type(int):
    print('Please enter a number >10') 