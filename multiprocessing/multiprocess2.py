'''
#here uses a normal syncronous fnction to execute this particular application
import time
def add_500(num):
    for _ in range(500):
        time.sleep(0.0001)
        num+=5
    return num
def sub_500(num):
    for _ in range(500):
        time.sleep(0.0001)
        num+=-5
    return num

if __name__=='__main__':
    total=500
    print(total)
    total = add_500(total)
    print(total)
    total=sub_500(total)
    print(total)
   
    '''
"""
import multiprocessing
import time
import os
def add_500(num,lock):
    for _ in range(500):
        time.sleep(0.0001)
        lock.acquire()
        num.value+=5
        print(f"process executed {os.getpid()}")
        lock.release()
def sub_500(num,lock):
    for _ in range(500):
        time.sleep(0.0001)
        lock.acquire()
        num.value+=-5
        print(f"process executed {os.getpid()}")
        lock.release()

if __name__=='__main__':
    total=multiprocessing.Value('i',500)
    lock = multiprocessing.Lock()
    add_process=multiprocessing.Process(target=add_500,args=(total,lock))
    sub_process=multiprocessing.Process(target=sub_500,args=(total,lock))
    add_process.start()
    sub_process.start()
    add_process.join()
    sub_process.join()
    print(total.value)
    """
    