class MyClass:
    def __init__(self,value):
        self._value = value
    def show(self):
        print(f"value is {self._value}")
        
    @property
    def value(self):
        return 10* self._value
    
    @value.setter
    def value(self,new_value):
        self._value = new_value(70)


obj = MyClass(10)
obj.ten_value = 67
print(obj.value)
obj.show()