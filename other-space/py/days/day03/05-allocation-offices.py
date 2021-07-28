import random

# def offices list
offices = [[],[],[]]

# def employees list
employees = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

# traver employees, allocation offices by randomint generate index 
for emp in employees:
    num = random.randint(0,2)
    offices[num].append(emp)

# print info
print(offices)

for i, office in enumerate(offices):
    print(f'office {i}: {len(office)}, in office emp:')
    for emp in office:
        print(emp, end=' ')
        print()