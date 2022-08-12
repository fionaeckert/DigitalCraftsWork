# Need to kick off 6 people (mark off red in matrix when seat is kicked off)

import random

class Flight:
    def __init__(self, leaveNegativeReview: int, refuseMove: int, violentFlyer: int, happinessMeter: int, delayedFlight: int):
        self.leaveNegativeReview = leaveNegativeReview
        self.refuseMove = refuseMove
        self.violentFlyer = violentFlyer
        self.happinessmeter = 100
        self.delayedFlight = 0
        
        
    # Flight class
    # Happiness meter will start at 100
    # Contains the 16 rows
    # Contains leaveNegReview(), refuseMove(), violentFryer(),

    def chance(self):
        return random.randint(1, 100)

        


class First(Flight):
    def __init__(self): 
        self.negativeReview = 80          # 80% chance of negative review
        self.refuseMove = 50              # 50% chance of refusing to removed from flight (?)
        self.violent = 1                  # 1% chance of punching flight attendant

class Business(Flight):
    def __init__(self):
        self.negativeReview = 70             # 70% chance of negative review 
        self.refuseMove = 30                 # 30% chance of refusing to removed from flight (?)
        self.violent = 2                     # 2% chance of punching flight attendant   

    

class Comfort(Flight):          # ComfortPlus class
    def __init__(self):
        self.negativeReview = 50       # 50% chance of negative review
        self.refuseMove = 20            # 20% chance of refusing to removed from flight (?)
        self.violent = 5               # 5% chance of punching flight attendant
          

class Economy(Flight):                        # Economy class
    def _init__(self):
        self.negativeReview = 10        # 10% chance of negative review
        self.refuseMove = 10            # 10% chance of refusing to removed from flight (?)
        self.violent = 15               # 15% chance of punching flight attendant
        self.chuckNorris = 5            # 5% special ability to knock out a flight attendant which will cancel flight


firstClassList=[]
for seat in range(1,3):
    firstClassList.append(seat)


businessList = []
for seat in range(3, 6):
    businessList.append(seat)

comfortList = []
for seat in range(6,11):
    comfortList.append(seat)
    
economyList = []
for seat in range(11,17):
    economyList.append(seat)



flight = { 

'first':{   'A':firstClassList,
            'B':firstClassList,
            'C':firstClassList,
            'D':firstClassList},

'business':{'A':businessList,
            'B':businessList,
            'C':businessList,
            'D':businessList},


'comfort':{'A': comfortList,
            'B':comfortList,
            'C':comfortList,
            'D':comfortList},


'economy':{ 'A': economyList,
            'B': economyList,
            'C': economyList,
            'D': economyList}

}

# Beginning of game
removedPassengers = 0
