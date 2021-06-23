list1 = [10, 20, 30, 20, 40, 50]
set1 = {100, 300, 200, 500}   # set
t1 = ('a', 'b', 'c', 'd', 'e')

# 1. tuple(): 转换成元组
print(tuple(list1))
print(tuple(set1))
# print(tuple(t1))


# 2. list()：转换成列表
print(list(set1))
print(list(t1))


# 3. set()：转换成集合
print(set(list1))
print(set(t1))

# 1. 集合可以快速完成列表去重
# 2. 集合不支持下标