import multiprocessing
import time


def task(count):
    for i in range(count):
        print('run task')

    else:
        print('task end')    

if __name__ == '__main__':
    task_process = multiprocessing.Process(target=task, args=(5, ))

    task_process.start()