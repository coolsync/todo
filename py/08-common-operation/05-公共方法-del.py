s1 = 'abcdefg'

l1 = [10, 20, 30, 40, 50]

t1 = (10, 20, 30, 40, 50)

set1 = {'a', 'b', 'c', 'd', 'e'}

d1 = {"name": "bob", "age": 30}

# str
# del(s1)
# print(s1)   # NameError: name 's1' is not defined

# list
# del(l1)
del(l1[0])
print(l1)

# tuple
# del(t1)
print(t1)

# set
#del(set1)
print(set1)

# dict
# del(d1)
del(d1['name'])
print(d1)