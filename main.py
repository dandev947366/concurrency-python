import time 
import threading
def calculate_sum_square(n):   
    sum_square = 0
    for i in range(n):
        sum_square += i **2
        
    print(sum_square)
    
def sleep_a_little(seconds):
    time.sleep(seconds)
    
def main():
    calc_start_time = time.time()
    current_threads = []
    for i in range(5):
        maximum_value = (i+1) *1000000
        t = threading.Thread(target=calculate_sum_square, args=(maximum_value, ))
        #calculate_sum_square(maximum_value)
        t.start()
        current_threads.append(t)
        
    for i in range(len(current_threads)):
        current_threads[i].join()
        
    print('Calculating sum of square took: ', round(time.time() - calc_start_time, 3))
    
    sleep_start_time = time.time()
    
    for seconds in range(1,6):
        t = threading.Thread(target=sleep_a_little, args=(seconds,))
        #sleep_a_little(i)
        t.start()
        current_threads.append(t)
    for i in range(len(current_threads)):
        current_threads[i].join()
        
    print('Sleep took: ', round(time.time() - sleep_start_time, 3))
    
    
if __name__ == "__main__":
    main()