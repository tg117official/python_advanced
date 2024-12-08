############################## BASIC ##########################################

# Exercise 1: Basic function definition
# Problem: Write a function that takes a name and prints a greeting message.
# Relevance: Demonstrates how to define and call a function.
def greet(name):
    print(f"Exercise 1: Hello, {name}!")

greet("Alice")
# Output: Exercise 1: Hello, Alice!


# Exercise 2: Function with default arguments
# Problem: Write a function to greet a user, with a default greeting if no name is provided.
# Relevance: Demonstrates default arguments in function definitions.
def greet_with_default(name="Guest"):
    print(f"Exercise 2: Hello, {name}!")

greet_with_default()
greet_with_default("Bob")
# Output:
# Exercise 2: Hello, Guest!
# Exercise 2: Hello, Bob!


# Exercise 3: Function with return value
# Problem: Write a function that adds two numbers and returns the result.
# Relevance: Demonstrates how to return values from functions.
def add_numbers(a, b):
    return a + b

result = add_numbers(10, 5)
print("Exercise 3: Sum is", result)
# Output: Exercise 3: Sum is 15


# Exercise 4: Function with multiple arguments
# Problem: Write a function that calculates the average of three numbers.
# Relevance: Demonstrates how to handle multiple arguments in a function.
def calculate_average(a, b, c):
    return (a + b + c) / 3

average = calculate_average(10, 20, 30)
print("Exercise 4: Average is", average)
# Output: Exercise 4: Average is 20.0


# Exercise 5: Function with variable-length arguments
# Problem: Write a function that takes a variable number of arguments and returns their sum.
# Relevance: Demonstrates using `*args` for variable-length arguments.
def sum_numbers(*args):
    return sum(args)

total = sum_numbers(1, 2, 3, 4, 5)
print("Exercise 5: Total sum is", total)
# Output: Exercise 5: Total sum is 15


# Exercise 6: Function with keyword arguments
# Problem: Write a function that accepts keyword arguments to format a greeting message.
# Relevance: Demonstrates using `**kwargs` for keyword arguments.
def personalized_greet(**kwargs):
    print(f"Exercise 6: Hello, {kwargs.get('name', 'Guest')} from {kwargs.get('location', 'Unknown')}!")

personalized_greet(name="Charlie", location="New York")
# Output: Exercise 6: Hello, Charlie from New York!


# Exercise 7: Recursive function
# Problem: Write a function to calculate the factorial of a number using recursion.
# Relevance: Demonstrates recursion in function definitions.
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print("Exercise 7: Factorial of 5 is", factorial(5))
# Output: Exercise 7: Factorial of 5 is 120


# Exercise 8: Function with lambda
# Problem: Write a lambda function to calculate the square of a number.
# Relevance: Demonstrates anonymous functions using `lambda`.
square = lambda x: x ** 2
print("Exercise 8: Square of 6 is", square(6))
# Output: Exercise 8: Square of 6 is 36


# Exercise 9: Function with nested function
# Problem: Write a function that contains a nested function to multiply two numbers.
# Relevance: Demonstrates the use of nested functions.
def outer_function(x, y):
    def multiply(a, b):
        return a * b
    return multiply(x, y)

print("Exercise 9: Product is", outer_function(3, 4))
# Output: Exercise 9: Product is 12


# Exercise 10: Function with global variable
# Problem: Write a function that modifies a global variable.
# Relevance: Demonstrates interaction between functions and global scope.
count = 0

def increment():
    global count
    count += 1

increment()
increment()
print("Exercise 10: Count is", count)
# Output: Exercise 10: Count is 2

##################################### INTERMEDIATE ################################

# Exercise 1: Function for Fibonacci sequence
# Problem: Write a function that generates the first N Fibonacci numbers.
# Relevance: Demonstrates iterative logic and list handling in functions.
def generate_fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    fibonacci = [0, 1]
    for i in range(2, n):
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    return fibonacci

fib_sequence = generate_fibonacci(10)
print("Exercise 1: First 10 Fibonacci numbers are", fib_sequence)
# Output: Exercise 1: First 10 Fibonacci numbers are [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


