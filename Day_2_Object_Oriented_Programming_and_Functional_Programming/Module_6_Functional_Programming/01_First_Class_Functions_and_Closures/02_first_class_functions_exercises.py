############################## BASIC ##########################################

# Exercise 1: Pass a function as an argument
# Problem: Create a function `apply_twice` that takes another function and a value as arguments,
# applies the function to the value twice, and returns the result.
# Relevance: Demonstrates passing functions as arguments for flexible and reusable code.
def apply_twice(func, value):
    return func(func(value))

def increment(x):
    return x + 1

result = apply_twice(increment, 5)  # Should return 7 (5 + 1 + 1)
print(f"Exercise 1 Result: {result}")  # Output: 7

# Exercise 2: Return a function from another function
# Problem: Create a function `multiply_by` that takes a number and returns a function
# that multiplies its input by that number.
# Relevance: Highlights creating functions dynamically for flexible logic.
def multiply_by(factor):
    def multiplier(x):
        return x * factor
    return multiplier

times_three = multiply_by(3)
result = times_three(10)  # Should return 30 (10 * 3)
print(f"Exercise 2 Result: {result}")  # Output: 30

# Exercise 3: Store functions in a data structure
# Problem: Create a dictionary where the keys are operation names and values are corresponding functions,
# then use the dictionary to perform an operation based on user input.
# Relevance: Illustrates the versatility of storing and accessing functions dynamically.
operations = {
    "add": lambda x, y: x + y,
    "subtract": lambda x, y: x - y,
    "multiply": lambda x, y: x * y,
    "divide": lambda x, y: x / y if y != 0 else "undefined"
}

result = operations["add"](10, 5)  # Should return 15 (10 + 5)
print(f"Exercise 3 Result: {result}")  # Output: 15

# Exercise 4: Use a function as a callback
# Problem: Write a function `greet` that takes a name and a function to format the name,
# then calls the formatting function before greeting the person.
# Relevance: Demonstrates how callbacks can control the behavior of a function dynamically.
def greet(name, formatter):
    formatted_name = formatter(name)
    return f"Hello, {formatted_name}!"

uppercase = lambda name: name.upper()
result = greet("Alice", uppercase)  # Should return "Hello, ALICE!"
print(f"Exercise 4 Result: {result}")  # Output: Hello, ALICE!

# Exercise 5: Closures
# Problem: Create a function `make_counter` that returns a counter function. Each call to the counter
# function should increment and return a count.
# Relevance: Explains closures, where inner functions retain access to variables in their scope.
def make_counter():
    count = 0
    def counter():
        nonlocal count # This tells Python to use the 'count' variable from the enclosing scope (make_counter).
        count += 1
        return count

    return counter

counter = make_counter()
print(f"Exercise 5 Result: {counter()}")  # Output: 1
print(f"Exercise 5 Result: {counter()}")  # Output: 2

# Exercise 6: Function-based validation pipeline
# Problem: Write a function `validate_pipeline` that takes a list of validation functions and a value.
# It should apply each validation function in sequence and return True if all validations pass, otherwise False.
# Relevance: Useful in industry projects for creating modular and reusable validation pipelines (e.g., data validation).
def validate_pipeline(validations, value):
    return all(validation(value) for validation in validations)

is_positive = lambda x: x > 0
is_integer = lambda x: isinstance(x, int)

validators = [is_positive, is_integer]
result = validate_pipeline(validators, 10)  # Should return True (10 is positive and an integer)
print(f"Exercise 1 Result: {result}")  # Output: True

# Exercise 7: Higher-order function for rate-limited APIs
# Problem: Write a function `rate_limiter` that takes a function and limits its execution rate.
# (Simulated with a print statement in this exercise.)
# Relevance: Helps in implementing rate-limited API calls in projects where throttling is required.
import time

def rate_limiter(func, delay):
    def wrapper(*args, **kwargs):
        time.sleep(delay)  # Simulate rate-limiting with a delay
        return func(*args, **kwargs)
    return wrapper

@rate_limiter
def fetch_data():
    return "Data fetched!"

