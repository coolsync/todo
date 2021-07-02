import threading
import time

def dance():
    print('dance current thread: ', threading.current_thread())
    for i in range(3):
        print('-----dance %d' % i)
        time.sleep(.2)


def sing():
    print('sing current thread: ', threading.current_thread())
    for i in range(3):
        print('sing %d' % i)
        time.sleep(.1)

    

if __name__ == '__main__':
    # create thread
    dance_thread = threading.Thread(target=dance)
    sing_thread = threading.Thread(target=sing)


    dance_thread.start()
    sing_thread.start()