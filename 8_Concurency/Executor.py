import threading
import time
from concurrent.futures import ThreadPoolExecutor

import requests
def activity():
    requests.get("https://yandex.ru")
    print("OK")
def run(threaded=False):
    start = time.time()
    if not threaded:
        for e in range(10):
            activity()
    else:
        executor = ThreadPoolExecutor()
        for _ in range(10):
            executor.submit(activity)
        executor.shutdown(wait=True)
    end = time.time()
    print(f'Time: {end - start} seconds')

if __name__ == '__main__':
    run(threaded=True)