import threading
import time

def show_info():
    for i in range(5):
        print('show: ', i)
        time.sleep(.2)

if __name__ == '__main__':
    show_thread = threading.Thread(target=show_info)
    # Guarding the main thread 2
    show_thread.daemon = True
    
    # Guarding the main thread 1
    # show_thread = threading.Thread(target=show_info, daemon=True)

    show_thread.start()

    time.sleep(.5)
    print('over')


# 主线程 等待 所有子线程执行后 再结束

# Guarding the main thread destroy sub thread