def cache(func):
    results = {}
    def wrapper(*args):
        if args not in results:
            results[args] = func(*args)
        return results[args]
    return wrapper

@cache
def square(n):
    return n * n

print(f"Exercise 5 Result: {square(4)}")  # Output: 16
print(f"Exercise 5 Result: {square(4)}")  # Output: 16 (cached)