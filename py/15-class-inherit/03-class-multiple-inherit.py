# basic
class Master(object):
    def __init__(self) -> None:
        # super().__init__()
        self.kongfu = "Master cook method"

    def make_cook(self):
        print(f'use {self.kongfu} make')


class School(object):
    def __init__(self) -> None:
        self.kongfu = "School cook method"

    def make_cook(self):
        print(f'use {self.kongfu} make')

    

# derived
class Prentice(Master, School):
    pass

p = Prentice()

# visit instance property
print(p.kongfu)

# visit instance method
p.make_cook()

""" 
Master cook method
use Master cook method make

注意：当⼀个类有多个⽗类的时候，默认使用第⼀个⽗类的同名属性和⽅法
"""