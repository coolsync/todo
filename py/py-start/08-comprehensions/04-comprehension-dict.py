# 1. 创建一个字典：字典key是1-5数字，value是这个数字的2次方。

d1 = {i: i**2 for i in range(1, 5)}

print(d1)   # {1: 1, 2: 4, 3: 9, 4: 16} 

# 2. 将两个列表合并为一个字典
l1 = ['name', 'age', 'gender']
l2 = ['bob', 30, 'man']

d2 = {l1[i]: l2[i] for i in range(len(l1))}

print(d2)   # {'name': 'bob', 'age': 30, 'gender': 'man'}

# 3. 提取 dict 目标数据
counts = {'MBP': 268, 'HP': 125, 'DELL': 201, 'Lenovo': 199, 'acer': 99}

# 需求：提取上述电脑数量 >=200 的字典数据
# for
# count1 = {} 
# for k, v in counts.items():
#     if v >= 200:
#         count1[k] = v


count1 = {k: v for k, v in counts.items() if v >= 200}  

print(count1) # {'MBP': 268, 'DELL': 201}