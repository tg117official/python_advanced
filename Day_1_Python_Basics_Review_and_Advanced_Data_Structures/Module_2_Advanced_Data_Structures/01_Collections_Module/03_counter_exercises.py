#################################### Basic ##################################################################

# Exercise 1: Word Frequency Counter
# Problem:
# Write a Python program that counts the frequency of each word in a given string.
#
# Code:

from collections import Counter

# Input string
text = "The quick brown fox jumps over the lazy dog"

# Split into words and count
word_count = Counter(text.split())

# Display the result
print(dict(word_count))


# Output:
# {'The': 1, 'quick': 1, 'brown': 1, 'fox': 1, 'jumps': 1, 'over': 1, 'the': 1, 'lazy': 1, 'dog': 1}




# Exercise 2: Character Frequency Counter
# Problem:
# Count the frequency of each character in a given string, ignoring spaces.
#
# Code:

from collections import Counter

# Input string
text = "hello world"

# Remove spaces and count characters
char_count = Counter(text.replace(" ", ""))

# Display the result
print(dict(char_count))


# Output:
# {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}




# Exercise 3: Most Common Elements
# Problem:
# Find the top 2 most common elements in a list.
#
# Code:

from collections import Counter

# Input list
numbers = [1, 2, 3, 4, 1, 2, 1, 2, 2, 3]

# Count elements and find most common
most_common = Counter(numbers).most_common(2)

# Display the result
print(most_common)


# Output:
# [(2, 4), (1, 3)]




# Exercise 4: Removing Low Frequency Elements
# Problem:
# Remove elements that occur only once in a list of words.
#
# Code:

from collections import Counter

# Input list
words = ['apple', 'banana', 'apple', 'orange', 'banana', 'grape']

# Count elements
word_count = Counter(words)

# Filter elements with frequency > 1
filtered_words = {word: count for word, count in word_count.items() if count > 1}

# Display the result
print(filtered_words)


# Output:
# {'apple': 2, 'banana': 2}




# Exercise 5: Combining Two Counters
# Problem:
# Combine the counts of two inventories represented as `Counter` objects.
#
# Code:

from collections import Counter

# Input counters
store_1 = Counter({'apple': 3, 'banana': 2, 'orange': 1})
store_2 = Counter({'banana': 3, 'orange': 4, 'grape': 2})

# Combine counters
combined_inventory = store_1 + store_2

# Display the result
print(dict(combined_inventory))


# Output:
# {'apple': 3, 'banana': 5, 'orange': 5, 'grape': 2}




# Exercise 6: Count Words Ignoring Case
# Problem:
# Count the frequency of each word in a string, ignoring the case.
#
# Code:

from collections import Counter

# Input string
text = "Python is fun. python is versatile. PYTHON is powerful."

# Convert to lowercase and split into words
word_count = Counter(text.lower().split())

# Display the result
print(dict(word_count))


# Expected Output:
# {'python': 3, 'is': 3, 'fun.': 1, 'versatile.': 1, 'powerful.': 1}




# Exercise 7: Subtract Elements in Counters
# Problem:
# Create two counters and subtract the counts of one counter from another.
#
# Code:

from collections import Counter

# Input counters
inventory_1 = Counter({'apple': 5, 'banana': 3, 'orange': 2})
inventory_2 = Counter({'apple': 2, 'orange': 1, 'grape': 4})

# Subtract inventory_2 from inventory_1
remaining_inventory = inventory_1 - inventory_2

# Display the result
print(dict(remaining_inventory))


# Expected Output:
# {'apple': 3, 'banana': 3, 'orange': 1}




# Exercise 8: Count Elements in a Nested List
# Problem:
# Count the frequency of elements in a nested list.
#
# Code:

from collections import Counter

# Input nested list
nested_list = [[1, 2, 3], [1, 2], [3, 4, 5, 1]]

