# 偶数, 能被2整除的数是偶数  num % 2 == 0
#  循环生成 1- 100 之间的数字
# 定义变量记录初始的值
my_sum = 0
i = 1
while i <= 100:
    # 先判断数字是不是偶数,如果是偶数求和
    if i % 2 == 0:
        my_sum += i  # my_sum = my_sum + i
    # 改变i的值
    i += 1

# 将代码放在循环的缩进里边.还是外边,可以思考,这行代码想让他打印输出几次,如果只输出一次,放在外边,
# 如果想要多次输出,放在里边
print('求和的结果为', my_sum)


