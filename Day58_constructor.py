class Person:
    def __init__(self,n,o):
        print("hey i am a person")
        self.name = n
        self.occ = o
    name = "vikash"
    occ = "se"
    def info(self):
        print(f"{self.name} is a {self.occ}")
    
    
a = Person("vikash","developer")
b=Person("bholu","se")
a.name = "vikash pandey"
#a.occ  = "eng"
a.info()