def hello():
    print("hello world")
    

def greet(fx):
    def mfx():
        print("good morning")
        fx()
        print("thanks for usign this  function")
    return mfx

@greet
def hello():
    print("helo woer")
    
def add(a,b):
    print(a+b)
    
hello()
