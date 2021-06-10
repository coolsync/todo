s1 = 'hello world and do something do simple'

s2 = s1.replace('do', 'result')
print(s1)
print(s2)


s2 = s1.replace('do', 'result', 1)
print(s1)
print(s2)

print('--------split--------')

r = s1.split('do')
print(r)

r = s1.split('do', 1)
print(r)

r = s1.rsplit('do', 1)  # ['hello world and do something ', ' simple']
print(r)

print('--------join--------')
s1 = '_'.join('hello')  # h_e_l_l_o
print(s1)

# def list
my_list = ['hello', 'cpp', 'python']
print('_'.join(my_list))
print(' '.join(my_list))
print('_*_'.join(my_list))


w = {'name': 'baidu', 'url': 'www.baidu.com'}
print(f'{w["name"]}: {w["url"]}')

