#Dictionary: a list of key value pairs

student = {
    "id": 790283,
    "name": "Dre Taylor",
    "class": "Senior",
    "GPA": 3.87
}

#print(student["GPA"])


student1 = {
    "id": "478923",
    "name": "Wes Fountain",
    "bootcamp": "Digitalcrafts"
}


student2 = {
    "id": "578490",
    "name": "Jorge Rodriguez",
    "bootcamp": "Digitalcrafts"
}

student3 = {
    "id": "453789",
    "name": "Khanh Trinh",
    "bootcamp": "Digitalcrafts"
}

student4 = {
    "id": "945890",
    "name": "Jonathan",
    "bootcamp": "Digitalcrafts"
}

student5 = {
    "id": "578909",
    "name": "Fiona Eckert",
    "bootcamp": "Digitalcrafts"
}


# List of dictionaries
digitalcrafts_class = [student1, student2, student3, student4, student5]
# print(digitalcrafts_class)
#    i am here!! 
#    hello world!!
#print(digitalcrafts_class[1]["name"])


# Create a function using the class list above, return a list that contains the student bio of any student whose id is less 500000
def listReturn(dcList: list) -> list:
    newList = []
    for st in dcList:
        stTest = int(st["id"]) 
        if(stTest<500000):
            newList.append(st)
    return newList  


#print(listReturn(digitalcrafts_class))


# Given the list above, write a function that sorts the students in the class based on their id, and returns that list


def listSort(oldList: list) -> list:
    newList = []
    topNumber = 0 
    for x in oldList:
        idNum = int(x["id"])
        print(idNum)
        if idNum > topNumber:
            topNumber = idNum
            newList.append(x)
        elif idNum < topNumber:
            i = 0
            print(len(newList))
            while i < 5:
                print('Index: ', i)
                newIdNum = int(newList[i]["id"])
                if idNum < newIdNum:
                    newList.insert(i, x)
                i += 1
print(newList)

listSort(digitalcrafts_class)