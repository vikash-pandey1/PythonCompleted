a = int(input("Enter your first no"))
b = int(input("Enter your second no"))
print("the addition is",a+b)
print("the substraction is ",a-b)
print("the multiplication is ",a*b)
print("the division is ", a/b)
print("the remainder is ",a%b)
fn = int(input("Enter your first no"))
sn = int(input("Enter your second no"))
op = input("Enter your operator")
match op:
    case '+':
        print(fn+sn)
    case '-':
        print(fn-sn)
    case '*':
        print(fn*sn)
    case '/':
        print(fn/sn)q
    case '%':
        print(fn%sn)
    case _:
        print("Enter your valid input")
    