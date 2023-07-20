class Emp:
    def __init__(self,name):
        self.name = name
    def __len__(self):
        i=0
        for c in self.name:
            i = i+1
            return i
e = Emp("Vikash")
print(e.name)
print(len(e))