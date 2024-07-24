import threading

class SquaredSumWorker(threading.Thread):
    def __init__(self, n, **kwargs):
        super(SquaredSumWorker, self).__init__(**kwargs)
        self._n = n
        self.start()

    def calculate_sum_square(self, n):
        sum_square = 0
        for i in range(n):
            sum_square += i ** 2
        print(sum_square)

    def run(self):
        self.calculate_sum_square(self._n)