# Exercise 2: Function with decorators
# Problem: Write a decorator that logs the arguments and result of a function.
# Relevance: Demonstrates the use of higher-order functions for logging and debugging.
def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with arguments {args} and {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

@logger
def multiply(a, b):
    return a * b

result = multiply(3, 4)
# Output:
# Calling multiply with arguments (3, 4) and {}
# multiply returned 12


# Exercise 3: Function with caching (memoization)
# Problem: Write a function to calculate the factorial of a number with caching.
# Relevance: Demonstrates optimization techniques using dictionaries to store results.
cache = {}

def cached_factorial(n):
    if n in cache:
        return cache[n]
    if n == 0 or n == 1:
        cache[n] = 1
    else:
        cache[n] = n * cached_factorial(n - 1)
    return cache[n]

factorial_result = cached_factorial(6)
print("Exercise 3: Factorial of 6 is", factorial_result)
# Output: Exercise 3: Factorial of 6 is 720


# Exercise 4: Function with variable unpacking
# Problem: Write a function that takes a dictionary of student grades and prints their average.
# Relevance: Demonstrates using unpacking with dictionaries and complex argument handling.
def calculate_average_grades(**grades):
    total = sum(grades.values())
    count = len(grades)
    return total / count

average_grade = calculate_average_grades(John=85, Alice=90, Bob=78)
print("Exercise 4: Average grade is", average_grade)
# Output: Exercise 4: Average grade is 84.33333333333333


# Exercise 5: Function with error handling
# Problem: Write a function to divide two numbers, handling division by zero errors.
# Relevance: Demonstrates error handling in functions to prevent crashes.
def safe_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return "Error: Division by zero"
    return result

division_result = safe_divide(10, 0)
print("Exercise 5: Division result is", division_result)
# Output: Exercise 5: Division result is Error: Division by zero



################################### INTERMEDIATE ###############################

# Exercise 1: Function for Fibonacci sequence
# Problem: Write a function that generates the first N Fibonacci numbers.
# Relevance: Demonstrates iterative logic and list handling in functions.
def generate_fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    fibonacci = [0, 1]
    for i in range(2, n):
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    return fibonacci

fib_sequence = generate_fibonacci(10)
print("Exercise 1: First 10 Fibonacci numbers are", fib_sequence)
# Output: Exercise 1: First 10 Fibonacci numbers are [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


# Exercise 2: Function with decorators
# Problem: Write a decorator that logs the arguments and result of a function.
# Relevance: Demonstrates the use of higher-order functions for logging and debugging.
def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with arguments {args} and {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

@logger
def multiply(a, b):
    return a * b

result = multiply(3, 4)
# Output:
# Calling multiply with arguments (3, 4) and {}
# multiply returned 12


# Exercise 3: Function with caching (memoization)
# Problem: Write a function to calculate the factorial of a number with caching.
# Relevance: Demonstrates optimization techniques using dictionaries to store results.
cache = {}

def cached_factorial(n):
    if n in cache:
        return cache[n]
    if n == 0 or n == 1:
        cache[n] = 1
    else:
        cache[n] = n * cached_factorial(n - 1)
    return cache[n]

factorial_result = cached_factorial(6)
print("Exercise 3: Factorial of 6 is", factorial_result)
# Output: Exercise 3: Factorial of 6 is 720


# Exercise 4: Function with variable unpacking
# Problem: Write a function that takes a dictionary of student grades and prints their average.
# Relevance: Demonstrates using unpacking with dictionaries and complex argument handling.
def calculate_average_grades(**grades):
    total = sum(grades.values())
    count = len(grades)
    return total / count

average_grade = calculate_average_grades(John=85, Alice=90, Bob=78)
print("Exercise 4: Average grade is", average_grade)
# Output: Exercise 4: Average grade is 84.33333333333333


# Exercise 5: Function with error handling
# Problem: Write a function to divide two numbers, handling division by zero errors.
# Relevance: Demonstrates error handling in functions to prevent crashes.
def safe_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return "Error: Division by zero"
    return result

division_result = safe_divide(10, 0)
print("Exercise 5: Division result is", division_result)
# Output: Exercise 5: Division result is Error: Division by zero

