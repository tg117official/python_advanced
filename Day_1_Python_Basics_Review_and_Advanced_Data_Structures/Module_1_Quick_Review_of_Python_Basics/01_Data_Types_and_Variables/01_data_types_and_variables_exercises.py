#################################### BASIC ##################################

# Exercise 1: Integer operations
# Problem: Write a program to calculate the factorial of an integer using a loop.
# Relevance: Demonstrates the use of integers in mathematical computations.
num = 5
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print("Exercise 1: Factorial of", num, "is", factorial)
# Output: Factorial of 5 is 120

# Exercise 2: Floating-point arithmetic
# Problem: Write a program to calculate the area of a circle with a given radius.
# Relevance: Floating-point numbers are essential for precise scientific and engineering calculations.
radius = 3.5
area = 3.14159 * radius ** 2
print("Exercise 2: Area of circle with radius", radius, "is", area)
# Output: Area of circle with radius 3.5 is 38.4844775

# Exercise 3: String manipulation
# Problem: Write a program to reverse a string.
# Relevance: Strings are a fundamental data type used in text processing.
string = "Hello, World!"
reversed_string = string[::-1]
print("Exercise 3: Reversed string is", reversed_string)
# Output: Reversed string is !dlroW ,olleH

# Exercise 4: Boolean logic
# Problem: Check if a given number is positive, negative, or zero.
# Relevance: Boolean values are critical for decision-making in programming.
number = -10
if number > 0:
    result = "Positive"
elif number < 0:
    result = "Negative"
else:
    result = "Zero"
print("Exercise 4:", number, "is", result)
# Output: -10 is Negative

# Exercise 5: List operations
# Problem: Write a program to find the largest number in a list.
# Relevance: Lists are versatile and used to store collections of data.
numbers = [10, 20, 30, 40, 50]
largest_number = max(numbers)
print("Exercise 5: Largest number is", largest_number)
# Output: Largest number is 50

# Exercise 6: Dictionary usage
# Problem: Create a dictionary of students and their scores, and find the average score.
# Relevance: Dictionaries are useful for key-value mappings in structured data.
students = {"Alice": 85, "Bob": 78, "Charlie": 92}
average_score = sum(students.values()) / len(students)
print("Exercise 6: Average score is", average_score)
# Output: Average score is 85.0

# Exercise 7: Tuple immutability
# Problem: Write a program to swap two numbers using a tuple.
# Relevance: Tuples are immutable and useful for fixed collections of data.
a, b = (5, 10)
a, b = b, a
print("Exercise 7: After swapping, a =", a, "and b =", b)
# Output: After swapping, a = 10 and b = 5

# Exercise 8: Set operations
# Problem: Find the common elements between two sets.
# Relevance: Sets are efficient for mathematical set operations like union, intersection, etc.
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
common_elements = set1 & set2
print("Exercise 8: Common elements are", common_elements)
# Output: Common elements are {3, 4}

# Exercise 9: Byte data type
# Problem: Convert a string to bytes and decode it back to a string.
# Relevance: Byte data types are essential for file I/O and network programming.
byte_string = b"Hello, World!"
decoded_string = byte_string.decode('utf-8')
print("Exercise 9: Decoded string is", decoded_string)
# Output: Decoded string is Hello, World!

# Exercise 10: Complex numbers
# Problem: Write a program to add and multiply two complex numbers.
# Relevance: Complex numbers are used in scientific computing, especially in signal processing.
complex1 = 2 + 3j
complex2 = 1 + 4j
sum_complex = complex1 + complex2
product_complex = complex1 * complex2
print("Exercise 10: Sum is", sum_complex, "and Product is", product_complex)
# Output: Sum is (3+7j) and Product is (-10+11j)


################################ INTERMEDIATE #####################################


# Exercise 1: Variables and type casting
# Problem: Convert a string representation of a number to an integer and perform arithmetic operations.
# Relevance: Demonstrates type casting between data types, a common requirement in data processing.
number_str = "123"
number_int = int(number_str)
result = number_int * 2
print("Exercise 1: Double of", number_str, "is", result)
# Output: Double of 123 is 246

