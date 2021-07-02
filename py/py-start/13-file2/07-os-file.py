import os

# 1. rename file
# os.rename('1.txt', '10.txt')

# 2. remove file
# os.remove('10.txt')

# 3. create dir
# os.mkdir('aa')

# 4. delete dir
# os.rmdir('aa')

# 5. 返回当前文件所在目录路径
# print(os.getcwd())          # /home/dart/todo/py/13-file2

# 6. 改变默认⽬录
# os.mkdir('aa')
# 需求：在aa里面创建bb文件夹: 1. 切换目录到aa，2创建bb
# os.chdir('aa')
# os.mkdir('bb')

# 7. 获取某个文件夹下所有文件，返回一个列表
print(os.listdir())     # ['07-os-file.py', 'aa']
print(os.listdir('./aa')) # ['bb']

# 8. rename dir
# os.mkdir('bb')
# os.rename('bb', 'bbbb')
