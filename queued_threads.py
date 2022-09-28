import time
import random
import queue

from threading import Thread


counter = 0
job_queue = queue.Queue() # things to be printed out
counter_queue = queue.Queue() # amounts by which `counter` should be increased.


def increment_manager():
    global counter
    while True:
        increment = counter_queue.get() # this will lock the thread and dosen't sharee the resource with anyone. This waits until an item is available and then locks the thread
        old_counter = counter
        counter = old_counter + increment
        time.sleep(random.random())
        job_queue.put((f"New Counter Value is : {counter}", "----------"))
        time.sleep(random.random())
        counter_queue.task_done() # this will unlock the thread. And the resource is shared


Thread(target=increment_manager, daemon=True).start()

def print_manager():
    while True:
        time.sleep(random.random())
        for line in job_queue.get():
            print(line)
        
        job_queue.task_done()


Thread(target=print_manager, daemon=True).start()

def increment_counter():
    counter_queue.put(1)

# these are thethreads, wheere the target is the increment counter.
worker_threads = [Thread(target=increment_counter) for thread in range(10)]

for t in worker_threads:
    time.sleep(random.random())
    t.start()

for t in worker_threads:
    t.join()

counter_queue.join()
time.sleep(random.random())
job_queue.join()


# Even if we add random time.sleep(), output will still be in sequrntiual. Becvause we are locking the threads.


