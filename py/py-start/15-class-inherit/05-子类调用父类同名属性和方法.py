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

    def master_make_cook(self):
        Master.__init__(self)
        Master.make_cook(self)
    
    def school_make_cook(self):
        School.__init__(self)
        School.make_cook(self)


r = Prentice()
print(r.kongfu)

r.make_cook()           # use Self create cook method make

r.master_make_cook()

r.school_make_cook()

r.make_cook()           # use School cook method make

""" 
Self create cook method
use Self create cook method make
use Master cook method make
use School cook method make
use School cook method make
"""

