Processes and threads are two important aspects of how a computer works.

__Process__ : Program under execution.

    - Different stages of a process :
        1. New state -> Program is converted into process
        2. Ready state -> Process is in memory; Readu Queue waiting for CPU
        3. Running state -> CPU is allocated to the process
        4. Waiting state -> Waiting for I/O to complete.
        5. TErminated -> Process completed.

__Concurrency__ : Ability to execute multiple instructions at the same time.

__Thread__ : 
- Single sequence stream within a process.
- Light weight process
- Used to achieve parallelism by dividing a process's tasks which are independent path of execution.


- Each computer has number of cores, processor(Cpu). THESE PROCESORS HAVE NO OF CORES AND REASONABLY INDEPENDENT.

- EACH CORE IS  a unit that performs mathematical operations.

- Each core is responsioble for runnig one thing at a time.

- If we compare with Dining Philosophers Problems, waiting philospher is a waiting Thread, that do not have enough forks(cores) to eat(process).

- A thread in computing is a line of code execution. A python prgram can run in a single thread.

- One thread can run in one core at a time.

- Process : A process is not something that runs. Thread is what runs on the cores. Process a wrapper around the thread. 

- Priocess has atleast one thread in it. PLus some resources set aside by the OS.
EG : Cores (but could also be netrwork , hard drive, file prointers.)


- A thread is that runs and process is what that manages the resources that are needed to run a thread.

- The resources continuously changes as the process' needs change.

- Process is just a wrapper around the Thread and the processes they need

- Say; in the philosophers problem, we have 5 CORES and each philosopher needs two reaources(forks) to run. So, they need two cores. We have 5 philosophers sitting on the table.  So, now we have two philosophers running and one core is idle because it doesn't have enough reosuces(fork).

- Now, say we have 2 threads and 2 cores running. All is good -> These two threads can run forever.

- These 2 threads could belong to same or different process. Lets say these two threads are for displaying on the monitor and using mouse. What if we have 5 more threda in the waiting line (keybord, printer, touchpad, etc). To tackle thus, we have to perform __Time Slicing__.,else the waitiing threads will starve.

- Time Slicing : Moving one thread from the core and adding aother one form the waiting list. it is not free by the way. The operating system has to save the current status of the thread so that when it comes back to the core, it soesn't start from the beginning.

## PYTHON GIL :

-   Global Interpreter lock
-   When we launch a python app(VIA VSCODE), we get a new python process.
-  That means we are getting atleast one thread with it.
-   In python, we get one starting thread(main thread), but we can make more.
-   Given that we know only a single thread can run in a core at once, what is the benefit of making more/
-   Due to how Python is implemented, we cannot run two threads in one process at the same time.
-   Each porcess in python creates a key resource. When a thread is running, it must acquire that reosuce.
-   Since there is only one of that, only one thread can run in a process at once.
-   The resouces the process is creating, is called __GIL__. THIS IS the resource thread must must acquire. 
-   What about Mutiple Pythoms? We can do that.
    - Each process in Python creates its own GIL.
    - Each process creates one thread.
    - But they cannot easilt share data (e.g have the same variables)

### So whats the point of __threads__  in python? Python allows to create multiple threads but they cannot run simultaneoulsy.

- If we use threds, they make the program slow and cannot run at the same time.
- Lets say a program does two things
    1. A complex mathematical operation (Thread takes long time because its a compelx operation)
    2. Ask the user for some input and themn greet them (May take long time becvause the user mayy take long time to type)

- So, in a singe thread, we can do these two operations instead of using two threads.
- Thread performing a mathematical operation, whenever the user interrupts for typing input. Threads take the inpout and then continues the mathematical oeration.
-  ***COOPERATIVE MULTITASKING***

- ![Alt text](https://www.digikey.bg/maker-media/ad878381-74bb-43ef-9b9b-2eb149d179df)

- Here, yiels means releasing the GIL.

-So back to our question. Whats the point of threads in Python > __Reducing Waiting Time__.

- If all the threads are doing things, multiple threads won't help in Pytbon.

-The OS will give priority to threads that are doing things, so if a thread is waiting it will run less frequently.


### DON'T KILL THREADS IN PYTHON

- If we kill it before it releases the GILL, the GILL is gone. No other thread can catch the GILL. Program will STOP, but wont be TERMINATED. -> __DEAD LOCK__ 


## MULTIPROCESSING IN PYTHON

- We can launch multiple processes in Python. Each process has it's own threads and running in its own Cores.
- So, two processes will be entirey separated from one another.
- As part of doing that, we can also set p communication betrween the processes. THis communication can be slow, but we can run two things at he same time.

- Normally, we use Processes(Multiple) when we have multiple cores on our machine and we have to perform complex calculations on both.

- For operations like __USER INPUT__, where we have to wait, We should use __Multi Threading__, but large complex operations, we use __MUlti Processing__.



## ATOMIC OPERATIONS:

- An Atomic Operation is something, thta cannot be interrupted in the middle of execution.
- It should be fininshed before the thread is unplugged for the Core and replaced with another Thread.

- Ex : Print Statement cannot be interrupted in the middle, Appending to DEQUE cannot be interrupted half way through.


## NON Locked Threads

- If we want operations to happen sequentillay. Simple, don't use threads.
- If we want operations to happen sequentially and also want to use Multi threading with a common __SHARED STATE__, may be a counter. Then we have to use complex __QUEUING SYSTEM__. 

- When we need threads to share __STATES__, we need __QUEUES__.


## Using Python __GENERATORS__ for doing multiple things without using __THREADS_.
- Parallelism is actually doing things simultaneously. In Python we cannot do that.
- In __GENERATORS__, we are using to suspend the task temporarily, and bring it back at some point in future. Ex: When user enetrs input, when can yield the complex mathematical oeprations and print user input and then go back to the COmplex Operation.


## How to __YIELD__ from another __ITERATOR__
- Ex : yield_two_way.py

## Receiving data through YIELD:
- Receiving through yield is what makes __Asynchronnous__ Python Programming Possible.
- Ex : receiving_through_yield.py
- ***THIS IS HOW PYTHON ASYNCRONOUS DEVELOPMENT RUNS INSIDE***

- More Info on Couroutines and Concurency -> [Source1](https://www.youtube.com/watch?v=MCs5OvhV9S4) AND  [Source2](https://www.youtube.com/watch?v=Z_OAlIhXziw)


## ASYNC_AWAIT

- To reduce the compexity of "__yield from generator__", async-await syntax is introduced.

## LEARNING SOURCERS FOR MORE DETAILS ;
[Source 1](https://www.youtube.com/watch?v=MCs5OvhV9S4)

[Source 2](https://www.youtube.com/watch?v=Z_OAlIhXziw)

[Source 3](https://www.youtube.com/watch?v=ZzfHjytDceU)

[Source 4](https://www.youtube.com/watch?v=9zinZmE3Ogk)

[Source 5](https://www.youtube.com/watch?v=Obt-vMVdM8s)

[Source 6](https://www.javatpoint.com/python-asynchronous-programming-asyncio-and-await)





