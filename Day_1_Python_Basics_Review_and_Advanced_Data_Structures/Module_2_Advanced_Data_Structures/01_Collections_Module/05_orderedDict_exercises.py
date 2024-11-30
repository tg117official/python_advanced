
#################################### BASIC #############################################

# Exercise 1: Creating and Displaying an OrderedDict
# Problem:
# Create an `OrderedDict` with three key-value pairs and display the keys in the order they were added.
#
# Code:

from collections import OrderedDict

# Create an OrderedDict
ordered_dict = OrderedDict()
ordered_dict['apple'] = 1
ordered_dict['banana'] = 2
ordered_dict['cherry'] = 3

# Display the keys
print(list(ordered_dict.keys()))


# Expected Output:
#
# ['apple', 'banana', 'cherry']




# Exercise 2: Compare OrderedDict with Regular Dictionary
# Problem:
# Create a regular dictionary and an `OrderedDict` with the same key-value pairs but in different orders. Compare if they are considered equal.
#
# Code:

from collections import OrderedDict

# Create a regular dictionary and an OrderedDict
dict1 = {'a': 1, 'b': 2, 'c': 3}
ordered_dict = OrderedDict([('a', 1), ('b', 2), ('c', 3)])

# Compare
print(dict1 == ordered_dict)


# Expected Output:
#
# True




# Exercise 3: Rearrange an OrderedDict
# Problem:
# Create an `OrderedDict`, move a key to the end, and display the updated order of keys.
#
# Code:

from collections import OrderedDict

# Create an OrderedDict
ordered_dict = OrderedDict([('x', 10), ('y', 20), ('z', 30)])

# Move 'y' to the end
ordered_dict.move_to_end('y')

# Display the keys
print(list(ordered_dict.keys()))


# Expected Output:
#
# ['x', 'z', 'y']




# Exercise 4: Sort an OrderedDict by Keys
# Problem:
# Create an `OrderedDict` and sort it by keys. Display the updated dictionary.
#
# Code:

from collections import OrderedDict

# Create an OrderedDict
unordered_dict = OrderedDict([('c', 3), ('a', 1), ('b', 2)])

# Sort by keys
sorted_dict = OrderedDict(sorted(unordered_dict.items()))

# Display the result
print(sorted_dict)


# Expected Output:
#
# OrderedDict([('a', 1), ('b', 2), ('c', 3)])




# Exercise 5: Remove and Add Items in OrderedDict
# Problem:
# Create an `OrderedDict`, remove the first item, and add a new key-value pair at the end.
#
# Code:

from collections import OrderedDict

# Create an OrderedDict
ordered_dict = OrderedDict([('apple', 1), ('banana', 2), ('cherry', 3)])

# Remove the first item
ordered_dict.popitem(last=False)

# Add a new item
ordered_dict['date'] = 4

# Display the updated OrderedDict
print(ordered_dict)


# Expected Output:
# OrderedDict([('banana', 2), ('cherry', 3), ('date', 4)])




