# prompting user for name
name = input('What is your name?')
print(name.upper())
#prints FONA
print(name.capitalize())
#prints Fona
print(len(name))
#prints number of letters
print('Your name has %s letters in it' % int(len(name)))
#converting the number of letters into a string

#day of week
day = input('Day (0-6)?')
days_of_week = {
    "0":"Sunday",
    "1":"Monday",
    "2":"Tuesday",
    "3":"Wednesday",
    "4":"Thursday",
    "5":"Friday",
    "6":"Saturday"
}
for day in range(0-7):
    print(days_of_week[day])

#celsius to farenheit 
degreeC = input('Enter a temp in Celsius')
farenheitCalc = str((degreeC * 9/5)+32)
for degreeC in farenheitCalc:
    print(farenheitCalc)

i = 0
while i<=10:
    i=i+1
    print(i)

# tip amount
bill = input('how much does it cost')
service = input('how good was your service')
divideBy = input('number of eaters')

for total in bill:
    if service =='good':
        print(int(bill)*.2+int(bill)/int(divideBy))
    elif service == 'fair':
        print(int(bill)*.15+int(bill)/int(divideBy))
    elif service == 'bad':
        print(int(bill)*.1+int(bill)/int(divideBy))

# how many coins
howMany = input('do you want a coin? ')
totalCoins = str()
for coins in totalCoins:
    if howMany == 'yes':
        print("1"+totalCoins)

# how to make a box
#n=int(input('Please enter a positive integer between 1 and 15: '))
#for row in range(n):
 #   for col in range(2*n):
  #      print('*' if row in(0,n-1) or col in(0,(2*n)-1) else ' ', end=' ')
   # print()

height = int(input('please enter height: '))
width= int(input('please enter width: '))
def parameters(height,width):

    for row in range(1,width + 1):
        for col in range(1,height + 1):
            if row==1 or row==width or col==1 or col==height:
                print('*',end='')
            else:
                print(' ',end='')
        print()
parameters(height,width)

