class Emp:
    def __init__(self,name,id):
        self.name = name
        self.id = id
    def showDetail(self):
        print(f"The name of Emp :{self.id} is {self.name}")
        
e1 = Emp("Rohan Das",400)
e1.showDetail()
e2 = Emp("vi",434)
e2.showDetail()