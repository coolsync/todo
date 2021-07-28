# 需求：创建列列表如下：
# [(1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

l1 = []

l1 = [(i, j) for i in range(1,3) for j in range(3)]

print(l1)