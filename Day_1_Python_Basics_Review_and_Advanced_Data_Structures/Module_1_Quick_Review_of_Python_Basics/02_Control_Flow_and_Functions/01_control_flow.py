################################ BASIC ###################################

# Exercise 1: If-else statement
# Problem: Check if a number is even or odd.
# Relevance: Demonstrates the use of basic if-else control flow for decision-making.
number = 4
if number % 2 == 0:
    print("Exercise 1:", number, "is even")
else:
    print("Exercise 1:", number, "is odd")
# Output: Exercise 1: 4 is even

# Exercise 2: Nested if-else
# Problem: Check if a number is positive, negative, or zero.
# Relevance: Demonstrates nested if-else for handling multiple conditions.
number = -5
if number > 0:
    print("Exercise 2:", number, "is positive")
elif number < 0:
    print("Exercise 2:", number, "is negative")
else:
    print("Exercise 2:", number, "is zero")
# Output: Exercise 2: -5 is negative

# Exercise 3: For loop with range
# Problem: Print all numbers from 1 to 5.
# Relevance: Demonstrates the use of a for loop to iterate over a range.
for i in range(1, 6):
    print("Exercise 3: Number is", i)
# Output:
# Exercise 3: Number is 1
# Exercise 3: Number is 2
# Exercise 3: Number is 3
# Exercise 3: Number is 4
# Exercise 3: Number is 5

# Exercise 4: While loop
# Problem: Print numbers from 1 to 5 using a while loop.
# Relevance: Demonstrates the use of a while loop for repeated execution.
i = 1
while i <= 5:
    print("Exercise 4: Number is", i)
    i += 1
# Output:
# Exercise 4: Number is 1
# Exercise 4: Number is 2
# Exercise 4: Number is 3
# Exercise 4: Number is 4
# Exercise 4: Number is 5

# Exercise 5: Break statement
# Problem: Stop a loop when a specific condition is met.
# Relevance: Demonstrates the use of `break` to exit loops prematurely.
for i in range(1, 10):
    if i == 5:
        break
    print("Exercise 5: Number is", i)
# Output:
# Exercise 5: Number is 1
# Exercise 5: Number is 2
# Exercise 5: Number is 3
# Exercise 5: Number is 4

# Exercise 6: Continue statement
# Problem: Skip a specific iteration in a loop.
# Relevance: Demonstrates the use of `continue` to skip certain conditions in loops.
for i in range(1, 6):
    if i == 3:
        continue
    print("Exercise 6: Number is", i)
# Output:
# Exercise 6: Number is 1
# Exercise 6: Number is 2
# Exercise 6: Number is 4
# Exercise 6: Number is 5

# Exercise 7: Using else with loops
# Problem: Print all numbers from 1 to 5 and execute an else block when the loop ends.
# Relevance: Demonstrates the use of an `else` clause with loops.
for i in range(1, 6):
    print("Exercise 7: Number is", i)
else:
    print("Exercise 7: Loop completed")
# Output:
# Exercise 7: Number is 1
# Exercise 7: Number is 2
# Exercise 7: Number is 3
# Exercise 7: Number is 4
# Exercise 7: Number is 5
# Exercise 7: Loop completed

# Exercise 8: Nested loops
# Problem: Print a multiplication table for numbers 1 to 3.
# Relevance: Demonstrates the use of nested loops for processing two dimensions of data.
for i in range(1, 4):
    for j in range(1, 4):
        print(f"Exercise 8: {i} x {j} = {i * j}")
# Output:
# Exercise 8: 1 x 1 = 1
# Exercise 8: 1 x 2 = 2
# Exercise 8: 1 x 3 = 3
# Exercise 8: 2 x 1 = 2
# Exercise 8: 2 x 2 = 4
# Exercise 8: 2 x 3 = 6
# Exercise 8: 3 x 1 = 3
# Exercise 8: 3 x 2 = 6
# Exercise 8: 3 x 3 = 9

# Exercise 9: Pass statement
# Problem: Create a loop that does nothing for specific iterations.
# Relevance: Demonstrates the use of `pass` for placeholder logic.
for i in range(1, 6):
    if i == 3:
        pass
    else:
        print("Exercise 9: Number is", i)
# Output:
# Exercise 9: Number is 1
# Exercise 9: Number is 2
# Exercise 9: Number is 4
# Exercise 9: Number is 5

# Exercise 10: Conditional expressions (ternary operator)
# Problem: Check if a number is even or odd using a single line of code.
# Relevance: Demonstrates the use of a ternary operator for concise conditional checks.
number = 10
result = "even" if number % 2 == 0 else "odd"
print("Exercise 10:", number, "is", result)
# Output: Exercise 10: 10 is even


################################# INTERMEDIATE ##################################

# Exercise 1: Prime number checker
# Problem: Check if a number is a prime number using loops and conditional statements.
# Relevance: Demonstrates nested loops and conditions for decision-making.
number = 29
is_prime = True
if number < 2:
    is_prime = False
else:
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            is_prime = False
            break
if is_prime:
    print("Exercise 1:", number, "is a prime number")
else:
    print("Exercise 1:", number, "is not a prime number")
# Output: Exercise 1: 29 is a prime number

# Exercise 2: FizzBuzz problem
# Problem: Print numbers from 1 to 20. For multiples of 3, print "Fizz", for multiples of 5, print "Buzz",
# and for multiples of both 3 and 5, print "FizzBuzz".
# Relevance: Demonstrates combining loops and multiple conditions.
for i in range(1, 21):
    if i % 3 == 0 and i % 5 == 0:
        print("Exercise 2: FizzBuzz")
    elif i % 3 == 0:
        print("Exercise 2: Fizz")
    elif i % 5 == 0:
        print("Exercise 2: Buzz")
    else:
        print(f"Exercise 2: {i}")
# Output: Numbers from 1 to 20 with Fizz, Buzz, or FizzBuzz substitutions.

# Exercise 3: Factorial using recursion
# Problem: Calculate the factorial of a number using recursion.
# Relevance: Demonstrates recursion, a control flow mechanism for repetitive tasks.
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

number = 5
result = factorial(number)
print("Exercise 3: Factorial of", number, "is", result)
# Output: Exercise 3: Factorial of 5 is 120

# Exercise 4: Find the largest number in a nested list
# Problem: Write a program to find the largest number in a nested list structure.
# Relevance: Demonstrates handling nested loops and conditional logic for complex data structures.
nested_list = [[10, 20, 30], [5, 15, 25], [35, 10, 5]]
largest_number = float('-inf')
for sublist in nested_list:
    for num in sublist:
        if num > largest_number:
            largest_number = num
print("Exercise 4: Largest number in nested list is", largest_number)
# Output: Exercise 4: Largest number in nested list is 35

# Exercise 5: Count occurrences of words in a sentence
# Problem: Count the number of occurrences of each word in a given sentence.
# Relevance: Demonstrates loops, dictionaries, and string manipulation for control flow.
sentence = "the quick brown fox jumps over the lazy dog the quick fox"
word_counts = {}
for word in sentence.split():
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1
print("Exercise 5: Word counts:", word_counts)
# Output: Exercise 5: Word counts: {'the': 3, 'quick': 2, 'brown': 1, 'fox': 2, 'jumps': 1, 'over': 1, 'lazy': 1, 'dog': 1}
