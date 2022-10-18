# Given a file, write a function that swap all cases. All uppercase letters should become lower case and vice versa. Write unit tests to confirm 

import unittest
from curses.ascii import isupper

# poem = ''
# def swapCase(poem:str)->str:            
#     poem=open('/Users/fionaeckert/Documents/DigitalCrafts/DigitalCraftsWork/Interview_Questions/9_12_one.txt','r')
#     # print(poem.read())
#     # print(type(poem.read()))
#     poem=poem.read()
#     for word in poem:
#         if word.islower() == True:
#             poem = poem.replace(word,word.upper())
#         else:
#             poem=poem.replace(word,word.lower())
#     print(poem)

# swapCase(poem)


# class swapPoems(unittest.TestCase):
#     def testSwapCase(self):
#         self.assertIsNot(poem,'/Users/fionaeckert/Documents/DigitalCrafts/DigitalCraftsWork/Interview_Questions/9_12_one.txt')
# unittest.main()

poem2 = ''
def swapCase(poem2:str)->str:            
    poem2=open('/Users/fionaeckert/Documents/DigitalCrafts/DigitalCraftsWork/Interview_Questions/9_12_two.txt','r')
    poem2=poem2.read()
    newObject = ''
    for letter in poem2:
        if letter.islower() == True:
            newObject += letter.capitalize()   
        #     poem2 = poem2.replace(letter,letter.upper())
        elif letter.isupper() == True:
            newObject += letter.lower()
    #         poem2 = poem2.replace(letter,letter.lower())
    #         # poem2=poem2.replace(letter,letter.lower())
    print(newObject)

swapCase(poem2)


# class swapPoems(unittest.TestCase):
#     def testSwapCase(self):
#         self.assertIsNot(poem,'/Users/fionaeckert/Documents/DigitalCrafts/DigitalCraftsWork/Interview_Questions/9_12_one.txt')
# unittest.main()

