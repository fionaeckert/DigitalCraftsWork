# creating a file via python
# W creates a file if the file doesn't already exist
file=open('newFile.txt','w')
print(type(file))
# To write to a file:
file.write('Good morning, it is Friday!')
file.close()

# To read a file:
file = open('newFile.txt', 'r')
# print(file.read())
file.close()

#Modifying a file:
#a = append new data to the end of the file
file = open('newFile.txt', 'a')
file.write(' HAGS')
file.close()
file = open('newFile.txt', 'r')
print(file.read())
file.close()

#Overwriting a file:
file = open('newFile.txt', 'w')
file.write(' We will be learning about bootstrap today.')
file.close()
#this will delete all of the previous text added to the doc