# basic
class Master(object):
    def __init__(self) -> None:
        # super().__init__()
        self.kongfu = "Master cook method"

    def make_cook(self):
        print(f'use {self.kongfu} make')


class School(Master):
    def __init__(self) -> None:
        self.kongfu = "School cook method"

    def make_cook(self):
        print(f'use {self.kongfu} make')
        # super(School, self).__init__()
        # super(School, self).make_cook()

        super().__init__()
        super().make_cook()

# derived
class Prentice(School):
    def __init__(self) -> None:
        self.kongfu = "Self create cook method"

    def make_cook(self):
        print(f'use {self.kongfu} make')

    def make_old_cook(self):
        # method 1
        # School.__init__(self)
        # School.make_cook(self)
        # Master.__init__(self)
        # Master.make_cook(self)

        # method 2 super
        # super(Prentice, self).__init__()
        # super(Prentice, self).make_cook()

        super().__init__()
        super().make_cook()

p = Prentice()

p.make_old_cook()