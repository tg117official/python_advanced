

class Car :
    number_of_wheels = 4
    num_instances = 0
    def __init__(self, make, model, color):
        self.make = make
        self.model = model
        self.color = color
    @classmethod
    def update_wheels(cls):
        cls.number_of_wheels = 6
        print("This is class method", cls)
    def start(self):
        print(f"{self.model} Car Starts...", self)
    def stop(self):
        print("car Stops...")
    def apply_breaks(self):
        print("Break Applied...")

    @staticmethod
    def greet_driver(name):
        print(f"Hello {name}, Drive Safe")

#################### Basic Ops ###########################

car1 = Car("Tata", "Tiago-xt", "orange")
# Car.__init__(car1,"Tata", "Tiago-xt", "orange" )
car1.potrait = "Allu Arjun"


car2 = Car("MS", "WagonR", "White")
# Car(car2,"Tata", "Tiago-xt", "orange" )


car1.start()
# Car.start(car1)
print(car1.make, car1.model, car1.color, car1.potrait)

car2.start()
print(car2.make, car2.model, car2.color)


############################ Class Variable vs Instance Variables ###################

# Accessing Class Variable values
print(Car.number_of_wheels)
print(car1.number_of_wheels)
print(car2.number_of_wheels)

# Accessing Instance variable(model) value
# print(Car.model) Cannot access using class
print(car1.model)
print(car2.model)


# Modify class variable using class
# Car.number_of_wheels = 6
# print(Car.number_of_wheels)
# print(car1.number_of_wheels)
# print(car2.number_of_wheels)

# Modify a class variable using instance
car1.number_of_wheels = 6
print(Car.number_of_wheels)
print(car1.number_of_wheels)
print(car2.number_of_wheels)


############################ Class | Instance | Static Methods ##############################

# Instance Methods

# Instance is passed as first argument for instance method

# Instance methods are specific to the instance, even if you update
# the value of a class variable using instance method, the value wil
# be updated for that particular instance only.
car1.start()
Car.start(car1)
car2.start()
Car.start(car2)

# Class Methods

# Class is passed as first argument for class methods

# You can call class methods using instance as well as class
# If the method updated value of a class variable, it'll update the value globally
# for all instances regardless it's called using instance or class.

Car.update_wheels()
car1.update_wheels()
car2.update_wheels()

# Static Method

# Neither class nor Instance is passed as first argument

Car.greet_driver("John")
car1.greet_driver("Pushpa")
car2.greet_driver("Katappa")


print(Car.num_instances)
