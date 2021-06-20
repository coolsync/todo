""" 
案例需求：
1. 通过⽤户键盘输⼊，获取年龄
2. 判断年龄是否满⾜18岁，满⾜输出 
    哥18岁了，可以进⼊⽹吧为所欲为了
3. 程序最后输出， if 判断结束 (不管是否满⾜，都会输出)
"""

age = input('Please input age:')
age = int(age)

if age >= 18:
    print('哥18岁了，可以进⼊⽹吧为所欲为了')
else:
    print('hello, 你太年轻了')

print('if end')




