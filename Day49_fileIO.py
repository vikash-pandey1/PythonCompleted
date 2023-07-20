# for read the data
# f = open('myfile.txt','r')
# #print(f)
# text = f.read()
# print(text)
# f.close()

# for write the data from file
# f = open('myfile.txt','w')
# f.write("added")
# f.close()

# for append the data in file

f = open('myfile.txt','a')
f.write(" append data")
f.close()

with open('myfile.txt','r') as f:
        text =f.read()
        print(text)
        

