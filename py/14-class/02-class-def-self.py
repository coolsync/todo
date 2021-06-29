# def class
class Washer():
    def wash(self):
        print('wash 衣服')
        print(self)

# create obj
haire = Washer()    # 

# call obj method
print(haire)

haire.wash()


""" 
<__main__.Washer object at 0x7f4f2160a7c0>
wash 衣服
<__main__.Washer object at 0x7f4f2160a7c0>
"""


# 由于打印对象和打印self得到的内存地址相同，所以self指的是调用该函数的对象