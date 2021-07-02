
# 1. read
from os import readlink


f = open('t1.txt', 'r')

# print(f.read()) # read all
# print(f.read(2))    # read specify file size

f.close()

# 2. readlines
f2 = open('t1.txt', 'r')
contents = f2.readlines()   

# print(contents)     # ['hello\n', 'abcdefg\n', 'aaa\n', 'bbb\n', 'ccc']

f2.close()

# 3 readline() every read a line content
f3 = open('t1.txt', 'r')
ct = f3.readline()
print(ct,  end=' ')

ct2 = f3.readline()
print(ct2,  end=' ')
f3.close()

