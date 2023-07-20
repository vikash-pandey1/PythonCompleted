class Emp:
    # class variable
    companyName = "microsoft"
    def __init__(self,name):
        self.name = name
        # instance variable that can change 
        self.raise_amount = 43.3
    def showDetails(self):
        print(f"The name of the Emp is {self.name} and raise amount is {self.raise_amount} and belong to {self.companyName}")
emp1 = Emp("vikash")
Emp.showDetails(emp1)
emp2 = Emp("Rohan")
emp2.raise_amount = 535
emp2.companyName = "apple"
Emp.showDetails(emp2)