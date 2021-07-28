# Location parameter

def user_info(name, password):
    print(f'your name: {name}, password: {password}')

# user_info('bob', '123456')

# keyword parameter
user_info(password='123', name='paul')

# default parameter
def user_info2(name, password='123'):
    print(f'your name: {name}, password: {password}')


user_info2('mark')
user_info2('jerry', password='456')


print('-'*20)

# variable parameter
# 可变参数

# 1 包裹位置传递
def user_info3(*args):
    print(args)

user_info3('mark', '32')    # ('mark', '32')


# 2 包裹关键字传递
def user_info4(**keyword_agrs):
    print(keyword_agrs)

user_info4(name="paul", password="123")     # dict, {'name': 'paul', 'password': '123'}


