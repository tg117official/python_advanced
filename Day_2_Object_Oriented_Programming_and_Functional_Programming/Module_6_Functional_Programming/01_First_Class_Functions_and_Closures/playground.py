def outer_function(x):
    def inner_function(y):
        def innermost_function(z) :
            return x+y+z
        return innermost_function
    return inner_function

# closure = outer_function(5)
print(outer_function(5)(5)(5))  # Output: 8
