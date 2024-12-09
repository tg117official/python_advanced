class ECommerce:
    total_customers = 0  # Class-level attribute shared across all instances

    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.cart = []  # Instance-specific attribute to store items in the cart
        ECommerce.total_customers += 1  # Increment total customers when a new customer is created

    # Instance Method: Add items to the customer's cart
    def add_to_cart(self, item, price):
        self.cart.append({'item': item, 'price': price})
        print(f"{self.customer_name} added {item} worth ${price} to their cart.")

    # Instance Method: View the customer's cart
    def view_cart(self):
        if not self.cart:
            print(f"{self.customer_name}'s cart is empty.")
        else:
            print(f"{self.customer_name}'s Cart:")
            for entry in self.cart:
                print(f"- {entry['item']}: ${entry['price']}")

    # Class Method: Display total customers
    @classmethod
    def total_customers_count(cls):
        print(f"Total customers: {cls.total_customers}")

    # Static Method: Calculate discount on an item
    @staticmethod
    def calculate_discount(price, discount_rate):
        discounted_price = price - (price * discount_rate / 100)
        return discounted_price


# Usage
# Creating customers
customer1 = ECommerce("Alice")
customer2 = ECommerce("Bob")

# Instance Methods
customer1.add_to_cart("Laptop", 1000)
customer1.add_to_cart("Mouse", 50)
customer1.view_cart()

customer2.add_to_cart("Keyboard", 150)
customer2.view_cart()

# Class Method
ECommerce.total_customers_count()

# Static Method
original_price = 200
discount_rate = 10
discounted_price = ECommerce.calculate_discount(original_price, discount_rate)
print(
    f"The discounted price of the item worth ${original_price} with {discount_rate}% discount is ${discounted_price:.2f}.")
