import time
from workers.WikiWorker import WikiWorker
from workers.YahooFinanceWorker import YahooFinanceWorker

def main():
    scraper_start_time = time.time()
    
    wikiWorker = WikiWorker()
    current_workers = []
    for symbol in WikiWorker.get_sp_500_companies():
        YahooFinanceWorker = YahooFinanceWorker(symbol=symbol)
        current_workers.append(YahooFinanceWorker)
        
    for i in range(len(current_workers)):
        current_workers[i].join()
    print('Extracting time took: ', round(time.time() - scraper_start_time, 1))