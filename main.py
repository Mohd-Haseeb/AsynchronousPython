import time
from threading import Thread


# print("Hello world")



def ask_user():
    start = time.time()
    user_input = input("Enter your name -> ") # This is a blocking operation
    message = f"Hello {user_input}"
    print(message)
    print(f"ask_user -> {time.time() - start}")

def complex_operation():
    start = time.time()
    print("Started ...")
    [x**2 for x in range(20000000)]
    print("Endd...")
    print(f"complex_operation -> {time.time() - start}")

start = time.time()
ask_user()
complex_operation()
print(f"Single thread -> {time.time() - start}")

thread1 = Thread(target=complex_operation)
thread2 = Thread(target=ask_user)

# Now, we have 3 three threads -> Main thread running through the applicatin, and thread1 and thread2

thread_start = time.time()

# running the threads
thread1.start()
thread2.start()



# We have to tell main thread to wait to finish the above 2 threads. We do that by join(). These are called blocking operations.
thread1.join()
thread2.join()

print(f"Two threads -> {time.time() - thread_start}")

## Output 

# Enter your name -> s
# Hello s
# ask_user -> 0.9686582088470459
# Started ...
# Endd...
# complex_operation -> 4.228470802307129
# Single thread -> 5.197185039520264
# Started ...
# Enter your name -> s
# Hello s
# ask_user -> 0.934088945388794
# Endd...
# complex_operation -> 4.188339948654175
# Two threads -> 4.188483238220215

## Lets run complex on two threads!!!



thread3 = Thread(target=complex_operation)
thread4 = Thread(target=complex_operation)

start = time.time()

thread3.start()
thread4.start()


thread3.join()
thread4.join()

print(f"Two threads time for Complex operations -> {time.time() - start}")

# Output:
# Started ...
# Started ...
# Endd...
# complex_operation -> 8.527835130691528
# Endd...
# complex_operation -> 8.683486938476562
# Two threads time for Complex operations -> 8.703208923339844


# See, it doesn't make sense here to use TWo threads. INstead it is taking more time bacause of all the TIME SLICING.

