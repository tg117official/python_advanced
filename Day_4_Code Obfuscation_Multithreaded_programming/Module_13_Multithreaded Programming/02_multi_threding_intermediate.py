# Intermediate Multithreading Exercises in Python
# These exercises build on fundamental multithreading concepts and explore more complex scenarios.

import threading
import time
from queue import Queue
from concurrent.futures import ThreadPoolExecutor

# Exercise 1: Thread Synchronization with Condition Variables
# Problem: Create a program where one thread generates numbers and another processes them, synchronized using a condition variable.
# Goal: Learn thread coordination using `threading.Condition`.
class SharedResource:
    def __init__(self):
        self.data = None
        self.condition = threading.Condition()

def producer(resource):
    for i in range(1, 6):
        with resource.condition:
            print(f"Producer generated: {i}")
            resource.data = i
            resource.condition.notify()
            resource.condition.wait()

def consumer(resource):
    for _ in range(5):
        with resource.condition:
            resource.condition.wait()
            print(f"Consumer processed: {resource.data}")
            resource.condition.notify()

resource = SharedResource()
producer_thread = threading.Thread(target=producer, args=(resource,))
consumer_thread = threading.Thread(target=consumer, args=(resource,))

producer_thread.start()
consumer_thread.start()
producer_thread.join()
consumer_thread.join()

# Exercise 2: Thread Pool with Results
# Problem: Use a thread pool to download multiple files concurrently and store their results in a dictionary.
# Goal: Work with `ThreadPoolExecutor` to manage results from multiple threads.
import random

def download_file(file_id):
    time.sleep(random.uniform(1, 3))  # Simulate download delay
    print(f"File {file_id} downloaded.")
    return f"Content of file {file_id}"

file_ids = [1, 2, 3, 4, 5]
results = {}

with ThreadPoolExecutor(max_workers=3) as executor:
    futures = {executor.submit(download_file, file_id): file_id for file_id in file_ids}
    for future in futures:
        file_id = futures[future]
        results[file_id] = future.result()

print("Downloaded Files:", results)

# Exercise 3: Parallel Search
# Problem: Implement a multithreaded search that looks for a target number in multiple segments of a large list.
# Goal: Divide a task into chunks and search in parallel using threads.
def search_segment(segment, target, result, index):
    if target in segment:
        print(f"Found {target} in segment {index}.")
        result[0] = True
    else:
        print(f"Target not in segment {index}.")

target = 42
large_list = list(range(1, 101))
segments = [large_list[i:i+20] for i in range(0, len(large_list), 20)]
result = [False]
threads = []

for i, segment in enumerate(segments):
    thread = threading.Thread(target=search_segment, args=(segment, target, result, i))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("Search Result:", "Found" if result[0] else "Not Found")

# Exercise 4: Multithreaded Logging System
# Problem: Implement a logging system where multiple threads log messages to a shared file safely.
# Goal: Use threading locks to handle file operations.
log_lock = threading.Lock()
def log_message(file_path, message):
    with log_lock:
        with open(file_path, "a") as log_file:
            log_file.write(message + "\n")

log_file_path = "threaded_log.txt"
threads = []

for i in range(5):
    thread = threading.Thread(target=log_message, args=(log_file_path, f"Log from thread {i}"))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print(f"Logs written to {log_file_path}.")

# Exercise 5: Task Scheduling with Timers
# Problem: Schedule periodic tasks using a thread-based timer.
# Goal: Use `threading.Timer` to execute a task at fixed intervals.
def scheduled_task():
    print(f"Task executed at {time.ctime()}.")
    threading.Timer(2, scheduled_task).start()

print("Starting scheduled task...")
threading.Timer(2, scheduled_task).start()
time.sleep(10)  # Allow tasks to run for 10 seconds
print("Main program ends.")

# Summary: These exercises explore thread coordination, thread pools, parallel tasks, thread-safe file operations, and timers.
# Each exercise demonstrates an intermediate use case for multithreading in Python.
