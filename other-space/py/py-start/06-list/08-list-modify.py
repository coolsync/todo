name_list = ['bob', 'mark', 'paul']

name_list[0] = 'hello'
print(name_list)    # ['hello', 'mark', 'paul']

list1 = [1, 3, 2, 5, 4]

# reverse
list1.reverse()
# print(list1)

# sort
list1.sort()    # [1, 2, 3, 4, 5]
list1.sort(reverse=True)    # [5, 4, 3, 2, 1]
print(list1)
