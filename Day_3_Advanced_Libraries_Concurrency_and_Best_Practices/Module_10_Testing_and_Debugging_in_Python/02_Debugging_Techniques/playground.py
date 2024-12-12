def calculate_sum(numbers):
    sum = 0
    for n in numbers :
        sum = sum + n

    return sum

print("Exercise 1 Result:", calculate_sum([1, 2, 3, 4, 5]))  # Expected: 15, Buggy Output: 6
