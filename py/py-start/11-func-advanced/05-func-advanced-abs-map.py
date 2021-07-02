# 需求：⼀一个函数完成计算任意两个数字的绝对值之和

def add_nums(a, b):
    return abs(a) + abs(b)

print(add_nums(-1, 2))

# 2
def add_nums2(a, b, f):
    return f(a) + f(b)

print(add_nums2(-1, 2, abs))
print(abs)  # <built-in function abs>

# map()
l1 = [1, 2, 3, 4, 5]    


def fn(x):
    return x ** 2

r = map(fn, l1)

print(r)    # <map object at 0x7f4a99867fa0>
print(list(r))  # [1, 4, 9, 16, 25]




