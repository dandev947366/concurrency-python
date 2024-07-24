import time
import threading

def calculate_sum_square(n):
    sum_square = 0
    for i in range(n):
        sum_square += i ** 2
    print(sum_square)

def sleep_a_little(seconds):
    time.sleep(seconds)

def main():
    calc_start_time = time.time()
    calc_threads = []
    for i in range(5):
        maximum_value = (i + 1) * 1000000
        t = threading.Thread(target=calculate_sum_square, args=(maximum_value,))
        t.start()
        calc_threads.append(t)
        
    for t in calc_threads:
        t.join()
        
    print('Calculating sum of square took:', round(time.time() - calc_start_time, 3))
    
    sleep_start_time = time.time()
    sleep_threads = []
    
    for seconds in range(1, 6):
        t = threading.Thread(target=sleep_a_little, args=(seconds,))
        t.start()
        sleep_threads.append(t)
        
    for t in sleep_threads:
        t.join()
        
    print('Sleep took:', round(time.time() - sleep_start_time, 3))

if __name__ == "__main__":
    main()
