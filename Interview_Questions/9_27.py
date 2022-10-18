# Given an array, write a function that sorts
#  all names in reverse from Z-A. Write a unit 
#  test using the names of every student in this class to verify your solution.

import unittest

unorderedNames = ['Jonathan','Carlos','Matt','Jordan','Kahn','An','Jorge','Fiona','Wes']

orderedNames = sorted(unorderedNames)
revOrderedNames = list(reversed(orderedNames))
orderedAlpha = []


def reverseAlpha(unorderedNames:list)->list:
    for i in range(len(unorderedNames)):
        for j in range(0,len(unorderedNames)-i-1):
            if unorderedNames[j]<unorderedNames[j+1]:
                unorderedNames[j],unorderedNames[j+1]=unorderedNames[j+1],unorderedNames[j]
    return unorderedNames      
    # orderedAlpha.append(unorderedNames)
    # print(orderedAlpha)
reverseAlpha(unorderedNames)


class testReverseOrder(unittest.TestCase):
    def testreverseOrder(self):
        self.assertSequenceEqual(reverseAlpha(unorderedNames),revOrderedNames)
unittest.main()
