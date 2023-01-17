import multiprocessing
import os
def square(num):
    sq=num*num
    print(f"the square of the number is {sq}")
    process_id=os.getpid()
    print(f"the process id of the current processs is {process_id}")
if __name__=='__main__':
    numbers = range(1,5)
    for number in numbers:
        p=multiprocessing.Process(target=square,args=(number,))
        p.start()