import threading
import requests
from lxml import html
import time
import random
import queue  # Use the standard queue library

class YahooFinanceWorker:
    def __init__(self, symbol):
        self._symbol = symbol
        self._base_url = "https://finance.yahoo.com/quote/"
        self._url = f'{self._base_url}{self._symbol}'
        
    def get_price(self):
        # Random delay to avoid hitting the server too frequently
        time.sleep(20 * random.random())
        
        try:
            response = requests.get(self._url)
            response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
        except requests.exceptions.RequestException as e:
            print(f'Error fetching data for {self._symbol}: {e}')
            return None
        
        if response.status_code == 404:
            print(f'{self._symbol}: Symbol not found on Yahoo Finance.')
            return None
        
        page_contents = html.fromstring(response.text)
        price_elements = page_contents.xpath('//*[@id="nimbus-app"]/section/section/section/article/section[1]/div[2]/div[1]/section/div/section[1]/div[1]/fin-streamer[1]/span')  # Updated XPath
        
        if price_elements:
            try:
                price = float(price_elements[0].text)
                return price
            except (ValueError, IndexError) as e:
                print(f'Error parsing price for {self._symbol}: {e}')
                return None
        else:
            print(f'{self._symbol}: Price element not found on the page.')
            return None

class YahooFinancePriceScheduler(threading.Thread):
    def __init__(self, input_queue, **kwargs):
        super(YahooFinancePriceScheduler, self).__init__(**kwargs)
        self._input_queue = input_queue
        self.start()
        
    def run(self):
        while True:
            symbol = self._input_queue.get()
            if symbol == 'DONE':
                self._input_queue.task_done()  # Signal that the task is done
                break
            
            worker = YahooFinanceWorker(symbol)
            price = worker.get_price()
            if price is not None:
                print(f'{symbol}: {price}')
                
            self._input_queue.task_done()  # Signal that the task is done
            time.sleep(random.random())
