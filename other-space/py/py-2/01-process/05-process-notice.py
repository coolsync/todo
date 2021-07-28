
# 1 进程之间不共享全局变量


import multiprocessing
import time

g_list = []

def add_data():
    # global g_list

    for i in range(3):
        g_list.append(i)
        print('add data: ', i)
        time.sleep(.2)

    print('add data end: ', g_list)

def read_data():
    print('read data: ', g_list)


if __name__ == '__main__':
    add_process = multiprocessing.Process(target=add_data)

    read_process = multiprocessing.Process(target=read_data)

    add_process.start()
    add_process.join()      # wait add data process end

    read_process.start()

    print('main: ', g_list)


  # 总结: 多进程之间不共享全局变量