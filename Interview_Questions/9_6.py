# Using python, make an API call to the random user api. 
# Retrieve 10 users and store the first and last name of each user you retrieve. 
# Store the list of users in alphabetical order by last name.

# url = 'https://random-data-api.com/api/v2/users?size=10'

import requests

userList = []

response = requests.get('https://random-data-api.com/api/v2/users?size=10').json
print(response)
fullName = (response['first_name'],response['last_name'])
userList.append(fullName)

for x in range(len(userList)):
    for y in range(len(userList)-1-x):
        if userList[y][1]>userList[y+1][1]:
            temp = userList[y+1]
            userList[y+1] = userList[y]
            userList[y] = temp

print(userList)

