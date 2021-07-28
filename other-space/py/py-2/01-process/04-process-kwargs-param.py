import multiprocessing
import time

def task(count):
    for i in range(count):
        print('task run')
        time.sleep(.2)
    else:
        print('task end')


if __name__ == '__main__':
    task_process = multiprocessing.Process(target=task, kwargs={"count": 3})
    task_process.start()

# kwargs={"count", 3}   note: ,
# TypeError: cannot convert dictionary update sequence element #0 to a sequence