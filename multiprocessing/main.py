import time
from multiprocessing import Process, Queue

def check_value_in_list(x, i, num_of_processes, queue):
    max_num_to_check = 10**8
    lower = int(i * max_num_to_check / num_of_processes)
    upper = int((i + 1) * max_num_to_check / num_of_processes)
    number_of_hits = 0
    for j in range(lower, upper):
        if j in x:
            number_of_hits += 1
    queue.put((lower, upper, number_of_hits))

if __name__ == '__main__':
    num_processes = 4
    comparision_list = [1, 2, 3]
    comparision_set = set(comparision_list)  # Using a set for faster lookup
    queue = Queue()

    start_time = time.time()
    processes = []
    for i in range(num_processes):
        t = Process(target=check_value_in_list, args=(comparision_set, i, num_processes, queue))
        processes.append(t)

    for t in processes:
        t.start()

    for t in processes:
        t.join()

    queue.put('DONE')

    while True:
        v = queue.get()
        if v == 'DONE':
            break
        lower, upper, number_of_hits = v
        print("Between", lower, "and", upper, "we have", number_of_hits)

    print("Everything took:", time.time() - start_time, "seconds")
