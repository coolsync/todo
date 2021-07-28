a = "Hello"
b = "Python"

print("a + b 输出结果：", a + b)
print("a * 2 输出结果：", a * 2)
print("a[1] 输出结果：", a[1])
print("a[1:4] 输出结果：", a[1:4]) # yth ell


if ('H' in a):
    print('a contain H')
else:
    print('a not contain H')

if ('M' not in a):
    print('a not contain M')
else:
    print('a contain M')

print(r'\n')
print(R'\n')

print('--------f-string--------')

# f-string
name = 'bob'
print('hello %s' % name)

print(f'hello {name}')
print(f'{1+2=}')

