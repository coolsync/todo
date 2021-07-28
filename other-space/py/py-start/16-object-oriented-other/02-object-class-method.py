class Dog(object):
    __tooth = 10
    @classmethod
    def get_tooth(cls):
        return cls.__tooth

    @staticmethod
    def print_info():   # can not write self
        print('this is dog class, statice method!')


wang = Dog()

r = wang.get_tooth()
print(r)
print(Dog.get_tooth())

wang.print_info()
Dog.print_info()