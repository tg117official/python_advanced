# Tuple vs namedtuple

from collections import namedtuple

# Step 1: Define the namedtuple
Employee = namedtuple('Employee', ['name', 'age', 'position', 'salary'])

# Step 2: Create data
# Using a regular tuple
employee_tuple = ("Alice", 30, "Engineer", 70000, 566)

# Using a namedtuple
employee_namedtuple = Employee(name="Alice", age=30, position="Engineer", salary=70000)

# Step 3: Access and print data
print("Using Tuple:")
print(f"Name: {employee_tuple[0]}, Age: {employee_tuple[1]}, Position: {employee_tuple[2]}, Salary: {employee_tuple[3]}")

print("\nUsing NamedTuple:")
print(f"Name: {employee_namedtuple.name}, Age: {employee_namedtuple.age}, Position: {employee_namedtuple.position}, Salary: {employee_namedtuple.salary}")

# Step 4: Simulate updates
# Regular tuple update
updated_tuple = (employee_tuple[0], employee_tuple[1], "Senior Engineer", 90000)

# NamedTuple update
updated_namedtuple = employee_namedtuple._replace(position="Senior Engineer", salary=90000)

print("\nUpdated Tuple:")
print(updated_tuple)

print("\nUpdated NamedTuple:")
print(updated_namedtuple)

# Step 5: Compare
print("\nComparison:")
print("Tuple requires remembering the index of each field, which is less readable.")
print("NamedTuple allows accessing fields by name, making the code more readable and maintainable.")







# Basic: Create and Access Fields
# Problem: Create a `namedtuple` called `Person` with fields `name`, `age`, and `city`.
# Create an instance for a person named "Alice", aged 30, living in "New York".
# Print each field of the `namedtuple` separately.
#
# Solution:

from collections import namedtuple

# Define the namedtuple
Person = namedtuple('Person', ['name', 'age', 'city'])

# Create an instance
person = Person(name="Alice", age=30, city="New York")

# Access fields
print(person.name)  # Output: Alice
print(person.age)   # Output: 30
print(person.city)  # Output: New York




# 2. Calculate Areas of Rectangles
# Problem: Create a `namedtuple` called `Rectangle` with fields `length` and `width`.
# Write a function that takes a `Rectangle` as input and returns its area.
# Create a rectangle with length 10 and width 5 and calculate its area.
#
# Solution:

from collections import namedtuple

# Define the namedtuple
Rectangle = namedtuple('Rectangle', ['length', 'width'])

# Function to calculate area
def calculate_area(rect):
    return rect.length * rect.width

# Create a rectangle instance
rect = Rectangle(length=10, width=5, height=55)

# Calculate and print the area
print(calculate_area(rect))  # Output: 50




# Store and Sort Employee Data
# Problem: Create a `namedtuple` called `Employee` with fields `id`, `name`, and `salary`.
# Create a list of employees and sort them by salary in descending order.
# Print the sorted list.
#
# Solution:

from collections import namedtuple

# Define the namedtuple
Employee = namedtuple('Employee', ['id', 'name', 'salary'])

# Create a list of employees
employees = [
    Employee(id=1, name="John", salary=50000),
    Employee(id=2, name="Jane", salary=60000),
    Employee(id=3, name="Doe", salary=40000)
]

# Sort by salary in descending order
sorted_employees = sorted(employees, key=lambda emp: emp.salary, reverse=True)

# Print the sorted list
for emp in sorted_employees:
    print(emp)
# Output:
# Employee(id=2, name='Jane', salary=60000)
# Employee(id=1, name='John', salary=50000)
# Employee(id=3, name='Doe', salary=40000)




# Calculate Distance Between Points
# Problem: Create a `namedtuple` called `Point` with fields `x` and `y`.
# Write a function to calculate the distance between two points using the distance formula:
# \[
# \text{Distance} = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}
# \]
# Test the function with points `(3, 4)` and `(7, 1)`.



from collections import namedtuple
import math

# Define the namedtuple
Point = namedtuple('Point', ['x', 'y'])

# Function to calculate distance
def calculate_distance(p1, p2):
    return math.sqrt((p2.x - p1.x)**2 + (p2.y - p1.y)**2)

# Create two points
point1 = Point(3, 4)
point2 = Point(7, 1)

# Calculate and print the distance
print(calculate_distance(point1, point2))  # Output: 5.0





# Nested namedtuples for Product Details
# Problem: Create a `namedtuple` called `Product` with fields `id`, `name`, and `price`.
# Create another `namedtuple` called `Order` with fields `order_id`, `customer_name`, and `products`
# (a list of `Product` instances). Calculate the total price of all products in an order.



from collections import namedtuple

# Define the namedtuples
Product = namedtuple('Product', ['id', 'name', 'price'])
Order = namedtuple('Order', ['order_id', 'customer_name', 'products'])

# Create product instances
product1 = Product(id=1, name="Laptop", price=1000)
product2 = Product(id=2, name="Mouse", price=50)
product3 = Product(id=3, name="Keyboard", price=70)

# Create an order with products
order = Order(order_id=101, customer_name="Alice", products=[product1, product2, product3])

# Calculate the total price of the order
total_price = sum(product.price for product in order.products)

# Print the total price
print(f"Total price for order {order.order_id}: ${total_price}")
# Output: Total price for order 101: $1120