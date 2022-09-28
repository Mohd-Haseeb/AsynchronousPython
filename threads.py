import time
from concurrent.futures import ThreadPoolExecutor

# ThreadPoolExecutor is a Bunch of threads without anyy Target

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


thread_start = time.time()

with ThreadPoolExecutor(max_workers=2) as pool:
    pool.submit(complex_operation)
    pool.submit(ask_user)

print(f"Two threads -> {time.time() - thread_start}")