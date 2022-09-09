# write a function that orders a list least to greatest by comparing indices. 
# if the value of one index is greater than the next swap the two indices.


unsortedList = [5778,6262,9887,233,90,58,80]

# def sorted(unsortedList:list)->list:
#     for i in range(len(unsortedList)-1,0,-1): # sorts through the unsorted list backwards
#         # print(unsortedList[i]) # test
#         for j in range(i):                    # sorting through second time to compare both index values
#             if j < unsortedList[j + 1]:         # 
#                 temp = unsortedList[j]        # assigning the greater value to temp variable to store
#                 unsortedList[j] = unsortedList[j + 1]   
#                 unsortedList[j + 1] = temp
#     print(unsortedList)

# sorted(unsortedList)



def sorted(unsortedList:list)->list:
    for i in range(len(unsortedList)): #iterating from front to back of the list
            # since the last index traversed in the previous iteration will always be the largest
            # value, decrease the number of indices traversed by 1
            # with a list of length 5, in the first iteration we traverse 5 indices,
            # in the second iteration we traverse 4 indices,
            # in the third iteration we traverse 3 indices, etc.
        for currentIndex in range(0,len(unsortedList)-i-1): #don't need to go to the end of the array each time because we know that the largest number is already at the end. 
            # checking if the current index is greater than the next index
            if unsortedList[currentIndex]>unsortedList[currentIndex+1]:   # so we're taking the last index to look at as wherever i is - 1
                # swap the values
                unsortedList[currentIndex], unsortedList[currentIndex+1] = unsortedList[currentIndex+1], unsortedList[currentIndex]
    print(unsortedList)

sorted(unsortedList)                                      













# def sortList(numList):
#     for i in range(0, len(numList) -1):         # iterating through numList
#         # print(i)
#         for x in range(i, len(numList)):    # iterating a second time to compare
#             if numList[x] < numList[i]:         # comparing current index to the index from second list
#                 temp = numList[x]              # assigning temporary variable to the greater number
#                 numList[x] = numList[i]         
#                 numList[i] = temp                   
                
#     print(numList)
# sortList(unsortedList)