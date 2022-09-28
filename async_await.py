from collections import deque
from types import coroutine


friends = deque(('ROSS', 'RACHEL', 'CHANDLER', 'JOEY', 'MONICA', 'PHOEBE'))


@coroutine
def friend_lower():
    while friends:
        friend = friends.popleft().lower()
        greeting = yield
        print(f"{greeting} {friend}")

# In above generator we are receiving data, not generating. They are called COROUTINE GENERATOR


async def greet(g): # async tells function, it can avoid COROUTINEs
    await g

greeter = greet(friend_lower())

greeter.send(None)
greeter.send("Hello")
print("MultiTasking is ON!!!")
greeter.send("How you doing ??")