#create a program capable of displaying question to the user like kbc
# use list data type to store the questions and their correct answers
# display the final amount the person is taking home after playing the game
question = [["which language was used to create fb?","python","french","javascript","php","None",4],
        ["which language was used to create fb?","python","french","javascript","php","None",4],
        ["which language was used to create fb?","python","french","javascript","php","None",4],
        ["which language was used to create fb?","python","french","javascript","php","None",4],
        ["which language was used to create fb?","python","french","javascript","php","None",4],
        ["which language was used to create fb?","python","french","javascript","php","None",4],
        ["which language was used to create fb?","python","french","javascript","php","None",4],
        ["which language was used to create fb?","python","french","javascript","php","None",4],
        ["which language was used to create fb?","python","french","javascript","php","None",4],
        ["which language was used to create fb?","python","french","javascript","php","None",4],
        ["which language was used to create fb?","python","french","javascript","php","None",4],
        ["which language was used to create fb?","python","french","javascript","php","None",4],
        ["which language was used to create fb?","python","french","javascript","php","None",4],
        ["which language was used to create fb?","python","french","javascript","php","None",4],
        ["which language was used to create fb?","python","french","javascript","php","None",4],
        ["which language was used to create fb?","python","french","javascript","php","None",4],
        ["which language was used to create fb?","python","french","javascript","php","None",4],
        ["which language was used to create fb?","python","french","javascript","php","None",4],
        ["which language was used to create fb?","python","french","javascript","php","None",4],
        ["which language was used to create fb?","python","french","javascript","php","None",4],
        ]

levels = [1000,2000,4000,8000,15000,50000,100000,150000,500000,10000000,200000000,500000000,7.500000]
money = 0
for i in range (0,len(question)):
    ques = question[i]
    print(f"Question for Rs, {levels[i]}")
    print(f"a.{ques[1]}     b.{ques[2]} ")
    print(f"c.{ques[3]}     d.{ques[4]} ")
    reply = int(input("Enter your answer(1-4)"))
    if(reply == ques[-1]):
        print(f"correct answer ,you have won Rs.{levels[i]}")
        if(i==4):
            money = 10000
    elif(i==9):
        money = 320000
    elif(i==14):
        money = 10000000
    else:
        print("wrong answer")
        break
print(f"your take home money is {money}")