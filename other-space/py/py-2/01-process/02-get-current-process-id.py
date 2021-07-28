import multiprocessing
import time
import os


def dance():
    print('dance: ', os.getpid())       # 获取当前进程的编号
    print('dance ', multiprocessing.current_process())     # 获取当前进程
    print("dance parent's process id: ", os.getppid())
    for i in range(3):
        print('----------dance...')
        time.sleep(.2)
        os.kill(os.getpid(), 9)


def sing():
    print('sing: ', os.getpid())            # 获取当前进程的编号
    print('sing ', multiprocessing.current_process())   # 获取当前进程
    print("dance parent's process id: ", os.getppid())

    for i in range(3):
        print('sing...')
        time.sleep(.2)


if __name__ == '__main__':
    print('main: ', os.getpid())
    print('main: ', multiprocessing.current_process())
    dance_process = multiprocessing.Process(target=dance)
    sing_process = multiprocessing.Process(target=sing)

    dance_process.start()
    sing_process.start()
