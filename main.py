import time
from workers.SleepyWorkers import SleepyWorkers
from workers.SquaredSumWorkers import SquaredSumWorker

def main():
    calc_start_time = time.time()
    calc_workers = []
    for i in range(5):
        maximum_value = (i + 1) * 1000000
        squared_sum_worker = SquaredSumWorker(n=maximum_value)
        calc_workers.append(squared_sum_worker)
        
    for worker in calc_workers:
        worker.join()
        
    print('Calculating sum of square took:', round(time.time() - calc_start_time, 3))
    
    sleep_start_time = time.time()
    sleep_workers = []
    
    for seconds in range(1, 6):
        sleepy_worker = SleepyWorkers(seconds=seconds)
        sleep_workers.append(sleepy_worker)
        
    for worker in sleep_workers:
        worker.join()
        
    print('Sleep took:', round(time.time() - sleep_start_time, 3))

if __name__ == "__main__":
    main()
