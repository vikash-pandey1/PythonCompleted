# dir()
# x = [1,2,3] 
# print(dir(x))

# __dict__
# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
# p = Person("vikash",30)
# print(p.__dict__)

# help()
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
p = Person("vikash",30)
print(help(Person))
