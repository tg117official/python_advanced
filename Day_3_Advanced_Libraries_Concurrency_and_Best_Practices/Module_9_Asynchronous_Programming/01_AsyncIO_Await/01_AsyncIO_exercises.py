import asyncio

# Exercise 1: Simple asynchronous function
# Problem: Write an async function that prints a message and waits for 2 seconds before printing another message.
# Relevance: Demonstrates how to define and run basic asynchronous tasks.
async def simple_task():
    print("Task started...")
    await asyncio.sleep(2)
    print("Task completed!")

asyncio.run(simple_task())
# Output: Task started... (2-second pause) Task completed!

# Exercise 2: Running multiple tasks concurrently
# Problem: Run three tasks concurrently, each printing a message after waiting for different durations.
# Relevance: Useful for handling concurrent I/O operations like API calls or file downloads.
async def task1():
    await asyncio.sleep(1)
    print("Task 1 done!")

async def task2():
    await asyncio.sleep(2)
    print("Task 2 done!")

async def task3():
    await asyncio.sleep(3)
    print("Task 3 done!")

async def run_tasks():
    await asyncio.gather(task1(), task2(), task3())

asyncio.run(run_tasks())
# Output: Task 1 done!, Task 2 done!, Task 3 done! (concurrently)

# Exercise 3: Sequential execution of async functions
# Problem: Run three async functions sequentially.
# Relevance: Understand when to run tasks sequentially instead of concurrently.
async def sequential_tasks():
    await task1()
    await task2()
    await task3()

asyncio.run(sequential_tasks())
# Output: Task 1 done! (1s) Task 2 done! (1s more) Task 3 done! (1s more)

# Exercise 4: Async function with return values
# Problem: Write an async function that returns the square of a number.
# Relevance: Demonstrates how async functions can return values for further processing.
async def compute_square(x):
    await asyncio.sleep(1)
    return x * x

async def compute_example():
    result = await compute_square(5)
    print(f"Exercise 4 Result: {result}")

asyncio.run(compute_example())
# Output: Exercise 4 Result: 25

# Exercise 5: Using asyncio.as_completed
# Problem: Run multiple tasks and process their results as they complete.
# Relevance: Used in scenarios where tasks may have different completion times.
async def task_with_result(name, duration):
    await asyncio.sleep(duration)
    return f"{name} completed in {duration} seconds"

async def as_completed_example():
    tasks = [
        task_with_result("Task 1", 2),
        task_with_result("Task 2", 1),
        task_with_result("Task 3", 3)
    ]
    for coro in asyncio.as_completed(tasks):
        result = await coro
        print(result)

asyncio.run(as_completed_example())
# Output: Task 2 completed in 1 seconds, Task 1 completed in 2 seconds, Task 3 completed in 3 seconds

# Exercise 6: Creating an asyncio event loop
# Problem: Manually create and run an event loop.
# Relevance: Shows how to manage event loops in scenarios where asyncio.run() isn't ideal.
async def manual_event_loop_example():
    await asyncio.sleep(1)
    print("Manual event loop example executed!")

loop = asyncio.new_event_loop()
loop.run_until_complete(manual_event_loop_example())
loop.close()
# Output: Manual event loop example executed!

# Exercise 7: Using asyncio.Lock
# Problem: Demonstrate shared resource access control using asyncio.Lock.
# Relevance: Prevents race conditions in shared resources.
lock = asyncio.Lock()

async def protected_task(name):
    async with lock:
        print(f"{name} acquired the lock")
        await asyncio.sleep(2)
        print(f"{name} released the lock")

async def lock_example():
    await asyncio.gather(protected_task("Task A"), protected_task("Task B"))

asyncio.run(lock_example())
# Output: Task A acquired the lock, Task A released the lock, Task B acquired the lock, Task B released the lock

# Exercise 8: Timeout with asyncio.wait_for
# Problem: Implement a timeout for a long-running async task.
# Relevance: Useful in scenarios where tasks need to have strict time constraints.
async def long_task():
    await asyncio.sleep(5)
    return "Long task completed!"

async def timeout_example():
    try:
        result = await asyncio.wait_for(long_task(), timeout=2)
        print(result)
    except asyncio.TimeoutError:
        print("Task timed out!")

asyncio.run(timeout_example())
# Output: Task timed out!

# Exercise 9: Using asyncio.Queue
# Problem: Create a producer-consumer system using asyncio.Queue.
# Relevance: Common in event-driven systems and inter-task communication.
async def producer(queue):
    for i in range(5):
        print(f"Producing item {i}")
        await queue.put(i)
        await asyncio.sleep(1)

async def consumer(queue):
    while True:
        item = await queue.get()
        print(f"Consumed item {item}")
        queue.task_done()
        if item == 4:  # Stop condition
            break

async def queue_example():
    queue = asyncio.Queue()
    await asyncio.gather(producer(queue), consumer(queue))

asyncio.run(queue_example())
# Output: Produces and consumes items 0 to 4 sequentially.

