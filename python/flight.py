# Need to kick off 6 people (mark off red in matrix when seat is kicked off)
import random

class Flight:                                               # Flight class
    def __init__(self, leaveNegativeReview: int, refuseMove: int, violentFlyer: int, happinessMeter: int, delayedFlight: int):
        self.leaveNegativeReview = leaveNegativeReview
        self.refuseMove = refuseMove
        self.violentFlyer = violentFlyer
        self.happinessMeter = happinessMeter
        happinessMeter = 100                        # Happiness meter will start at 100
        self.delayedFlight = delayedFlight
        delayedFlight = 0
        
    # Contains the 16 rows
    # Contains leaveNegReview(), refuseMove(), violentFryer(),

    def firstClassActions(negativeReview, refuseMove, violent):
        for passengers in range(8):
            seat += 1
            print('Passenger : ', seat)

            negRev = random.randint(1, 100)
            if negRev <= negativeReview:
                Flight.happinessMeter -= 1
                print('Negative review recieved!')
            
            elif refuse <= refuseMove:
                refuse = random.randint(1, 100)
                Flight.delayedFlight += 5
                print('Passenger has refused to move. The flight has been delayed by 5 minutes!')
                
            elif punch == violent:
                punch = random.randint(1, 100)
                Flight.happinessMeter -= 10
                print('Oh no! A flight attendant has been punched!')
            else:
                print('Passenger does nothing')
    # firstClassActions(80, 50, 1)

    def businessActions(negativeReview, refuseMove, violent):
        for passengers in range(12):
            seat += 1
            print('Passenger : ', seat)

            negRev = random.randint(1, 100)
            if negRev <= negativeReview:
                Flight.happinessMeter -= 1
                print('Negative review recieved!')
            
            elif refuse <= refuseMove:
                refuse = random.randint(1, 100)
                Flight.delayedFlight += 5
                print('Passenger has refused to move. The flight has been delayed by 5 minutes!')
                
            elif punch <= violent:
                punch = random.randint(1, 100)
                Flight.happinessMeter -= 10
                print('Oh no! A flight attendant has been punched!')
            else:
                print('Passenger does nothing')
    # businessActions(70, 30, 2)

    def comfortActions(negativeReview, refuseMove, violent):
        for passengers in range(20):
            seat += 1
            print('Passenger : ', seat)

            negRev = random.randint(1, 100)
            if negRev <= negativeReview:
                Flight.happinessMeter -= 1
                print('Negative review recieved!')
            
            elif refuse <= refuseMove:
                refuse = random.randint(1, 100)
                Flight.delayedFlight += 5
                print('Passenger has refused to move. The flight has been delayed by 5 minutes!')
                
            elif punch <= violent:
                punch = random.randint(1, 100)
                Flight.happinessMeter -= 10
                print('Oh no! A flight attendant has been punched!')
            else:
                print('Passenger does nothing')
    # comfortActions(50, 20, 5)

    def economyActions(negativeReview, refuseMove, violent, chuckNorris):
        round=1
        for passengers in range(24):
            removedPassengers = 0   
        while removedPassengers < 6 and testing.happinessMeter >= 70:
            
            negRev = random.randint(1, 100)
            refuse = random.randint(1, 100)
            punch = random.randint(1, 100)
            knockOut = random.randint(1, 100)

            print('---------------------------------------------')
            print('Round %d' % round) #prints the round of the simulation to the user
            print('Removed passengers: %d' % removedPassengers)
            print('Happiness meter: %d' % testing.happinessMeter)
            print('Delayed flight minutes: %d' % testing.delayedFlight)


            if negRev <= negativeReview:
                testing.happinessMeter -=  1
                print('Negative review recieved! Happiness meter is at: %d' % testing.happinessMeter)

            
            elif refuse <= refuseMove:
                testing.delayedFlight += 5
                print('Passenger has refused to move. The flight has been delayed by 5 minutes! Delayed flight minutes: %d' % testing.delayedFlight)
                
            elif  punch <= violent:
                testing.happinessMeter -= 10
                print('Oh no! A flight attendant has been punched! Happiness meter is at: %d' % testing.happinessMeter)
                
            elif knockOut <= chuckNorris:
                print('Oh no! A flight attendant just got knocked out! Happiness meter is at: %d' %testing.happinessMeter)
                testing.happinessMeter -= 100

            else:
                removedPassengers += 1 
                print("Passenger is removed from the flight. Removed passenger count: %d" % removedPassengers)
        round += 1
        if removedPassengers == 6 and testing.happinessMeter >= 70: #ends the loop if 6 passengers are removed and the happiness meter is still above 70
                print("Congrats! You've won.")

    # economyActions(10, 10, 15)
testing = Flight(0,0,0,100,0)
Flight.economyActions(10,20,15,5)

class First(Flight):
    def __init__(self): 
        self.negativeReview = 80                        # 80% chance of negative review
        self.refuseMove = 50                            # 50% chance of refusing to removed from flight (?)
        self.violent = 1                                # 1% chance of punching flight attendant
        self.passengers = 8


class Business(Flight):
    def __init__(self):
        self.negativeReview = 70             # 70% chance of negative review 
        self.refuseMove = 30                 # 30% chance of refusing to removed from flight (?)
        self.violent = 2                     # 2% chance of punching flight attendant  
        self.passengers = 12

    

class Comfort(Flight):          # ComfortPlus class
    def __init__(self):
        self.negativeReview = 50       # 50% chance of negative review
        self.refuseMove = 20            # 20% chance of refusing to removed from flight (?)
        self.violent = 5               # 5% chance of punching flight attendant
        self.passengers = 20  

class Economy(Flight):                        # Economy class
    def _init__(self):
        self.negativeReview = 10        # 10% chance of negative review
        self.refuseMove = 10            # 10% chance of refusing to removed from flight (?)
        self.violent = 15               # 15% chance of punching flight attendant
        self.chuckNorris = 5            # 5% special ability to knock out a flight attendant which will cancel flight
        self.passengers = 20




# Beginning of simulation

# round = 0
# for passenger in range(24): # passes the number of seats within a specific class as the parameters for how many times the loop will run
#     removedPassengers = 0 #counts the number of passengers removed
#     round += 1 # adds another round if the loop continues
# while removedPassengers < 6 and testing.happinessMeter >= 70:
#     Flight.economyActions(10,20,15,5)      # passes in the parameters of the specific class
#         # print('The happiness meter is at: %d' % testing.happinessMeter) # prints the happiness meter level after each run
#         # print('The flight has been delayed: %d minutes' % testing.delayedFlight) # prints the number of minutes the flight has been delayed to the user
# if removedPassengers == 6 and testing.happinessMeter >= 70: #ends the loop if 6 passengers are removed and the happiness meter is still above 70
#         print("Congrats! You've won.") 








#Extra work:

# firstClassList=[]
# for seat in range(1,3):
#     firstClassList.append(seat)


# businessList = []
# for seat in range(3, 6):
#     businessList.append(seat)

# comfortList = []
# for seat in range(6,11):
#     comfortList.append(seat)
    
# economyList = []
# for seat in range(11,17):
#     economyList.append(seat)



# flight = { 

# 'first':{   'A':firstClassList,
#             'B':firstClassList,
#             'C':firstClassList,
#             'D':firstClassList},

# 'business':{'A':businessList,
#             'B':businessList,
#             'C':businessList,
#             'D':businessList},


# 'comfort':{'A': comfortList,
#             'B':comfortList,
#             'C':comfortList,
#             'D':comfortList},


# 'economy':{ 'A': economyList,
#             'B': economyList,
#             'C': economyList,
#             'D': economyList}

# }





