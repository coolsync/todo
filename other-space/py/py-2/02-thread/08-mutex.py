import threading

# lock = threading.Lock     # notice: Lock()
lock = threading.Lock()

# global var
g_num = 0

def sum1():
    global g_num

    lock.acquire()      # lock
    for i in range(100000):
        g_num += i
    lock.release()      # unlock
    
    print('g_num: ', g_num)

def sum2():
    global g_num

    lock.acquire()
    for i in range(100000):
        g_num += i
    lock.release()

    print('g_num: ', g_num)


if __name__ == '__main__':
    sum1_thread = threading.Thread(target=sum1)
    sum2_thread = threading.Thread(target=sum2)

    sum1_thread.start()
    sum2_thread.start()