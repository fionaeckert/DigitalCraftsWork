# Day 4
from termios import FIONREAD
from tkinter.messagebox import QUESTION


fullName = 'Fiona Eckert'
#In order to retrieve length of string or list, use len() function
len(fullName)
print(len(fullName))
drinks = ['Sprite','Dr. Pepper','Coke','Pepsi']
print(len(drinks))
#To retrieve the type of a value use the type() function
length_of_drinks = len(drinks)
print(length_of_drinks)

for item in drinks:
    print(item)

loop = 0
while loop <= len(drinks)-1:
    print(drinks[loop])
    loop=loop+1
#could also do
while loop < len(drinks):
    print(drinks[loop])
    loop = loop + 1
# Think of it by putting the number of loop into where "loop" is so while 0 < 4-1 (0<3), print drinks at the first index, which will be Sprite.


#Iterate through a string using a for loop
for letters in fullName:
    print(letters)

letters = 0
while letters < len(fullName):
    print(fullName[letters])
    letters = letters + 1
#exit condition: whatever is next to the while

# printing each number that's divisible by 2
numbers = [123, 765, 876, 2344, 659]
for i in numbers:
    if i % 2 == 0:
        print(i)
print(5%2)
# you only use modulo (%) on integers because it doesn't work out perfectly with floats (i.e. a float is never perfectly divisible)
print(5%.1)

#print all odd numbers
for i in numbers:
    if i %2==1:
        print(i)

#using the list of numbers above, allow user to pick a number to divide each number by, and only print numbers that are divisble by the number the user inputs

userInput=int(input('Enter a number to divide by: '))
for i in numbers:
    if i%userInput==0:
        print(i)

#Try/except - the program will attempt to run all the code in the try block but if it runs into an error, it will jump to the except block and run those lines of code
try:
    userInput=int(input('Enter a number to divide by: '))
    for i in numbers:
        if i%userInput==0:
            print(i)
except:
    print('This program can only take numbers')

print(numbers[-2])

print(hex(id(numbers)))
print(hex(id(numbers[1])))

# Lexicon comparison - essentially a string comparison
mysteryLetter = 'B'
firstNameLetter = 'b'
if firstNameLetter < mysteryLetter:
    print('firstname comes before mystery letter')
else:
    print('mystery letters comes before first name')

students = ['Matt','Carlos','An','Fiona']
breakoutroom1 = []
breakoutroom2 = []
cutoffLetter = 'I'
for element in students:
    if element[0]<=cutoffLetter:
        breakoutroom1.append(element)
    elif element[0]>cutoffLetter:
        breakoutroom2.append(element)

print(breakoutroom1)
print(breakoutroom2)


# Python programming language key works
# if, for, or, and, while, class, return, pass

# String concatenation (string manipulation)
firstName = 'Fiona'
lastName = 'Eckert'
fullName = firstName+' '+lastName
print(fullName)
#strings can only be added together, you can't subtract
#cannot combine a string with an integer or float but you could do the following:
diceRoll = 9
fullName = firstName + ' ' + lastName + str(diceRoll)
#or you could put 9 in quotes ('9')


#Write a short program that prints each number from 1 to 100 on a new line. 

#For each multiple of 3, print "Fizz" instead of the number. 

#For each multiple of 5, print "Buzz" instead of the number. 

#For numbers which are multiples of both 3 and 5, print "FizzBuzz" instead of the number.


for i in range(1,101):
    if i%3==0 and i%5!=0:
        print('Fizz')
    elif i%5==0 and i%3!=0:
        print('Buzz')
    elif i%3==0 and i%5==0:
        print('FizzBuzz')
    else:
        print(i)

# how to reverse string and list
sample = 'Hello world'
print(sample[::-1])

sampleA=['third','second','first']
#print(sampleA[::-1])
sampleB=[]

i = len(sampleA)-1
while i >=0:
    sampleB.append(sampleA[i]) 
    i = i-1
print(sampleB)


