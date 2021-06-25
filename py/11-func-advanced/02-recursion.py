# 3以内数字累加和
# 3 + 2 + 1


def sum_nums(n):
    # 1.如果是1，直接返回1 -- 出⼝
    if n == 1:
        return 1
    
    # 2.如果不是1，重复执⾏行行累加:
    r = n + sum_nums(n-1)

    # 3.返回累加结果
    return r

n = sum_nums(3)
print(n)