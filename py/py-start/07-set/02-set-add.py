

# add 
# s1 = {10, 20}
# s1.add(100)
# s1.add(10)
# print(s1)       # {100, 10, 20}

# update 追加的数据是序列。
s1 = {10, 20}
# s1.update(100)  # TypeError: 'int' object is not iterable 可迭代的
# s1.update([100,200])   # {100, 10, 20, 200}
s1.update('abcd')       # {'a', 10, 'c', 'd', 'b', 20}
print(s1)      

