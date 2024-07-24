import time 

def calculate_sum_square(n):   
    sum_square = 0
    for i in range(n):
        sum_square += i **2
        
    print(sum_square)
    
def sleep_a_little(seconds):
    time.sleep(seconds)
    
def main():
    calc_start_time = time.time()
    for i in range(5):
        calculate_sum_square(i)
        
    print('Calculating sum of square took: ', round(time.time() - calc_start_time))
    
    sleep_start_time = time.time()
    for i in range(1,6):
        sleep_a_little(i)
    print('Sleeping time took: ', round(time.time() - sleep_start_time))
if __name__ == "__main__":
    main()