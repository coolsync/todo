"""
特点：
1. 集合可以去掉重复数据；
2. 集合数据是无序的，故不不⽀支持下标
"""

s1 = {10, 20, 30, 40, 50}
print(s1)   # {50, 20, 40, 10, 30}

s2 = {10, 20, 30, 40, 50, 30, 40, 50}   # {50, 20, 40, 10, 30}
print(s2)

s3 = set('abcdefg') 
print(s3)   # {'b', 'c', 'a', 'e', 'g', 'f', 'd'}

s4 = set()
print(s4)   # set()
print(type(s4))     # <class 'set'>

s5 = {}
print(type(s5))     # <class 'dict'>



