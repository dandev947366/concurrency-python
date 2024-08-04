'''
Lock in python
Source: https://docs.python.org/3/library/threading.html#lock-objects
'''
import threading
from threading import Lock

lock = Lock()
x = 0

def increment():
    global x
    lock.acquire()
    x = x + 1
    lock.release()
    
def operation():
    for _ in range(100000000):
        increment()
        
        
t1 = threading.Thread(target=operation, name="Thread #1")
t2 = threading.Thread(target=operation, name="Thread #2")

t1.start()
t2.start()
t1.join()
t2.join()

print('The value of x: ' + str(x))