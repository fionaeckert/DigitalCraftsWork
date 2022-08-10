#do the bonus prompt

'''
classes: Tree, Gnome, Woodchuck, Garden
water gauge
chance of rain
chance of tree disappearing
each turn: rain or woodchuck

'''

import random
from unicodedata import name

# Classes
class Tree:
    def __init__(self):
        self.shade = -2

class Woodchuck:
    def __init__(self):
        self.disappearingTreeChance = 5
  
class Gnome: 
    def __init__(self):
        self.rainChance = 5
    
class Garden:
    def __init__(self):
        self.trees = []
        self.woodchucks = []
        self.gnomes = []
        self.waterLevel = 300
        self.waterLoss = 20
        self.rainChance = 20
        self.woodchuckChance = 10
        self.disappearingTreeChance = 0

# Functions        
    def addTree(self):
        tree = Tree()
        self.trees.append(tree)
        
    def addGnome(self):
        gnome = Gnome()
        self.gnomes.append(gnome)
        self.rainChance += gnome.rainChance
    
    def removeGnomes(self):
        gnomes=count(Gnome())
        self.gnomes.pop(gnomes)
        
    def addWoodchuck(self):
        woody = Woodchuck()
        self.woodchucks.append(woody)
        self.disappearingTreeChance += woody.disappearingTreeChance

    def rain(self):
        self.waterLevel += 60


# Simulation loop
ourGarden = Garden()

i = 1
newTree = 0
rainChance = ourGarden.rainChance
while len(ourGarden.trees) < 10 and ourGarden.waterLevel > 0:
    print('Round %d' % i)
    print('Water Level: %d' % ourGarden.waterLevel)
    print('Trees: %d' % len(ourGarden.trees))
    print('Gnomes: %d' % len(ourGarden.gnomes))
    print('Woodchucks: %d' % len(ourGarden.woodchucks))
    
    chance = random.random() * 100
    if chance < rainChance:
        ourGarden.rain()
        newTree += 1
        print('It rained! Water levels increased.')

    if newTree % 3 == 0 and newTree > 0:
        ourGarden.addTree()
        print('A new tree has blossomed!')

    chance = random.random() * 100
    if chance < ourGarden.woodchuckChance:
        ourGarden.addWoodchuck()
        print('A pesky woodchuck has entered the garden!')

    if i % 3 == 0:
        chance = random.random() * 100
        if chance > 50:
            ourGarden.addTree()
            print('A tree was added to the garden')
        else:
            ourGarden.addGnome()
            print('The garden has been blessed with a new gnome!')
    if i % 3 >= 1 and len(ourGarden.gnomes)>=3:
        gnomeTrade = input("Would you like to trade 3 gnomes for 1 tree? Enter yes or no: ")
        if gnomeTrade == "yes":
            ourGarden.addTree()
            ourGarden.removeGnomes()
            ourGarden.removeGnomes()
            ourGarden.removeGnomes()
            print("The garden lost 3 gnomes but gained 1 tree!")
        if gnomeTrade =="no":
            print("You have chosen to keep your gnomes. The garden did not gain a tree.")

    chance = random.random() * 100
    if chance < ourGarden.disappearingTreeChance and len(ourGarden.trees) > 0:
        del ourGarden.trees[0]
        print('The woodchucks destroyed a tree!')
    decrease = ourGarden.waterLoss - (len(ourGarden.trees) * 2)
    ourGarden.waterLevel -= decrease


    input('Enter a key to continue: ')
    i += 1



# Win and lose conditions
if len(ourGarden.trees) >= 10:
    print('You have won!')
elif ourGarden.waterLevel <= 0:
    print('You have lost!')