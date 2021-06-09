
# price = input('please input 苹果 price:')

# weight = input('please input 苹果 重量：')

# result = float(price) + float(weight)

# print(f"apple 单价: {price}, app weight: {weight}, total price: {result}")

pi = 3.14
num = int(pi)
print(type(pi))
print(type(num))

num6 = eval('10')
num7 = eval('1.1')

print(type(num6))
print(type(num7))

num8 = eval('num7')
print(type(num8), num8)




""" 
Traceback (most recent call last):
  File "/home/dart/todo/Py/day01/07-type-convert.py", line 6, in <module>
    result = float(price) + float(weight)
ValueError: could not convert string to float: 'dfh'
 """