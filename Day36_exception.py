# exception handling is the process of responding to unwanted or unexpected events when a computer program runs.
# Exception handling deals with these events 

# a = input("Enter the number")
# print(f"multiplication table of {a} is :")
# try:
#  for i in range(1,11):
#     print(f"{int(a)} X {i}= {int(a)*i}")
# except Exception:
#     print("Invalid input")
# print("Some lines of code")
# print("End of program")

try:
    num = int(input("Enter an integere"))
    a = [6,3]
    print(a[num])
except ValueError:
    print("NUmber entered is not an integer")
    
except IndexError:
    print("index error")