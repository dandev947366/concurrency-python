import time
from workers.WikiWorker import WikiWorker
from workers.YahooFinanceWorker import YahooFinanceWorker

def main():
    scraper_start_time = time.time()
    
    # Initialize WikiWorker
    wiki_worker = WikiWorker()
    
    # Fetch S&P 500 company symbols
    sp_500_symbols = wiki_worker.get_sp_500_companies()
    
    # Create and start YahooFinanceWorker threads
    current_workers = []
    for symbol in sp_500_symbols:
        worker = YahooFinanceWorker(symbol=symbol)
        worker.start()
        current_workers.append(worker)
        
    # Wait for all threads to complete
    for worker in current_workers:
        worker.join()
    
    print('Extracting time took: ', round(time.time() - scraper_start_time, 1))

if __name__ == "__main__":
    main()
