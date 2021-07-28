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

# store all emps
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

# delete
def del_info():
    """ delete emp info function """

    while True:
            # input emp id
        del_id = int(input('please input need delete emp id: '))

        global info

        # handle user exists
        if 0 <= del_id < len(info):
            
            del_flag = input('You sure you want to delete it? yes or no: ')
            
            if del_flag == 'yes':
                del info[del_id]
                
                print(info)

                break
        # handle user not exists
        else:
            print('The emp input is wrong, please re-enter!')

# modify
def modify_info():
    while True:
        # user input modify info[] index
        modify_num = int(input('Please enter the emp to be modified: '))

        global info

        if 0 <= modify_num < len(info):
            # handle user exists
            print(f'employee id: {info[modify_num]["id"]}, name: {info[modify_num]["name"]}, tel: {info[modify_num]["tel"]}')

            # Unterminated expression in f-string; missing close brace
            new_id = input('Please input id: ')
            new_name = input('Please input name: ')
            new_tel = input('Please input phone: ')

            info[modify_num]['id'] = new_id
            info[modify_num]['name'] = new_name
            info[modify_num]['tel'] = new_tel

            print(info)
            break
        # handle user not exists
        else:
            print('The emp input is wrong, please re-enter!')
     
# Query
def search_info():
    """ search emp info func """
    name_info = input('Please input looking for emp name: ')  

    # handle user exists
    for i in info:
        if name_info == i['name']:
            print(f'The emp id: {i["id"]}, name: {i["name"]}, tel: {i["tel"]}')
            break
    # handle user not exists
        else:
            print('Not this emp ... ')

# Show All employee info
def print_all_info():
    print('id\tname\ttel')
    for emp in info:
        print(f'{emp["id"]}\t{emp["name"]}\t{emp["tel"]}')


while True:
    # 显示功能界⾯面
    print_info()

    # 用户输⼊功能序号
    input_num = input('Please you choice: ')

    # 根据用户输⼊的功能序号，执行不同的功能
    if input_num == '1':
        add_info()
    elif input_num == '2':
        # print('Delete employee')
        del_info()
    elif input_num == '3':
        # print('Modify employee info')
        modify_info()
    elif input_num == '4':
        # print('Query employee info')
        search_info()
    elif input_num == '5':
        # print('Show All employee info')
        print_all_info()
    elif input_num == '6':
        # print('Exit')
        quit_flag = input('Are you sure you want to quit? yes or no: ')
        if quit_flag == 'yes':
            break
    else:
        print('Input error, please re-enter!!!')