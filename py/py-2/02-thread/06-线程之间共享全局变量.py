import threading
import time

# 
my_list = []

def add_data():
    for i in range(5):
        my_list.append(i)
        print('add data: ', i)
        time.sleep(.2)
    
    print("write_data:", my_list)

def read_data():
    print('my_list: ', my_list)


if __name__ == '__main__':
    add_thread = threading.Thread(target=add_data)

    read_thread = threading.Thread(target=read_data)

    add_thread.start()
    add_thread.join()

    print('start read data: ')
    read_thread.start()