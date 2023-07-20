class Emp:
    def __init__(self,name):
        self.name = name
        
    def show(self):
        print(f"The dance is {self.dance}")
class Dancer:
    def __init__(self,dance):
        self.dance = dance
class DanceEmp(Emp,Dancer):
    def __init__(self,dance,name):
        self.name = name
        self.dance = dance
        
o = DanceEmp("dj","shita")
print(o.name)
print(o.dance)
o.show()