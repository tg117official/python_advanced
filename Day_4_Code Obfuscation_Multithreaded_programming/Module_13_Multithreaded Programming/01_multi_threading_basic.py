# Multithreading Exercises in Python
# These exercises will help you understand and implement multithreading.

import threading
import time
from queue import Queue

# Exercise 1: Basic Threading
# Problem: Create two threads, one to print even numbers and another to print odd numbers up to 10.
# Goal: Understand how to start and join threads.
def print_even():
    for i in range(0, 11, 2):
        print(f"Even: {i}")
        time.sleep(0.5)

def print_odd():
    for i in range(1, 11, 2):
        print(f"Odd: {i}")
        time.sleep(0.5)

# Starting threads
thread1 = threading.Thread(target=print_even)
thread2 = threading.Thread(target=print_odd)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

# Exercise 2: Using Thread Locks
# Problem: Write a program where multiple threads update a shared counter, ensuring thread safety.
# Goal: Learn to use threading locks.
counter = 0
counter_lock = threading.Lock()

def increment_counter():
    global counter
    for _ in range(10):
        with counter_lock:
            counter += 1
            print(f"Counter: {counter}")
        time.sleep(0.1)

threads = [threading.Thread(target=increment_counter) for _ in range(5)]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()

# Exercise 3: Producer-Consumer Problem
# Problem: Implement a producer-consumer model using a queue.
# Goal: Understand thread communication using queues.
def producer(queue):
    for i in range(5):
        print(f"Produced: {i}")
        queue.put(i)
        time.sleep(1)

def consumer(queue):
    while True:
        item = queue.get()
        if item is None:
            break
        print(f"Consumed: {item}")
        time.sleep(2)

queue = Queue()
producer_thread = threading.Thread(target=producer, args=(queue,))
consumer_thread = threading.Thread(target=consumer, args=(queue,))

producer_thread.start()
consumer_thread.start()

producer_thread.join()
queue.put(None)  # Signal the consumer to exit
consumer_thread.join()

# Exercise 4: Multithreading with a ThreadPoolExecutor
# Problem: Use a ThreadPoolExecutor to compute squares of numbers in parallel.
# Goal: Explore high-level multithreading with ThreadPoolExecutor.
from concurrent.futures import ThreadPoolExecutor

def compute_square(n):
    print(f"Square of {n}: {n**2}")
    time.sleep(0.5)

numbers = [1, 2, 3, 4, 5]
with ThreadPoolExecutor(max_workers=3) as executor:
    executor.map(compute_square, numbers)

# Exercise 5: Daemon Threads
# Problem: Create a daemon thread that prints a message every second, while the main thread ends after 5 seconds.
# Goal: Understand the concept of daemon threads.
def background_task():
    while True:
        print("Daemon thread running...")
        time.sleep(1)

daemon_thread = threading.Thread(target=background_task, daemon=True)
daemon_thread.start()

time.sleep(5)
print("Main thread ends.")

# Summary: These exercises cover creating threads, using locks for thread safety, thread communication with queues,
# high-level threading with ThreadPoolExecutor, and daemon threads.