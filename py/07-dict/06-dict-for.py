d1 = {'name': 'bob', 'age': 18, 'gender': 'man'}

# key
for key in d1.keys():
    print(key)

# value
for val in d1.values():
    print(val)

# 遍历字典的元素
for item in d1.items():
    print(item)

# traverse dict key and value
for k, v in d1.items():
    print(f'{k}:{v}')