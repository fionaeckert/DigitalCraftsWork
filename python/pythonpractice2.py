sampleA=['third','second','first']
sampleB=[]

i = len(sampleA)-1
while i >=0:
    sampleB.append(sampleA[i]) 
    i = i-1
print(sampleB)

# How to print a reversed list
ordinalList = ['1st', '2nd', '3rd']
reversedOrdinalList = []
while len(ordinalList) > 0:
    ordinal = ordinalList.pop()
    reversedOrdinalList.append(ordinal)
print(reversedOrdinalList)
#---------------------------------------------
