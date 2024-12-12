# Code Obfuscation Exercises
# These exercises will help you understand basic techniques for obfuscating code.

# Exercise 1: Renaming Variables and Functions
# Goal: Obfuscate by replacing meaningful names with meaningless ones.
def add_numbers(a, b):
    return a + b

print("Sum:", add_numbers(5, 10))  # Output: Sum: 15

# Obfuscated Version
# Replace function and variable names with random strings.
def x1x(x2x, x3x):
    return x2x + x3x

print("Sum:", x1x(5, 10))

# Exercise 2: Adding Redundant Code
# Goal: Obfuscate by adding unnecessary operations or logic.
def multiply_numbers(a, b):
    return a * b

print("Product:", multiply_numbers(3, 4))  # Output: Product: 12

# Obfuscated Version
# Add redundant code that does not affect the output.
def x2x(x4x, x5x):
    x6x = 0
    for _ in range(0):  # Redundant loop
        x6x += 1
    return x4x * x5x

print("Product:", x2x(3, 4))

# Exercise 3: Encoding Strings
# Goal: Obfuscate by encoding string literals.
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))  # Output: Hello, Alice!

# Obfuscated Version
# Use encoded strings and decode them at runtime.
def x3x(x7x):
    import base64
    greeting = base64.b64decode(b"SGVsbG8sIHtuYW1lfSE=").decode("utf-8")
    return greeting.replace("{name}", x7x)

print(x3x("Alice"))

# Exercise 4: Flattening Control Structures
# Goal: Obfuscate by replacing control structures with function calls or complex expressions.
def is_even(number):
    if number % 2 == 0:
        return True
    return False

print(is_even(4))  # Output: True

# Obfuscated Version
# Flatten the control structure into a single return statement.
def x4x(x8x):
    return (x8x % 2 == 0)

print(x4x(4))

# Exercise 5: Removing Whitespace and Comments
# Goal: Obfuscate by compacting the code to remove readability.
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))  # Output: 120

# Obfuscated Version
# Remove whitespace and comments.
def x5x(x9x):return 1 if x9x in(0,1)else x9x*x5x(x9x-1)
print(x5x(5))

# Summary: These exercises demonstrate renaming variables, adding redundant code, encoding strings,
# flattening control structures, and removing whitespace/comments as basic obfuscation techniques.