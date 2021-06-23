# enumerate(可遍历对象, start=0)
# 注意：start参数⽤来设置遍历数据的下标的起始值，默认为0。
# 用于将⼀个可遍历的数据对象(如列表、元组或字符串)组合为⼀个索引序列，一般⽤在 for 循环当中。

list1 = ['a', 'b', 'c', 'd', 'e']

# for i in enumerate(list1):
#     print(i)

for i in enumerate(list1, start=1):
    print(i)

# enumerate 返回结果是元组，
# 元组第一个数据是原迭代对象的数据对应的下标，
# 元组第二个数据是原迭代对象的数据

