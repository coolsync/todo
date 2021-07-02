# 需求1：把code文件夹所有文件重命名 Python_xxxx

import os
# 1. list cond dir all dir and file
file_list = os.listdir()

# print(file_list)

# 2. construct new name
for i in file_list:
    new_name = 'Python_' + i

# 3. rename operation
    os.rename(i, new_name)