# Flatten the list and count elements
flat_list = [item for sublist in nested_list for item in sublist]
element_count = Counter(flat_list)

# Display the result
print(dict(element_count))


# Expected Output:
# {1: 3, 2: 2, 3: 2, 4: 1, 5: 1}




# Exercise 9: Elements Method
# Problem:
# Use the `elements()` method of `Counter` to list all the elements in the counter based on their counts.
#
# Code:

from collections import Counter

# Input counter
counter = Counter({'apple': 3, 'banana': 1, 'orange': 2})

# List all elements based on their counts
all_elements = list(counter.elements())

# Display the result
print(all_elements)


# Expected Output:
# ['apple', 'apple', 'apple', 'banana', 'orange', 'orange']




# Exercise 10: Find Least Common Elements
# Problem:
# Find the least common elements in a list using `Counter`.
#
# Code:

from collections import Counter

# Input list
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

# Count elements
number_count = Counter(numbers)

# Find least common elements
least_common = number_count.most_common()[:-2:-1]

# Display the result
print(least_common)


# Expected Output:
# [(1, 1)]


############################################ INTERMEDIATE ###########################################

# Exercise 1: Count Overlapping Elements in Two Lists
# Problem:
# Given two lists, count the overlapping elements and their frequencies using `Counter`.
#
# Code:

from collections import Counter

# Input lists
list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 4, 5, 6, 6, 6, 7, 8]

# Count elements in each list
counter1 = Counter(list1)
counter2 = Counter(list2)

# Find overlap
overlap = counter1 & counter2

# Display the result
print(dict(overlap))


# Expected Output:
# {4: 1, 5: 1, 6: 1}




# Exercise 2: Combine Counters with Weights
# Problem:
# Combine two counters with different weights (scaling the counts of one counter).
#
# Code:

from collections import Counter

# Input counters
counter1 = Counter({'a': 3, 'b': 5, 'c': 2})
counter2 = Counter({'a': 4, 'b': 2, 'c': 6})

# Apply weights
weighted_counter1 = Counter({key: value * 2 for key, value in counter1.items()})
combined = weighted_counter1 + counter2

# Display the result
print(dict(combined))


# Expected Output:
# {'a': 10, 'b': 12, 'c': 10}




# Exercise 3: Filter Counter Based on Threshold
# Problem:
# Given a list of words, use `Counter` to count the words and filter out those that occur less than 3 times.
#
# Code:

from collections import Counter

# Input list
words = ['apple', 'banana', 'apple', 'orange', 'banana', 'grape', 'apple', 'banana', 'banana']

# Count words
word_count = Counter(words)

# Filter words
filtered_words = {word: count for word, count in word_count.items() if count >= 3}

# Display the result
print(filtered_words)


# Expected Output:
# {'apple': 3, 'banana': 4}




# Exercise 4: Compare Two Texts
# Problem:
# Compare the frequencies of characters in two strings and identify characters that appear more frequently in one string than the other.
#
# Code:

from collections import Counter

# Input strings
text1 = "hello world"
text2 = "world peace"

# Count characters in each text
counter1 = Counter(text1.replace(" ", ""))
counter2 = Counter(text2.replace(" ", ""))

# Compare frequencies
difference = counter1 - counter2

# Display the result
print(dict(difference))


# Expected Output:
# {'h': 1, 'e': 1, 'l': 2}




# Exercise 5: Top N Most Common in Nested List
# Problem:
# Count the frequency of all elements in a nested list and find the top 3 most common elements.
#
# Code:

from collections import Counter

# Input nested list
nested_list = [[1, 2, 3], [1, 2, 2, 4], [3, 4, 4, 5]]

# Flatten the list and count elements
flat_list = [item for sublist in nested_list for item in sublist]
element_count = Counter(flat_list)

# Find top 3 most common
top_3 = element_count.most_common(3)

# Display the result
print(top_3)


# Expected Output:
# [(4, 3), (2, 3), (1, 2)]



