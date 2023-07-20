# seek
# with open('myfile.txt','r') as f:
#     print(type(f))
#     f.seek(10) # skip till 10 and write
#     data = f.read(5)
#     print(data)
    
# tell 
# with open('myfile.txt','r') as f:
#     print(type(f))
#     f.seek(10) # skip till 10 and write
#     print(f.tell())
#     data = f.read(5)
#     print(data)

# truncate
with open('myfile.txt','w') as f:
    f.write('hello java')
    f.truncate(7)
    
with open('myfile.txt','r') as f:
    print(f.read())
