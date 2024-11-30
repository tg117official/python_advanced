########################## BASIC #################################################

# Exercise 1: Square of a number
# Problem: Use a lambda function to calculate the square of a given number.
# Relevance: Simplifies small mathematical operations in data transformations.
square = lambda x: x ** 2
print(f"Exercise 1 Result: {square(5)}")  # Output: 25

# Exercise 2: Add two numbers
# Problem: Use a lambda function to add two numbers.
# Relevance: Useful for quick arithmetic operations in analytics and data processing.
add = lambda x, y: x + y
print(f"Exercise 2 Result: {add(10, 20)}")  # Output: 30

# Exercise 3: Check if a number is even
# Problem: Use a lambda function to check if a number is even.
# Relevance: Frequently used in filtering operations or validation checks.
is_even = lambda x: x % 2 == 0
print(f"Exercise 3 Result: {is_even(8)}")  # Output: True

# Exercise 4: Find the maximum of two numbers
# Problem: Use a lambda function to find the maximum of two numbers.
# Relevance: Helps in ranking or sorting data elements.
maximum = lambda x, y: x if x > y else y
print(f"Exercise 4 Result: {maximum(15, 10)}")  # Output: 15

# Exercise 5: Sort a list of tuples by the second element
# Problem: Use a lambda function as a key to sort a list of tuples based on the second element.
# Relevance: Common in sorting operations on complex data structures.
data = [(1, 3), (2, 1), (3, 2)]
sorted_data = sorted(data, key=lambda x: x[1])
print(f"Exercise 5 Result: {sorted_data}")  # Output: [(2, 1), (3, 2), (1, 3)]

# Exercise 6: Extract the first letter of a string
# Problem: Use a lambda function to extract the first letter of a string.
# Relevance: Useful for preprocessing text data in NLP tasks.
first_letter = lambda s: s[0]
print(f"Exercise 6 Result: {first_letter('Lambda')}")  # Output: L

# Exercise 7: Double elements in a list using map
# Problem: Use a lambda function with `map` to double each element in a list.
# Relevance: Applies transformations in data pipelines for preprocessing.
numbers = [1, 2, 3, 4]
doubled = list(map(lambda x: x * 2, numbers))
print(f"Exercise 7 Result: {doubled}")  # Output: [2, 4, 6, 8]

# Exercise 8: Filter strings with length greater than 3
# Problem: Use a lambda function with `filter` to extract strings longer than 3 characters.
# Relevance: Common in cleaning datasets by removing irrelevant or short entries.
strings = ["cat", "elephant", "dog", "lion"]
long_strings = list(filter(lambda s: len(s) > 3, strings))
print(f"Exercise 8 Result: {long_strings}")  # Output: ['elephant', 'lion']

# Exercise 9: Multiply corresponding elements of two lists
# Problem: Use a lambda function with `map` to multiply corresponding elements of two lists.
# Relevance: Frequently used in element-wise computations for vector-like operations.
list1 = [1, 2, 3]
list2 = [4, 5, 6]
product = list(map(lambda x, y: x * y, list1, list2))
print(f"Exercise 9 Result: {product}")  # Output: [4, 10, 18]

# Exercise 10: Check if a string is a palindrome
# Problem: Use a lambda function to check if a string is a palindrome.
# Relevance: Useful in text analytics or validation tasks.
is_palindrome = lambda s: s == s[::-1]
print(f"Exercise 10 Result: {is_palindrome('radar')}")  # Output: True


############################## INTERMEDIATE #############################################

from functools import reduce

# Exercise 1: Conditional transformation using a mix of lambda and named functions
# Problem: Write a named function that uses a lambda function to apply conditional transformations to a list of numbers.
# Relevance: Frequently used in ETL pipelines for dynamic data transformations.
def transform_numbers(numbers):
    return list(map(lambda x: x * 2 if x % 2 == 0 else x * 3, numbers))

numbers = [1, 2, 3, 4, 5]
print(f"Exercise 1 Result: {transform_numbers(numbers)}")  # Output: [3, 4, 9, 8, 15]

# Exercise 2: Apply multiple transformations to a dataset
# Problem: Write a named function that applies multiple lambda functions (e.g., scaling and filtering) to a dataset.
# Relevance: Used in preprocessing pipelines for machine learning.
def preprocess_data(data, scale_factor):
    scale = lambda x: x * scale_factor
    filter_valid = lambda x: x > 0
    scaled_data = list(map(scale, data))
    return list(filter(filter_valid, scaled_data))

