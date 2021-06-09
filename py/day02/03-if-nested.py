
money = input('please your money:')
money = int(money)

if money >= 2:
    print('in car')
    seat = int(input('please seat num:'))
    if seat >= 1:
        print('seat')
    else:
        print('stand')
else:
    print('down car')