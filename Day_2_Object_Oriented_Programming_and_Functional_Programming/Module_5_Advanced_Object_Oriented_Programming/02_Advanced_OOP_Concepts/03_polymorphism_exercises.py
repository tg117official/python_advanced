# 1. Method Polymorphism (Different Classes, Same Method Name)
# Problem: Define two classes, `Bird` and `Fish`, both with a method `move()`.
# Relevance: Demonstrates method polymorphism by calling the same method on different objects.

class Bird:
    def move(self):
        print("I fly in the sky!")

class Fish:
    def move(self):
        print("I swim in water!")

def demonstrate_movement(creature):
    creature.move()

# Using polymorphism
bird = Bird()
fish = Fish()
print("Exercise 1:")
demonstrate_movement(bird)  # Output: I fly in the sky!
demonstrate_movement(fish)  # Output: I swim in water!


# 2. Polymorphism with Built-in Functions
# Problem: Use the `len()` function on a string, list, and dictionary.
# Relevance: Showcases polymorphism with built-in functions operating on different data types.

print("\nExercise 2:")
print(len("Python"))  # Output: 6 (string length)
print(len([1, 2, 3]))  # Output: 3 (list length)
print(len({'a': 1, 'b': 2}))  # Output: 2 (dictionary length)


# 3. Operator Overloading
# Problem: Use the `+` operator with integers, strings, and custom objects.
# Relevance: Demonstrates how operators behave differently based on context.

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Point({self.x}, {self.y})"

point1 = Point(1, 2)
point2 = Point(3, 4)

print("\nExercise 3:")
print(5 + 3)                # Output: 8 (integer addition)
print("Hello " + "World")   # Output: Hello World (string concatenation)
print(point1 + point2)      # Output: Point(4, 6) (custom addition)


# 4. Polymorphism with Inheritance
# Problem: Create a base class `Shape` with a method `area()` and derive classes `Rectangle` and `Circle`.
# Relevance: Highlights method overriding, where subclasses provide their specific implementation.

import math

class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2

shapes = [Rectangle(4, 5), Circle(3)]
print("\nExercise 4:")
for shape in shapes:
    print(f"Area: {shape.area()}")  # Output: Area of Rectangle and Circle


# 5. Polymorphism with Custom Methods
# Problem: Create a `Vehicle` class and derived classes `Car` and `Bike`, both with a `start()` method.
# Relevance: Demonstrates polymorphism in user-defined methods.

class Vehicle:
    def start(self):
        print("Vehicle is starting...")

class Car(Vehicle):
    def start(self):
        print("Car is starting with a key.")

class Bike(Vehicle):
    def start(self):
        print("Bike is starting with a button.")

vehicles = [Car(), Bike()]
print("\nExercise 5:")
for vehicle in vehicles:
    vehicle.start()  # Output: Calls `start` method specific to Car or Bike
