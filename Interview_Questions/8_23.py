# Write a function that orders a list least to greatest by comparing the 
# current index value to the next index value. if the next index is lower 
# than the current index, swap the values. continue this until you reach the end of the list

# unorderedList = [1,4,6,8,3,5]
# def ordered(lst:list)->list:
#     orderedList=[]
#     for number in range(len(unorderedList)):
#         for integer in range(number+1,len(unorderedList)):
#             if unorderedList[number]>unorderedList[integer]:
#                 orderedList.append(unorderedList[number])
#     print(orderedList)

# ordered(unorderedList)



# unorderedList = [1,4,6,8,3,5]

# def ordered(unorderedList:list)->list:
#     orderedList = []
#     while unorderedList: # sets up a loop which will run until the unordered list is empty
#         minimum = unorderedList[0] # random number from the unordered list
#         for i in unorderedList: # iterates through the unordered list
#             if i < minimum: # compares each individual value from the unordered list to the randomly selected "minimum" defined above
#                 minimum = i # makes the minimum the lesser of the two and continues to go through the list until all values have been compared
#         orderedList.append(minimum) 
#         unorderedList.remove(minimum)
#     print(orderedList)

# ordered(unorderedList)


# Correct solution: BUBBLE SORT
lst = [1,4,6,8,3,5]

def ordered(lst:list)->list:
    for x in range(len(lst)-1,0,-1):
        for y in range(x):
            if lst[y] > lst[y+1]:
                temp=lst[y]
                lst[y]=lst[y+1]
                lst[y+1]=temp
    print(lst)

ordered(lst)


