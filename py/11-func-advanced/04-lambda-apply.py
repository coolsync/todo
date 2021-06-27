# 带判断的lambda
print((lambda a, b: a if a > b else b)(1000,500))

# 列表data按字典key的值排序
emps = [
    {'name': 'mark', 'age': 32},
    {'name': 'paul', 'age': 27},
    {'name': 'bob', 'age': 30},
]

emps.sort(key=(lambda x: x['name']))
print(emps)

emps.sort(key=lambda x: x['name'], reverse=True)
print(emps)

emps.sort(key=lambda x: x['age']) 
print(emps)

# r: 
# [{'name': 'bob', 'age': 30}, {'name': 'mark', 'age': 32}, {'name': 'paul', 'age': 27}]
# [{'name': 'paul', 'age': 27}, {'name': 'mark', 'age': 32}, {'name': 'bob', 'age': 30}]
# [{'name': 'paul', 'age': 27}, {'name': 'bob', 'age': 30}, {'name': 'mark', 'age': 32}]