result = fetch_data()  # Should return "Data fetched!" after a delay
print(f"Exercise 2 Result: {result}")  # Output: Data fetched!

# Exercise 8: Dynamic strategy selection
# Problem: Write a function `apply_strategy` that takes a strategy function and data, then applies the strategy to the data.
# Relevance: Used in industry for dynamic behavior selection, such as choosing algorithms at runtime.
def apply_strategy(strategy, data):
    return strategy(data)

sort_desc = lambda data: sorted(data, reverse=True)
data = [3, 1, 4, 1, 5]
result = apply_strategy(sort_desc, data)  # Should return [5, 4, 3, 1, 1]
print(f"Exercise 3 Result: {result}")  # Output: [5, 4, 3, 1, 1]

# Exercise 9: Factory function for creating loggers
# Problem: Write a function `create_logger` that takes a logging level and returns a logger function.
# The logger should prepend the level to each log message.
# Relevance: Industry use case for implementing custom logging frameworks.
def create_logger(level):
    def logger(message):
        return f"[{level}] {message}"
    return logger

info_logger = create_logger("INFO")
result = info_logger("System initialized.")  # Should return "[INFO] System initialized."
print(f"Exercise 4 Result: {result}")  # Output: [INFO] System initialized.

# Exercise 10: Function composition
# Problem: Write a function `compose` that takes two functions and returns their composition.
# Relevance: Common in functional programming patterns, such as combining transformations in ETL pipelines.
def compose(func1, func2):
    return lambda x: func1(func2(x))

increment = lambda x: x + 1
double = lambda x: x * 2
composed_function = compose(double, increment)  # First increment, then double
result = composed_function(5)  # Should return 12 (5 + 1 = 6, 6 * 2 = 12)
print(f"Exercise 5 Result: {result}")  # Output: 12


############################# INTERMEDIATE ###########################################

# Exercise 1: Dynamic function decorator
# Problem: Write a function `dynamic_decorator` that takes a decorator as input and applies it to multiple functions.
# Relevance: Allows dynamic and reusable function modifications in large-scale applications.
def dynamic_decorator(decorator, funcs):
    return [decorator(func) for func in funcs]

def add_exclamation(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs) + "!"
    return wrapper

@add_exclamation
def greet():
    return "Hello"

result = greet()  # Should return "Hello!"
print(f"Exercise 1 Result: {result}")  # Output: Hello!

# Exercise 2: Middleware simulation
# Problem: Implement a `middleware` function that takes a list of middleware functions and an input function to modify its behavior.
# Relevance: Mimics web frameworks' middleware behavior for request processing.
def middleware(middlewares, func):
    for mw in middlewares:
        func = mw(func)
    return func

def log_input(func):
    def wrapper(*args, **kwargs):
        print(f"Input: {args}, {kwargs}")
        return func(*args, **kwargs)
    return wrapper

def double_output(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs) * 2
    return wrapper

middlewares = [log_input, double_output]
func = middleware(middlewares, lambda x: x + 1)
result = func(10)  # Should log input and return 22
print(f"Exercise 2 Result: {result}")  # Output: 22

# Exercise 3: Caching function results
# Problem: Write a `cache` decorator that caches the results of a function for specific inputs.
# Relevance: Optimizes repeated computations in performance-critical applications.
def cache(func):
    cache_store = {}

    def wrapper(*args):
        if args not in cache_store:
            cache_store[args] = func(*args)
        return cache_store[args]
    return wrapper

@cache
def expensive_computation(x):
    return x ** 2

result = expensive_computation(5)  # Should return 25 and cache the result
print(f"Exercise 3 Result: {result}")  # Output: 25

# Exercise 4: Dynamic event handlers
# Problem: Create a system where event listeners can be dynamically registered to handle events.
# Relevance: Mimics event-driven architectures like user interaction in GUIs.
class EventManager:
    def __init__(self):
        self.listeners = []

    def register_listener(self, listener):
        self.listeners.append(listener)

    def trigger_event(self, event):
        for listener in self.listeners:
            listener(event)

