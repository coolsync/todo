class Employee(object):
    # name, gender, tel
    def __init__(self, name, gender, tel) -> None:
        self.name = name
        self.gender = gender
        self.tel = tel

    def __str__(self) -> str:
        return f'{self.name}, {self.gender}, {self.tel}'


# aa = Employee('aa', 'man', 193)
# print(aa)