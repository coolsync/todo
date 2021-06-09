import random

user = int(input('please input a num:'))

computer = random.randint(1, 3)

print(computer)

if user == computer:
    print('平局')
elif (user == 3 and computer == 2) or (user == 3 and computer == 1) or (user == 2 and computer == 1):
    print('user ok')
else:
    print('you guess failed')
    
