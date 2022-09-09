from re import search
from turtle import distance


criminals = [{
    "name": "Bob",
    "distance": 1.2,
    "crimes_committed": 1,
    "address": "4325 Birch St"
},
{
    "name": "May",
    "distance": 0.3,
    "crimes_committed": 3,
    "address": "8903 Trolley St"
},
{
    "name": "Tyler",
    "distance": 0.8,
    "crimes_committed": 0,
    "address": "2348 Magnolia Dr"
},
{
    "name": "Reggie",
    "distance": 0.5,
    "crimes_committed": 1,
    "address": "3478 Seminole Ln"
},
{
    "name": "Seth",
    "distance": 3.2,
    "crimes_committed": 0,
    "address": "9803 Azul St"
},
{
    "name": "Ray",
    "distance": 2.9,
    "crimes_committed": 0,
    "address": "3467 Frost St"
},
{
    "name": "Kim",
    "distance": 0.1,
    "crimes_committed": 0,
    "address": "7893 Daisy Ln"
},
{
    "name": "Lisa",
    "distance": 1.2,
    "crimes_committed": 1,
    "address": "2345 Gale St"
},
{
    "name": "Ashley",
    "distance": 1.5,
    "crimes_committed": 5,
    "address": "6783 Sycamore St"
},
{
    "name": "Turner",
    "distance": 4.3,
    "crimes_committed": 1,
    "address": "8923 Pecan Ln"
},
]

# def catchEm(criminals):
#     inRange = []
#     for i in criminals["distance"]:
#         if i <= 2:
#             inRange.append(criminals[i])
#     print(inRange)
# catchEm(criminals)



def searchHomes(homeList:list)->list:
    finalList = []
    for home in homeList:
        if home['distance']<2:
            if len(finalList)==0:
                finalList.append(home)
            else:
                for x in range(len(finalList)):
                    if home['distance']<=finalList[x]['distance']:
                        finalList.insert(x,home)
                        break
                    elif x == len(finalList)-1:
                        finalList.append(home)
    print(finalList)

searchHomes(homeList)




for perp in homeList:
    # use bubble sort to arrange addresses from least distance to greatest
    for i in range(len(homeList)):
        for currentIndex in range(0, len(homeList) - i - 1):
            if perp.get('distance') > perp[currentIndex + 1]:
                perp[currentIndex], perp[currentIndex + 1] = perp[currentIndex + 1], perp[currentIndex]
    print(homeList)        
    



criminal1Dist = criminals[0]["distance"]
criminal2Dist = criminals[1]["distance"]
criminal3Dist = criminals[2]["distance"]
criminal4Dist = criminals[3]["distance"]
criminal5Dist = criminals[4]["distance"]
criminal6Dist = criminals[5]["distance"]
criminal7Dist = criminals[6]["distance"]
criminal8Dist = criminals[7]["distance"]
criminal9Dist = criminals[8]["distance"]
criminal10Dist = criminals[9]["distance"]

criminalDistances = [criminal1Dist,criminal2Dist, criminal3Dist, criminal4Dist, criminal5Dist, criminal6Dist, criminal7Dist, criminal8Dist, criminal9Dist, criminal10Dist]
sortedList = sorted(criminalDistances)
print(sortedList)

# criminal1Addy = criminals[0]["address"]
# criminal2Addy = criminals[1]["address"]
# criminal3Addy = criminals[2]["address"]
# criminal4Addy = criminals[3]["address"]
# criminal5Addy = criminals[4]["address"]
# criminal6Addy = criminals[5]["address"]
# criminal7Addy = criminals[6]["address"]
# criminal8Addy = criminals[7]["address"]
# criminal9Addy = criminals[8]["address"]
# criminal10Addy = criminals[9]["address"]




# # print(criminalDistances)

# # def catchEm(criminalDistances:list)->list:
# #     for i in range(len(criminalDistances)-1,0,-1):
# #         for j in range(i):
# #             if j<criminalDistances[j+1]:
# #                 temp = criminalDistances[j]
# #                 criminalDistances[j] = criminalDistances[j+1]
# #                 criminalDistances[j+1]=temp
# #     print(criminalDistances)
# # catchEm(criminalDistances)


# # def catchEm(criminalDistances:list)->list:
# #     sortedList = []
# #     criminalDistances.sort
# #     print(sortedList)
# # catchEm(criminalDistances)