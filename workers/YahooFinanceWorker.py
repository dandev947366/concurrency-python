import threading
import requests
from lxml import html
import time
import random

class YahooFinanceWorker(threading.Thread):
    def __init__(self, symbol, **kwargs):
        super(YahooFinanceWorker, self).__init__(**kwargs)
        self._symbol = symbol
        base_url = "https://finance.yahoo.com/quote/"
        self._url = f'{base_url}{self._symbol}'
        
    def run(self):
        # Random delay to avoid hitting the server too frequently
        time.sleep(20 * random.random())
        
        try:
            response = requests.get(self._url)
            response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
        except requests.exceptions.RequestException as e:
            print(f'Error fetching data for {self._symbol}: {e}')
            return
        
        if response.status_code == 404:
            print(f'{self._symbol}: Symbol not found on Yahoo Finance.')
            return
        
        page_contents = html.fromstring(response.text)
        price_elements = page_contents.xpath('//*[@id="nimbus-app"]/section/section/section/article/section[1]/div[2]/div[1]/section/div/section/div[1]/fin-streamer[1]/span')
        
        if price_elements:
            try:
                price = float(price_elements[0].text)
                print(f'{self._symbol}: {price}')
            except (ValueError, IndexError) as e:
                print(f'Error parsing price for {self._symbol}: {e}')
        else:
            print(f'{self._symbol}: Price element not found on the page.')
