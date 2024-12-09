# 1. Single Inheritance
# Problem: Create a `Vehicle` class with a `drive` method. Derive a `Car` class that inherits and uses the `drive` method.
class Vehicle:
    def drive(self):
        print("Vehicle is driving.")

class Car(Vehicle):
    def drive(self):
        print("Car is driving smoothly.")

print("Exercise 1: Single Inheritance")
car = Car()
car.drive()  # Output: Car is driving smoothly.


# 2. Multilevel Inheritance
# Problem: Create a `Person` class. Inherit `Employee` from `Person`, and `Manager` from `Employee`. Add a method in each class.
class Person:
    def details(self):
        print("I am a person.")

class Employee(Person):
    def details(self):
        print("I am an employee.")

class Manager(Employee):
    def details(self):
        print("I am a manager.")

print("\nExercise 2: Multilevel Inheritance")
manager = Manager()
manager.details()  # Output: I am a manager.


# 3. Multiple Inheritance
# Problem: Create classes `Mother` and `Father` with a `trait` method. Inherit both into a `Child` class and call the `trait` method.
class Mother:
    def trait(self):
        print("Kindness from Mother.")

class Father:
    def trait(self):
        print("Strength from Father.")

class Child(Mother, Father):
    pass  # Child inherits both Mother and Father.

print("\nExercise 3: Multiple Inheritance")
child = Child()
child.trait()  # Output: Kindness from Mother. (Method Resolution Order)


# 4. Hierarchical Inheritance
# Problem: Create a `Parent` class with a `message` method. Inherit `Child1` and `Child2` from `Parent`, each calling the `message` method.
class Parent:
    def message(self):
        print("Message from Parent.")

class Child1(Parent):
    def message(self):
        print("Message from Child 1.")

class Child2(Parent):
    def message(self):
        print("Message from Child 2.")

print("\nExercise 4: Hierarchical Inheritance")
child1 = Child1()
child1.message()  # Output: Message from Child 1.
child2 = Child2()
child2.message()  # Output: Message from Child 2.


# 5. Hybrid Inheritance
# Problem: Create a `Base` class, inherit `Intermediate1` and `Intermediate2` from it, and create a `Final` class inheriting both intermediate classes.
class Base:
    def base_message(self):
        print("This is the base class.")

class Intermediate1(Base):
    def message1(self):
        print("This is intermediate class 1.")

class Intermediate2(Base):
    def message2(self):
        print("This is intermediate class 2.")

class Final(Intermediate1, Intermediate2):
    def final_message(self):
        print("This is the final class.")

print("\nExercise 5: Hybrid Inheritance")
final_obj = Final()
final_obj.base_message()  # Output: This is the base class.
final_obj.message1()      # Output: This is intermediate class 1.
final_obj.message2()      # Output: This is intermediate class 2.
final_obj.final_message() # Output: This is the final class.


###################### A comprehensive example ######################################


class Employee:
    """Base class for all employees."""
    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary

    def show_details(self):
        """Display basic details of an employee."""
        print(f"Employee ID: {self.emp_id}, Name: {self.name}, Salary: ${self.salary}")

    def calculate_annual_salary(self):
        """Calculate annual salary."""
        return self.salary * 12


class Manager(Employee):
    """Derived class for managers."""
    def __init__(self, name, emp_id, salary, bonus_percentage):
        super().__init__(name, emp_id, salary)  # Initialize parent attributes
        self.bonus_percentage = bonus_percentage

    def calculate_bonus(self):
        """Calculate annual bonus based on the bonus percentage."""
        return self.salary * 12 * (self.bonus_percentage / 100)

    def show_details(self):
        """Override the parent method to include bonus details."""
        super().show_details()  # Call parent method
        print(f"Bonus Percentage: {self.bonus_percentage}%")
        print(f"Annual Bonus: ${self.calculate_bonus()}")


class Intern(Employee):
    """Derived class for interns."""
    def __init__(self, name, emp_id, salary, duration_months):
        super().__init__(name, emp_id, salary)
        self.duration_months = duration_months

    def calculate_stipend(self):
        """Calculate the total stipend for the internship period."""
        return self.salary * self.duration_months

    def show_details(self):
        """Override the parent method to include internship details."""
        super().show_details()
        print(f"Internship Duration: {self.duration_months} months")
        print(f"Total Stipend: ${self.calculate_stipend()}")


# Usage of the system
print("=== Employee Management System ===")

# Create a regular employee
employee = Employee("Alice", "E001", 5000)
print("\nEmployee Details:")
employee.show_details()
print(f"Annual Salary: ${employee.calculate_annual_salary()}")

# Create a manager
manager = Manager("Bob", "M001", 8000, 15)  # 15% bonus
print("\nManager Details:")
manager.show_details()

# Create an intern
intern = Intern("Charlie", "I001", 2000, 6)  # 6 months internship
print("\nIntern Details:")
intern.show_details()