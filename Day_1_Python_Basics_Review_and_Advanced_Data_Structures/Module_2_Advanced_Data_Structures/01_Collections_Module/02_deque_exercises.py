# Exercise 1: Initialize and Append Elements
# Create a deque, append the numbers 1, 2, and 3 to it, and print the resulting deque.
#
# Solution:

from collections import deque

# Initialize a deque
d = deque()

# Append elements
d.append(1)
d.append(2)
d.append(3)

# Print the deque
print(d)


# Output:
# deque([1, 2, 3])




# Exercise 2: Insert Elements at Both Ends
# Create a deque and add elements to both ends. Insert 10 at the left and 20 at the right.
#
# Solution:

from collections import deque

# Initialize a deque
d = deque()

# Add elements to both ends
d.appendleft(10)
d.append(20)

# Print the deque
print(d)


# Output:
# deque([10, 20])




# Exercise 3: Remove Elements from Both Ends
# Create a deque with the elements [1, 2, 3, 4]. Remove an element from the left and the right, and print the resulting deque.
#
# Solution:

from collections import deque

# Create a deque
d = deque([1, 2, 3, 4])

# Remove elements from both ends
d.popleft()
d.pop()

# Print the deque
print(d)


# Output:
# deque([2, 3])




# Exercise 4: Rotate the Deque
# Create a deque with the elements [10, 20, 30, 40, 50]. Rotate it 2 steps to the right and print the resulting deque.
#
# Solution:

from collections import deque

# Create a deque
d = deque([10, 20, 30, 40, 50])

# Rotate 2 steps to the right
d.rotate(2)

# Print the deque
print(d)

#
# Output:
#
# deque([40, 50, 10, 20, 30])




# Exercise 5: Extend the Deque
# Create a deque with elements [1, 2]. Extend it by adding the elements [3, 4, 5] to the right.

# Solution:

from collections import deque

# Create a deque
d = deque([1, 2])

# Extend the deque
d.extend([3, 4, 5])

# Print the deque
print(d)


# Output:
# deque([1, 2, 3, 4, 5])



# Exercise 6: Check the Length of a Deque
# Create a deque with the elements `[5, 10, 15, 20]` and find the length of the deque.
#
# Solution:

from collections import deque

# Create a deque
d = deque([5, 10, 15, 20])

# Find and print the length
print(len(d))


# Output:
# 4




# Exercise 7: Clear All Elements
# Create a deque with elements `[1, 2, 3, 4, 5]`, clear all elements, and check if the deque is empty.
#
# Solution:

from collections import deque

# Create a deque
d = deque([1, 2, 3, 4, 5])

# Clear all elements
d.clear()

# Check if deque is empty
print(d)


# Output:
# deque([])




# Exercise 8: Access First and Last Elements
# Create a deque with elements `[100, 200, 300, 400]`. Access and print the first and last elements without removing them.
#
# Solution:

from collections import deque

# Create a deque
d = deque([100, 200, 300, 400])

# Access and print the first and last elements
print("First element:", d[0])
print("Last element:", d[-1])


# Output:
# First element: 100
# Last element: 400




# Exercise 9: Reverse a Deque
# Create a deque with the elements `[10, 20, 30, 40]` and reverse its order.
#
# Solution:

from collections import deque

# Create a deque
d = deque([10, 20, 30, 40])

# Reverse the deque
d.reverse()

# Print the reversed deque
print(d)


# Output:
# deque([40, 30, 20, 10])




# Exercise 10: Count Occurrences of an Element
# Create a deque with elements `[1, 2, 2, 3, 4, 2, 5]` and count how many times `2` appears in the deque.
#
# Solution:

from collections import deque

# Create a deque
d = deque([1, 2, 2, 3, 4, 2, 5])

# Count occurrences of 2
count = d.count(2)

# Print the count
print(count)


# Output:
# 3



################################################### INTERMEDIATE EXERCISES ########################################################


