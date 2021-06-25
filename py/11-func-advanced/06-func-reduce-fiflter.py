# reduce(func(x,y)，lst)
# 每次func计算的结果继续和序列列的下⼀一个元素做累积计算
# 需求：计算 list1 序列列中各个数字的累加和。
import functools

l1 = [1, 2, 3, 4, 5]


def fn1(x, y):
    return x + y


r1 = functools.reduce(fn1, l1)

print(r1)  # 15

# ﬁlter(func, lst)函数⽤用于过滤序列列, 过滤掉不不符合条件的元素, 返回⼀一个 ﬁlter 对象,。如果要转换为列列表, 可以使用 list() 来转换。
l2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def fn2(x):
    return x % 2 == 0


r2 = filter(fn2, l2)

print(r2)  # <filter object at 0x7f1d51a33fa0>
print(list(r2))  # [2, 4, 6, 8, 10]
