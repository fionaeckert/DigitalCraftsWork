#without using the built in python library, sort an array of integers from least to greatest.
unsortedArray = [12, 8, 55, 6, 1, 78, 46, 98]
sortedArray = []



#INFINITE LOOP
# while unsortedArray:
#     minimum = unsortedArray[0] 
#     for number in unsortedArray:
#         if number < minimum:
#             minimum = number
#     sortedArray.append(minimum)
#     print(sortedArray)

#INFINITE LOOP
# for number in range(len(unsortedArray)):
#     for integer in range(number + 1,len(unsortedArray)):
#         if unsortedArray[number]>unsortedArray[integer]:
#             unsortedArray[number], unsortedArray[integer] = unsortedArray[integer], unsortedArray[number]

# print(unsortedArray)

#work on this in sections
#work on looping forward and backward