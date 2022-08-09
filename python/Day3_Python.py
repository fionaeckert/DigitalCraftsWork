# Functions - a reusable block that can be called at any time

#User will pass in a name as a parameter, and the computer will say "Hey name_of_user"
from unittest.util import sorted_list_difference
from xmlrpc.client import boolean


name=input("What is your name? ")
def sayHey(name: str)->str:           #this is a parameter. computer is taking the argument that was passed in by the function caller and storing that value in a variable called userName
    print('Hey', name)
sayHey(name)

#name=input("What is your name? ")
#def sayHey(userName):           #this is a parameter. computer is taking the argument that was passed in by the function caller and storing that value in a variable called userName
#    print('Hey', userName)
#sayHey(name)
#what is above is the example from class...not sure why he introduced userName instead of just using name

firstName = input('first name? ')
lastName = input('last name? ')
def sayHello(firstName: str, lastName: str)->str:
    print('Hello', firstName + ' ' + lastName)
sayHello(firstName, lastName) #this will prints as many times as you call it

#basic function that calculates the area of a rectangle
def rectangleArea(length: int,width: int)->int:
    return length*width     #This returns the value that is present on the line back to the caller
area_rectangle = rectangleArea(5,6)
print(area_rectangle)

def circleArea(radiu:int)->int:
    pi = 3.14
    return pi*radius**2
area_of_cirlce = circleArea(2)
print(area_of_cirlce)

#should I wear a sweater 
def sweater()->None:          #no reason to pass in parameters since we're getting input from user
    temperature=int(input('What is the temp outside? '))
    humidity=int(input('What is the humidity outside? '))
    windSpeed=int(input('What is the wind speed outside? '))
    wearSweater = False
    if temperature<55:
        wearSweater=True
    elif temperature>=55 and temperature<65 and humidity<30:
        wearSweater=True
    elif temperature<60 and windSpeed>10:
        wearSweater=True
    
    return wearSweater
print(sweater())

#------------------------------------------------------------------------------------------------------------------------
#if you need to set the exact type of a variable:
#def squareArea(length:int, width: int)->int:
    #tells the computer and user that length and width are both integers and the result should also be an integer

def rectangleArea(length: int,width: int)->int:
    return length*width     #This returns the value that is present on the line back to the caller
area_rectangle = rectangleArea(5,6)
print(area_rectangle)
#function to calculate how much flooring to order, which calls the previous rectangleArea function
def orderFlooring(orderNumber:int, length:int, width:int)->int:
    if orderNumber<=0:
        print('Invalid order number')
    amount_of_flooring = rectangleArea(length, width)
    return amount_of_flooring

print('You ordered',orderFlooring(101,20,15), 'sq. ft of flooring')

#------------------------------------------------------------------------------------------------------------------------
#Dictionary: list of key:value pairs
student={
    "id":1234,
    "name":"Fona bo Bona",
    "class":"Senior",
    "GPA":3.9
}
print(student["id"])

student1={
    "id": "4321",
    "name":"Tim bo Bim",
    "school":"Bowdoin"
}
student2={
    "id": "5678",
    "name":"Darcy Miklus",
    "school":"Doggy Daycare"
}
student3={
    "id": "8765",
    "name":"Molly Eckert",
    "school":"Preschool"
}
student4={
    "id": "87654",
    "name":"Conor Eckert",
    "school":"DJ"
}
student5={
    "id": "23456",
    "name":"Fiona Eckert",
    "school":"DigitalCrafts"
}
studentList=[student1,student2,student3,student4,student5]
print(studentList)

print(studentList[2]["name"])

#create a function using the list above, return a list that contains the student bios of any student who's id is < 50000

for students in studentList:

    print(students["name"])


def returnBio(list):
    student_list=[]
    for students in list:
       eligibleStudents=int(students["id"])
       if (students["id"]<"50000"):
           student_list.append(students)
    return student_list
returnBio(studentList)
print(returnBio(studentList))


# given the list above, sort the students in the class based on their id and return that list

def listSort(oldList:list) ->list:
    sortedList = []
    for students in oldList:
        sortedList.append(students["id"])
        sortedList.sort
    return sortedList
listSort(studentList)

print(listSort(studentList))


# listSort(favoritePeople)
# print(sortedList)

# def listSort(oldList:list)->list
# newList=[]
# topNumber = 0
# for x in oldList:
#     idNum = int(x["id"])
#     print(idNum)
#     newList.append(x)
# print(newList)

