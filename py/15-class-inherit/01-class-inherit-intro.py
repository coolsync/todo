# def basic class
class A(object):
    def __init__(self) -> None:
        self.num = 1

    def print_info(self):
        print(self.num)

# def derived class
class B(A):
    pass

r = B()

r.print_info()  # 1
