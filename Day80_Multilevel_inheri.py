class Animal:
    def __init__(self,name,species):
        self.name = name
        self.species = species
    def show(self):
        print(f"Name: {self.name}")
        print(f"Species:{self.species}")
        
class Dog(Animal):
    def __init__(self,name,bread):
        Animal.__init__(self,name,species= "Dog")
        self.breed = bread
    def show(self):
        Animal.show(self)
        print(f"Breed: {self.breed}")
class GoldenRetriver(Dog):
    def __init__(self,name,color):
        Dog.__init__(self,name,bread="Golden Retriever")
        self.color = color
    def show(self):
        Dog.show(self)
        print(f"Color: {self.color}")
        
o = GoldenRetriver("Tommy","Black")
o.show()