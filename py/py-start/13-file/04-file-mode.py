
# r+
# f = open('test.txt', 'r+')
# f = open('test1.txt', 'r+')

# w+: file pointer at file start, new content conver origin content
# f = open('test.txt', 'w+')
# f = open('test1.txt', 'w+')

# a+
f = open('test.txt', 'a+')

con = f.read()
print(con)