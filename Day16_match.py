x = int(input("Enter your first no"))
y = int(input("Enter your second no"))
opt = input("Enter your operation")
match(opt):
    case '+':
        print("addition of two no is:x+y ",x+y)
    case '-':
        print("substraction of two no is: $x-y",x-y)
    case '*':
        print("multiplication of two no is: $x*y",x*y)
    case '/':
        print("division of two no is: $x/y",x/y)
    case '%':
        print("floor division of two no is: $x%y",x%y)
    case '_':
        print("please enter the valid input")