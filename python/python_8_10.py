#when given two strings from the user, write a function 
#that checks if each string is an anagram of the other. If yes, return true. 
#Otherwise, return false.

string1 = input('Please enter a string: ')
string2 = input('Please enter another string: ')

def anagramFunction(string1,string2):
    if sorted(string1)==sorted(string2):
        print('True')
    else:
        print('False')
anagramFunction(string1, string2)

#now do it without using a function/built in method

#interview questions like this are testing your knowledge of data structures

def anagramNoSortMethod(string1: str, string2: str):
    if len(string1) != len(string2):
        return "False"
    
    dict_string1={} #dictionaries allow us to store the letter as the key and the number of times the letter occurs as the pair
    dict_string2={}

    return "True" if dict_string1 == dict_string2 else "False"
print(anagramNoSortMethod(string1,string2))


word1 = input('Type in a word: ')
word2 = input('Type in another word: ')

dict1 = {}
dict2 = {}

# for letter in word1:
#     print(letter) #this prints each individual letter in the input

# for letter in word1:
#     dict1[letter]=1
# print(dict1)
#this prints: {'h': 1, 'e': 1, 'l': 1, 'o': 1}
#in a dictionary, each pair is unique
#we've hardcorded the values to be 1 so they all return 1


for letter in word1:
    #check if letter is already in dictionary
    if letter in dict1.keys():
        #if letter is not in dictionary, set number of occurences to 1
        dict1[letter]=dict1.get(letter)+1
        #letter already exists in dictionary
    else:
        dict1[letter]=1
for letter in word2:
    if letter in dict2.keys():
        dict2[letter]=dict2.get(letter)+1
    else:
        dict2[letter]=1

print(dict1)
print(dict2)
print(dict1.keys())

def isAnagram(word1: str, word2: str)->bool:
    dict1=createDictFromWord(word1)
    dict2=createDictFromWord(word2)
    return dict1 == dict2
def createDictFromWord(word:str) -> dict:
    strDict= {}
    for letter in word:
        if letter in strDict.keys():
            strDict[letter]=strDict.get(letter)+1
        else:
            strDict[letter]=1
    return strDict

print(isAnagram('god','dog'))

# create a list that has the name of everyone in the class and returns any name that is duplicated

classNames = ['Jordan','Jordan','Kahn','Kahn','An','Jorge','Carlos','Wes','Fiona','Matt','Dez','Dre']

def classNamesFunction(classNames: list) -> list:
    dict_classNames={}
    duplicateNames=[]
    for names in classNames:
        if names in dict_classNames.keys():
            duplicateNames.append(name)
    else:
        dict_classNames[names]=1
    return duplicateNames

print(classNamesFunction(classNames))


