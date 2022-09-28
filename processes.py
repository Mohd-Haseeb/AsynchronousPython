import time
from multiprocessing import Process

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

# start = time.time()
# ask_user()
# complex_operation()
# print(f"Single thread -> {time.time() - start}")

# PROCESSESs

process = Process(target=complex_operation)
process2 = Process(target=complex_operation)

if __name__ == '__main__':

    start = time.time()
    ask_user()
    complex_operation()
    print(f"Single thread -> {time.time() - start}")



    process.start()
    # process2.start()

    strt_time = time.time()

    ask_user()

    process.join()
    # process2.join()

    print(f"Two threads -> {time.time() - strt_time}")


# Enter your name -> l
# Hello l
# ask_user -> 0.4793999195098877
# Started ...
# Endd...
# complex_operation -> 4.319948673248291
# Single thread -> 4.7994208335876465

# Enter your name -> Started ...
# l
# Hello l
# ask_user -> 1.066141128540039
# Endd...
# complex_operation -> 4.24382710456848
# Two threads -> 4.272367238998413


# IF WE RUN TWO COMPLEX OPERATION PROCESSES SIMULTANEOUSLY
# O/P:

# Started ...
# Started ...
# Endd...
# complex_operation -> 4.519514083862305
# Endd...
# complex_operation -> 4.54771423339
# Two threads -> 4.573629140853882