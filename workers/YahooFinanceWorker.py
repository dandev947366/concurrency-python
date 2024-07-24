import threading

class YahooFinanceWorker(threading.Thread):
    def __init__(self, symbol, **kwargs):
        super(YahooFinanceWorker, self).__init__(**kwargs)
        
        self.start()
        
    def run(self):
        pass