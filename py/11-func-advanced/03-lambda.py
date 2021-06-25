# function
def fn1():
    return 200

# print(fn1)      # <function fn1 at 0x7f6bd1571160>
# print(fn1())    # 200

fn2 = lambda: 100

# print(fn2)      # <function <lambda> at 0x7fab9391e0d0>
# print(fn2())    # 100

# 计算a + b
def add(a, b):
    return a + b

r = add(1,2)
print(r)

print((lambda a, b: a+b)(1, 2))

# not param
print((lambda: 100))    # <function <lambda> at 0x7f12ef5f81f0>
print((lambda: 100)())  # 100

# a param
print((lambda a: a)('hello'))

# default param
print((lambda a, b, c=200: a+b+c)(10,20))

# 可变参数：**args
print((lambda *args: args)(10,20,30))   # (10, 20, 30)

print((lambda **keyword_agrs: keyword_agrs)(name="bob", age=20))    # {'name': 'bob', 'age': 20}