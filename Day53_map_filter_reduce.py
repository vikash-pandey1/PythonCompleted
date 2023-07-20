from functools import reduce

# reduce
l = [1,2,3,4,5]
sum = reduce(lambda x,y:x+y,l)
print(sum)

# map
# def cube(x):
#     return x*x*x
# print(cube(2))

# l = [1,2,4,6,4,3]
# newl = list(map(cube,l))
# print(newl)
# double = map(lambda x: x*2,l)
# print(list(double))

# filter
#l = [1,2,4,6,4,3]
# def filter_function(a):
#     return a>3
# newl = list(filter(filter_function,l))
   #or
#newl = list(filter(lambda x:x>2,l))
#print(newl)
