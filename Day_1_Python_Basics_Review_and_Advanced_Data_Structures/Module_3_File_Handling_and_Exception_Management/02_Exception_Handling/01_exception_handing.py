############################## BASIC ##################################

# Exercise 1: Handling division by zero
# Problem: Write a program that safely handles division by zero.
# Relevance: Demonstrates handling common mathematical errors.
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print("Exercise 1: Error -", e)
# Output: Exercise 1: Error - division by zero


# Exercise 2: Handling invalid input
# Problem: Write a program to safely convert a string to an integer.
# Relevance: Demonstrates handling errors during data conversion.
try:
    user_input = "abc"
    number = int(user_input)
except ValueError as e:
    print("Exercise 2: Error -", e)
# Output: Exercise 2: Error - invalid literal for int() with base 10: 'abc'


# Exercise 3: File not found
# Problem: Safely handle a situation where a file does not exist.
# Relevance: Demonstrates handling file-related errors.
try:
    with open("non_existent_file.txt", "r") as file:
        content = file.read()
except FileNotFoundError as e:
    print("Exercise 3: Error -", e)
# Output: Exercise 3: Error - [Errno 2] No such file or directory: 'non_existent_file.txt'


# Exercise 4: Index out of range
# Problem: Write a program to safely access an index in a list.
# Relevance: Demonstrates handling out-of-range errors in data structures.
try:
    my_list = [1, 2, 3]
    print(my_list[5])
except IndexError as e:
    print("Exercise 4: Error -", e)
# Output: Exercise 4: Error - list index out of range


# Exercise 5: Key not found in dictionary
# Problem: Safely handle a situation where a key is not present in a dictionary.
# Relevance: Demonstrates handling missing keys in data lookups.
try:
    my_dict = {"a": 1, "b": 2}
    value = my_dict["c"]
except KeyError as e:
    print("Exercise 5: Error -", e)
# Output: Exercise 5: Error - 'c'


# Exercise 6: Attribute error
# Problem: Handle an error where an invalid attribute is accessed.
# Relevance: Demonstrates handling incorrect object property access.
try:
    number = 5
    number.append(6)  # Invalid attribute for an integer
except AttributeError as e:
    print("Exercise 6: Error -", e)
# Output: Exercise 6: Error - 'int' object has no attribute 'append'


# Exercise 7: Type error
# Problem: Handle an error where incompatible types are used in an operation.
# Relevance: Demonstrates handling type mismatches.
try:
    result = "string" + 10
except TypeError as e:
    print("Exercise 7: Error -", e)
# Output: Exercise 7: Error - can only concatenate str (not "int") to str


# Exercise 8: Value error in mathematical operations
# Problem: Safely handle invalid input for mathematical operations (e.g., square root of a negative number).
# Relevance: Demonstrates handling invalid inputs in mathematical functions.
import math
try:
    result = math.sqrt(-1)
except ValueError as e:
    print("Exercise 8: Error -", e)
# Output: Exercise 8: Error - math domain error


# Exercise 9: Handling multiple exceptions
# Problem: Write a program that handles both `ZeroDivisionError` and `TypeError`.
# Relevance: Demonstrates handling multiple potential errors.
try:
    result = 10 / "abc"  # Intentional error
except (ZeroDivisionError, TypeError) as e:
    print("Exercise 9: Error -", e)
# Output: Exercise 9: Error - unsupported operand type(s) for /: 'int' and 'str'


# Exercise 10: Using `finally` for cleanup
# Problem: Write a program to demonstrate the use of `finally` for resource cleanup.
# Relevance: Ensures cleanup code is executed regardless of exceptions.
try:
    with open("non_existent_file.txt", "r") as file:
        content = file.read()
except FileNotFoundError as e:
    print("Exercise 10: Error -", e)
finally:
    print("Exercise 10: Cleanup complete")
# Output:
# Exercise 10: Error - [Errno 2] No such file or directory: 'non_existent_file.txt'
# Exercise 10: Cleanup complete


####################################### INTERMEDIATE ##################################

# Exercise 1: Nested exception handling
# Problem: Write a program that handles exceptions in nested try-except blocks.
# Relevance: Demonstrates handling multiple potential exceptions in nested operations.
try:
    num1 = int(input("Enter numerator: "))  # Input might be invalid
    num2 = int(input("Enter denominator: "))  # Input might be invalid
    try:
        result = num1 / num2
        print("Exercise 1: Result is", result)
    except ZeroDivisionError as e:
        print("Exercise 1: Error -", e)
except ValueError as e:
    print("Exercise 1: Error - Invalid input. Please enter integers.")
# Expected Outputs:
# Case 1: Invalid input for numerator or denominator
# Output: Exercise 1: Error - Invalid input. Please enter integers.
# Case 2: Denominator is 0
# Output: Exercise 1: Error - division by zero
# Case 3: Valid inputs
# Output: Exercise 1: Result is <result>


# Exercise 2: Raising custom exceptions
# Problem: Write a program that raises a custom exception for invalid input.
# Relevance: Demonstrates creating and using custom exceptions for specific conditions.
class NegativeNumberError(Exception):
    pass

def check_positive(number):
    if number < 0:
        raise NegativeNumberError("Number cannot be negative!")

try:
    check_positive(-5)
except NegativeNumberError as e:
    print("Exercise 2: Error -", e)
# Output: Exercise 2: Error - Number cannot be negative!


# Exercise 3: Logging exceptions
# Problem: Write a program to log exceptions to a file instead of printing them.
# Relevance: Demonstrates how to log exceptions for later debugging.
import logging

logging.basicConfig(filename="exceptions.log", level=logging.ERROR)

try:
    result = 10 / 0
except ZeroDivisionError as e:
    logging.error("Exercise 3: Exception occurred", exc_info=True)
print("Exercise 3: Exception logged in exceptions.log")
# Output: Exception logged in the "exceptions.log" file:
# ERROR:root:Exception occurred
# Traceback (most recent call last):
#   File "<script>", line <line>, in <module>
#     result = 10 / 0
# ZeroDivisionError: division by zero


# Exercise 4: Exception propagation
# Problem: Write a program that propagates exceptions from one function to another.
# Relevance: Demonstrates how exceptions can be propagated across multiple layers.
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed")
    return a / b

def calculate():
    try:
        return divide(10, 0)
    except ZeroDivisionError as e:
        print("Exercise 4: Error -", e)
        raise  # Re-raises the exception for further handling

try:
    calculate()
except ZeroDivisionError as e:
    print("Exercise 4: Propagated error -", e)
# Output:
# Exercise 4: Error - Division by zero is not allowed
# Exercise 4: Propagated error - Division by zero is not allowed


# Exercise 5: Exception handling with context managers
# Problem: Write a program to handle exceptions while using context managers for file operations.
# Relevance: Ensures resource cleanup with exception handling.
try:
    with open("non_existent_file.txt", "r") as file:
        content = file.read()
except FileNotFoundError as e:
    print("Exercise 5: Error -", e)
else:
    print("Exercise 5: File content is", content)
finally:
    print("Exercise 5: File operation attempted")
# Output:
# Exercise 5: Error - [Errno 2] No such file or directory: 'non_existent_file.txt'
# Exercise 5: File operation attempted
