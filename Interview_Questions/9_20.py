# Given an array containing None values fill in the None values with most recent value
# Ex: [1,2, None] -> [1,2,2]


randomArray = [1,2,None,3,4]

def newArray(randomArray:list)->list:
    newArray = []
    for x in randomArray:
        newArray.append(x)
    for i in range(len(newArray)-1):
        if newArray[i] == None:
            newArray[i] = newArray[i-1]
    print(newArray)

newArray(randomArray)

# def newArray(randomArray:list)->list:
#     for i in range(len(randomArray)-1):
#         if randomArray[i] == None:
#             randomArray[i] = randomArray[i-1]
#     print(randomArray)

# newArray(randomArray)