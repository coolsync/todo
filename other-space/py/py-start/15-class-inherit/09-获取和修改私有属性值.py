# basic
class Master(object):
    def __init__(self) -> None:
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
        # self.money = 20000000000        # publice property
        self.__money = 20000000000        # private property

    ####################################
    def get_money(self):
        return self.__money

    def set_money(self):
        self.__money = 500    
    ####################################
    
    def __print_info(self):              # private method
        print('this is private method')

    
    def make_cook(self):
        print(f'use {self.kongfu} make')

    def master_make_cook(self):
        Master.__init__(self)
        Master.make_cook(self)
    
    def school_make_cook(self):
        School.__init__(self)
        School.make_cook(self)


class Tusun(Prentice):
    pass

t = Tusun()

print(t.get_money())

t.set_money()

print(t.get_money())
