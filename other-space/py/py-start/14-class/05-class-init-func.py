# 目标： 定义init魔法方法设置初始化属性 并访问调用

class Washer():
    def __init__(self) -> None:
        # add instance property
        self.width = 400
        self.height = 500

    def print_info(self):
        print(f'washer width: {self.width}, height: {self.height}')
        

w1 = Washer()

w1.print_info()