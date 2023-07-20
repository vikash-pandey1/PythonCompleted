import re
patten = " "
text = '''
hey my name is this and 
i am very glad to thanks to the gla university to help me to show my future and 
where i learn lot of things that help me to crack my interview and thank lot to the facutly of 
gla and other dept member

'''
# matches = re.search(patten,text)
# print(matches)

matches = re.finditer(patten,text)
for match in matches:
    print(match.span()) 
    print(text[match.span()[0]:
    match.span()[1]])