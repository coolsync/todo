# 类外面添加和获取对象属性

class Washer():
    def wash(self):
        print('wash something')

w1 = Washer()

# add
w1.width = 400
w1.height = 500

# get
print(f'washer width: {w1.width}, height: {w1.height}')
