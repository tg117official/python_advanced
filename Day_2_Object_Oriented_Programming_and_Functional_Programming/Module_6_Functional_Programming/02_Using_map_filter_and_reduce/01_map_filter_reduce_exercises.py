################################### BASIC #############################################

from functools import reduce

# Exercise 1: Double each number using map
# Problem: Use `map` to double the numbers in a list.
# Relevance: Useful in industry for applying transformations to collections of data.
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(f"Exercise 1 Result: {doubled}")  # Output: [2, 4, 6, 8, 10]

# Exercise 2: Filter even numbers
# Problem: Use `filter` to extract even numbers from a list.
# Relevance: Common in data filtering tasks for analytics or ETL processes.
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Exercise 2 Result: {even_numbers}")  # Output: [2, 4]

# Exercise 3: Sum of numbers using reduce
# Problem: Use `reduce` to calculate the sum of all numbers in a list.
# Relevance: Used in summarization tasks like aggregating data in reports.
sum_of_numbers = reduce(lambda x, y: x + y, numbers)
print(f"Exercise 3 Result: {sum_of_numbers}")  # Output: 15

# Exercise 4: Convert numbers to strings
# Problem: Use `map` to convert all integers in a list to strings.
# Relevance: Common in formatting data for display or database storage.
string_numbers = list(map(str, numbers))
print(f"Exercise 4 Result: {string_numbers}")  # Output: ['1', '2', '3', '4', '5']

# Exercise 5: Filter names starting with a specific letter
# Problem: Use `filter` to get names that start with the letter "A".
# Relevance: Useful in querying data with specific conditions, such as search filters.
names = ["Alice", "Bob", "Amanda", "Charlie"]
a_names = list(filter(lambda name: name.startswith("A"), names))
print(f"Exercise 5 Result: {a_names}")  # Output: ['Alice', 'Amanda']

# Exercise 6: Product of all numbers
# Problem: Use `reduce` to calculate the product of all numbers in a list.
# Relevance: Helps in calculating aggregate metrics like compounded growth rates.
product_of_numbers = reduce(lambda x, y: x * y, numbers)
print(f"Exercise 6 Result: {product_of_numbers}")  # Output: 120

# Exercise 7: Extract domain names from emails
# Problem: Use `map` to extract domain names from a list of email addresses.
# Relevance: Used in analytics or personalization tasks based on email domains.
emails = ["user1@gmail.com", "user2@yahoo.com", "user3@hotmail.com"]
domains = list(map(lambda email: email.split("@")[1], emails))
print(f"Exercise 7 Result: {domains}")  # Output: ['gmail.com', 'yahoo.com', 'hotmail.com']

# Exercise 8: Filter numbers greater than a threshold
# Problem: Use `filter` to extract numbers greater than 10 from a list.
# Relevance: Common in threshold-based filtering for alerts or analytics.
large_numbers = list(filter(lambda x: x > 10, [5, 10, 15, 20]))
print(f"Exercise 8 Result: {large_numbers}")  # Output: [15, 20]

# Exercise 9: Combine words into a sentence
# Problem: Use `reduce` to combine a list of words into a single sentence.
# Relevance: Used in string aggregation tasks like generating text summaries.
words = ["Python", "is", "awesome"]
sentence = reduce(lambda x, y: x + " " + y, words)
print(f"Exercise 9 Result: {sentence}")  # Output: Python is awesome

# Exercise 10: Square of numbers using map
# Problem: Use `map` to calculate the square of each number in a list.
# Relevance: Frequently used in mathematical or data transformation operations.
squares = list(map(lambda x: x ** 2, numbers))
print(f"Exercise 10 Result: {squares}")  # Output: [1, 4, 9, 16, 25]


#################################### INTERMEDIATE ###############################################

from functools import reduce

# Exercise 1: Normalize a list of numbers using map
# Problem: Use `map` to normalize a list of numbers to a range of 0-1 based on the max value in the list.
# Relevance: Common in machine learning preprocessing steps.
numbers = [10, 20, 30, 40, 50]
max_value = max(numbers)
normalized = list(map(lambda x: x / max_value, numbers))
print(f"Exercise 1 Result: {normalized}")  # Output: [0.2, 0.4, 0.6, 0.8, 1.0]

