import threading
import time

class SleepyWorkers(threading.Thread):
    def __init__(self, seconds, **kwargs):
        super(SleepyWorkers, self).__init__(**kwargs)
        self._seconds = seconds
        self.start()

    def _sleep_a_little(self, seconds):
        time.sleep(seconds)

    def run(self):
        self._sleep_a_little(self._seconds)
