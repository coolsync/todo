def a1():
    print('-'*10)
    print('this a1 func')
    print('-'*10)


def a2():
    print('-'*20)
    print('this a2 func')
    a1()
    print('-'*20)

a2()