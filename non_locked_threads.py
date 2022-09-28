from threading import Thread
import time
import random

# Global variable
count = 0

def increase_count():
    global count
    count += 1
    print(f"Incremented value of count : {count}")
    print('---------------')

def increase_count_sleep():
    global count
    time.sleep(random.random())
    count += 1
    time.sleep(random.random())
    print(f"Incremented value of count : {count}")
    time.sleep(random.random())
    print('---------------')

# running on single thread
# for i in range(10):
#     increase_count()

# running on multiple threads
# for i in range(10):
#     t = Thread(target=increase_count)
#     t.start()
    # same output as in single thread. No difference
    # Whats happeing here is, by the time we go to create a new thread, previous thread is already finihsed ezexuting increase_count()
    # So they are happening one after another.

# so, to visualize all the threads running si,ultaneously. Add time.sleep() in functions lines
# running on multiple threads
for i in range(10):
    t = Thread(target=increase_count_sleep)
    time.sleep(random.random())
    t.start()

# Multi threaded code with shared state is very complicated. We can see in above example, count value is same for few threads.