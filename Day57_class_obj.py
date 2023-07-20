class Person:
    name = 'vikash'
    occupation = 'se'
    natworth = 100000
    def info(self):
        print(f"{self.name} is a {self.occupation}")

a = Person()
a.name = "pandey"
a.occupation = 'ca'
#print(a.Person,a.occupation)
a.info()