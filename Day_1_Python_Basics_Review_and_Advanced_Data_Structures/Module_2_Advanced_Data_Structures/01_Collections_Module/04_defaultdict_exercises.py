
######################################## BASIC ######################################


# Exercise 1: Grouping Words by Their Length
# Problem:
# Use `defaultdict` to group words in a list based on their lengths.
#
# Code:

from collections import defaultdict

# Input list
words = ["apple", "banana", "pear", "kiwi", "grape"]

# Group words by length
grouped = defaultdict(list)
for word in words:
    grouped[len(word)].append(word)

# Display the result
print(dict(grouped))


# Expected Output:
# {5: ['apple', 'grape'], 6: ['banana'], 4: ['pear', 'kiwi']}




# Exercise 2: Counting Frequency of Characters
# Problem:
# Use `defaultdict` to count the frequency of characters in a string.
#
# Code:

from collections import defaultdict

# Input string
text = "hello world"

# Count character frequency
char_count = defaultdict(int)
for char in text.replace(" ", ""):
    char_count[char] += 1

# Display the result
print(dict(char_count))


# Expected Output:
# {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}




# Exercise 3: Creating a Dictionary with Default Values
# Problem:
# Use `defaultdict` to store students' scores, with a default value of 0 for subjects not entered.
#
# Code:

from collections import defaultdict

# Initialize defaultdict with default value 0
scores = defaultdict(int)

# Add some scores
scores['Math'] = 95
scores['Science'] = 88

# Access a non-existing key
print("Math score:", scores['Math'])
print("History score (default):", scores['History'])


# Expected Output:
# Math score: 95
# History score (default): 0




# Exercise 4: Appending Values to Keys
# Problem:
# Use `defaultdict` to store multiple values for a single key (e.g., students in the same class).
#
# Code:

from collections import defaultdict

# Input list of students and their classes
students = [("Class A", "John"), ("Class B", "Alice"), ("Class A", "Bob"), ("Class B", "Carol")]

# Group students by class
class_dict = defaultdict(list)
for cls, student in students:
    class_dict[cls].append(student)

# Display the result
print(dict(class_dict))


# Expected Output:
# {'Class A': ['John', 'Bob'], 'Class B': ['Alice', 'Carol']}




# Exercise 5: Initialize Nested Dictionaries
# Problem:
# Use `defaultdict` to create a nested dictionary structure for storing data.
#
# Code:

from collections import defaultdict

# Create a nested defaultdict
nested_dict = defaultdict(lambda: defaultdict(int))

# Add some values
nested_dict['Alice']['Math'] = 90
nested_dict['Alice']['Science'] = 85
nested_dict['Bob']['Math'] = 78

# Access values
print(nested_dict['Alice']['Math'])
print(nested_dict['Bob']['Science'])  # Default value for non-existing key


# Expected Output:
# 90
# 0


######################################### INTERMEDIATE #######################################


# Exercise 1: Grouping Words by First Letter
# Problem:
# Use `defaultdict` to group words from a list by their first letter.
#
# Code:

from collections import defaultdict

# Input list of words
words = ["apple", "banana", "apricot", "blueberry", "cherry", "avocado"]

# Group words by first letter
grouped = defaultdict(list)
for word in words:
    grouped[word[0]].append(word)

# Display the result
print(dict(grouped))


# Expected Output:
# {'a': ['apple', 'apricot', 'avocado'], 'b': ['banana', 'blueberry'], 'c': ['cherry']}




# Exercise 2: Word Frequency by Line
# Problem:
# Use `defaultdict` to count the frequency of words in each line of a multiline string.
#
# Code:

from collections import defaultdict

# Input multiline string
text = """apple banana apple
banana cherry apple
cherry cherry banana"""

# Count word frequency by line
line_word_count = defaultdict(lambda: defaultdict(int))
for line_no, line in enumerate(text.splitlines(), start=1):
    for word in line.split():
        line_word_count[line_no][word] += 1

# Display the result
print({line: dict(word_count) for line, word_count in line_word_count.items()})


# Expected Output:
# {1: {'apple': 2, 'banana': 1}, 2: {'banana': 1, 'cherry': 1, 'apple': 1}, 3: {'cherry': 2, 'banana': 1}}




# Exercise 3: Create an Adjacency List
# Problem:
# Use `defaultdict` to represent a graph as an adjacency list.
#
# Code:

from collections import defaultdict

# Input edges of a graph
edges = [("A", "B"), ("A", "C"), ("B", "D"), ("C", "D"), ("D", "E")]

# Create adjacency list
graph = defaultdict(list)
for start, end in edges:
    graph[start].append(end)

# Display the result
print(dict(graph))


# Expected Output:
# {'A': ['B', 'C'], 'B': ['D'], 'C': ['D'], 'D': ['E']}




# Exercise 4: Count Pair Occurrences
# Problem:
# Use `defaultdict` to count the number of occurrences of pairs in a list of tuples.
#
# Code:

from collections import defaultdict

# Input list of pairs
pairs = [("apple", "banana"), ("apple", "banana"), ("banana", "cherry"), ("apple", "cherry")]

# Count occurrences of pairs
pair_count = defaultdict(int)
for pair in pairs:
    pair_count[pair] += 1

# Display the result
print(dict(pair_count))


# Expected Output:
# {('apple', 'banana'): 2, ('banana', 'cherry'): 1, ('apple', 'cherry'): 1}




# Exercise 5: Invert a Dictionary with Multiple Values
# Problem:
# Use `defaultdict` to invert a dictionary where each key maps to multiple values.
#
# Code:

from collections import defaultdict

# Input dictionary
original_dict = {
    "fruit": ["apple", "banana"],
    "vegetable": ["carrot", "broccoli"],
    "grain": ["wheat", "rice"]
}

# Invert the dictionary
inverted_dict = defaultdict(list)
for key, values in original_dict.items():
    for value in values:
        inverted_dict[value].append(key)

# Display the result
print(dict(inverted_dict))


# Expected Output:
# {'apple': ['fruit'], 'banana': ['fruit'], 'carrot': ['vegetable'], 'broccoli': ['vegetable'], 'wheat': ['grain'], 'rice': ['grain']}




