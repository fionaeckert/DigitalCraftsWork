class Cat: 
    def __init__(self, breed: str, weight: int, furColor: str, name: str):
        self.breed = breed
        self.weight = weight
        self.furColor = furColor
        self.name = name
    def purr(self):
        print('%s purrs at his owner.' % self.name)
        
class Dog: 
    def __init__(self, breed: str, weight: int, furColor: str, name: str):
        self.breed = breed
        self.weight = weight
        self.furColor = furColor
        self.name = name
    def bark(self):
        print('%s barks at his owner.' % self.name)

class CatDog(Cat, Dog): 
    def meowof(self):
        print('%s meowofs at his owner.' % self.name)

bond = Cat('Tuxedo',18,'black and white','Bond')
james = Dog('Poodle', 20, 'grey', 'James')
jamesBond = CatDog('Tuxoodle', 38, 'tan', 'James Bond')
bond.purr()
james.bark()
jamesBond.bark()
jamesBond.purr()
jamesBond.meowof()
print(jamesBond.furColor)
