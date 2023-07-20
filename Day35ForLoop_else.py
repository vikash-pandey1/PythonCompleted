# as you have learned before, the else clause is used along with the if statement
for i in range(5):
    print(i)
    i=i+1
    if i ==4: # here else statement will not print because loop is not completed , when loop is completed then else statement is print
        break
    
else:
    print("sorry no i")