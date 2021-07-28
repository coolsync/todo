import threading
import time

def task():
    time.sleep(1)
    print('Current Thread: ', threading.current_thread().name)


if __name__ == '__main__':

    for _ in range(5):
        tast_thread = threading.Thread(target=task)
        tast_thread.start()

# r: 
""" 
Current Thread:  Thread-1
Current Thread:  Thread-5
Current Thread:  Thread-2
Current Thread:  Thread-3
Current Thread:  Thread-4
"""