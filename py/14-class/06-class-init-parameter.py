class Washer():
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height

    def print_info(self):
        print(f'washer width: {self.width}, height: {self.height}')


w1 = Washer(10, 20)
w1.print_info()

w2 = Washer(100, 200)
w2.print_info()