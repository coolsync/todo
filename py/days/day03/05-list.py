








list1 = []
print(list1, type(list1))

list2 = list()
print(list2, type(list2))

list3 = [1, 3.14, True, 'isnice']
print(list3, type(list3))

num = len(list3)
print(num)

print(list3[1])  # 3.14
print(list3[-1])    # 'isnice'
print(list3[1:3])   # 3.14, True

list3[0] = 18
print(list3)
list3[-1] = 'hello'
print(list3)

list3[0] = 'hello'
print(list3)
""" 
Traceback (most recent call last):
  File "/home/dart/todo/py/day03/05-list.py", line 19, in <module>
    num = len(list3)
TypeError: object of type 'types.GenericAlias' has no len()

"""