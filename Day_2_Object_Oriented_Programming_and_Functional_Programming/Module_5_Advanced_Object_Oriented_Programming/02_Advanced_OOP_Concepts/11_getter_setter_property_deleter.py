##################################### BASIC ###############################################

# 1. Basic Getter and Setter
# Problem: Create a class `Temperature` with a private attribute `__celsius`.
# Use a getter and setter to convert between Celsius and Fahrenheit.

class Temperature:
    def __init__(self, celsius):
        self.__celsius = celsius

    @property
    def celsius(self):
        return self.__celsius

    @celsius.setter
    def celsius(self, value):
        self.__celsius = value

    @property
    def fahrenheit(self):
        return self.__celsius * 9 / 5 + 32

print("Exercise 1: Getter and Setter")
temp = Temperature(25)
print(f"Celsius: {temp.celsius}, Fahrenheit: {temp.fahrenheit}")  # Output: Celsius: 25, Fahrenheit: 77.0
temp.celsius = 30
print(f"Celsius: {temp.celsius}, Fahrenheit: {temp.fahrenheit}")  # Output: Celsius: 30, Fahrenheit: 86.0


# 2. Validation with Setter
# Problem: Create a class `BankAccount` with a private balance attribute.
# Use a setter to ensure the balance cannot be negative.

class BankAccount:
    def __init__(self, initial_balance):
        self.__balance = initial_balance

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        if value >= 0:
            self.__balance = value
        else:
            raise ValueError("Balance cannot be negative!")

print("\nExercise 2: Validation with Setter")
account = BankAccount(100)
print(f"Initial Balance: {account.balance}")  # Output: 100
account.balance = 200
print(f"Updated Balance: {account.balance}")  # Output: 200
# account.balance = -50  # Uncomment to raise a ValueError


# 3. Using Deleter
# Problem: Create a class `User` with a private attribute `__username`.
# Allow deleting the username with a deleter method.

class User:
    def __init__(self, username):
        self.__username = username

    @property
    def username(self):
        return self.__username

    @username.deleter
    def username(self):
        print("Deleting username...")
        del self.__username

print("\nExercise 3: Using Deleter")
user = User("Alice123")
print(f"Username: {user.username}")  # Output: Alice123
del user.username  # Output: Deleting username


# 4. Combining Getters, Setters, and Deleters
# Problem: Create a class `Rectangle` with private attributes `__width` and `__height`.
# Use getters, setters, and deleters to manage these attributes.

class Rectangle:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if value > 0:
            self.__width = value
        else:
            raise ValueError("Width must be positive!")

    @width.deleter
    def width(self):
        print("Deleting width...")
        del self.__width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if value > 0:
            self.__height = value
        else:
            raise ValueError("Height must be positive!")

    @height.deleter
    def height(self):
        print("Deleting height...")
        del self.__height

print("\nExercise 4: Rectangle Attributes")
rect = Rectangle(5, 10)
print(f"Width: {rect.width}, Height: {rect.height}")  # Output: Width: 5, Height: 10
rect.width = 7
print(f"Updated Width: {rect.width}")  # Output: Updated Width: 7
del rect.width  # Output: Deleting width...


# 5. Read-Only Property
# Problem: Create a class `Circle` with a private radius attribute.
# Make the area a read-only property based on the radius.

import math

class Circle:
    def __init__(self, radius):
        self.__radius = radius

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, value):
        if value > 0:
            self.__radius = value
        else:
            raise ValueError("Radius must be positive!")

    @property
    def area(self):
        return math.pi * self.__radius ** 2

print("\nExercise 5: Read-Only Property")
circle = Circle(5)
print(f"Radius: {circle.radius}, Area: {circle.area:.2f}")  # Output: Radius: 5, Area: 78.54
circle.radius = 7
print(f"Updated Radius: {circle.radius}, Area: {circle.area:.2f}")  # Output: Radius: 7, Area: 153.94



##################################### INTERMEDIATE #####################################


# Scenario:
# In an inventory management system:
#
# A class Product represents individual products with attributes:
# __name: Name of the product (private).
# __price: Price of the product (private).
# __quantity: Available quantity in stock (private).
# Use getters, setters, and deleters to:
# Get and set the product name, ensuring it is a non-empty string.
# Get and set the product price, ensuring it is a positive number.
# Get and set the product quantity, ensuring it is a non-negative integer.
# Implement a @property to calculate the total stock value (price * quantity).
# Allow deleting the product name using a deleter, but prevent setting the name after deletion.


class Product:
    """Class to represent a product in the inventory."""
    def __init__(self, name, price, quantity):
        self.__name = name
        self.__price = price
        self.__quantity = quantity

    # Getter for name
    @property
    def name(self):
        return self.__name

    # Setter for name
    @name.setter
    def name(self, value):
        if value and isinstance(value, str):
            self.__name = value
        else:
            raise ValueError("Name must be a non-empty string.")

    # Deleter for name
    @name.deleter
    def name(self):
        print("Deleting product name...")
        self.__name = None

    # Getter for price
    @property
    def price(self):
        return self.__price

    # Setter for price
    @price.setter
    def price(self, value):
        if value > 0:
            self.__price = value
        else:
            raise ValueError("Price must be a positive number.")

    # Getter for quantity
    @property
    def quantity(self):
        return self.__quantity

    # Setter for quantity
    @quantity.setter
    def quantity(self, value):
        if value >= 0:
            self.__quantity = value
        else:
            raise ValueError("Quantity cannot be negative.")

    # Read-only property for total stock value
    @property
    def total_stock_value(self):
        return self.__price * self.__quantity


# Usage
print("=== Inventory Management ===")
# Create a product
product = Product("Laptop", 1000, 10)

# Access and modify product details
print("\nProduct Details:")
print(f"Name: {product.name}")
print(f"Price: ${product.price}")
print(f"Quantity: {product.quantity}")
print(f"Total Stock Value: ${product.total_stock_value}")

print("\nUpdating Price and Quantity:")
product.price = 1200  # Update price
product.quantity = 8  # Update quantity
print(f"Updated Price: ${product.price}")
print(f"Updated Quantity: {product.quantity}")
print(f"Updated Stock Value: ${product.total_stock_value}")

print("\nDeleting Product Name:")
del product.name
print(f"Name after deletion: {product.name}")  # Output: None
# product.name = "Smartphone"  # Uncomment to raise an error (name was deleted)

