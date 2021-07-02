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
    def __init__(self) -> None:
        self.kongfu = "Self create cook method"

    def make_cook(self):
        print(f'use {self.kongfu} make')

r = Prentice()

# visit instance property
print(r.kongfu)

# visit instance method
r.make_cook()

print(Prentice.__mro__)

""" 
Self create cook method
use Self create cook method make

(<class '__main__.Prentice'>, <class '__main__.Master'>, <class '__main__.School'>, <class 'object'>)


"""
