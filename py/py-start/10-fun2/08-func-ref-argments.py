def f(a):
    print(a)
    print(id(a))

    a += a

    print(a)
    print(id(a))

# int：计算前后id值不不同
b = 1
f(b)

# # 列列表：计算前后id值相同
list1 = [10, 20]
f(list1)
