# 1. ⾃己的文件名 不要和已有模块名 重复，否则导致 模块功能 ⽆法使用
# import random

# r = random.randint(1,5)
# print(r)

# 2. 当使用from xx import function, 导入模块的 fucntion 的时候，
# 如果function 名字重复，会导入 后定义或后导入 同名 function

# from time import sleep

# def sleep():
#     print('custom sleep function!')

# sleep(2)

# 要避免 名字重复
import time
print(time)     # <module 'time' (built-in)>

time = 1
print(time)

# 结论： data 是通过 引用传递