# # creating a file via python
# # W creates a file if the file doesn't already exist
# file=open('newFile.txt','w')
# print(type(file))
# # To write to a file:
# file.write('Good morning, it is Friday!')
# file.close()

# # To read a file:
# file = open('newFile.txt', 'r')
# # print(file.read())
# file.close()

# #Modifying a file:
# #a = append new data to the end of the file
# file = open('newFile.txt', 'a')
# file.write(' HAGS')
# file.close()
# file = open('newFile.txt', 'r')
# print(file.read())
# file.close()

# #Overwriting a file:
# file = open('newFile.txt', 'w')
# file.write(' We will be learning about bootstrap today.')
# file.close()
#this will delete all of the previous text added to the doc

# write a function that reads a file. return and print the word that appears the most

# from collections import Counter
# from posixpath import split

# file = open('web-ft-08-22/Code/python/week3/sample/thisIsJustToSay.txt','r')
# read_data=file.read()
# split_it=read_data.split()
# counter = Counter(split_it)
# most_occur = Counter.most_common(4)
# print(most_occur)


# for words in read_data:
#     print(read_data.count(words))


# class classRead:
    # def __init__(self, openFile, wordCount, closeFile) -> None:
    #     self.openFile = openFile
    #     self.wordCount = wordCount
    #     self.closeFile = closeFile
    # def functionRead():
    #     wordCount=0
    #     file = open('web-ft-08-22/Code/python/week3/sample/theRoadNotTaken.txt','r')
    #     read_data=file.read()
    #     for words in file.read():
    #         print(read_data.lower().count(words))
    #     # print(file.read(wordCount))
    #     closeFile = file.close()

    # print(functionRead())

def wordFreq(file:str) -> int:            
    poem=open('/Users/fionaeckert/Documents/DigitalCrafts/web-ft-08-22/Code/python/week3/sample/thisIsJustToSay.txt','r')
    # print(poem.read())
    # print(type(poem.read()))
    poem=poem.read() #converts the poem to a string
    poem=poem.lower().split() #takes the white space and converts the letters into words and places them into a string
    # print(type(poem)) #now the type of variable poem is a list

    wordCount = {}
    for word in poem:
        #keep track of each individual word. If the word is not in the dictionary, set the value to 1.
        if wordCount.get(word)==None:
            wordCount[word]=1
        #else case: word already exists in the dictionary, so now we increment
        else:
            wordCount[word]+=1
    print(wordCount.values()) #prints the count of each word
    print(wordCount.keys()) #prints the list of each word from the poem

    mostFrequentWord = ('',0)
    for word in wordCount:
        if wordCount[word]>mostFrequentWord[1]:
            mostFrequentWord=(word, wordCount[word])
    print(mostFrequentWord)
    return mostFrequentWord[1]
wordFreq("/Users/fionaeckert/Documents/DigitalCrafts/web-ft-08-22/Code/python/week3/sample/thisIsJustToSay.txt")

