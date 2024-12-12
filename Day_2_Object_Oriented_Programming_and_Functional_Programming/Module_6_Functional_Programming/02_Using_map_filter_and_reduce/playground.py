from functools import reduce

numbers = [1, 2, 3, 4, 5]
# [1, 2, 3, 4, 5]
sum_of_numbers = reduce(lambda x, y: x + y, numbers)
sum_of_numbers = reduce(lambda prev, curr: prev + curr, numbers)
print(f"Exercise 3 Result: {sum_of_numbers}")  # Output: 15