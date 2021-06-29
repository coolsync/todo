# 当删除对象时，python解释器器也会默认调⽤用 __del__() ⽅方法。

class Washer():
    def __init__(self) -> None:
        self.width = 200

    def __del__(self):      # after call class end, auto call
        print('obj del')

h1 = Washer()

print(h1)

""" 
<__main__.Washer object at 0x7f8dbaaa5820>
obj del
"""