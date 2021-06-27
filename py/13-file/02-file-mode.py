"""
Total:
1. 访问模式对文件的影响
2. 访问模式对write()的影响
3. 访问模式是否可以省略
"""

# r: 如果文件不存在，报错；不支持写入操作，表示只读
# f = open('t1.txt', 'r')
# f.write('world')    # io.UnsupportedOperation: not writable
# f.close()

# w：只写, 如果文件不存在，新建文件；执行写入，会覆盖原有内容
# f = open('1.txt', 'w')
# f.write('hello')
# f.close()

# a：追加，如果文件不存在，新建文件；在原有内容基础上，追加新内容
# f = open('2.txt', 'a')

# f.write('hello')
# f.close()

# omit mode, only read
f = open('1.txt')
f.close()