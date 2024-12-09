
################################### Basic ################################################


from abc import ABC, abstractmethod

# 1. Abstract Class: Shape
# Problem: Create an abstract class `Shape` with abstract methods `area` and `perimeter`.
# Implement `Rectangle` and `Circle` classes and calculate their area and perimeter.

class Shape(ABC):
    """Abstract class representing a generic shape."""

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Rectangle(Shape):
    """Concrete class for Rectangle."""
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class Circle(Shape):
    """Concrete class for Circle."""
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius


print("Exercise 1: Shape Abstraction")
rect = Rectangle(5, 10)
circle = Circle(7)
print(f"Rectangle Area: {rect.area()}, Perimeter: {rect.perimeter()}")
print(f"Circle Area: {circle.area()}, Perimeter: {circle.perimeter()}")


# 2. Abstract Class: Animal
# Problem: Create an abstract class `Animal` with an abstract method `sound`.
# Implement `Dog` and `Cat` classes to make appropriate sounds.

class Animal(ABC):
    """Abstract class representing a generic animal."""

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    """Concrete class for Dog."""
    def sound(self):
        return "Woof! Woof!"


class Cat(Animal):
    """Concrete class for Cat."""
    def sound(self):
        return "Meow! Meow!"


print("\nExercise 2: Animal Abstraction")
dog = Dog()
cat = Cat()
print(f"Dog Sound: {dog.sound()}")
print(f"Cat Sound: {cat.sound()}")


# 3. Abstract Class: Vehicle
# Problem: Create an abstract class `Vehicle` with abstract methods `start` and `stop`.
# Implement `Car` and `Bike` classes to define their behaviors.

class Vehicle(ABC):
    """Abstract class for vehicles."""

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Car(Vehicle):
    """Concrete class for Car."""
    def start(self):
        return "Car is starting with a key."

    def stop(self):
        return "Car is stopping with brakes."


class Bike(Vehicle):
    """Concrete class for Bike."""
    def start(self):
        return "Bike is starting with a button."

    def stop(self):
        return "Bike is stopping with a brake lever."


print("\nExercise 3: Vehicle Abstraction")
car = Car()
bike = Bike()
print(f"Car: {car.start()} {car.stop()}")
print(f"Bike: {bike.start()} {bike.stop()}")


# 4. Abstract Class: Appliance
# Problem: Create an abstract class `Appliance` with methods `turn_on` and `turn_off`.
# Implement `Fan` and `Light` classes to define specific behavior.

class Appliance(ABC):
    """Abstract class for home appliances."""

    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass


class Fan(Appliance):
    """Concrete class for Fan."""
    def turn_on(self):
        return "Fan is now ON."

    def turn_off(self):
        return "Fan is now OFF."


class Light(Appliance):
    """Concrete class for Light."""
    def turn_on(self):
        return "Light is now ON."

    def turn_off(self):
        return "Light is now OFF."


print("\nExercise 4: Appliance Abstraction")
fan = Fan()
light = Light()
print(f"Fan: {fan.turn_on()} {fan.turn_off()}")
print(f"Light: {light.turn_on()} {light.turn_off()}")


# 5. Abstract Class: Payment
# Problem: Create an abstract class `Payment` with an abstract method `make_payment`.
# Implement `CreditCardPayment` and `PayPalPayment` for specific payment methods.

class Payment(ABC):
    """Abstract class for payment systems."""

    @abstractmethod
    def make_payment(self, amount):
        pass


class CreditCardPayment(Payment):
    """Concrete class for credit card payment."""
    def make_payment(self, amount):
        return f"Paid ${amount} using Credit Card."


class PayPalPayment(Payment):
    """Concrete class for PayPal payment."""
    def make_payment(self, amount):
        return f"Paid ${amount} using PayPal."


print("\nExercise 5: Payment Abstraction")
credit_card = CreditCardPayment()
paypal = PayPalPayment()
print(credit_card.make_payment(100))
print(paypal.make_payment(200))


######################## Intermediate Exercise #########################################


from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    """Abstract base class for payment methods."""

    @abstractmethod
    def authenticate(self):
        """Authenticate the user."""
        pass

    @abstractmethod
    def make_payment(self, amount):
        """Process the payment."""
        pass


class CreditCardPayment(PaymentMethod):
    """Concrete class for Credit Card payment."""
    def __init__(self, card_number, cvv):
        self.card_number = card_number
        self.cvv = cvv

    def authenticate(self):
        print(f"Authenticating Credit Card {self.card_number}...")
        return True  # Simulated authentication

    def make_payment(self, amount):
        print(f"Processing credit card payment of ${amount}.")
        return f"Paid ${amount} using Credit Card."


class PayPalPayment(PaymentMethod):
    """Concrete class for PayPal payment."""
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def authenticate(self):
        print(f"Authenticating PayPal account for {self.email}...")
        return True  # Simulated authentication

    def make_payment(self, amount):
        print(f"Processing PayPal payment of ${amount}.")
        return f"Paid ${amount} using PayPal."


class UPIPayment(PaymentMethod):
    """Concrete class for UPI payment."""
    def __init__(self, upi_id):
        self.upi_id = upi_id

    def authenticate(self):
        print(f"Authenticating UPI ID {self.upi_id}...")
        return True  # Simulated authentication

    def make_payment(self, amount):
        print(f"Processing UPI payment of ${amount}.")
        return f"Paid ${amount} using UPI."


# Function to process any payment method
def process_payment(payment_method, amount):
    """Generic function to process payments."""
    if payment_method.authenticate():
        receipt = payment_method.make_payment(amount)
        print(receipt)
    else:
        print("Authentication failed. Payment could not be processed.")


# Simulating the system
print("=== Online Payment System ===")
cc_payment = CreditCardPayment("1234-5678-9876-5432", "123")
paypal_payment = PayPalPayment("user@example.com", "password123")
upi_payment = UPIPayment("user@upi")

print("\nProcessing Credit Card Payment:")
process_payment(cc_payment, 100)

print("\nProcessing PayPal Payment:")
process_payment(paypal_payment, 200)

print("\nProcessing UPI Payment:")
process_payment(upi_payment, 150)
