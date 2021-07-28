# 需求：创建0-10的偶数列列表

l1 = []

# step impl
# l1 = [i for i in range(0, 10, 2)]
# print(l1)   # [0, 2, 4, 6, 8]

# if impl
l1 = [i for i in range(10) if i % 2 == 0]
print(l1)