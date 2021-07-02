import random
# 1. ready data
emps = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

offices = [[],[],[]]

# 2. allocation offfices
for name in emps:
    num = random.randint(0, 2)
    offices[num].append(name)
    

# print(offices)

# 3. validation results
i = 1
for office in offices:
    print(f'office id: {i} number is: {len(office)}, Respectively are:')
    
    for name in office:
        print(name)
    i += 1