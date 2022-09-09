# Create a program that generates 30 students. Each student should have an ID and grade(numerical 0-100)
# Take those students grades and curve them, the highest grade becoming a 95. Adjust your gradebook to assign a letter grade based on the new values
# Write a unittest to verify that your function is working

import random

# def gradebook():
#     testScores = []
#     for student in range(1,31):
#         student = {str(random.randint(100000000,999999999)):random.randint(0,100)}
#         # print(student)
#         testScores.append(list(student.values()))
#         testScores.sort()
#         print(testScores)
#         for i in testScores:
#             if i >= 80:

# gradebook()
        

def gradebook():
    results = []
    for student in range(1,31):
        student = { 'id':str(random.randint(100000000,999999999)),'grade':random.randint(0,100)}
        results.append(student)
        print(results)
        for student in results:
            print(student.get('grade'))
        #     if student.values() >= 80:
        #         student.values()=='A'
        #     elif student.values()>=60 and student.values() < 80:
        #         student.values()=='B'
        #     elif student.values()>=40 and student.values()<60:
        #         student.values()=='C'
        #     elif student.values()>=20 and student.values()<40:
        #         student.values()=='D'
        #     else:
        #         student.values()=='F'
        # print(student)
gradebook()
        
# step 1: create a single student with an auto generated ID

# classroom = {}
# student={
#     'id':random.randint(100000000,999999999),
#     'grade':random.randint(1,100)
# }

# print(student)

# step 2: create 30 students
# for i in range(1,30):
#     student={
#     'id':random.randint(100000000,999999999),
#     'grade':random.randint(1,100)}
#     print(student)
#     # add each student to the class
#     classroom.append(student)

# step 3: taking the student with the highest grade and rounding it to a 95
    # take the difference between the highest grade and 95, and save that difference 
    # ex: 60
    # iterate through the dictionary and add 60 points to each student's grade

# step 4: write switch statement to translate numbers to letter grades
#   i.e. 84 -> B 

# step 5: write unittest
# 5a. verify that each student has unique ID 
# 5b. make sure each grade is between 0-100
# 5c. verify that each number grade is converted to proper letter