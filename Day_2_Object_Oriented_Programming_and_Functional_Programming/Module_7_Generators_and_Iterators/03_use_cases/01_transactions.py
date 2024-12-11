import json
from functools import reduce, lru_cache

# Data Source (Simulated Database and API responses)
products = [
    {"id": 1, "name": "Laptop", "category": "Electronics", "price": 800},
    {"id": 2, "name": "Smartphone", "category": "Electronics", "price": 500},
    {"id": 3, "name": "Shirt", "category": "Apparel", "price": 20},
    {"id": 4, "name": "Shoes", "category": "Apparel", "price": 50},
]

transactions = [
    {"id": 1, "product_id": 1, "quantity": 2, "date": "2024-12-01"},
    {"id": 2, "product_id": 2, "quantity": 1, "date": "2024-12-02"},
    {"id": 3, "product_id": 3, "quantity": 5, "date": "2024-12-03"},
    {"id": 4, "product_id": 4, "quantity": 3, "date": "2024-12-04"},
]

# 1. Using First-Class Functions for Data Retrieval
def get_products():
    return products

def get_transactions():
    return transactions

# 2. Using LRU Cache for Optimized Caching of Expensive Operations
@lru_cache(maxsize=100)
def calculate_total_sales(product_id):
    relevant_transactions = filter(lambda t: t['product_id'] == product_id, transactions)
    return sum(
        t['quantity'] * next(p['price'] for p in products if p['id'] == t['product_id'])
        for t in relevant_transactions
    )

# 3. Using Map, Filter, Reduce

def summarize_sales():
    summary = map(lambda product: {
        "product_name": product["name"],
        "total_sales": calculate_total_sales(product["id"])
    }, products)

    return list(summary)

# 4. Using Decorators for Data Validation
def validate_transaction(func):
    def wrapper(transaction):
        if not transaction.get("product_id") or not transaction.get("quantity"):
            raise ValueError("Invalid transaction: Missing required fields.")
        return func(transaction)
    return wrapper

@validate_transaction
def add_transaction(transaction):
    transactions.append(transaction)
    return "Transaction added successfully."

# 5. Using Generators for Streaming Transactions
def transaction_generator():
    for transaction in transactions:
        yield transaction

# 6. Using an Iterator for Iterating Over Products
class ProductIterator:
    def __init__(self, products):
        self.products = products
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.products):
            product = self.products[self.index]
            self.index += 1
            return product
        else:
            raise StopIteration

# 7. Main Functionality
if __name__ == "__main__":
    while True:
        print("\nOptions:")
        print("1. Add a new transaction")
        print("2. View sales summary")
        print("3. Calculate total revenue")
        print("4. View all transactions (Generator)")
        print("5. View all products (Iterator)")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            try:
                transaction_id = int(input("Enter transaction ID: "))
                product_id = int(input("Enter product ID: "))
                quantity = int(input("Enter quantity: "))
                date = input("Enter transaction date (YYYY-MM-DD): ")

                new_transaction = {"id": transaction_id, "product_id": product_id, "quantity": quantity, "date": date}
                print(add_transaction(new_transaction))
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "2":
            sales_summary = summarize_sales()
            print(json.dumps(sales_summary, indent=4))

        elif choice == "3":
            sales_summary = summarize_sales()
            total_revenue = reduce(lambda acc, product: acc + product["total_sales"], sales_summary, 0)
            print(f"Total Revenue: ${total_revenue}")

        elif choice == "4":
            print("Transactions:")
            for transaction in transaction_generator():
                print(transaction)

        elif choice == "5":
            print("Products:")
            product_iter = ProductIterator(products)
            for product in product_iter:
                print(product)

        elif choice == "6":
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")
