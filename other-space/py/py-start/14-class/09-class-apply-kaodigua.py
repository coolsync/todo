
class SweetPotato():
    def __init__(self) -> None:
        self.cook_time = 0
        self.cook_state = '生的'
        self.cook_condiments = []   # 调料
        
    def cook(self, time):
        self.cook_time += time

        if 0 <= self.cook_time < 3:
            self.cook_state = '生的'
        elif 3 <= self.cook_time < 5:
            self.cook_state = '半生的'
        elif 5 <= self.cook_time < 8:
            self.cook_state = '熟的'
        elif self.cook_time >= 8:
            self.cook_state = '烤户了'

    def add_condiments(self, condiment):
        self.cook_condiments.append(condiment)

    def __str__(self) -> str:
        return f'sweetpotato cook time: {self.cook_time}, cook state: {self.cook_state}， condiments： {self.cook_condiments}'

digua1 =  SweetPotato()
print(digua1)

digua1.cook(2)
digua1.add_condiments('酱油')
print(digua1)

digua1.cook(2)
digua1.add_condiments('辣椒')
print(digua1)

