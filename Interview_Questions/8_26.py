from itertools import count
import unittest


# def rectangleArea(length: int,width: int)->int:
#     return length*width     

# def circleArea(radius:int)->int:
#     pi = 3.14
#     return pi*radius**2

# class TestAreas(unittest.TestCase):
#     def testRectangleArea(self): #this test fails if the two arguments passed in do not satisfy the == operator
#         print(self.assertEqual(rectangleArea(3,3),9)) #we would expect 3*3 = 9 based on the formula established below for the area of a rectangle
# unittest.main() #this finds the unittest with the parameters and run the functions within the particular test case

#     def testCircleArea(self):
#         self.assertEqual(circleArea(5),78.5)
# unittest.main()

# #example with strings
# isAnagram = []
# class AnagramsTest(unittest.TestCase):
#     def testAnagram(self):
#         self.assertEqual(isAnagram('plane','train'), False) #we are expecting this will fail because plane and train are not the same word

# unittest.main()

# duplicateNames = ['Jordan','Jordan','Dez','Dre','Dez']
# class DuplicateNamesTest(unittest.TestCase):
#     def testDuplicate(self):
#         self.assertEquals(duplicateNames(['Jordan','Jordan','Dez','Dre'],['Jordan']))

# unittest.main()


# class DuplicateNamesTest(unittest.TestCase):
#     def testDuplicate(self):
#         self.assertSequenceEqual(duplicateNames(['Jordan','Jordan','Dez','Dre','Dez'],['Dez','Jordan'])) #it should catch this and say test was a fail because the order is incorrect
# unittest.main()

# given a list of users, ensure each user has a valid email, phone number, and zip code.



user1 = ['Tina','tina@gmail.com','(789)-098-6767']
user2 = ['jim','jim@outlook.com','(668)-093-9099']
user3 = ['Emily','e.grace@gmail.com','456-989-2333']
user4 = ['gerard','gerardrox@hotmail.com','3349890000']
user5 = ['Joseph','copejoesph@gmail.com','(782)-456-0912']

def userFormat(user2:list):
    for user2[1] in user2:
        if user2[1].count('@gmail.com') == 1 or user2[1].count('@hotmail.com') == 1 or user2[1].count('@yahoo.com') == 1:
            return True
    for user2[2] in user2:
        if user2[2].count('(') == 1 and user2[2].count(')') == 1 and user2[2].count('-') == 2:
            return True
    else:
        return False 
        
userFormat(user2)

class Validation(unittest.TestCase):
    def testUserFormat(self):
        self.assertEquals(userFormat(user2),True)
unittest.main()

# def userFormat(user2:list)->bool:
#     if "@gmail.com" or "@yahoo.com" or "@hotmail.com" in user2[1]:
#         print(True)
#         if "(" or ")" or "-" in user2[2]:
#             print(True)
#     else:
#         print(False)
# userFormat(user2)


# def rectangleArea(length: int,width: int)->int:
#     return length*width     

# def circleArea(radius:int)->int:
#     pi = 3.14
#     return pi*radius**2

# class TestAreas(unittest.TestCase):
#     def testRectangleArea(self): #this test fails if the two arguments passed in do not satisfy the == operator
#         print(self.assertEqual(rectangleArea(3,3),9)) #we would expect 3*3 = 9 based on the formula established below for the area of a rectangle
# unittest.main() #this finds the unittest with the parameters and run the functions within the particular test case