#Functions are used to make your modular and to avoid having to rewrite code
#Whenever we call a function we type in the name exampleFunction(...)
#The ... means you need to put in parameters
#Parameters are values that a function receives. The parameters are variables that are created and can only be used within the scope of the function

#The scope of this function is only lines 5-6, therefore date cannot be called on line 11
from array import array
from unittest.util import strclass


date=12
def whatsTheDate(date:int)->str:
    return "Today's date is %s"% date

whatsTheDate(8)
print(date)
#inside the function, the date is 8. outside the function the date is 12.

#functions can call other functions
def whatsTheMonth(month: str):
    return 'We are in the month of %s.'% month
    #calling the previous functioon to print the date
    print(whatsTheDate(8))

whatsTheMonth('August')

def dateTeller(month:str,date:str,year:str)->str:
    print(whatsTheMonth(month), whatsTheDate(date), year)
dateTeller('August','8','2022.')

#tuples
#can store two values to one variable. not mutable meaning values cannot be changed after instatiation
my_favorite_colors=('blue','purple')
print(type(my_favorite_colors))
print(my_favorite_colors[0])

#has a few applications like dice games, etc.
diceRoll=(3,5)
diceRoll[0]=1       #this won't work because tuples are not mutable
arrayDiceRoll=[3,5]
arrayDiceRoll[0]=1      #this works because arrays are mutable
print(arrayDiceRoll)

Chicago=(34.12345,43.12234)
#tuples can extend beyond 2 objects
#---------------------------------------------------------------------------------------------------------
#given a string, create a function that returns the string reversed

def reverse(string:str)->str:
    reverseString=string[::-1]
    return reverseString
print(reverse('Hello world'))

#slicing
#changes the way we iterate over a string or a list
#the first number represents the index we are starting at
#the second number is our ending index
#the last number dictates how many numbers to skip by

#lets get the odd numbers from a string
number = '1234567890'
print(number[0:9:2]) #prints all odd numbers
print(number[::2]) #does the same thing as the above
print(number[1:9:2]) #prints all even numbers

#now get the prime numbers in reverse order
#prime number is any number >1 and is only divisible by 1 and itself
#finish for homework
reverseOrder=number[::-1]
primeNumbers=[]
for prime in reverseOrder:
    if int(prime) % 2==1 and int(prime) > 1:
        primeNumbers.append(prime)
    #elif reverseOrder
print(primeNumbers)

#Edge case of slicing
print(number[3:9:-2]) #there's no way to start at the end of the array but also start at index 3

#---------------------------------------------------------------------------------------------------------
#Object oriented programming
#class is a definition of an object
#classes are mutable 

#define a class, class names typically start with an uppercase letter 
class Pokemon:
    #constructor: defines the bare minimum to define an object
    def __init__(self, hp: int, name: str, type: tuple, weakness: tuple):         #self refers to this particular object
        __hitPoints = 0     #double underscore
        self.hp=hp        #anything typed below ^ are variables that create the object we're trying to work with
        self.name = name        #commonplace to have the same variable name passed as the parameter
        self.type = type
        self.weakness = weakness
        self.damage = 0
        self.status = {
            "Frozen": False,
            "Burned": False,
            "Poisoned":False,
            "Paralyzed": False
            }
    
    def __run(self):
        print('You fled the battle.')
    def useItem(self, item):
        print('You used the %s.' % item) 
class Pikachu(Pokemon):
    def thunderbolt(self):
        print('%s used thunderbolt!' % self.name)
        damage=50
    def quickAttack(self):
        print('%s used quick attack!' % self.name)
        damage=30
    def thunderWave(self):
        damage=0
    #using setters to update a pokemon's hp
    def heal(self, hp):
        self.hp += 100
    def setHp(self, hp):
        if hp>100:
            print('Error: Cannot heal Pokemon by that amount')
        else:
            self.hp += hp

    def useItem(self, item):
        print('You used the %s.'% item)
        print("It's still Pikachu's turn, select a move!")

class Electrabuzz(Pokemon):
    def thunderbolt(self):
        damage = 80

class Squirtle(Pokemon):
    def surf(self):
        print('%s used surf' % self.name)
        damage=60
    def watergun(self):
        print('%s used watergun' % self.name)
        damage=40
    def bubble(self):
        print('%s used bubble' % self.name)
    def hydropump(self):
        print('%s used hydropump!'% self.name)
        damage = 120




class Bulbasaur(Pokemon):
    def vineWhip(self):
        print('%s used vine whip!' % self.name)
    def synthesis(self):
        print('%s used synthesis!'% self.name)
    def razorLeaf(self):
        print('%s used razor leaf!'% self.name)
    def solarBeam(self):
        print('%s used solar beam!'% self.name)
    

pikachu = Pokemon(40,'Pikachu','electric','ground')
print(pikachu) #prints the location of this in the machine
print(pikachu.hp) #print the attribute defined 
pikachu.hp = 55 #can change a parameter like this

squirtle = Pokemon(50,'squirtle','water','grass')
print(squirtle.type)

squirtle.run()
pikachu.run()

pikachu.useItem('potion')

blaziken = Pokemon(120, 'Blaziken', ('fire','fighting'),('water','psychic'))
print(blaziken.type) #prints both types
print(blaziken.type[1]) #prints the type in index 2

#inheritance
#when a child class takes on the properities of a parent class

# raichu = Pikachu(100,'Raichu',('electric'),('ground'))
# raichu.thunderbolt()
# raichu.quickAttack()

steven=Pikachu(100,'Steven',('electric'),('ground'))
steven.thunderbolt()

# shelly = Squirtle(50,'Shelly',('water'),('grass','electric'))
# shelly.hydropump()

# ivy=Bulbasaur(50,'Ivy',('grass'),('fire'))
# ivy.razorLeaf()


pikachu.useItem('elder berry') #this prints that pikachu used the cure. it DOES NOT PRINT that it's still Pikachu's turn because it was created within the Pokemon class
steven.useItem('cure') #this prints that steven used the cure AND that it's still Pikachu's turn because it was created within the Pikachu class
steven.setHp(100000) #this prints an error due to the private variables defined above

#Create a cat/dog game, create a class for both the cat and dog. both animals should have: breed, weight, fur color, name. each animal must make their own unique sound. create cat/dog class which can do everything that both animals can do but in its own way

# class Pokemon:
#     #constructor: defines the bare minimum to define an object
#     def __init__(self, hp: int, name: str, type: tuple, weakness: tuple):         #self refers to this particular object
#         __hitPoints = 0     #double underscore
#         self.hp=hp        #anything typed below ^ are variables that create the object we're trying to work with
#         self.name = name        #commonplace to have the same variable name passed as the parameter
#         self.type = type
#         self.weakness = weakness
#         self.damage = 0
#         self.status = {
#             "Frozen": False,
#             "Burned": False,
#             "Poisoned":False,
#             "Paralyzed": False
#             }
