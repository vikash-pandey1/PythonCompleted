def func1():
    
 try:
    l= [1,5,3,6]
    i = int(input("Enter the index"))
    print(l[i])
 except:
    print("some error occurred")
    return 0
 finally:
    print("i  will always exucuted")
x = func1()
print(x)