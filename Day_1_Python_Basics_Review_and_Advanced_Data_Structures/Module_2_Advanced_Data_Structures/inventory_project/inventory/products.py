from collections import namedtuple

# Define the Product namedtuple
Product = namedtuple("Product", ["id", "name", "price", "stock"])

# Dictionary to store products by their ID
products = {}

def add_product(product_id, name, price, stock):
    products[product_id] = Product(product_id, name, price, stock)

def update_stock(product_id, quantity):
    if product_id in products:
        current = products[product_id]
        products[product_id] = current._replace(stock=current.stock + quantity)
    else:
        print(f"Product with ID {product_id} does not exist.")

def get_product(product_id):
    return products.get(product_id, None)
