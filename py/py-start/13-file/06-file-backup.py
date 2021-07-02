import sys

# input file name   sound.txt.mp3
old_name = input('Please input file name: ')

# make new file
index = old_name.rfind('.')
# print(old_name[:index])
# print(old_name[index:])

# invalid file
if index == 0:
    print('file name is invalid!')
    sys.exit(1)

new_name = old_name[:index] + '[backup]' + old_name[index:]
print(new_name)

# open file
old_f = open(old_name, 'rb')    # read binary
new_f = open(new_name, 'wb')

# write file
while True:
    con = old_f.read(1024)
    if len(con) == 0:
        break
    new_f.write(con)

# close file
old_f.close()
new_f.close()