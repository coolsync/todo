s1 = 'hello world and do something do simple'

index = s1.find('hello')
print(index)

print(s1.find('hello', 3))  # from 3 location find
print(s1.find('do'))
print(s1.find('do', 17))
print(s1.rfind('do'))

print(s1.index('hello'))
print(s1.index('do'))
print(s1.rindex('do'))

print(s1.count('aaaa'))
print(s1.count('hello'))
print(s1.count('do'))
print(s1.count('do', 20))   # from index 20 location find




