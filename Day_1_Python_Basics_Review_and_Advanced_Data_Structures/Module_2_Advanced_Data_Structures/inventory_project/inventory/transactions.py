from collections import deque
from .products import update_stock, get_product

# Deque to track the last 5 transactions
transactions = deque(maxlen=5)

def add_transaction(product_id, quantity):
    product = get_product(product_id)
    if product and product.stock >= quantity:
        transactions.append((product_id, quantity, product.price * quantity))
        update_stock(product_id, -quantity)
    else:
        print("Transaction failed: Insufficient stock or invalid product.")
