# Write a program to check if the given number is a palindrome number.
# A palindrome number is a number that is same after reverse. For example 545, is the palindrome numbers

# userInput = input('Please enter a number > 10: ')
# reverseInput = userInput[::-1]

# if userInput == reverseInput and int(userInput)>10:
#     print('Your number is a palindrome!')
# elif userInput != reverseInput or int(userInput)<10:
#     print('Your number is not a palindrome!')
# elif userInput != type(int):
#     print('Please enter a number >10') 
#-----------------------------------------------------
matrix = [[1,2,3],[4,5,6],[7,8,9]]
# print(matrix[2][1])

for rows in range(len(matrix)):
   # print(matrix[rows])
    for cols in range(len(matrix[rows])):
        print(matrix[rows][cols])
#print out the contents of the matrix backwards

for rows in range(len(matrix)-1,-1,-1):
   # print(matrix[rows])
    for cols in range(len(matrix[rows])-1,-1,-1):
        print(matrix[rows][cols])

# sampleA=['third','second','first']
# #print(sampleA[::-1])
# sampleB=[]

# i = len(sampleA)-1
# while i >=0:
#     sampleB.append(sampleA[i]) 
#     i = i-1
# print(sampleB)

rows=len(matrix)-1
cols=len(matrix[rows])-1

while rows>=0:
    cols=len(matrix[rows])-1
    while cols>=0:
        print(matrix[rows][cols])
        cols-=1

    rows-=1