import threading
import time
import requests
def activity():
    # for e in range(1000000):
    #     abs(round(e ** 2 / 122) + e * 3.14)
    requests.get("https://yandex.ru")

def run(threaded=False):
    start = time.time()
    if not threaded:
        for e in range(10):
            activity()
    else:
        threads = [threading.Thread(target=activity, daemon=True) for _ in range(10)]
        for e in threads:
            e.start()
        for e in threads:
            e.join()
    end = time.time()
    print(f'Time: {end - start} seconds')

if __name__ == '__main__':
    run(threaded=True)