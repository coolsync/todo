name_list = ['bob', 'mark', 'paul']

# del, pop, remove, clear

# del name_list     # result: name 'name_list' is not defined
# del name_list[0]    # ['mark', 'paul']

# del_name = name_list.pop()    # paul
# del_name = name_list.pop(1)     # mark
# print(del_name) 

# name_list.remove('mark')

name_list.clear()   # []

print(name_list)    