# 共⽤全局变量

glo_num = 0

def test1():
    global glo_num
    glo_num = 100

def test2():
    print(glo_num)

test1() # must be first call
test2()

# return value work for other func params 传递
def test3():
    return 50

def test4(num):
    print(num)

r = test3()

test4(r)

test4(test3())

