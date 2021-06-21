d1 = {'name': 'bob', 'age': 18, 'gender': 'man'}

# key值 find
# print(d1['name'])
# print(d1['id'])   # keyError: 'id'

# get
print(d1.get('name'))
print(d1.get('id', 100))    # temp id, value is 100
print(d1.get('id'))     # None

# keys
print(d1.keys())    # dict_keys(['name', 'age', 'gender'])


# values
print(d1.values())  # dict_values(['bob', 18, 'man'])

# items
print(d1.items())   # # dict_items([('name', 'bob'), ('age', 18), ('gender', 'man')])
