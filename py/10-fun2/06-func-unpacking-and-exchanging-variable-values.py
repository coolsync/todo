
# 1. 拆包：tuple
def return_num():
    return 10, 20   # result is tuple

n1, n2 = return_num()
print(n1, n2)

# 拆包：dick
d1 = {'name': 'bob', 'age': 18}

a, b = d1

print(a, b)     # name age: key

print(d1[a], d1[b]) # bob 18: value


# 2 交换变量值
# 需求：有变量a = 10和b = 20，交换两个变量的值。

# method 1
c = 0

a = 10
b = 20

c = a
a = b
b = c

print(a, b)

# method 2
a, b = 1, 2
a, b = b, a
print(a, b)