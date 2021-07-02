class Emp(object):
    def __init__(self, name, value) -> None:
        self.name = name
        self.value = value


emps_list = []

e1 = Emp('bob', 11)
e2 = Emp('paul', 22)
e3 = Emp('mark', 33)

emps_list.append(e1)
emps_list.append(e2)
emps_list.append(e3)

# print(emps_list)  # [<__main__.Emp object at 0x7fc1fcac8fd0>, <__main__.Emp object at 0x7fc1fcac8f70>, <__main__.Emp object at 0x7fc1fcac8ee0>]

new_list = [i.__dict__ for i in emps_list]

print(new_list)     # [{'name': 'bob', 'value': 11}, {'name': 'paul', 'value': 22}, {'name': 'mark', 'value': 33}]

print(type(new_list))   # <class 'list'>

print(str(new_list))        # [{'name': 'bob', 'value': 11}, {'name': 'paul', 'value': 22}, {'name': 'mark', 'value': 33}]

print(type(str(new_list))) # <class 'str'>



