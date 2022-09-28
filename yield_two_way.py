from collections import deque

friends = deque(('ROSS', 'RACHEL', 'CHANDLER', 'JOEY', 'MONICA', 'PHOEBE'))

def get_friend():
    yield from friends


obj_friend = get_friend()

# print(next(obj_friend))
# print(next(obj_friend))
# print(next(obj_friend))

def greet(g):
    while True:
        try :
            friend = next(g)
            yield f"Hello, {friend}"
        except StopIteration:
            pass
    
friends_geenrator = get_friend()

g = greet(friends_geenrator)

print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))