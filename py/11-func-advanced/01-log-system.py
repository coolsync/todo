# 需求：进⼊入系统显示系统功能界⾯面，功能如下：
# 添加学员
# 删除学员
# 修改学员信息
# 查询学员信息
# 显示所有学员信息
# 退出系统
# 系统共6个功能，⽤用户根据⾃自⼰己需求选取。

def print_info():
    print('*'*20)
    print('Welcome enter employess manage system:')
    print('1: Add employee')
    print('2: Delete employee')
    print('3: Modify employee info')
    print('4: Query employee info')
    print('5: Show All employee info')
    print('6: Exit')
    print('*'*20)

# store all users
info = []

# Add
def add_info():
    """ Add employee function """
    # 1 recieve user input
    new_id = input('Please input id: ')
    new_name = input('Please input name: ')
    new_tel = input('Please input phone: ')

    global info
    
    # 2 handle user exists
    for i in info:
        if new_name == i['name']:
            print('user already exists!')
            return

    # 3 handle user not exists, dict, list
    info_dict = {}

    info_dict['id'] = new_id
    info_dict['name'] = new_name
    info_dict['tel'] = new_tel

    info.append(info_dict)
    print(info)

while True:
    # 显示功能界⾯面
    print_info()

    # 用户输⼊功能序号
    input_num = input('Please you choice: ')

    # 根据用户输⼊的功能序号，执行不同的功能
    if input_num == '1':
        add_info()
    elif input_num == '2':
        print('Delete employee')
    elif input_num == '3':
        print('Modify employee info')
    elif input_num == '4':
        print('Query employee info')
    elif input_num == '5':
        print('Show All employee info')
    elif input_num == '6':
        print('Exit')
    else:
        print('Input error, please re-enter!!!')