import threading
import time


def task(n):
    for i in range(n):
        print('task run %d' % i)
        time.sleep(.2)

    print('task end')

if __name__ == '__main__':
    task_thread = threading.Thread(target=task, kwargs={'n': 3})  # the form of dict

    task_thread.start()