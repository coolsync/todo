# 2 主进程会等待所有的子进程执行结束再结束

import multiprocessing
import time


def task():
    for i in range(5):
        print('task runing')
        time.sleep(.2)

    print('task process end')
    

if __name__ == '__main__':
<<<<<<< HEAD
    task_process = multiprocessing.Process(target=task)
=======
    # task_process = multiprocessing.Process(target=task)
    task_process = multiprocessing.Process(target=task, daemon=True)
>>>>>>> tmp
    task_process.start()

    time.sleep(.5)
    print('main over')
    
    # sub process destroy
<<<<<<< HEAD
    task_process.terminate()
=======
    # task_process.terminate()
>>>>>>> tmp

    exit()


    # 总结： 主进程会等待所有的子进程执行完成以后程序再退出

    # 如果想要 主进程退出, 子进程销毁，可以 设置守护主进程或者在主进程 退出之前 让子进程销毁


""" 
[dart@localhost 01-network]$ python 06-process-notice2.py 
task runing
task runing
task runing
main over
task runing
task runing
task process end

[dart@localhost 01-network]$ python 06-process-notice2.py 
task runing
task runing
task runing
main over
"""