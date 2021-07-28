t1 = ('aa', 'bb', 'cc', 'bb')
# t1[0] = 'aaa'   # TypeError: 'tuple' object does not support item assignment

# print(t1)


t2 = ('aa', 'bb', ['cc', 'bb'])
print(t2[2])
print(t2[2][0])

t2[2][0] = 'mark'   # ('aa', 'bb', ['mark', 'bb'])
print(t2)