# Exercise 2: Filter palindromic strings
# Problem: Use `filter` to extract strings that are palindromes from a list.
# Relevance: Useful in text analytics or data validation tasks.
words = ["radar", "python", "level", "world", "madam"]
palindromes = list(filter(lambda word: word == word[::-1], words))
print(f"Exercise 2 Result: {palindromes}")  # Output: ['radar', 'level', 'madam']

# Exercise 3: Calculate weighted average using reduce
# Problem: Use `reduce` to calculate the weighted average of a list of numbers with given weights.
# Relevance: Used in analytics, such as calculating grades or portfolio returns.
values = [50, 75, 100]
weights = [0.2, 0.3, 0.5]
weighted_avg = reduce(lambda acc, vw: acc + vw[0] * vw[1], zip(values, weights), 0)
print(f"Exercise 3 Result: {weighted_avg}")  # Output: 85.0

# Exercise 4: Extract unique email domains using map and set
# Problem: Use `map` to extract domains from email addresses and find unique domains.
# Relevance: Used in customer segmentation or spam detection systems.
emails = ["a@gmail.com", "b@yahoo.com", "c@gmail.com", "d@outlook.com"]
unique_domains = set(map(lambda email: email.split("@")[1], emails))
print(f"Exercise 4 Result: {unique_domains}")  # Output: {'gmail.com', 'yahoo.com', 'outlook.com'}

# Exercise 5: Filter valid IP addresses
# Problem: Use `filter` to validate and extract IPv4 addresses from a list.
# Relevance: Useful in network data processing and validation tasks.
ip_addresses = ["192.168.0.1", "256.256.256.256", "10.0.0.1", "abc.def.ghi.jkl"]
valid_ips = list(filter(lambda ip: all(0 <= int(part) < 256 for part in ip.split('.') if part.isdigit()), ip_addresses))
print(f"Exercise 5 Result: {valid_ips}")  # Output: ['192.168.0.1', '10.0.0.1']

# Exercise 6: Aggregate sales data by region using reduce
# Problem: Use `reduce` to aggregate sales by region from a list of tuples (region, sales).
# Relevance: Common in sales and financial data processing.
sales_data = [("North", 100), ("South", 200), ("North", 150), ("East", 300)]
aggregated_sales = reduce(lambda acc, item: {**acc, item[0]: acc.get(item[0], 0) + item[1]}, sales_data, {})
print(f"Exercise 6 Result: {aggregated_sales}")  # Output: {'North': 250, 'South': 200, 'East': 300}

# Exercise 7: Map list of dictionaries to extract specific keys
# Problem: Use `map` to extract 'name' from a list of dictionaries containing employee data.
# Relevance: Useful in transforming structured data for reporting or analytics.
employees = [{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}, {"name": "Charlie", "age": 35}]
employee_names = list(map(lambda emp: emp["name"], employees))
print(f"Exercise 7 Result: {employee_names}")  # Output: ['Alice', 'Bob', 'Charlie']

# Exercise 8: Filter products by availability
# Problem: Use `filter` to extract products that are in stock (availability > 0).
# Relevance: Essential in inventory management and e-commerce platforms.
products = [{"id": 1, "name": "Laptop", "availability": 5}, {"id": 2, "name": "Phone", "availability": 0}]
available_products = list(filter(lambda p: p["availability"] > 0, products))
print(f"Exercise 8 Result: {available_products}")  # Output: [{'id': 1, 'name': 'Laptop', 'availability': 5}]

# Exercise 9: Reduce to find the longest string
# Problem: Use `reduce` to find the longest string in a list of words.
# Relevance: Common in text analysis tasks.
words = ["data", "analytics", "science", "AI"]
longest_word = reduce(lambda acc, word: word if len(word) > len(acc) else acc, words)
print(f"Exercise 9 Result: {longest_word}")  # Output: analytics

# Exercise 10: Transform JSON data with map
# Problem: Use `map` to transform a list of JSON objects, doubling the 'quantity' field.
# Relevance: Used in ETL pipelines for data transformation.
json_data = [{"item": "apple", "quantity": 10}, {"item": "banana", "quantity": 5}]
transformed_data = list(map(lambda x: {**x, "quantity": x["quantity"] * 2}, json_data))
print(f"Exercise 10 Result: {transformed_data}")  # Output: [{'item': 'apple', 'quantity': 20}, {'item': 'banana', 'quantity': 10}]
