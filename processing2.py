from re import L
import time
from concurrent.futures import ProcessPoolExecutor

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


if __name__ == '__main__':

    start = time.time()
    ask_user()
    complex_operation()
    print(f"Single thread -> {time.time() - start}")

    start_time = time.time()

    with ProcessPoolExecutor(max_workers=2) as pool:
        pool.submit(complex_operation)
        pool.submit(complex_operation)


    print(f"Two threads -> {time.time() - start_time}")

# O/P : 

    # Enter your name -> l
    # Hello l
    # ask_user -> 0.40265512466430664
    # Started ...
    # Endd...
    # complex_operation -> 4.315800189971924
    # Single thread -> 4.718524932861328
    # Started ...
    # Started ...
    # Endd...
    # complex_operation -> 4.475466012954712
    # Endd...
    # complex_operation -> 4.475751876831055
    # Two threads -> 4.51648473739624
