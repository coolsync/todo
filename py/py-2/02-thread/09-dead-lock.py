import threading
import time

lock = threading.Lock()


def get_value(index):

    lock.acquire()
    print(threading.current_thread())
    my_list = [1, 8, 3, 6]

    if index >= len(my_list):
        print('index out bound')
        lock.release()       # the position release, avoid dead lock
        return

    value = my_list[index]
    print(value)
    lock.release()


if __name__ == '__main__':
    for i in range(30):
        sub_thread = threading.Thread(target=get_value, args=(i, ))
        sub_thread.start()
