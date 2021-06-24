# 如果一个func has two return ，程序如何执⾏？

def return_num():
    return 1
    return 2

print(return_num()) # 1

# 如果一个func 有多个返回值，该如何书写代码？

def return_num2():
    return 1, 2

print(return_num2()) # (1, 2)

# 注意：
# 1. return a, b 写法，返回多个数据的时候，默认是元组类型。
# 2. return后⾯面可以连接列列表、元组或字典，以返回多个值。