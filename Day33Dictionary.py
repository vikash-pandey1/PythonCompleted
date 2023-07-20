# dic = {
#     "vikash":"human being",
#     "spoon":"object"
# }
# print(dic["vikash"])

dic = {
    23: "vikash", # here 23 is key and vikash is value
    24:" vinay",
    34:"rahul"
}
# print(dic.get(38)) # it is also use to print value but if keys is not found it will not give error
# print(dic[34]) # use to print value through key if key not found it will give error
# print(dic)  # use to print all keys and value
# print(dic.keys()) # use to print all keys 
# print(dic.values()) # use to print all value 
# for key in dic.keys(): # use to print key and value through loop 
#     print(f"The value corresponding to the key {key} us {dic[key]}")
print(dic.items())
for key,Value in dic.items():
    print(f"The value corresponding to the key {key} is {Value}")