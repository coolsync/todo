
class Furniture():
    def __init__(self, name, area) -> None:
        self.name = name
        self.area = area


class House():
    def __init__(self, address, area) -> None:
        self.address = address
        self.area = area
        self.free_area = area
        self.furnitures = []

    def __str__(self) -> str:
        return f'The House addr: {self.address}, area: {self.area}, free_area: {self.free_area}, furnitures: {self.furnitures}'

    def add_furniture(self, item):
        if self.free_area >= item.area:
            self.furnitures.append(item.name)
            self.free_area -= item.area
        else:
            print(f'furniture: "{item.name}" is too big, not place in house')


f1 = Furniture('bed', 10)

h1 = House('WD', 1000)
h1.add_furniture(f1)
print(h1)

f2 = Furniture('sofa', 50)
h1.add_furniture(f2)
print(h1)

f3 = Furniture('ball playgroud', 2000)
h1.add_furniture(f3)
print(h1)