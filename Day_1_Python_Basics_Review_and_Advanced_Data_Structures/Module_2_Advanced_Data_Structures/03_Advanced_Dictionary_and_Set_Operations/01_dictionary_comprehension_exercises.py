####################################### BASIC ##########################################

# Exercise 1: Square of Numbers
# Problem:
# Create a dictionary where the keys are numbers from 1 to 5, and the values are their squares.
#
# Code:

# Dictionary comprehension
squares = {x: x**2 for x in range(1, 6)}

# Display the result
print(squares)


# Expected Output:
#
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}




# Exercise 2: Uppercase Keys
# Problem:
# Given a dictionary, create a new dictionary with the keys converted to uppercase.
#
# Code:

# Input dictionary
original_dict = {'apple': 1, 'banana': 2, 'cherry': 3}

# Dictionary comprehension
uppercase_keys = {key.upper(): value for key, value in original_dict.items()}

# Display the result
print(uppercase_keys)


# Expected Output:
#
# {'APPLE': 1, 'BANANA': 2, 'CHERRY': 3}




# Exercise 3: Filter Even Values
# Problem:
# Create a dictionary from a range of numbers (1 to 10) where the keys are the numbers and the values are the numbers themselves, but only include even numbers.
#
# Code:

# Dictionary comprehension
even_numbers = {x: x for x in range(1, 11) if x % 2 == 0}

# Display the result
print(even_numbers)


# Expected Output:
#
# {2: 2, 4: 4, 6: 6, 8: 8, 10: 10}




# Exercise 4: Word Lengths
# Problem:
# Given a list of words, create a dictionary where the keys are the words and the values are their lengths.
#
# Code:

# Input list
words = ['python', 'java', 'c', 'javascript']

# Dictionary comprehension
word_lengths = {word: len(word) for word in words}

# Display the result
print(word_lengths)


# Expected Output:
#
# {'python': 6, 'java': 4, 'c': 1, 'javascript': 10}




# Exercise 5: Reverse Key-Value Pairs
# Problem:
# Given a dictionary, create a new dictionary where the keys are the original values, and the values are the original keys.
#
# Code:

# Input dictionary
original_dict = {'a': 1, 'b': 2, 'c': 3}

# Dictionary comprehension
reversed_dict = {value: key for key, value in original_dict.items()}

# Display the result
print(reversed_dict)


# Expected Output:
#
# {1: 'a', 2: 'b', 3: 'c'}


################################# INTERMEDIATE #######################################


# Exercise 1: Filter and Transform a Dictionary
# Problem:
# Given a dictionary of student names and their marks, create a new dictionary that only includes students with marks greater than 50, and multiply their marks by 2.
#
# Code:

# Input dictionary
students = {'Alice': 45, 'Bob': 82, 'Charlie': 58, 'David': 49, 'Eve': 90}

# Dictionary comprehension
filtered_transformed = {name: marks * 2 for name, marks in students.items() if marks > 50}

# Display the result
print(filtered_transformed)


# Expected Output:
#
# {'Bob': 164, 'Charlie': 116, 'Eve': 180}




# Exercise 2: Combine Two Lists into a Dictionary
# Problem:
# Given two lists, one of keys and another of values, create a dictionary using dictionary comprehension. If the lists are of unequal lengths, use `None` for missing values.
#
# Code:

# Input lists
keys = ['a', 'b', 'c', 'd']
values = [1, 2, 3]

# Dictionary comprehension
combined_dict = {keys[i]: values[i] if i < len(values) else None for i in range(len(keys))}

# Display the result
print(combined_dict)


# Expected Output:
#
# {'a': 1, 'b': 2, 'c': 3, 'd': None}




# Exercise 3: Frequency Counter
# Problem:
# Given a list of words, create a dictionary that counts the frequency of each word using dictionary comprehension.
#
# Code:

# Input list
words = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']

# Dictionary comprehension
word_count = {word: words.count(word) for word in set(words)}

# Display the result
print(word_count)


# Expected Output:
#
# {'orange': 1, 'banana': 2, 'apple': 3}




# Exercise 4: Nested Dictionary Comprehension
# Problem:
# Create a nested dictionary where the outer keys are numbers from 1 to 3, and the inner dictionary contains the number and its square.
#
# Code:

# Nested dictionary comprehension
nested_dict = {x: {'number': x, 'square': x**2} for x in range(1, 4)}

# Display the result
print(nested_dict)


# Expected Output:
#
# {1: {'number': 1, 'square': 1}, 2: {'number': 2, 'square': 4}, 3: {'number': 3, 'square': 9}}




# Exercise 5: Merge Two Dictionaries
# Problem:
# Given two dictionaries, merge them into a new dictionary using dictionary comprehension. In case of key conflicts, use the value from the second dictionary.
#
# Code:

# Input dictionaries
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 20, 'c': 30, 'd': 40}

# Dictionary comprehension
merged_dict = {key: dict2.get(key, dict1.get(key)) for key in dict1.keys() | dict2.keys()}

# Display the result
print(merged_dict)


# Expected Output:
#
# {'a': 1, 'b': 20, 'c': 30, 'd': 40}
