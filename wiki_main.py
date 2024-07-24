import time
from workers.WikiWorker import WikiWorker
from workers.YahooFinanceWorker import YahooFinanceWorker, YahooFinancePriceScheduler
import queue

def main():
    symbol_queue = queue.Queue()
    scraper_start_time = time.time()
    
    # Initialize WikiWorker
    wiki_worker = WikiWorker()
    
    # Fetch S&P 500 company symbols
    symbols = wiki_worker.get_sp_500_companies()
    
    # Create and start the scheduler thread
    yahoo_finance_price_scheduler_threads = []
    num_threads = 8  # Number of threads to run concurrently (adjust as needed)
    
    for _ in range(num_threads):
        scheduler = YahooFinancePriceScheduler(input_queue=symbol_queue)
        yahoo_finance_price_scheduler_threads.append(scheduler)
    
    # Add symbols to the queue
    for symbol in symbols:
        symbol_queue.put(symbol)
    
    # Add 'DONE' markers to signal threads to stop
    for _ in range(num_threads):
        symbol_queue.put('DONE')
    
    # Wait for all threads to finish
    for thread in yahoo_finance_price_scheduler_threads:
        thread.join()
    
    print('Extracting time took: ', round(time.time() - scraper_start_time, 1))

if __name__ == "__main__":
    main()
    # Wait for all threads to finish
    for thread in yahoo_finance_price_scheduler_threads:
        thread.join()
    
    print('Extracting time took: ', round(time.time() - scraper_start_time, 1))

if __name__ == "__main__":
    main()
