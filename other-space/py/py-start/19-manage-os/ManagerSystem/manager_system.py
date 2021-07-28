# 系统功能
# 添加 Employee
# 删除 Employee
# 修改 Employee
# 查询 Employee 信息
# 显示所有 Employee 信息
# 保存 Employee 信息退出系统


from employee import *
# from ManagerSystem.employee import Employee


class EmployeeManager(object):
    # emp list
    def __init__(self) -> None:
        self.emps_list = []      # store emps

    # def enter function
    def run(self):
        # load emp data
        self.load_emp()

        while True:
            self.show_menu()

            n = int(input('Please you choice: '))

            if n == 1:
                self.add_emp()
            elif n == 2:
                self.del_emp()
            elif n == 3:
                self.modify_emp()
            elif n == 4:
                self.search_emp()
            elif n == 5:
                self.show_all_emps()
            elif n == 6:
                self.save_emp()
            elif n == 7:
                print('Exit')
                break

    # show menu

    @staticmethod
    def show_menu():
        print('-'*20)
        print('Welcome enter employess manage system: ')
        print('1: Add employee')
        print('2: Delete employee')
        print('3: Modify employee info')
        print('4: Query employee info')
        print('5: Show All employee info')
        print('6: Save employee info')
        print('7: Exit')
        print('-'*20)

    def load_emp(self):
        # open file, not exists, prompt the user, use 'w' open
        try:
            f = open('emps.data', 'r')
        except:
            print('load emps.data failed, create!')
            f = open('emps.data', 'w')
        else:
            # read data to list
            data = f.read()

            new_list = eval(data)   # convert str to list

            print(new_list)

            # convert dict in list to object data, use lambda collect object to self list 
            self.emps_list = [Employee(i['name'], i['gender'], i['tel']) for i in new_list] 

        finally:
            f.close() 

    def add_emp(self):  # add
        name = input("Please input name: ")
        gender = input("Please input gender: ")
        tel = int(input("Please input tel: "))

        # create emp obj
        emp = Employee(name, gender, tel)

        # save emp obj to list
        self.emps_list.append(emp)

        # print info
        print(self.emps_list)
        print(emp)

    def del_emp(self):
        del_name = input('Please input delete emp name: ')

        # exists and not exists
        for i in self.emps_list:
            if i.name == del_name:
                self.emps_list.remove(i)
                break
            else:
                print('No such employee')

        print(self.emps_list)

    def modify_emp(self):
        modify_name = input('Please input modify emp name: ')

        # exists and not exists
        for i in self.emps_list:
            if i.name == modify_name:
                print(f'emp origin info: {i.name}, {i.gender}, {i.tel}\n')

                i.name = input('modify name: ')
                i.gender = input('modify gender: ')
                i.tel = int(input('modify tel: '))

                print(f'emp modify ok: {i.name}, {i.gender}, {i.tel}\n')

                break
            else:
                print('No such employee')

        print(self.emps_list)

    def search_emp(self):
        search_name = input('Please input search emp name: ')

        for i in self.emps_list:
            if i.name == search_name:
                print(f'emp info: name: {i.name}, gender: {i.gender}, tel: {i.tel}\n')
                break
            
            else:
                print('No such Employee!')
        print(self.emps_list)

    def show_all_emps(self):
        print('\tname\tgender\ttel')
        for i in self.emps_list:
            print(f'\t{i.name}\t{i.gender}\t{i.tel}')

    def save_emp(self):
        # open file
        f = open('emps.data', 'w')

        # wirte file, use the form of dict,
        new_list = [i.__dict__ for i in self.emps_list]
        
        f.write(str(new_list))

        # close file
        f.close()

        print('save ok!')

# emp_mgr = EmployeeManager()

# emp_mgr.show_menu()
