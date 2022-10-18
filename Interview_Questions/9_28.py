# You ask one of your developers to write a code that will give you the area of a circle. 
# The code the developer writes for you is listed below. Write unit tests to test the following criteria:
# * Test area when radius is >= 0
# * Test that value errors are raised when necessary
# * Test that type errors are raised when necessary
# * Once you have completed the above steps, edit the code below to correct any errors that might occur. 

import math 
import unittest
pi = math.pi

def area_circle(radius):
     return pi*(radius**2)

print(area_circle(10))

class testCircleArea(unittest.TestCase):
    def testcircleArea(self):
        self.assertGreaterEqual(area_circle(10),0)
    def testValueError(self):
        with self.assertRaises(ValueError):
            area_circle(-3)
    def testTypeError(self):
        self.assertWarns(TypeError,area_circle(10))
unittest.main()


