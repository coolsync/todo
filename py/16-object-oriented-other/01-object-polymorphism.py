# base class
class Animal(object):
    def __init__(self, name) -> None:
        self.name = name

    def eat(self):
        print(f'{self.name} eat')

# derived class
class Cat(Animal):
    def __init__(self, name) -> None:
        super(Cat, self).__init__(name)


class Dog(Animal):
    def __init__(self, name) -> None:
        super(Dog, self).__init__(name)

class Person():
    def feedAnimal(self, animal):
        animal.eat()

cat = Cat('Tom')

dog = Dog('dahei')

per = Person()

per.feedAnimal(cat)

per.feedAnimal(dog)