# Exercise 10: Periodic task with asyncio
# Problem: Create a task that runs periodically.
# Relevance: Used for recurring tasks like polling APIs or monitoring systems.
async def periodic_task():
    while True:
        print("Periodic task executed!")
        await asyncio.sleep(3)

async def periodic_example():
    task = asyncio.create_task(periodic_task())
    await asyncio.sleep(10)  # Let it run for 10 seconds
    task.cancel()
    try:
        await task
    except asyncio.CancelledError:
        print("Periodic task canceled!")

asyncio.run(periodic_example())
# Output: Periodic task executed! (repeated every 3 seconds for 10 seconds)



######################################## INTERMEDIATE ##########################################

import asyncio
import random

# Exercise 1: Task prioritization using asyncio.PriorityQueue
# Problem: Implement a system where tasks with different priorities are executed based on their priority.
# Relevance: Useful in job scheduling or managing prioritized task queues in industry workflows.
async def priority_task(name, delay):
    await asyncio.sleep(delay)
    print(f"Task {name} completed after {delay} seconds")

async def priority_example():
    queue = asyncio.PriorityQueue()
    await queue.put((1, priority_task("Low", 3)))
    await queue.put((0, priority_task("High", 1)))
    await queue.put((2, priority_task("Medium", 2)))

    while not queue.empty():
        _, task = await queue.get()
        await task

asyncio.run(priority_example())
# Output:
# Task High completed after 1 seconds
# Task Medium completed after 2 seconds
# Task Low completed after 3 seconds

# Exercise 2: Simulating API calls with rate limiting
# Problem: Implement an async function that makes API calls while respecting a rate limit.
# Relevance: Ensures compliance with API rate limits in real-world applications.
async def rate_limited_api_call(api_url, delay):
    await asyncio.sleep(delay)
    print(f"API call to {api_url} completed")

async def rate_limited_example():
    urls = [f"https://api.example.com/resource/{i}" for i in range(5)]
    semaphore = asyncio.Semaphore(2)  # Limit concurrent API calls to 2

    async def limited_call(url):
        async with semaphore:
            await rate_limited_api_call(url, random.uniform(1, 3))

    await asyncio.gather(*(limited_call(url) for url in urls))

asyncio.run(rate_limited_example())
# Output: Simulates API calls with a maximum of 2 running concurrently.

# Exercise 3: Implementing retry logic with backoff
# Problem: Write an async function that retries a task on failure with an exponential backoff.
# Relevance: Common in network applications to handle transient failures gracefully.
async def retry_with_backoff(task, retries=3, backoff_factor=2):
    delay = 1
    for attempt in range(retries):
        try:
            return await task()
        except Exception as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            if attempt < retries - 1:
                await asyncio.sleep(delay)
                delay *= backoff_factor
    raise Exception("All retries failed")

async def unreliable_task():
    if random.choice([True, False]):
        raise Exception("Task failed")
    return "Task succeeded"

async def retry_example():
    try:
        result = await retry_with_backoff(unreliable_task, retries=3)
        print(result)
    except Exception as e:
        print(e)

asyncio.run(retry_example())
# Output: Shows retry attempts and handles failure after maximum retries.

# Exercise 4: Progress tracking for long-running tasks
# Problem: Implement a progress tracker for multiple tasks using asyncio.
# Relevance: Used in industry for tracking the progress of large-scale jobs like data processing.
async def long_running_task(task_id, duration):
    for i in range(1, duration + 1):
        await asyncio.sleep(1)
        print(f"Task {task_id}: {i}/{duration} seconds completed")
    return f"Task {task_id} completed"

async def progress_tracking_example():
    tasks = [long_running_task(f"T{i}", random.randint(3, 6)) for i in range(3)]
    results = await asyncio.gather(*tasks)
    for result in results:
        print(result)

asyncio.run(progress_tracking_example())
# Output: Shows progress for each task in real-time and reports completion.

# Exercise 5: Pipeline processing with asyncio.Queue
# Problem: Implement a pipeline where producers generate data, workers process it, and consumers log the results.
# Relevance: Mimics real-world ETL pipelines or event-driven systems.
async def producer(queue):
    for i in range(10):
        item = f"Item {i}"
        print(f"Produced: {item}")
        await queue.put(item)
        await asyncio.sleep(random.uniform(0.1, 0.5))
    await queue.put(None)  # Signal completion

async def worker(queue, result_queue):
    while True:
        item = await queue.get()
        if item is None:
            await result_queue.put(None)  # Signal completion
            break
        processed_item = f"Processed {item}"
        print(processed_item)
        await result_queue.put(processed_item)
        queue.task_done()

async def consumer(result_queue):
    while True:
        item = await result_queue.get()
        if item is None:
            break
        print(f"Consumed: {item}")
        result_queue.task_done()

async def pipeline_example():
    queue = asyncio.Queue()
    result_queue = asyncio.Queue()

    await asyncio.gather(
        producer(queue),
        worker(queue, result_queue),
        consumer(result_queue)
    )

asyncio.run(pipeline_example())
# Output: Simulates a producer-worker-consumer pipeline with data flow.
