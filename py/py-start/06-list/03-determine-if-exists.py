name_list = ['bob', 'mark', 'paul']

# in
print('bob' in name_list)   # True
print('bobs' in name_list)  # Talse

# not in
print('bob' not in name_list)   # Talse
print('bobs' not in name_list)  # True


# use in email
name = input('please input name: ')

if name in name_list:
    # exists
    print('name aready exists!')
else:
    # not exists
    print('name can use')