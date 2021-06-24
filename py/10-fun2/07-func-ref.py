# 在python中，值是靠引⽤用来传递来的。
# 可以⽤用 id() 来判断两个变量量是否为同⼀一个值的引⽤用

# 1 int type
a = 1
b = a

# print(b)

print(id(a))    # 139830412888368
print(id(b))    # 139830412888368

a = 2
# print(b)    # 1     说明int类型 为不可变类型

print(id(a))    # 139830412888400   # 此时得到是的数据2的内存地址
print(id(b))    # 139830412888368

# 2 list
l1 = [10, 20]
l2 = l1

print(id(l1))   # 140524472930240
print(id(l2))   # 140524472930240

l1.append(30)
print(l2)      # [10, 20, 30] list is multable type

print(id(l1))   # 140524472930240
print(id(l2))   # 140524472930240


