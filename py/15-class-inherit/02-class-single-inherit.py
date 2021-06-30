# basic
class Master(object):
    def __init__(self) -> None:
        # super().__init__()
        self.make_some = "Master cook method"

    def make_cook(self):
        print(f'use {self.make_some} make')

# derived
class Prentice(Master):
    pass

p = Prentice()

# visit instance property
print(p.make_some)

# visit instance method
p.make_cook()
