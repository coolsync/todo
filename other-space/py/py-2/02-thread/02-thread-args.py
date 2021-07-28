import threading
import time


def task(n):
    for i in range(n):
        print('task run %d' % i)
        time.sleep(.2)

    print('task end')

if __name__ == '__main__':
    task_thread = threading.Thread(target=task, args=(5,))  # the form of tuple

    task_thread.start()