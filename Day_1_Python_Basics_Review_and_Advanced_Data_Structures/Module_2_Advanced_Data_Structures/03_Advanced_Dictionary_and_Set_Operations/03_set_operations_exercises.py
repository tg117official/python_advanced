
############################################## BASIC ###############################################

# 1. Create a Set
# Description: Create a set from a list of elements.
#
# Code:

my_set = set([1, 2, 3, 4])
print(my_set)


# Output:
#
# {1, 2, 3, 4}




# 2. Add an Element to a Set
# Description: Add a single element to a set using `add()`.
#
# Code:

my_set = {1, 2, 3}
my_set.add(4)
print(my_set)


# Output:
#
# {1, 2, 3, 4}




# 3. Remove an Element
# Description: Remove an element using `remove()` (raises an error if the element does not exist) or `discard()` (does not raise an error).
#
# Code:

my_set = {1, 2, 3}
my_set.remove(2)
my_set.discard(4)  # Does nothing as 4 is not in the set
print(my_set)


# Output:
#
# {1, 3}




# 4. Check Membership
# Description: Check if an element exists in a set using `in`.
#
# Code:

my_set = {1, 2, 3}
print(2 in my_set)  # True
print(5 in my_set)  # False


# Output:
#
# True
# False




# 5. Union of Sets
# Description: Combine elements from two sets using the `union()` method or `|` operator.
#
# Code:

set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)
# or
# union_set = set1 | set2
print(union_set)


# Output:
#
# {1, 2, 3, 4, 5}




# 6. Intersection of Sets
# Description: Find common elements between two sets using `intersection()` or `&` operator.
#
# Code:

set1 = {1, 2, 3}
set2 = {2, 3, 4}
intersection_set = set1.intersection(set2)
# or
# intersection_set = set1 & set2
print(intersection_set)


# Output:
#
# {2, 3}




# 7. Difference of Sets
# Description: Find elements in one set but not in another using `difference()` or `-` operator.
#
# Code:

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5}
difference_set = set1.difference(set2)
# or
# difference_set = set1 - set2
print(difference_set)


# Output:
#
# {1, 2}




# 8. Symmetric Difference
# Description: Find elements in either set but not in both using `symmetric_difference()` or `^` operator.
#
# Code:

set1 = {1, 2, 3}
set2 = {3, 4, 5}
symmetric_difference_set = set1.symmetric_difference(set2)
# or
# symmetric_difference_set = set1 ^ set2
print(symmetric_difference_set)


# Output:
#
# {1, 2, 4, 5}




# 9. Clear a Set
# Description: Remove all elements from a set using `clear()`.
#
# Code:

my_set = {1, 2, 3}
my_set.clear()
print(my_set)


# Output:
#
# set()




# 10. Subset and Superset
# Description: Check if a set is a subset or superset of another set using `issubset()` and `issuperset()`.
#
# Code:

set1 = {1, 2}
set2 = {1, 2, 3, 4}
print(set1.issubset(set2))  # True
print(set2.issuperset(set1))  # True


# Output:
#
# True
# True


############################################# INTERMEDIATE #########################################


# Exercise 1: Find the Common Elements Across Multiple Sets
# Problem:
# Find the intersection of three sets.
#
# Code:

# Input sets
set1 = {1, 2, 3, 4}
set2 = {2, 3, 5, 6}
set3 = {3, 4, 7, 8}

# Find common elements
common_elements = set1 & set2 & set3

# Display the result
print(common_elements)


# Expected Output:
#
# {3}




# Exercise 2: Remove Duplicates from a List Using Sets
# Problem:
# Given a list with duplicate elements, use a set to remove duplicates and retain unique elements.
#
# Code:

# Input list
numbers = [1, 2, 2, 3, 4, 4, 5]

# Remove duplicates
unique_numbers = set(numbers)

# Convert back to a list (optional)
unique_numbers_list = list(unique_numbers)