# Exercise 2: List slicing and modification
# Problem: Reverse a list and replace its middle element with a new value.
# Relevance: Demonstrates advanced list slicing and element modification.
numbers = [10, 20, 30, 40, 50]
numbers = numbers[::-1]
numbers[len(numbers) // 2] = 99
print("Exercise 2: Modified list is", numbers)
# Output: Modified list is [50, 40, 99, 20, 10]

# Exercise 3: Nested dictionaries
# Problem: Create a nested dictionary to represent a company's departments and employee names.
# Relevance: Demonstrates working with hierarchical data structures using dictionaries.
company = {
    "HR": {"Alice": "Manager", "Bob": "Recruiter"},
    "IT": {"Charlie": "Developer", "David": "SysAdmin"}
}
it_employees = list(company["IT"].keys())
print("Exercise 3: IT Employees are", it_employees)
# Output: IT Employees are ['Charlie', 'David']

# Exercise 4: Tuple unpacking
# Problem: Unpack a tuple containing student information and print their details.
# Relevance: Highlights tuple unpacking, which is useful for handling structured data.
student = ("Alice", 20, "Computer Science")
name, age, department = student
print(f"Exercise 4: {name} is {age} years old and studies {department}")
# Output: Alice is 20 years old and studies Computer Science

# Exercise 5: Sets and symmetric difference
# Problem: Find unique elements that are in one of two sets but not in both.
# Relevance: Demonstrates set operations, commonly used in data analysis.
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
unique_elements = set1 ^ set2
print("Exercise 5: Unique elements are", unique_elements)
# Output: Unique elements are {1, 2, 5, 6}

# Exercise 6: String formatting
# Problem: Format a string to include dynamic variables and align text.
# Relevance: Demonstrates advanced string formatting for creating reports or logs.
name = "Alice"
score = 95.6789
formatted_string = f"Student: {name:<10} | Score: {score:.2f}"
print("Exercise 6:", formatted_string)
# Output: Student: Alice      | Score: 95.68

# Exercise 7: List comprehensions with conditions
# Problem: Create a list of squares for even numbers only from a given list.
# Relevance: Demonstrates efficient data transformations using list comprehensions.
numbers = [1, 2, 3, 4, 5, 6]
squares = [n**2 for n in numbers if n % 2 == 0]
print("Exercise 7: Squares of even numbers are", squares)
# Output: Squares of even numbers are [4, 16, 36]

# Exercise 8: Immutable vs mutable types
# Problem: Compare the behavior of mutable and immutable types during modification.
# Relevance: Highlights the importance of understanding mutability in variables.
mutable_list = [1, 2, 3]
immutable_tuple = (1, 2, 3)

mutable_list[0] = 99  # Mutable, modification allowed
try:
    immutable_tuple[0] = 99  # Immutable, raises an error
except TypeError as e:
    print("Exercise 8: Error modifying tuple:", e)
print("Mutable list is", mutable_list)
# Output: Mutable list is [99, 2, 3]

# Exercise 9: Using `zip` with lists
# Problem: Combine two lists into a dictionary using `zip`.
# Relevance: Demonstrates the use of `zip` for pairing elements from multiple iterables.
keys = ["name", "age", "department"]
values = ["Alice", 20, "Physics"]
combined_dict = dict(zip(keys, values))
print("Exercise 9: Combined dictionary is", combined_dict)
# Output: Combined dictionary is {'name': 'Alice', 'age': 20, 'department': 'Physics'}

# Exercise 10: Working with `bytes` and `bytearray`
# Problem: Modify a bytearray and convert it back to a string.
# Relevance: Demonstrates working with low-level data types used in networking or file I/O.
byte_array = bytearray(b"hello")
byte_array[0] = ord("H")  # Modify the first byte
modified_string = byte_array.decode("utf-8")
print("Exercise 10: Modified string is", modified_string)
# Output: Modified string is Hello
