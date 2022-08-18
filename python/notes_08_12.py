#UNIT TEST

import unittest


def rectangleArea(length: int,width: int)->int:
    return length*width     

def circleArea(radius:int)->int:
    pi = 3.14
    return pi*radius**2

class TestAreas(unittest.TestCase):
    def testRectangleArea(self): #this test fails if the two arguments passed in do not satisfy the == operator
        print(self.assertEqual(rectangleArea(3,3),9)) #we would expect 3*3 = 9 based on the formula established below for the area of a rectangle
unittest.main() #this finds the unittest with the parameters and run the functions within the particular test case

    def testCircleArea(self):
        self.assertEqual(circleArea(5),78.5)
unittest.main()

#example with strings
isAnagram = []
class AnagramsTest(unittest.TestCase):
    def testAnagram(self):
        self.assertEqual(isAnagram('plane','train'), False) #we are expecting this will fail because plane and train are not the same word

unittest.main()

duplicateNames = ['Jordan','Jordan','Dez','Dre','Dez']
class DuplicateNamesTest(unittest.TestCase):
    def testDuplicate(self):
        self.assertEquals(duplicateNames(['Jordan','Jordan','Dez','Dre'],['Jordan']))

unittest.main()


class DuplicateNamesTest(unittest.TestCase):
    def testDuplicate(self):
        self.assertSequenceEqual(duplicateNames(['Jordan','Jordan','Dez','Dre','Dez'],['Dez','Jordan'])) #it should catch this and say test was a fail because the order is incorrect
unittest.main()