# Exercise 1: Simulate a Queue with Fixed Size
# Create a deque with a maximum size of 5. Simulate adding elements [1, 2, 3, 4, 5, 6, 7] to the deque.
# Observe and explain what happens when the deque exceeds its maximum size.
#
# Solution:

from collections import deque

# Create a deque with a maximum size of 5
d = deque(maxlen=5)

# Add elements to the deque
for i in [1, 2, 3, 4, 5, 6, 7]:
    d.append(i)
    print(f"Deque after adding {i}: {d}")

# Explanation:
# When the deque exceeds its maximum size, the oldest element (from the left) is automatically removed.


# Output:
# Deque after adding 1: deque([1], maxlen=5)
# Deque after adding 2: deque([1, 2], maxlen=5)
# Deque after adding 3: deque([1, 2, 3], maxlen=5)
# Deque after adding 4: deque([1, 2, 3, 4], maxlen=5)
# Deque after adding 5: deque([1, 2, 3, 4, 5], maxlen=5)
# Deque after adding 6: deque([2, 3, 4, 5, 6], maxlen=5)
# Deque after adding 7: deque([3, 4, 5, 6, 7], maxlen=5)




# Exercise 2: Rotate and Reverse Together
# Create a deque with the elements `[10, 20, 30, 40, 50]`. First, rotate it 2 steps to the left, and then reverse the deque.
#
# Solution:

from collections import deque

# Create a deque
d = deque([10, 20, 30, 40, 50])

# Rotate 2 steps to the left
d.rotate(-2)

# Reverse the deque
d.reverse()

# Print the final deque
print(d)


# Output:
# deque([30, 20, 10, 50, 40])




# Exercise 3: Filter Elements in a Deque
# Create a deque with elements `[5, 12, 15, 20, 25, 30]`. Filter out all elements greater than 20 and create a new deque containing only the filtered elements.
#
# Solution:

from collections import deque

# Create a deque
d = deque([5, 12, 15, 20, 25, 30])

# Filter elements greater than 20
filtered_d = deque(x for x in d if x <= 20)

# Print the new deque
print(filtered_d)


# Output:
# deque([5, 12, 15, 20])




# Exercise 4: Merge Two Deques
# Create two deques: `d1 = deque([1, 2, 3])` and `d2 = deque([4, 5, 6])`. Merge them such that the elements of `d2` are appended to `d1`, and then reverse the merged deque.
#
# Solution:

from collections import deque

# Create two deques
d1 = deque([1, 2, 3])
d2 = deque([4, 5, 6])

# Merge d2 into d1
d1.extend(d2)

# Reverse the merged deque
d1.reverse()

# Print the final deque
print(d1)


# Output:
# deque([6, 5, 4, 3, 2, 1])




# Exercise 5: Simulate a Sliding Window
# Given a list `[10, 20, 30, 40, 50, 60]`, use a deque with a maximum size of 3 to simulate a sliding window over the list. Print the deque after each step.
#
# Solution:

from collections import deque

# Initialize a deque with max size of 3
window = deque(maxlen=3)

# List to process
nums = [10, 20, 30, 40, 50, 60]

# Simulate sliding window
for num in nums:
    window.append(num)
    print(f"Sliding window: {window}")


# Output:
# Sliding window: deque([10], maxlen=3)
# Sliding window: deque([10, 20], maxlen=3)
# Sliding window: deque([10, 20, 30], maxlen=3)
# Sliding window: deque([20, 30, 40], maxlen=3)
# Sliding window: deque([30, 40, 50], maxlen=3)
# Sliding window: deque([40, 50, 60], maxlen=3)




########################################### ADVANCED EXERCISES ###########################################################

# Exercise 1: Implement a Deque-Based Palindrome Checker
# Write a function that uses a deque to check if a given string is a palindrome. Ignore spaces, punctuation, and case differences.
#
# Solution:

from collections import deque
import string


