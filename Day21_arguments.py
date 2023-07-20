# def average(a,b):
#     print("The average is: ",(a+b)/2)

# average(3,5)

# default argument

# def average(a =4,b =3):
#     print("The average is: ",(a+b)/2)

# average(43)

# keyword argument

# def average(a =4,b =3):
#     print("The average is: ",(a+b)/2)

# average(b = 3,a =34)

# required argument

# def average(a,b):
#     print("The average is: ",(a+b)/2)

# average(43,5)

#keyword length argument

def average(*numbers):
    sum = 0
    for i in numbers:
        sum = sum+i
    print("average is: ",sum/len(numbers))
    
average(53,56,53)
