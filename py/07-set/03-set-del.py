# remove()，删除集合中的指定数据，如果数据不存在则报错。
s1 = {10, 20}
s1.remove(10)
# print(s1)

# s1.remove(10)   # KeyError: 10
# print(s1)


# discard()，删除集合中的指定数据，如果数据不存在也不会报错。
s2 = {10, 20}
s2.discard(10)
# print(s2)

s2.discard(10)  # ok
# print(s2)

# pop()，删除集合中的 max data，并返回这个数据。
s3 = {10, 20, 30, 40, 50}
del_num = s3.pop() 
print(del_num)  # 50
print(s3)       # 20, 40, 10, 30}