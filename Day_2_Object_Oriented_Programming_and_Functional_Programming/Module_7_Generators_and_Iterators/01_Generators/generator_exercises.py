########################### BASIC #########################################


# Exercise 1: Using a `for` loop to iterate over a generator
# Problem: Write a generator `countdown` that yields numbers in descending order from `n` to 1.
# Use a `for` loop to print each number.
# Relevance: In industry, `for` loops are commonly used to process large datasets
# or streams one element at a time, ensuring memory efficiency.
def countdown(n):
    for i in range(n, 0, -1):
        yield i

print("Exercise 1 Result:")
for num in countdown(5):
    print(num)  # Output: 5, 4, 3, 2, 1 (printed on separate lines)

# Exercise 2: Using `next()` to consume a generator one element at a time
# Problem: Create a generator `odd_numbers` that yields odd numbers up to `n`.
# Use `next()` to fetch elements one at a time.
# Relevance: In industry, using `next()` provides precise control over generator consumption,
# especially useful in streaming applications or processing large data batches incrementally.
def odd_numbers(n):
    for i in range(1, n + 1, 2):
        yield i

print("\nExercise 2 Result:")
gen = odd_numbers(10)
print(next(gen))  # Output: 1
print(next(gen))  # Output: 3
print(next(gen))  # Output: 5

# Exercise 3: Using `sum()` to aggregate generator values
# Problem: Write a generator `squares` that yields squares of numbers up to `n`.
# Use `sum()` to calculate the total sum of the generated squares.
# Relevance: This approach is used in data analytics pipelines to compute aggregate metrics
# (e.g., sums, averages) without needing to store intermediate results.
def squares(n):
    for i in range(1, n + 1):
        yield i ** 2

total_sum = sum(squares(5))
print(f"\nExercise 3 Result: {total_sum}")  # Output: 55 (1^2 + 2^2 + 3^2 + 4^2 + 5^2)

# Exercise 4: Using unpacking with `*` to expand generator values
# Problem: Write a generator `alphabets` that yields the first `n` lowercase letters of the alphabet.
# Use unpacking (`*`) to print all values as a single line.
# Relevance: Expanding generator results dynamically is useful in scenarios like
# generating query parameters, dynamic logs, or displaying compact data summaries.
import string

def alphabets(n):
    for i in range(n):
        yield string.ascii_lowercase[i]

print("\nExercise 4 Result:", *alphabets(5))  # Output: a b c d e

# Exercise 5: Using `zip()` with multiple generators
# Problem: Write two generators `evens` and `odds` to yield even and odd numbers respectively up to `n`.
# Use `zip()` to pair them together.
# Relevance: Pairing generators is essential in combinatorial data generation
# or merging two related streams (e.g., combining sensor readings or log entries).
def evens(n):
    for i in range(2, n + 1, 2):
        yield i

def odds(n):
    for i in range(1, n + 1, 2):
        yield i

print("\nExercise 5 Result:")
for even, odd in zip(evens(10), odds(10)):
    print(f"Even: {even}, Odd: {odd}")
# Output:
# Even: 2, Odd: 1
# Even: 4, Odd: 3
# Even: 6, Odd: 5
# Even: 8, Odd: 7
# Even: 10, Odd: 9


# Exercise 6: Generator for a sequence of numbers
# Problem: Write a generator `number_sequence` that yields numbers from 1 to n.
# Relevance: Useful for generating large sequences without loading all data into memory.
def number_sequence(n):
    for i in range(1, n + 1):
        yield i

print(f"Exercise 1 Result: {list(number_sequence(5))}")  # Output: [1, 2, 3, 4, 5]

# Exercise 7: Infinite sequence generator
# Problem: Write a generator `infinite_counter` that yields numbers starting from 1 indefinitely.
# Relevance: Used in streaming applications for continuous data generation.
def infinite_counter():
    i = 1
    while True:
        yield i
        i += 1

counter = infinite_counter()
print(f"Exercise 2 Result: {[next(counter) for _ in range(5)]}")  # Output: [1, 2, 3, 4, 5]

# Exercise 8: Generator for even numbers
# Problem: Write a generator `even_numbers` that yields even numbers up to n.
# Relevance: Useful for filtering specific sequences in data processing.
def even_numbers(n):
    for i in range(2, n + 1, 2):
        yield i

print(f"Exercise 3 Result: {list(even_numbers(10))}")  # Output: [2, 4, 6, 8, 10]

# Exercise 9: Fibonacci generator
# Problem: Write a generator `fibonacci` that yields Fibonacci numbers up to n terms.
# Relevance: Common in mathematical and algorithmic scenarios in industry.
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

print(f"Exercise 4 Result: {list(fibonacci(10))}")  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# Exercise 10: Generator for square numbers
# Problem: Write a generator `square_numbers` that yields squares of numbers up to n.
# Relevance: Useful in numerical simulations and computations.
def square_numbers(n):
    for i in range(1, n + 1):
        yield i ** 2

