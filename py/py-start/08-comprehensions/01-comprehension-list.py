# 1. 循环实现；2. 列表推导式(化简代码；创建或控制有规律的列表)
"""
1.1 创建空列表
1.2 循环将有规律的数据写入到列表
"""

# nil list
l1 = []

# while
# i = 0
# while i < 10:
#     l1.append(i)
#     i += 1
# print(l1)   # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# for
# for i in range(10):
#     l1.append(i)

# print(l1)

# comprehension
l1 = [i for i in range(10)]
print(l1)