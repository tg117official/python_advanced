# Regular function
def square(x):
    return x * x

# Lambda equivalent
cube = lambda x: x * square(x)

print(square(4))        # Output: 16
print(cube(4)) # Output: 16