def is_palindrome(s):
    # Clean the string (remove spaces and punctuation, convert to lowercase)
    s = ''.join(c for c in s if c.isalnum()).lower()
    d = deque(s)

    while len(d) > 1:
        if d.popleft() != d.pop():
            return False
    return True


# Test the function
print(is_palindrome("A man, a plan, a canal, Panama"))  # Output: True
print(is_palindrome("Hello"))  # Output: False

# Exercise 2: Sliding Window Maximum
# Given an array [10, 20, 15, 12, 18, 22, 25] and a window size k = 3, find the maximum element in each sliding window using a deque.
#
# Solution:

from collections import deque


def sliding_window_max(arr, k):
    # arr = [10, 20, 15, 12, 18, 22, 25]
    # k = 3
    d = deque()
    result = []

    for i in range(len(arr)):
        # Remove indices that are out of the current window
        if d and d[0] < i - k + 1:
            d.popleft()

        # Remove indices whose corresponding values are less than the current value
        while d and arr[d[-1]] < arr[i]:
            d.pop()

        # Add current index
        d.append(i)

        # Append the max value for the current window
        if i >= k - 1:
            result.append(arr[d[0]])

    return result


# Test the function
arr = [10, 20, 15, 12, 18, 22, 25]
k = 3
print(sliding_window_max(arr, k))  # Output: [20, 20, 18, 22, 25]



# Exercise 3: Implement a Circular Buffer
# Create a class CircularBuffer that uses a deque to implement a fixed-size buffer. Implement methods to add elements, retrieve elements, and check if the buffer is full or empty.
#
# Solution:

# class `CircularBuffer` that uses a deque to implement a fixed-size buffer.Implement methods to add elements, retrieve elements, and check if the buffer is full or empty.
#
#
# Solution:

from collections import deque


class CircularBuffer:
    def __init__(self, size):
        self.buffer = deque(maxlen=size)

    def add(self, value):
        self.buffer.append(value)

    def retrieve(self):
        if self.buffer:
            return self.buffer.popleft()
        return None

    def is_full(self):
        return len(self.buffer) == self.buffer.maxlen

    def is_empty(self):
        return len(self.buffer) == 0


# Test the CircularBuffer
cb = CircularBuffer(3)
cb.add(10)
cb.add(20)
cb.add(30)
print(cb.is_full())  # Output: True
print(cb.retrieve())  # Output: 10
cb.add(40)
print(cb.buffer)  # Output: deque([20, 30, 40], maxlen=3)


# Exercise 4: Deque-Based Undo-Redo System
# Simulate an undo-redo system using two deques: one for actions and one for undone actions.
#
# Solution:

from collections import deque


class UndoRedo:
    def __init__(self):
        self.actions = deque()
        self.undone = deque()

    def do(self, action):
        self.actions.append(action)
        self.undone.clear()

    def undo(self):
        if self.actions:
            action = self.actions.pop()
            self.undone.append(action)
            return action
        return None

    def redo(self):
        if self.undone:
            action = self.undone.pop()
            self.actions.append(action)
            return action
        return None


# Test the UndoRedo system
ur = UndoRedo()
ur.do("Action 1")
ur.do("Action 2")
print(ur.undo())  # Output: "Action 2"
print(ur.redo())  # Output: "Action 2"

# Exercise 5: Find the First Non-Repeating Character
# Given a string, use a deque to find the first non-repeating character as you iterate through the string.
#
# Solution:

from collections import deque, Counter


def first_non_repeating_char(s):
    d = deque()
    counts = Counter()

    for char in s:
        counts[char] += 1
        d.append(char)
        # Remove characters from the deque that are repeating
        while d and counts[d[0]] > 1:
            d.popleft()

    return d[0] if d else None


# Test the function
print(first_non_repeating_char("swiss"))  # Output: "w"
print(first_non_repeating_char("aabbcc"))  # Output: None