# Display the result
print(unique_numbers_list)


# Expected Output:
#
# [1, 2, 3, 4, 5]




# Exercise 3: Find Missing Elements
# Problem:
# Given two sets, find elements that are in one set but not in the other.
#
# Code:

# Input sets
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Find missing elements
missing_from_set2 = set1 - set2
missing_from_set1 = set2 - set1

# Display the results
print("Missing from set2:", missing_from_set2)
print("Missing from set1:", missing_from_set1)


# Expected Output:
#
# Missing from set2: {1, 2}
# Missing from set1: {5, 6}




# Exercise 4: Check for Disjoint Sets
# Problem:
# Check if two sets have no elements in common using `isdisjoint()`.
#
# Code:

# Input sets
set1 = {1, 2, 3}
set2 = {4, 5, 6}

# Check if the sets are disjoint
are_disjoint = set1.isdisjoint(set2)

# Display the result
print("Are the sets disjoint?", are_disjoint)


# Expected Output:
#
# Are the sets disjoint? True




# Exercise 5: Find Symmetric Difference Across Multiple Sets
# Problem:
# Find the symmetric difference of three sets (elements that are unique to each set).
#
# Code:

# Input sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3 = {5, 6, 7}

# Find symmetric difference
symmetric_diff = set1 ^ set2 ^ set3

# Display the result
print("Symmetric difference:", symmetric_diff)


# Expected Output:
#
# Symmetric difference: {1, 2, 4, 6, 7}


############################################## ADVANCED  #######################################



# Exercise 1: Find Unique Elements Across Multiple Sets
# Problem:
# Given multiple sets, find the elements that are unique to each set (not shared with any other set).
#
# Code:

# Input sets
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
set3 = {5, 6, 7, 8}

# Find unique elements in each set
unique_to_set1 = set1 - (set2 | set3)
unique_to_set2 = set2 - (set1 | set3)
unique_to_set3 = set3 - (set1 | set2)

# Combine all unique elements
unique_elements = unique_to_set1 | unique_to_set2 | unique_to_set3

# Display the result
print("Unique elements across sets:", unique_elements)


# Expected Output:
#
# Unique elements across sets: {1, 2, 7, 8}




# Exercise 2: Cartesian Product Using Sets
# Problem:
# Given two sets, generate the Cartesian product (all ordered pairs) of the sets.
#
# Code:

# Input sets
set1 = {1, 2}
set2 = {'a', 'b'}

# Find the Cartesian product
cartesian_product = {(x, y) for x in set1 for y in set2}

# Display the result
print("Cartesian product:", cartesian_product)


# Expected Output:
#
# Cartesian product: {(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b')}




# Exercise 3: Partition a Set
# Problem:
# Partition a set into two subsets: one containing elements divisible by 2, and the other containing the rest.
#
# Code:

# Input set
numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9}

# Partition the set
divisible_by_2 = {x for x in numbers if x % 2 == 0}
not_divisible_by_2 = numbers - divisible_by_2

# Display the result
print("Divisible by 2:", divisible_by_2)
print("Not divisible by 2:", not_divisible_by_2)


# Expected Output:
#
# Divisible by 2: {2, 4, 6, 8}
# Not divisible by 2: {1, 3, 5, 7, 9}




# Exercise 4: Find the Power Set
# Problem:
# Generate the power set of a set (all possible subsets, including the empty set and the set itself).
#
# Code:

from itertools import chain, combinations

# Input set
my_set = {1, 2, 3}

# Generate power set
power_set = {frozenset(subset) for subset in chain.from_iterable(combinations(my_set, r) for r in range(len(my_set) + 1))}

# Display the result
print("Power set:", power_set)


# Expected Output:
#
# Power set: {frozenset(), frozenset({1}), frozenset({2}), frozenset({3}), frozenset({1, 2}), frozenset({1, 3}), frozenset({2, 3}), frozenset({1, 2, 3})}