print(f"Exercise 5 Result: {list(square_numbers(5))}")  # Output: [1, 4, 9, 16, 25]

# Exercise 11: Generator for reading lines from a file
# Problem: Write a generator `read_lines` that yields lines from a file.
# Relevance: Efficient for processing large files line by line in data pipelines.
def read_lines(filename):
    with open(filename, 'r') as file:
        for line in file:
            yield line.strip()

# Uncomment to test with a file:
# print(f"Exercise 6 Result: {list(read_lines('example.txt'))}")

# Exercise 12: Reverse sequence generator
# Problem: Write a generator `reverse_sequence` that yields elements of a list in reverse order.
# Relevance: Useful in scenarios where data needs to be accessed in reverse.
def reverse_sequence(lst):
    for i in reversed(lst):
        yield i

print(f"Exercise 7 Result: {list(reverse_sequence([1, 2, 3, 4]))}")  # Output: [4, 3, 2, 1]

# Exercise 13: Generator for prime numbers
# Problem: Write a generator `prime_numbers` that yields prime numbers up to n.
# Relevance: Useful in cryptography and mathematical computations.
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_numbers(n):
    for i in range(2, n + 1):
        if is_prime(i):
            yield i

print(f"Exercise 8 Result: {list(prime_numbers(20))}")  # Output: [2, 3, 5, 7, 11, 13, 17, 19]

# Exercise 14: Generator for Cartesian product
# Problem: Write a generator `cartesian_product` that yields the Cartesian product of two lists.
# Relevance: Used in combinatorial problems and simulations.
def cartesian_product(list1, list2):
    for i in list1:
        for j in list2:
            yield (i, j)

print(f"Exercise 9 Result: {list(cartesian_product([1, 2], ['a', 'b']))}")
# Output: [(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b')]

# Exercise 15: Chunked data generator
# Problem: Write a generator `chunked` that yields chunks of size `chunk_size` from a list.
# Relevance: Efficient for processing data in smaller pieces to optimize memory usage.
def chunked(data, chunk_size):
    for i in range(0, len(data), chunk_size):
        yield data[i:i + chunk_size]

print(f"Exercise 10 Result: {list(chunked([1, 2, 3, 4, 5, 6], 2))}")
# Output: [[1, 2], [3, 4], [5, 6]]



################################# INTERMEDIATE #####################################


# Exercise 1: Paginated data generator
# Problem: Write a generator `paginate` that takes a list and a page size, yielding each page as a sublist.
# Relevance: Useful in handling large datasets by breaking them into smaller chunks for processing.
def paginate(data, page_size):
    for i in range(0, len(data), page_size):
        yield data[i:i + page_size]

data = list(range(1, 21))  # Sample dataset
print("Exercise 1 Result:")
for page in paginate(data, 5):
    print(page)
# Output: [1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]

# Exercise 2: Interleaved generator
# Problem: Write a generator `interleave` that alternates elements from two iterables.
# Relevance: Useful for combining data streams or interleaving log entries from multiple sources.
def interleave(iter1, iter2):
    for a, b in zip(iter1, iter2):
        yield a
        yield b

iter1 = [1, 2, 3]
iter2 = ['a', 'b', 'c']
print("\nExercise 2 Result:", list(interleave(iter1, iter2)))
# Output: [1, 'a', 2, 'b', 3, 'c']

# Exercise 3: Sliding window generator
# Problem: Write a generator `sliding_window` that yields sliding windows of size `n` from a list.
# Relevance: Common in time-series analysis and pattern detection tasks.
def sliding_window(data, window_size):
    for i in range(len(data) - window_size + 1):
        yield data[i:i + window_size]

data = [1, 2, 3, 4, 5]
print("\nExercise 3 Result:", list(sliding_window(data, 3)))
# Output: [[1, 2, 3], [2, 3, 4], [3, 4, 5]]

# Exercise 4: File chunk reader
# Problem: Write a generator `read_file_in_chunks` that reads a file in fixed-size chunks.
# Relevance: Efficiently processes large files without loading them entirely into memory.
def read_file_in_chunks(file_path, chunk_size):
    with open(file_path, 'r') as file:
        while chunk := file.read(chunk_size):
            yield chunk

# Uncomment to test with a file:
# print("\nExercise 4 Result:")
# for chunk in read_file_in_chunks('example.txt', 10):
#     print(chunk)

# Exercise 5: Batched computation
# Problem: Write a generator `batched_sum` that takes a list of numbers and yields the sum of batches of a given size.
# Relevance: Useful in distributed computations where operations are performed on data batches.
def batched_sum(data, batch_size):
    for i in range(0, len(data), batch_size):
        yield sum(data[i:i + batch_size])

data = [10, 20, 30, 40, 50, 60]
print("\nExercise 5 Result:", list(batched_sum(data, 2)))
# Output: [30, 70, 110]
