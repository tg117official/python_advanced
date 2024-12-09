from collections import deque

d = deque([10, 20, 30, 40, 50])

# Rotate 2 steps to the left
d.rotate(-2)

# Reverse the deque
d.reverse()

# Print the final deque
print(d)