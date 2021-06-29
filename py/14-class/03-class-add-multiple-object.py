class Washer():
    def wash(self):
        print('wash something')
        print(self)

w1 = Washer()
w1.wash()

w2 = Washer()
w2.wash()

"""
wash something
<__main__.Washer object at 0x7f777496a7c0>
wash something
<__main__.Washer object at 0x7f777490a100>
"""