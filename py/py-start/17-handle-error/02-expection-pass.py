# 需求1： 尝试只读打开test.txt 文件存在读取内容，不存在提示用户
# 需求2：读取内容：循环读取，当无内容的时候退出循环，如果用户意外终止，提示用户已经被意外终止

import time

try:
    f = open('t1.txt', 'r')
    try:
        while True:
            con = f.readline()
            if len(con) == 0:
                break
            time.sleep(2)
            print(con)
    except:
        print('意外终止')   # ctrl + c .etc

    finally:
        f.close()
        print('file aready close!')
        
except:
    print('no such file')