manager = EventManager()
manager.register_listener(lambda e: print(f"Event: {e}"))
manager.trigger_event("User Logged In")

# Exercise 5: Data transformation pipeline
# Problem: Create a transformation pipeline using a list of functions to process data sequentially.
# Relevance: Often used in ETL pipelines for data processing.
def transformation_pipeline(transformations, data):
    for transform in transformations:
        data = transform(data)
    return data

pipeline = [lambda x: x + 1, lambda x: x * 2, lambda x: x - 3]
result = transformation_pipeline(pipeline, 5)  # Should return 13
print(f"Exercise 5 Result: {result}")  # Output: 13

# Exercise 6: Dynamic retry mechanism
# Problem: Implement a `retry` decorator that retries a function a specified number of times upon failure.
# Relevance: Ensures reliability in handling transient errors in distributed systems.
import random

def retry(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Retrying due to {e}...")
            raise Exception("Max retries exceeded")
        return wrapper
    return decorator

@retry(3)
def unreliable_function():
    if random.random() < 0.5:
        raise ValueError("Random Failure")
    return "Success"

try:
    result = unreliable_function()
    print(f"Exercise 6 Result: {result}")
except Exception as e:
    print(f"Exercise 6 Failed: {e}")

# Exercise 7: Dynamic access control
# Problem: Implement an `access_control` decorator that restricts access to a function based on user roles.
# Relevance: Used in applications requiring dynamic role-based access management.
def access_control(allowed_roles):
    def decorator(func):
        def wrapper(user_role, *args, **kwargs):
            if user_role not in allowed_roles:
                raise PermissionError("Access Denied")
            return func(*args, **kwargs)
        return wrapper
    return decorator

@access_control(["admin", "manager"])
def sensitive_operation(user_role):
    return "Sensitive Operation Performed"

try:
    result = sensitive_operation("admin")  # Should return the message
    print(f"Exercise 7 Result: {result}")
except PermissionError as e:
    print(f"Exercise 7 Failed: {e}")

# Exercise 8: Dynamic query builder
# Problem: Write a `query_builder` function that takes filters as functions and applies them to a dataset.
# Relevance: Used in constructing SQL queries or filtering large datasets dynamically.
def query_builder(filters, dataset):
    for filter_func in filters:
        dataset = filter_func(dataset)
    return dataset

data = [10, 20, 30, 40, 50]
filters = [lambda x: [i for i in x if i > 20], lambda x: [i for i in x if i < 50]]
result = query_builder(filters, data)  # Should return [30, 40]
print(f"Exercise 8 Result: {result}")  # Output: [30, 40]

# Exercise 9: Dynamic metrics collector
# Problem: Write a `metrics_collector` decorator that tracks the number of times a function is called.
# Relevance: Useful in tracking application metrics like API usage in production systems.
def metrics_collector(func):
    func.call_count = 0

    def wrapper(*args, **kwargs):
        func.call_count += 1
        return func(*args, **kwargs)
    return wrapper

@metrics_collector
def sample_function(x):
    return x * 2

sample_function(10)
sample_function(20)
print(f"Exercise 9 Result: {sample_function.call_count}")  # Output: 2

# Exercise 10: Real-time event broadcasting
# Problem: Implement an `event_broadcaster` function that allows subscribers to dynamically receive real-time updates.
# Relevance: Mimics real-time message broadcasting in systems like pub-sub messaging architectures.
class EventBroadcaster:
    def __init__(self):
        self.subscribers = []

    def subscribe(self, callback):
        self.subscribers.append(callback)

    def broadcast(self, message):
        for subscriber in self.subscribers:
            subscriber(message)

broadcaster = EventBroadcaster()
broadcaster.subscribe(lambda msg: print(f"Subscriber 1 received: {msg}"))
broadcaster.subscribe(lambda msg: print(f"Subscriber 2 received: {msg}"))
broadcaster.broadcast("New Data Available!")  # Should notify all subscribers

# Exercise 10 Output:
# Subscriber 1 received: New Data Available!
# Subscriber 2 received: New Data Available!