# Exercise 5: Analyze a Dataset Using Sets
# Problem:
# Given two sets representing students enrolled in Math and Science classes, find:
# 1. Students taking both classes.
# 2. Students taking only one class.
# 3. Total unique students.
#
# Code:

# Input sets
math_students = {'Alice', 'Bob', 'Charlie', 'David'}
science_students = {'Charlie', 'David', 'Eve', 'Frank'}

# Students taking both classes
both_classes = math_students & science_students

# Students taking only one class
only_one_class = (math_students ^ science_students)

# Total unique students
total_students = math_students | science_students

# Display the results
print("Both classes:", both_classes)
print("Only one class:", only_one_class)
print("Total unique students:", total_students)


# Expected Output:
#
# Both classes: {'Charlie', 'David'}
# Only one class: {'Alice', 'Eve', 'Frank', 'Bob'}
# Total unique students: {'Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank'}


# Exercise 6: Detect Duplicates Across Multiple Lists
# Problem:
# Given multiple lists, determine if any duplicate elements exist across all lists.
#
# Code:

# Input lists
list1 = [1, 2, 3, 4]
list2 = [3, 5, 6, 7]
list3 = [7, 8, 9, 1]

# Convert lists to sets
set1, set2, set3 = set(list1), set(list2), set(list3)

# Find duplicates across all lists
duplicates = set1 & set2 & set3

# Display the result
print("Duplicate elements across lists:", duplicates)


# Expected Output:
#
# Duplicate elements across lists: set()  # No common duplicates across all three lists




# Exercise 7: Group Elements by Parity
# Problem:
# Partition a set of integers into subsets of even and odd numbers, and find the difference between the two sets.
#
# Code:

# Input set
numbers = {10, 15, 20, 25, 30, 35}

# Partition into even and odd sets
even_numbers = {x for x in numbers if x % 2 == 0}
odd_numbers = {x for x in numbers if x % 2 != 0}

# Find the difference
difference = even_numbers - odd_numbers

# Display the results
print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)
print("Difference (even - odd):", difference)


# Expected Output:
#
# Even numbers: {10, 20, 30}
# Odd numbers: {15, 25, 35}
# Difference (even - odd): {10, 20, 30}




# Exercise 8: Symmetric Difference Across Three Sets
# Problem:
# Find the symmetric difference across three sets (elements that are in any set but not in all).
#
# Code:

# Input sets
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
set3 = {5, 6, 7, 8}

# Symmetric difference across three sets
symmetric_diff = set1 ^ set2 ^ set3

# Display the result
print("Symmetric difference across three sets:", symmetric_diff)


# Expected Output:
#
# Symmetric difference across three sets: {1, 2, 7, 8}




# Exercise 9: Find Subsets Within a Set
# Problem:
# Generate all subsets of a set that have a specific size, e.g., subsets of size 2.
#
# Code:

from itertools import combinations

# Input set
my_set = {1, 2, 3, 4}

# Find subsets of size 2
subsets_of_size_2 = {frozenset(comb) for comb in combinations(my_set, 2)}

# Display the result
print("Subsets of size 2:", subsets_of_size_2)


# Expected Output:
#
# Subsets of size 2: {frozenset({1, 2}), frozenset({1, 3}), frozenset({1, 4}), frozenset({2, 3}), frozenset({2, 4}), frozenset({3, 4})}




# Exercise 10 : Find Maximum and Minimum Elements in a Set
# Problem:
# Find the maximum and minimum elements of a set, and determine the difference between them.
#
# Code:

# Input set
numbers = {45, 12, 78, 34, 56, 89, 23}

# Find max and min
max_element = max(numbers)
min_element = min(numbers)

# Calculate the difference
difference = max_element - min_element

# Display the result
print("Maximum element:", max_element)
print("Minimum element:", min_element)
print("Difference:", difference)


# Expected Output:
#
# Maximum element: 89
# Minimum element: 12
# Difference: 77



