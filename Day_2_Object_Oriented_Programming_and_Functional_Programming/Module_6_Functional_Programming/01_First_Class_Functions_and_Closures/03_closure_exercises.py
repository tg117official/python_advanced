#################################### BASIC ########################################

# Exercise 1: Basic Closure
# Problem: Write a function `make_adder` that takes a number `n` and returns a function that adds `n` to its input.
# Relevance: Demonstrates how closures can capture and use variables from their enclosing scope.
def make_adder(n):
    def adder(x):
        return x + n
    return adder

add_five = make_adder(5)
result = add_five(10)  # Should return 15
print(f"Exercise 1 Result: {result}")  # Output: 15

# Exercise 2: Counter Closure
# Problem: Create a function `counter` that returns a function which increments and prints a count each time it's called.
# Relevance: Shows how closures maintain state between function calls without using global variables.
def counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment

count = counter()
print(f"Exercise 2 Result: {count()}")  # Output: 1
print(f"Exercise 2 Result: {count()}")  # Output: 2

# Exercise 3: Multiplication Closure
# Problem: Write a function `make_multiplier` that takes a number `n` and returns a function that multiplies its input by `n`.
# Relevance: Illustrates how closures can create specialized functions.
def make_multiplier(n):
    def multiplier(x):
        return x * n
    return multiplier

times_three = make_multiplier(3)
result = times_three(7)  # Should return 21
print(f"Exercise 3 Result: {result}")  # Output: 21

# Exercise 4: Power Function Closure
# Problem: Create a function `make_power` that takes an exponent `n` and returns a function that raises its input to the power of `n`.
# Relevance: Highlights the use of closures for creating parameterized functions.
def make_power(n):
    def power(x):
        return x ** n
    return power

square = make_power(2)
result = square(4)  # Should return 16
print(f"Exercise 4 Result: {result}")  # Output: 16

# Exercise 5: Logging Closure
# Problem: Implement a function `logger` that takes a prefix string and returns a function that logs messages with that prefix.
# Relevance: Useful for creating customized logging functions.
def logger(prefix):
    def log_message(message):
        print(f"{prefix}: {message}")
    return log_message

info_logger = logger("INFO")
info_logger("This is an informational message.")  # Output: INFO: This is an informational message.

# Exercise 6: Configurable Divider Closure
# Problem: Write a function `make_divider` that takes a divisor `n` and returns a function that divides its input by `n`.
# Relevance: Demonstrates closures in creating functions with fixed parameters.
def make_divider(n):
    def divider(x):
        return x / n
    return divider

divide_by_two = make_divider(2)
result = divide_by_two(10)  # Should return 5.0
print(f"Exercise 6 Result: {result}")  # Output: 5.0

# Exercise 7: Greeting Closure
# Problem: Create a function `greet_maker` that takes a greeting string and returns a function that greets a person with that greeting.
# Relevance: Shows how closures can be used to customize functions.
def greet_maker(greeting):
    def greet(name):
        return f"{greeting}, {name}!"
    return greet

say_hello = greet_maker("Hello")
result = say_hello("Alice")  # Should return "Hello, Alice!"
print(f"Exercise 7 Result: {result}")  # Output: Hello, Alice!

# Exercise 8: Temperature Converter Closure
# Problem: Write a function `make_converter` that returns two functions to convert temperatures between Celsius and Fahrenheit.
# Relevance: Utilizes closures to maintain related functions together.
def make_converter():
    def to_celsius(f):
        return (f - 32) * 5 / 9
    def to_fahrenheit(c):
        return (c * 9 / 5) + 32
    return to_celsius, to_fahrenheit

to_celsius, to_fahrenheit = make_converter()
result_c = to_celsius(100)  # Should return 37.777...
result_f = to_fahrenheit(0)  # Should return 32.0
print(f"Exercise 8 Result: {result_c}")  # Output: 37.77777777777778
print(f"Exercise 8 Result: {result_f}")  # Output: 32.0

# Exercise 9: Password Protected Function
# Problem: Create a function `password_protect` that takes a function and a password. The returned function requires the correct password to execute.
# Relevance: Demonstrates closures for function access control.
def password_protect(func, password):
    def wrapper(pwd, *args, **kwargs):
        if pwd == password:
            return func(*args, **kwargs)
        else:
            return "Access Denied"
    return wrapper

def secret_function():
    return "Secret Data"

protected = password_protect(secret_function, "mypassword")
result = protected("mypassword")  # Should return "Secret Data"
print(f"Exercise 9 Result: {result}")  # Output: Secret Data

# Exercise 10: Memoization Closure
# Problem: Implement a function `memoize` that caches the results of a function with a single argument.
# Relevance: Shows how closures can be used to remember state between function calls.
def memoize(func):
    cache = {}
    def wrapper(n):
        if n not in cache:
            cache[n] = func(n)
        return cache[n]
    return wrapper

@memoize
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

result = fibonacci(10)  # Should return 55
print(f"Exercise 10 Result: {result}")  # Output: 55


####################################### INTERMEDIATE ###########################################

# Exercise 1: Throttling function calls
# Problem: Create a closure `rate_limiter` that limits the number of times a function can be called in a time window.
# Relevance: Useful in industry projects for implementing API rate limiting.
import time

def rate_limiter(func, max_calls, time_window):
    calls = 0
    start_time = time.time()

    def wrapper(*args, **kwargs):
        nonlocal calls, start_time
        if time.time() - start_time > time_window:
            start_time = time.time()
            calls = 0
        if calls < max_calls:
            calls += 1
            return func(*args, **kwargs)
        else:
            return "Rate limit exceeded"
    return wrapper

