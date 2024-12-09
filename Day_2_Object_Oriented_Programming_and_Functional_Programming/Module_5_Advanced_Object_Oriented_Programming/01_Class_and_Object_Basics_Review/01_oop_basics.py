
################################## BASIC EXERCISES ########################################

# 1. Exercise: Create a class `Student` with attributes `name`, `age`, and a method `greet`.
class Student:
    """Class to represent a student."""
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Relevance: Used to represent real-world entities like a person or student.
student = Student("Alice", 20)
student.greet()

# 2. Exercise: Create a `BankAccount` class with methods `deposit`, `withdraw`, and `check_balance`.
class BankAccount:
    """Class to represent a bank account."""
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. New balance: ${self.balance}.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}.")
        else:
            print("Insufficient balance!")

    def check_balance(self):
        print(f"Account Balance for {self.account_holder}: ${self.balance}")

# Relevance: Models financial transactions in banking systems.
account = BankAccount("Bob", 100)
account.deposit(50)
account.withdraw(30)
account.check_balance()

# 3. Exercise: Create a `Rectangle` class with attributes `length` and `width` and methods to calculate area and perimeter.
class Rectangle:
    """Class to represent a rectangle."""
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

# Relevance: Geometric shapes are common in simulations or graphic designs.
rect = Rectangle(5, 3)
print(f"Area: {rect.area()}, Perimeter: {rect.perimeter()}")

# 4. Exercise: Create a `Vehicle` class with attributes `brand` and `speed` and a method `drive`.
class Vehicle:
    """Class to represent a vehicle."""
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def drive(self):
        print(f"The {self.brand} is driving at {self.speed} km/h.")

# Relevance: Models transport systems or logistics.
vehicle = Vehicle("Toyota", 60)
vehicle.drive()

# 5. Exercise: Create a `Dog` class with attributes `name` and `breed` and methods `bark` and `sit`.
class Dog:
    """Class to represent a dog."""
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} says: Woof!")

    def sit(self):
        print(f"{self.name} is now sitting.")

# Relevance: Useful in animal simulations or pet management systems.
dog = Dog("Buddy", "Golden Retriever")
dog.bark()
dog.sit()


######################## A comprehensive example ######################################



# Comprehensive Example: OOP to represent a Library System

class Book:
    """A class to represent a book in the library."""
    def __init__(self, title, author, copies):
        self.title = title
        self.author = author
        self.copies = copies

    def borrow(self):
        """Decrement the number of copies if available."""
        if self.copies > 0:
            self.copies -= 1
            print(f"Borrowed '{self.title}'. Copies left: {self.copies}")
        else:
            print(f"Sorry, '{self.title}' is out of stock.")

    def return_book(self):
        """Increment the number of copies."""
        self.copies += 1
        print(f"Returned '{self.title}'. Copies now: {self.copies}")


class Library:
    """A class to represent a library with multiple books."""
    def __init__(self):
        self.books = []

    def add_book(self, book):
        """Add a book to the library."""
        self.books.append(book)
        print(f"Added '{book.title}' by {book.author}.")

    def list_books(self):
        """List all available books."""
        if not self.books:
            print("No books available.")
        for book in self.books:
            print(f"{book.title} by {book.author} - {book.copies} copies")

# Initialize library and books
library = Library()
book1 = Book("Python Programming", "John Doe", 3)
book2 = Book("Data Science with Python", "Jane Smith", 2)

library.add_book(book1)
library.add_book(book2)

# List books
library.list_books()

# Borrow and return books
book1.borrow()
book1.borrow()
book1.return_book()
book2.borrow()

# List books again
library.list_books()
