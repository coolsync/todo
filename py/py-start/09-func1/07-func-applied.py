# 打印图形
# 打印⼀条横线
def print_line():
    print('-'*20)

# print_line()

# 打印多条横线
def print_lines(num):
    i = 0
    while i < num:
        print_line()
        i+=1

# print_lines(5)

# 求三个数之和
def sum(x, y, z):
    return x + y + z

print(sum(1, 2, 3))

# 求三个数平均值
def nums_avg(x, y, z):
    return (x +y +z) / 3

print(nums_avg(1, 2 ,3))