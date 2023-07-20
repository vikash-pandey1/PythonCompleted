# a = int(input("Enter your age"))
# print("your age is ",a)
# if(a>18):
#     print("you can drive")
# elif(a==18):
#     print("you may be drive")
# else:
#     print("you can't drive")

# if statement
no = 10
if(no==10):
    print("no is equal to 10")
    
# if else

no = 233
if(no%2==0):
    print("even")
else:
    print("odd")
    
# if else elif

if(no<100):
    print("no is less than 100")
elif(no>100):
    print("no is greater than 100")
else:
    print("no is neighter less than 100 or greater than 100")
    
# nester if
b = 83
if(b<100):
    if(b<50):
        print("no is less than 50")
    else:
        print("no is less than 100 greater than 50")
else:
    print("no is greater than 100")