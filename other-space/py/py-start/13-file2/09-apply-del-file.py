# 需求1：把code文件夹所有文件重命名 Python_xxxx
# 需求2： 删除Python_ 重命名：1， markup option variable: flag, 2. if

import os
# 1. list cond dir all dir and file
file_list = os.listdir()

flag = 2

# 2. construct new name
for i in file_list:
    # add prefix
    if flag == 1:
        new_name = 'Python_' + i
    # del prefix
    elif flag == 2:
        n = len('Python_')
        new_name = i[n:]
        
# 3. rename operation
    os.rename(i, new_name)