data = [-1, 2, -3, 4]
print(f"Exercise 2 Result: {preprocess_data(data, 10)}")  # Output: [20, 40]

# Exercise 3: Dynamic key selector for sorting
# Problem: Write a named function that takes a key function (lambda) to sort a list of dictionaries.
# Relevance: Allows flexible sorting of complex data structures in reports or analytics.
def sort_data(data, key_func):
    return sorted(data, key=key_func)

employees = [{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}, {"name": "Charlie", "age": 35}]
sorted_employees = sort_data(employees, lambda emp: emp["age"])
print(f"Exercise 3 Result: {sorted_employees}")
# Output: [{'name': 'Bob', 'age': 25}, {'name': 'Alice', 'age': 30}, {'name': 'Charlie', 'age': 35}]

# Exercise 4: Nested lambda with named function
# Problem: Use a named function to return a lambda function for dynamic multiplication.
# Relevance: Useful for dynamically generating parameterized functions in scalable systems.
def multiplier(n):
    return lambda x: x * n

double = multiplier(2)
print(f"Exercise 4 Result: {double(10)}")  # Output: 20

# Exercise 5: Group data using lambda and named function
# Problem: Write a named function to group a list of tuples by a specific key using a lambda function.
# Relevance: Common in aggregating data for business analytics.
def group_by_key(data, key_func):
    grouped = {}
    for item in data:
        key = key_func(item)
        grouped.setdefault(key, []).append(item)
    return grouped

data = [("North", 100), ("South", 200), ("North", 150), ("East", 300)]
grouped_data = group_by_key(data, lambda x: x[0])
print(f"Exercise 5 Result: {grouped_data}")
# Output: {'North': [('North', 100), ('North', 150)], 'South': [('South', 200)], 'East': [('East', 300)]}

# Exercise 6: Apply lambda functions conditionally with a named function
# Problem: Write a named function to apply different lambda functions based on conditions.
# Relevance: Enables flexibility in applying dynamic rules in data workflows.
def conditional_transform(x):
    transform_even = lambda x: x + 10
    transform_odd = lambda x: x * 2
    return transform_even(x) if x % 2 == 0 else transform_odd(x)

print(f"Exercise 6 Result: {conditional_transform(5)}")  # Output: 10
print(f"Exercise 6 Result: {conditional_transform(4)}")  # Output: 14

# Exercise 7: Reduce with custom aggregation logic
# Problem: Use a lambda with a named function to aggregate data using custom logic (e.g., weighted sum).
# Relevance: Aggregation is key in analytics for metrics calculation.
def weighted_sum(values, weights):
    return reduce(lambda acc, vw: acc + vw[0] * vw[1], zip(values, weights), 0)

values = [10, 20, 30]
weights = [0.1, 0.5, 0.4]
print(f"Exercise 7 Result: {weighted_sum(values, weights)}")  # Output: 23.0

# Exercise 8: Combine named and lambda functions for feature extraction
# Problem: Use a named function with a lambda function to extract specific fields from a nested data structure.
# Relevance: Extracting features from nested data is common in ETL pipelines.
def extract_features(data, feature_func):
    return list(map(feature_func, data))

nested_data = [{"id": 1, "info": {"name": "Alice", "score": 90}}, {"id": 2, "info": {"name": "Bob", "score": 85}}]
features = extract_features(nested_data, lambda d: (d["id"], d["info"]["score"]))
print(f"Exercise 8 Result: {features}")  # Output: [(1, 90), (2, 85)]

# Exercise 9: Dynamic column selection in data processing
# Problem: Write a named function to dynamically select columns from a dataset using a lambda function.
# Relevance: Useful for data manipulation in data engineering workflows.
def select_columns(data, columns):
    return list(map(lambda row: {col: row[col] for col in columns}, data))

rows = [{"name": "Alice", "age": 30, "city": "NY"}, {"name": "Bob", "age": 25, "city": "SF"}]
selected = select_columns(rows, ["name", "city"])
print(f"Exercise 9 Result: {selected}")
# Output: [{'name': 'Alice', 'city': 'NY'}, {'name': 'Bob', 'city': 'SF'}]

# Exercise 10: Generate a series using lambda and named function
# Problem: Write a named function that generates a series of numbers using a lambda function for computation.
# Relevance: Useful for dynamic series generation in simulations or testing.
def generate_series(start, end, func):
    return list(map(func, range(start, end + 1)))

series = generate_series(1, 5, lambda x: x ** 2)
print(f"Exercise 10 Result: {series}")  # Output: [1, 4, 9, 16, 25]


