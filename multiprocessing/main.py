import time
from multiprocessing import Process



def sum_of_squares(n):
    total = 0
    for i in range(n):
        total += i * i

if __name__ == '__main__':
    num_processes = 4
    n = 10**7

    start_time = time.time()
    processes = []
    for i in range(num_processes):
        t = Process(target=sum_of_squares, args=(n,))
        processes.append(t)

    for t in processes:
        t.start()

    for t in processes:
        t.join()

    print("Everything took:", time.time() - start_time, "seconds")
