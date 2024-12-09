# 1. __init__ and __str__
# Problem: Create a class `Person` with attributes `name` and `age`. Use `__init__` to initialize the attributes and `__str__` to return a formatted string representation.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person(name={self.name}, age={self.age})"

print("Exercise 1: __init__ and __str__")
p = Person("Alice", 25)
print(p)  # Output: Person(name=Alice, age=25)


# 2. __add__
# Problem: Create a class `Vector` to represent a 2D vector with `x` and `y` coordinates. Implement `__add__` to add two vectors.

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

print("\nExercise 2: __add__")
v1 = Vector(1, 2)
v2 = Vector(3, 4)
v3 = v1 + v2  # Using __add__
print(v3)  # Output: Vector(4, 6)


# 3. __len__
# Problem: Create a class `CustomList` that wraps around a Python list and implements `__len__` to return the length of the list.

class CustomList:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)

print("\nExercise 3: __len__")
cl = CustomList([1, 2, 3, 4, 5])
print(len(cl))  # Output: 5


# 4. __getitem__ and __setitem__
# Problem: Create a class `Notebook` to store notes using a dictionary. Implement `__getitem__` and `__setitem__` for easy access and updates.

class Notebook:
    def __init__(self):
        self.notes = {}

    def __getitem__(self, key):
        return self.notes.get(key, "Note not found")

    def __setitem__(self, key, value):
        self.notes[key] = value

print("\nExercise 4: __getitem__ and __setitem__")
notebook = Notebook()
notebook["Python"] = "Python is a versatile language."  # Using __setitem__
print(notebook["Python"])  # Output: Python is a versatile language.
print(notebook["Java"])    # Output: Note not found


# 5. __eq__
# Problem: Create a class `Rectangle` with attributes `width` and `height`. Implement `__eq__` to compare two rectangles for equality.

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __eq__(self, other):
        return self.width == other.width and self.height == other.height

print("\nExercise 5: __eq__")
r1 = Rectangle(5, 10)
r2 = Rectangle(5, 10)
r3 = Rectangle(4, 8)
print(r1 == r2)  # Output: True
print(r1 == r3)  # Output: False
