import os
import threading
import time
from multiprocessing import Queue
from threading import Thread
from tkinter import *
from tkinter import ttk

def waiting(timeout):
    while timeout > 0:
        timeout -= 1
        time.sleep(1)
    print('Ok')

def thread_wait(timeout):
    thread = Thread(target=waiting, args=(timeout,), daemon=True)
    thread.start()
    return thread

def info():
    pid = os.getpid()
    name = threading.current_thread().name
    print(f"Process {pid}, name {name}")

counter = [0]
lock = threading.Lock()

def inc():
    lock.acquire()
    c = counter[0]
    time.sleep(0.1)
    counter[0] = c + 1
    lock.release()

queue = Queue()
queue.put(0)

def inc_queue():
    c = queue.get()
    time.sleep(0.1)
    queue.put(c+1)


if __name__ == '__main__':
    # tk = Tk()
    # button1 = ttk.Button(tk, text="WAIT", command=lambda: waiting(3))
    # button1.pack(side=LEFT)
    # button2 = ttk.Button(tk, text="THREAD", command=lambda: thread_wait(3))
    # button2.pack(side=LEFT)
    # tk.mainloop()
    #threads = [Thread(target=inc, daemon=True) for _ in range(100)]
    #threads = [Thread(target=info, daemon=True) for _ in range(10)]
    #threads = [Thread(target=lambda :waiting(5), daemon=False) for _ in range(3)]
    threads = [Thread(target=inc_queue, daemon=True) for _ in range(100)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    #info()
    #print(counter)
    print(queue.qsize())
    print(queue.get_nowait())