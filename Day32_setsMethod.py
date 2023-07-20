s = {4,36,6,3,2}
s1 = {3,63,634,3}
print(s)
print(s.union(s1))
print(s.intersection(s1))
print(s.update(s1))
print(s)
print(s.isdisjoint(s1))
print(s.issuperset(s1))
item = s.pop()
print(item)
print(s.clear())