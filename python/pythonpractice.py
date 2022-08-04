# Day 4
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