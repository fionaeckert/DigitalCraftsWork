import random
random.random()

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
    
    def run(self):
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
        chance = random.random()*100
        if chance < 70:
            print(super().useItem(item)) #super() jumps up to the parent class 
        elif chance >= 70 and chance <100:
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


# pikachu.useItem('elder berry') #this prints that pikachu used the cure. it DOES NOT PRINT that it's still Pikachu's turn because it was created within the Pokemon class
# steven.useItem('cure') #this prints that steven used the cure AND that it's still Pikachu's turn because it was created within the Pikachu class
# steven.setHp(100000) #this prints an error due to the private variables defined above

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
steven.useItem('potion',80) #this determiness what will return from lines 45-50
