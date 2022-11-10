# Given two .txt files that have lists of numbers in them, find the numbers that are overlapping.
# Write a function in python that takes two files as a parameter and returns a list of the numbers that exist in both files.
# Write a unittest to verify your answer

file1 = open('page1.txt', 'r')
file1 = file1.read().splitlines()

file2 = open('page2.txt','r')
file2 = file2.read().splitlines()

def overlappingNums(file1, file2)->list:
    duplicateNums = []
    for number in file1:
        if number in file2:
            duplicateNums.append(number)
            print(duplicateNums)

overlappingNums(file1,file2)
