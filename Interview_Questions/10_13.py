# Write a function in python to detect if it's Friday the 13th.
#  The function can accept two parameters. The first parameter will 
# be the number indicating the month, and the second will be the year in four digits. 
# Return True when the month contains a Friday the 13th, else return False.


import calendar

def spooky(month:int,year:int)->bool:
    firstDay = calendar.Calendar(firstweekday=0)
    givenMonthYr = firstDay.itermonthdays2(year,month)
    friThirt = (13,4)
    for day in givenMonthYr:
        if friThirt in givenMonthYr:
            print(True)
        else:
            print(False)

spooky(10,2023)
    