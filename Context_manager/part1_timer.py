import time


class Timer:
    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.end_time = time.time()
        self.elapsed_time = self.end_time - self.start_time
        print(f"Время выполнения: {self.elapsed_time:.4f} секунд")


with Timer() as timer:
    # Некоторый код, выполнение которого мы хотим измерить
    for i in range(1000000):
        pass