@rate_limiter
def process_request(request):
    return f"Processed: {request}"

print(process_request("Request 1"))  # Output: Processed: Request 1

# Exercise 2: Task retry mechanism
# Problem: Write a closure `retry_task` that retries a task function a fixed number of times upon failure.
# Relevance: Ensures resilience in distributed systems for transient errors.
def retry_task(task_func, retries):
    def wrapper(*args, **kwargs):
        nonlocal retries
        for attempt in range(retries):
            try:
                return task_func(*args, **kwargs)
            except Exception as e:
                print(f"Attempt {attempt + 1} failed: {e}")
        raise Exception("All retries failed")
    return wrapper

# Example task function
def unreliable_task():
    raise ValueError("Random failure")

reliable_task = retry_task(unreliable_task, 3)
print(reliable_task())

# Exercise 3: Dynamic configuration loader
# Problem: Implement a closure `config_loader` that loads configuration settings dynamically and caches them.
# Relevance: Optimizes performance in applications requiring frequent config lookups.
def config_loader(config_source):
    config_cache = {}

    def get_config(key):
        if key not in config_cache:
            # Simulate config loading
            config_cache[key] = config_source.get(key, "Default Value")
        return config_cache[key]
    return get_config

config = {"api_key": "12345", "timeout": "30s"}
get_config = config_loader(config)
print(f"Exercise 3 Result: {get_config('api_key')}")  # Output: 12345

# Exercise 4: Context-aware logging
# Problem: Create a closure `log_with_context` that logs messages with additional context (e.g., user ID, request ID).
# Relevance: Used in microservices for tracing and debugging.
def log_with_context(context):
    def logger(message):
        return f"[{context}] {message}"
    return logger

log = log_with_context("User123")
print(f"Exercise 4 Result: {log('Request received')}")  # Output: [User123] Request received

# Exercise 5: Adaptive caching
# Problem: Write a closure `adaptive_cache` that caches function results and expires entries after a time-to-live (TTL).
# Relevance: Improves performance and ensures data freshness in caching systems.
def adaptive_cache(func, ttl):
    cache = {}
    timestamps = {}

    def wrapper(*args):
        current_time = time.time()
        if args in cache and current_time - timestamps[args] < ttl:
            return cache[args]
        result = func(*args)
        cache[args] = result
        timestamps[args] = current_time
        return result
    return wrapper

@adaptive_cache
def compute(x):
    return x * x

print(f"Exercise 5 Result: {compute(4)}")  # Output: 16

# Exercise 6: Dynamic access token generator
# Problem: Implement a closure `token_generator` that generates and stores tokens securely for authenticated users.
# Relevance: Used in systems requiring secure user authentication and token management.
def token_generator():
    tokens = {}

    def generate(user_id):
        token = f"token_{user_id}_{time.time()}"
        tokens[user_id] = token
        return token

    def get_token(user_id):
        return tokens.get(user_id, "No token found")
    return generate, get_token

generate_token, get_token = token_generator()
print(f"Exercise 6 Result: {generate_token('User1')}")  # Example: token_User1_123456789.0

# Exercise 7: Real-time data aggregator
# Problem: Create a closure `data_aggregator` that dynamically collects and processes data for a specified period.
# Relevance: Useful for real-time analytics and monitoring.
def data_aggregator():
    data = []

    def add_entry(entry):
        data.append(entry)
        return data

    def reset():
        nonlocal data
        data = []
    return add_entry, reset

add_data, reset_data = data_aggregator()
add_data(10)
add_data(20)
print(f"Exercise 7 Result: {add_data(30)}")  # Output: [10, 20, 30]

# Exercise 8: Workflow executor
# Problem: Write a closure `workflow_executor` that executes a series of tasks with shared context.
# Relevance: Supports complex workflows where tasks depend on shared state.
def workflow_executor():
    context = {}

    def execute(task, *args):
        context[task.__name__] = task(*args, **context)
        return context

    return execute

def step1(x):
    return x * 2

def step2(y, step1):
    return y + step1

execute = workflow_executor()
execute(step1, 5)
print(f"Exercise 8 Result: {execute(step2, 3)}")  # Output: {'step1': 10, 'step2': 13}

# Exercise 9: Parameterized query builder
# Problem: Implement a closure `query_builder` that dynamically constructs SQL queries based on parameters.
# Relevance: Supports dynamic query generation for database operations.
def query_builder(base_query):
    params = {}

    def add_param(key, value):
        params[key] = value

    def build_query():
        query = base_query
        for key, value in params.items():
            query += f" AND {key}='{value}'"
        return query
    return add_param, build_query

add_param, build_query = query_builder("SELECT * FROM users WHERE active=1")
add_param("age", 30)
add_param("country", "US")
print(f"Exercise 9 Result: {build_query()}")  # Output: SELECT * FROM users WHERE active=1 AND age='30' AND country='US'

# Exercise 10: Modular feature toggling
# Problem: Create a closure `feature_toggle` that enables or disables features dynamically based on conditions.
# Relevance: Used in managing feature rollouts in production systems.
def feature_toggle():
    features = {}

    def enable(feature_name):
        features[feature_name] = True

    def disable(feature_name):
        features[feature_name] = False

    def is_enabled(feature_name):
        return features.get(feature_name, False)

    return enable, disable, is_enabled

enable, disable, is_enabled = feature_toggle()
enable("dark_mode")
print(f"Exercise 10 Result: {is_enabled('dark_mode')}")  # Output: True


