class car:
    def __init__(self, curbWeight:int, topSpeed:int, allWheel:bool, rearWheel:bool, horsepower:int):
        self.curbWeight = curbWeight
        self.topSpeed = topSpeed
        self.allWheel = allWheel
        self.rearWheel = rearWheel
        self.horsepower = horsepower
    def accelerate():
        return 'Moving!'
    def brake():
        return 'Stopping!'
    def reverse():
        return 'Backing up!'

class ICE(car):
    def __init__(self, curbWeight: int, topSpeed: int, allWheep: bool, 
    rearWheel: bool, horsepower: int, mpg:int):
        self.mpg = mpg
    def refill():
        return 'Filling up!'

class EV(car):
    def __init__(self, curbWeight: int, topSpeed: int, allWheep: bool, rearWheel: bool, 
    horsepower: int, batteryCapacity: int, range:int):
        self.batteryCapacity = batteryCapacity
        self.range = range
    def charge():
        return 'Charging!'

print(EV.charge())
