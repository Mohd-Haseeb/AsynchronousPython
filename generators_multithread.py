def countdown(n):
    while n > 0:
        yield n
        n -= 1

obj = countdown(2)
obj2 = countdown(5)
# print(next(obj))
# print(f"obj2 -> {next(obj2)}")
# print(next(obj))

# print(f"obj2 -> {next(obj2)}")
# print(f"obj2 -> {next(obj2)}")
# print(f"obj2 -> {next(obj2)}")
# print(next(obj))


tasks = [countdown(10), countdown(5), countdown(3)]

while tasks:
    task = tasks[0]
    tasks.remove(task)
    try:
        num = next(task)
        print(num)
        tasks.append(task)
    except StopIteration:
        print(f"Task Finished For {task}")

# This is an Example of Multitasking without using THREADS