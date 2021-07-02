import threading
import time


g_num = 0

def sum1():
    for i in range (100000):
        global g_num
        g_num += 1
        
    print('g_num: ', g_num)

def sum2():
    for i in range (100000):
        global g_num
        g_num += 1
        
    print('g_num: ', g_num)


if __name__ == '__main__':
    first_thread = threading.Thread(target=sum1)
    secode_thread = threading.Thread(target=sum2)

    first_thread.start()

    # lock
    first_thread.join()
    
    secode_thread.start()
