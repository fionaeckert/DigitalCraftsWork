#aniaml rescue center in Atlanta is overcrowded and needs to send some dogs to nearby locations. They will send any dogs with brown fur that weigh over 50 lbs. 
#write a function that returns the current allocation of dogs at each center
import unittest

dogInfo = [{'breed':'German Shepard', 'weight': 88, 'fur': 'brown'},{"breed": "Golden Retriever", "weight": 45, "fur": "tan"},{"breed": "Terrier", "weight": 29, "fur": "black"},{"breed": "French Bulldog", "weight": 12, "fur": "gray"}]
newCenter = []
def sortCenters(dogInfo:list)->tuple:
    for dog in dogInfo:
        if dog['fur']=='brown' or dog['weight']>50:
            newCenter.append(dog)
            dogInfo.remove(dog)
    print('The dogs at the first center include: ', dogInfo)
    print('The dogs at the new center include: ', newCenter)
    return(dogInfo, newCenter)
print(sortCenters(dogInfo))

result1 = [{'breed': 'German Shepard', 'weight': 88, 'fur': 'brown'}]

class TestShelter(unittest.TestCase):
    def testShelters(self):
        self.assertListEqual(newCenter,[{'breed': 'German Shepard', 'weight': 88, 'fur': 'brown'}])
unittest.main()