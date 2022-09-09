# TS = tropical storm; gets a name 
# TD = tropical depression; does not get a name 

import random

class weatherEvent:                                               
    def __init__(self, nothing, td, ts, cat1, cat2, cat3, cat4, cat5):
        self.nothing = nothing
        self.td = td
        self.ts = ts
        self.cat1= cat1
        self.cat2 = cat2
        self.cat3 = cat3
        self.cat4 = cat4
        self.cat5 = cat5

    def thisYearStorms (nothing, td, ts, cat1, cat2, cat3, cat4, cat5):
        stormNames = ['Ella', 'John', 'Francesa', 'Gerard', 'Sarah', 'Grace', 'Frank', 'Abigayle', 
        'Theresa', 'Holly', 'Carey', 'Jacob', 'Kurt', 'Lily', 'Colleen', 'Ryan', 'Zach', 'Walter']
        stormDestinations = ['Honolulu', 'Miami', 'Atlanta', 'Charlotte', 'Boston', 'New York', 'D.C.', 'Baltimore', 
        'Cape Hatteras', 'Morehead', 'Wilmington', 'Savannah', 'Myrtle Beach']
        stormSpeed = random.randomint(1,50)

        for stormEvents in range(25):
                event += 1
        while stormEvents<24:
            random_nothing = random.randint(1,100)
            random_td = random.randint(1,100)
            random_ts = random.randint(1,100)
            random_cat1 = random.randint(1,100)
            random_cat2 = random.randint(1,100)
            random_cat3 = random.randint(1,100)
            random_cat4 = random.randint(1,100)
            random_cat5 = random.randint(1,100)
            
        if random_nothing <= nothing:
            print('Nothing happened! Huzzah!')
        elif random_td <= td:
            print('Oh no, a tropical depression!')
        elif random_ts <= ts:
            print('Oh no! A tropical storm has made landfall!')
            print('Watch out for Tropical Storm %d!' % random.choice(stormNames))
            print('The Tropical Storm is travelling at %d miles per hour!' % stormSpeed)
            print('The Tropical Storm is headed for %d!'% random.choice(stormDestinations))
        elif random_cat1 <= cat1:
            print('Oh no! A category 1 hurricane has made landfall!')
            print('Watch out for Hurricane %d!' % random.choice(stormNames))
            print('The Hurricane is travelling at %d miles per hour!' % random.randomint(1,50))
            print('The Hurricane is headed for %d!'% random.choice(stormDestinations))
        elif random_cat2 <= cat2:
            print('Oh no! A category 2 hurricane has made landfall!')
            print('Watch out for Hurricane %d!' % random.choice(stormNames))
            print('The Hurricane is travelling at %d miles per hour!' % stormSpeed)
            print('The Hurricane is headed for %d!'% random.choice(stormDestinations))
        elif random_cat3 <= cat3:
            print('Oh no! A category 3 hurricane has made landfall!')
            print('Watch out for Hurricane %d!' % random.choice(stormNames))
            print('The Hurricane is travelling at %d miles per hour!' % stormSpeed)
            print('The Hurricane is headed for %d!'% random.choice(stormDestinations))
        elif random_cat4 <= cat4:
            print('Oh no! A category 4 hurricane has made landfall!')
            print('Watch out for Hurricane %d!' % random.choice(stormNames))
            print('The Hurricane is travelling at %d miles per hour!' % stormSpeed)
            print('The Hurricane is headed for %d!'% random.choice(stormDestinations))
        elif random_cat5 <= cat5:
            print('Oh no! A category 5 hurricane has made landfall!')
            print('Watch out for Hurricane %d!' % random.choice(stormNames))
            print('The Hurricane is travelling at %d miles per hour!' % stormSpeed)
            print('The Hurricane is headed for %d!'% random.choice(stormDestinations))    


weatherEvent.thisYearStorms(30,20,18,12,10,6,3,1)

