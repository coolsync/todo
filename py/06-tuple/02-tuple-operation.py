t1 = ('aa', 'bb', 'cc', 'bb')

# 1 subscript
print(t1[0])

# 2 index
print(t1.index('bb'))
# print(t1.index('bbb'))    # ValueError: tuple.index(x): x not in tuple

# 3 count
print(t1.count('bb')) # 2
print(t1.count('bbb')) # 0

# 4 len
print(len(t1))
