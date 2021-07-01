# 如果⼀个模块文件中有 __all__ 变量，
# 当使⽤ from xxx import * 导⼊时，只能导⼊入这个列表中的元素。

__all__ = ['testA']

def testA():
    print('testA')

def testB():
    print('testB')