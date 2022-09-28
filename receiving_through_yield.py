
from collections import deque

def greet():
    friend = yield # Here, funnction is suspended and once it is called again(next()), it sends te data to friend and prints it
    print(f"HELLO, {friend}")


# obj = greet()

# obj.send(None) # This is called PRIMING the GENERATOR -> 
# obj.send("HAseeb")

# print(next(obj))
# print(next(obj))

friends = deque(('ROSS', 'RACHEL', 'CHANDLER', 'JOEY', 'MONICA', 'PHOEBE'))

def friend_lower():
    while friends:
        friend = friends.popleft().lower()
        greeting = yield
        print(f"{greeting} {friend}")

# In above generator we are receiving data, not generating. They are called COROUTINE GENERATOR


def greet(g): #this function PRIMES the generator -> g
    g.send(None)
    while True:
        greeting = yield
        g.send(greeting)

greeter = greet(friend_lower())

greeter.send(None)
greeter.send("Hello")
print("MultiTasking is ON!!!")
greeter.send("How you doing ??")

# THIS IS HOW PYTHON ASYNCRONOUS DEVELOPMENT RUNS INSIDE