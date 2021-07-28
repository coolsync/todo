# import process module
import multiprocessing
import time

# task
def dance():
    for i in range(3):
        print('danceing ... ')
        time.sleep(.2)

def sing():
    for i in range(3):
        print('singing ... ')
        time.sleep(.2)


# task process
if __name__ == '__main__':
    dance_process = multiprocessing.Process(target=dance)
    sing_process = multiprocessing.Process(target=sing)

    dance_process.start()
    sing_process.start()