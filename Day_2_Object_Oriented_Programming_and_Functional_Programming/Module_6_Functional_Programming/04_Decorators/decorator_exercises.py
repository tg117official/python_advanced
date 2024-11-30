################################ BASIC ###########################################

# Exercise 1: Logging decorator
# Problem: Write a decorator `log` that logs the function name before calling it.
# Relevance: Useful in industry for debugging and monitoring function calls.
def log(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@log
def greet():
    return "Hello, World!"

print(f"Exercise 1 Result: {greet()}")  # Output: Calling greet \n Hello, World!

# Exercise 2: Timing decorator
# Problem: Write a decorator `timeit` to measure the execution time of a function.
# Relevance: Helps optimize performance in time-sensitive applications.
import time
def timeit(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.5f} seconds")
        return result
    return wrapper

@timeit
def slow_function():
    time.sleep(1)
    return "Done"

print(f"Exercise 2 Result: {slow_function()}")  # Output: slow_function took 1.000XX seconds \n Done

# Exercise 3: Authorization decorator
# Problem: Write a decorator `authorize` that checks if a user has access.
# Relevance: Common in securing APIs and ensuring role-based access control.
def authorize(role):
    def decorator(func):
        def wrapper(user_role, *args, **kwargs):
            if user_role == role:
                return func(*args, **kwargs)
            else:
                return "Access Denied"
        return wrapper
    return decorator

@authorize("admin")
def secret_data():
    return "This is secret data."

print(f"Exercise 3 Result: {secret_data('admin')}")  # Output: This is secret data.
print(f"Exercise 3 Result: {secret_data('guest')}")  # Output: Access Denied

# Exercise 4: Multiply result decorator
# Problem: Write a decorator `multiply_result` that multiplies the function result by 2.
# Relevance: Useful for applying transformations to function outputs.
def multiply_result(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs) * 2
    return wrapper

@multiply_result
def get_number():
    return 5

print(f"Exercise 4 Result: {get_number()}")  # Output: 10

# Exercise 5: Cache decorator
# Problem: Write a decorator `cache` that caches the results of a function.
# Relevance: Optimizes repeated computations in performance-critical applications.
def cache(func):
    results = {}
    def wrapper(*args):
        if args not in results:
            results[args] = func(*args)
        return results[args]
    return wrapper

@cache
def square(n):
    return n * n

print(f"Exercise 5 Result: {square(4)}")  # Output: 16
print(f"Exercise 5 Result: {square(4)}")  # Output: 16 (cached)

# Exercise 6: Error handling decorator
# Problem: Write a decorator `handle_errors` that catches and logs exceptions from a function.
# Relevance: Ensures robustness in applications by handling unexpected errors.
def handle_errors(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            return f"Error: {e}"
    return wrapper

@handle_errors
def divide(a, b):
    return a / b

print(f"Exercise 6 Result: {divide(10, 2)}")  # Output: 5.0
print(f"Exercise 6 Result: {divide(10, 0)}")  # Output: Error: division by zero

# Exercise 7: Prefix string decorator
# Problem: Write a decorator `prefix_string` to add a prefix to the string returned by a function.
# Relevance: Useful in formatting data dynamically in industry applications.
def prefix_string(prefix):
    def decorator(func):
        def wrapper(*args, **kwargs):
            return prefix + func(*args, **kwargs)
        return wrapper
    return decorator

@prefix_string("Hello, ")
def get_name():
    return "Alice"

print(f"Exercise 7 Result: {get_name()}")  # Output: Hello, Alice

# Exercise 8: Repeat execution decorator
# Problem: Write a decorator `repeat` that repeats a function's execution a fixed number of times.
# Relevance: Useful in stress testing and repeated operations in testing.
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def say_hello():
    print("Hello!")

print("Exercise 8 Result:")
say_hello()  # Output: Hello! (repeated 3 times)

# Exercise 9: Uppercase result decorator
# Problem: Write a decorator `uppercase_result` that converts the string result of a function to uppercase.
# Relevance: Common in text normalization tasks in ETL pipelines.
def uppercase_result(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return wrapper

@uppercase_result
def message():
    return "this is a message"

print(f"Exercise 9 Result: {message()}")  # Output: THIS IS A MESSAGE

# Exercise 10: Debug decorator
# Problem: Write a decorator `debug` that prints the function arguments and result.
# Relevance: Assists in debugging and tracing data in production systems.
def debug(func):
    def wrapper(*args, **kwargs):
        print(f"Function {func.__name__} called with args: {args} kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"Result: {result}")
        return result
    return wrapper

@debug
def add(a, b):
    return a + b

print(f"Exercise 10 Result: {add(10, 5)}")
# Output: Function add called with args: (10, 5) kwargs: {} \n Result: 15


################################# INTERMEDIATE ########################################

# Exercise 1: Dynamic argument validation
# Problem: Write a decorator `validate_args` that validates function arguments based on a condition.
# Relevance: Useful in ensuring data integrity in APIs or ETL pipelines.
def validate_args(condition):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if not all(condition(arg) for arg in args):
                return "Invalid arguments"
            return func(*args, **kwargs)

        return wrapper

    return decorator


@validate_args(lambda x: isinstance(x, int) and x > 0)
def add_positive(a, b):
    return a + b


print(f"Exercise 1 Result: {add_positive(5, 10)}")  # Output: 15
print(f"Exercise 1 Result: {add_positive(5, -10)}")  # Output: Invalid arguments


# Exercise 2: Function memoization
# Problem: Enhance a decorator `memoize` to cache results for both positional and keyword arguments.
# Relevance: Optimizes performance for expensive computations in analytics.
def memoize(func):
    cache = {}

    def wrapper(*args, **kwargs):
        key = (args, frozenset(kwargs.items()))
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]

    return wrapper


@memoize
def power(base, exp):
    return base ** exp


print(f"Exercise 2 Result: {power(2, 10)}")  # Output: 1024
print(f"Exercise 2 Result: {power(2, 10)}")  # Output: 1024 (cached)


# Exercise 3: Logging with levels
# Problem: Create a decorator `log_with_level` that logs messages with a configurable log level.
# Relevance: Improves logging flexibility in production systems.
def log_with_level(level):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"[{level.upper()}] Executing {func.__name__}")
            return func(*args, **kwargs)

        return wrapper

    return decorator


@log_with_level("debug")
def process_data():
    return "Processing data..."


print(f"Exercise 3 Result: {process_data()}")  # Output: [DEBUG] Executing process_data \n Processing data...

# Exercise 4: Retry decorator with delay
# Problem: Write a decorator `retry_with_delay` to retry a function upon failure with a delay.
# Relevance: Useful for handling transient errors in distributed systems.
import time


def retry_with_delay(retries, delay):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Error: {e}. Retrying in {delay} seconds...")
                    time.sleep(delay)
            raise Exception("All retries failed")

        return wrapper

    return decorator


@retry_with_delay(3, 2)
def flaky_function():
    raise ValueError("Random error")


try:
    print(f"Exercise 4 Result: {flaky_function()}")
except Exception as e:
    print(f"Exercise 4 Failed: {e}")

# Exercise 5: Execution time limit
# Problem: Write a decorator `time_limit` that raises an exception if a function takes too long.
# Relevance: Prevents long-running operations in production.
import signal


def time_limit(seconds):
    def decorator(func):
        def handler(signum, frame):
            raise TimeoutError("Function execution exceeded time limit")

        def wrapper(*args, **kwargs):
            signal.signal(signal.SIGALRM, handler)
            signal.alarm(seconds)
            try:
                return func(*args, **kwargs)
            finally:
                signal.alarm(0)

        return wrapper

    return decorator


@time_limit(2)
def slow_task():
    time.sleep(3)
    return "Task completed"


try:
    print(f"Exercise 5 Result: {slow_task()}")
except TimeoutError as e:
    print(f"Exercise 5 Failed: {e}")  # Output: Function execution exceeded time limit


# Exercise 6: Conditional execution
# Problem: Write a decorator `run_if` that only runs a function if a condition is met.
# Relevance: Helps in dynamic feature toggling in systems.
def run_if(condition):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if condition():
                return func(*args, **kwargs)
            return "Condition not met"

        return wrapper

    return decorator


@run_if(lambda: True)
def feature_function():
    return "Feature executed"


print(f"Exercise 6 Result: {feature_function()}")  # Output: Feature executed


# Exercise 7: Role-based access control
# Problem: Write a decorator `access_control` to restrict access to functions based on roles.
# Relevance: Enforces security in multi-user systems.
def access_control(allowed_roles):
    def decorator(func):
        def wrapper(role, *args, **kwargs):
            if role in allowed_roles:
                return func(*args, **kwargs)
            return "Access denied"

        return wrapper

    return decorator


@access_control(["admin", "manager"])
def restricted_function():
    return "Sensitive operation executed"


print(f"Exercise 7 Result: {restricted_function('admin')}")  # Output: Sensitive operation executed
print(f"Exercise 7 Result: {restricted_function('guest')}")  # Output: Access denied


# Exercise 8: Parameterized debugging
# Problem: Write a decorator `debug_with_params` that allows toggling debug messages with a parameter.
# Relevance: Useful in debugging production systems dynamically.
def debug_with_params(enable_debug):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if enable_debug:
                print(f"Debug: Calling {func.__name__} with args={args}, kwargs={kwargs}")
            return func(*args, **kwargs)

        return wrapper

    return decorator


@debug_with_params(True)
def multiply(a, b):
    return a * b


print(f"Exercise 8 Result: {multiply(3, 4)}")  # Output: Debug: Calling multiply with args=(3, 4), kwargs={} \n 12


# Exercise 9: Dynamic prefix decorator
# Problem: Write a decorator `add_prefix` that dynamically adds a prefix to function outputs.
# Relevance: Useful in dynamic data labeling and formatting.
def add_prefix(prefix_func):
    def decorator(func):
        def wrapper(*args, **kwargs):
            return f"{prefix_func()} {func(*args, **kwargs)}"

        return wrapper

    return decorator


@add_prefix(lambda: "[INFO]")
def log_message():
    return "System initialized"


print(f"Exercise 9 Result: {log_message()}")  # Output: [INFO] System initialized


# Exercise 10: Chained decorators
# Problem: Write two decorators `uppercase` and `add_exclamation` and chain them on a single function.
# Relevance: Combines multiple transformations for outputs.
def uppercase(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()

    return wrapper


def add_exclamation(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs) + "!"

    return wrapper


@uppercase
@add_exclamation
def greet():
    return "hello"


print(f"Exercise 10 Result: {greet()}")  # Output: HELLO!
