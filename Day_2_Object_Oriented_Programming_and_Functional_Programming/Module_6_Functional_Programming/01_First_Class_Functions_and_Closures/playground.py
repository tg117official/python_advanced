def memoize(func):
    cache = {}
    count = 0
    # {10: 55, 20: 6551}
    def wrapper(n):
        if n not in cache:
            cache[n] = func(n)
#           cache[10] = 55
        return cache[n]  #cache[10]
    return wrapper

@memoize
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

result = fibonacci(10)  # Should return 55
result2 = fibonacci(20)
result3 = fibonacci(10)
print(f"Exercise 10 Result: {result}")  # Output: 55