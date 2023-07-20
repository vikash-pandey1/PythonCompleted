class Emp:
    company = "apple"

    def show(self):
        print(f"The name is {self.name} and company is {self.company}")

    @classmethod
    def changeCompany(cls, newCompany):
        cls.company = newCompany


e1 = Emp()
e1.name = "vikash"
e1.show()
e1.changeCompany("Tesla")
e1.show()
print(Emp.company)
