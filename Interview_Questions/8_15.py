#given a list of numbers, write a function that tallies the nubmer of even and odd occurrences and returns the results
#write a unit test to confirm your function works

import unittest

listNumbers = [2,5,6,7,10,3,13]


def talliedNumbers (listNumbers: list, talliedEvenNumbers: list, talliedOddNumbers: list, talliedDict: dict)->dict:
    talliedEvenNumbers = []
    talliedOddNumbers = []
    for evenNumber in listNumbers:
        if evenNumber % 2 == 0:
            talliedEvenNumbers.append(evenNumber)
    talliedEvenNumbers = (len(talliedEvenNumbers))
    for oddNumber in listNumbers:
        if oddNumber % 2 != 0:
            talliedOddNumbers.append(oddNumber)
    talliedOddNumbers = len(talliedOddNumbers)
    talliedDict = {"Even:": talliedEvenNumbers,"Odd":talliedOddNumbers}
    return talliedDict

class TalliedTest(unittest.TestCase):
    def testTally(self):
        self.assertDictEqual(listNumbers,{'Even':3,'Odd':4})

