# Your task is to write a program that calculates how much of a tip to leave at a restaurant.
# Prompt the user for two things:
# The total bill amount
# The level of service, which can be one of the following: good, fair, or bad
# Calculate the tip amount and the total amount (bill amount + tip amount). The tip percentage based on the level of service is based on:
# good -> 20%
# fair -> 15%
# bad -> 10%
# Allow the ability to divide the check into equal parts amount a number of people. The user will enter the number of people to be divided amongst

bill = input('How much is the bill? ')
service = input('How was your service? Please enter good, fair, or bad. ')

for total in bill:
    if service =='good':
        totalPlusTip = int(int(bill)*.2+int(bill))
        print('Your total today is $%d.' % totalPlusTip)
        split = input('Would you like to split the bill? ')
        if split == 'no':
            break
        elif split == 'yes':
            checkSplit = int(input('How many people dined today? '))
            dividedBill = totalPlusTip/checkSplit
            print('Each diner owes $%d.' % dividedBill)
            break
    elif service == 'fair':
        totalPlusTip = int(bill)*.15+int(bill)
        print('Your total today is $%d.' % totalPlusTip)
        split = input('Would you like to split the bill? ')
        if split == 'no':
            break
        elif split == 'yes':
            checkSplit = int(input('How many people dined today? '))
            dividedBill = totalPlusTip/checkSplit
            print('Each diner owes $%d.' % dividedBill)
            break
    elif service == 'bad':
        totalPlusTip = int(bill)*.10+int(bill)
        print('Your total today is $%d.' % totalPlusTip)
        split = input('Would you like to split the bill? ')
        if split == 'no':
            break
        elif split == 'yes':
            checkSplit = int(input('How many people dined today? '))
            dividedBill = totalPlusTip/checkSplit
            print('Each diner owes $%d.' % dividedBill)
            break
