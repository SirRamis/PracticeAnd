import time
import requests
import threading

def activ():
    print("Запрос отправлен")
    requests.get("http://google.com")
    print(requests.get("http://google.com").status_code)
def run():
    start = time.time()
    threads = threading.Thread(target=activ, daemon=True)
    # for e in threads:
    #     e.start()
    # for e in threads:
    #     e.join()
    end = time.time()
    print(end - start)


if __name__ == '__main__':
    run()