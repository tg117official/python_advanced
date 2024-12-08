from inventory.products import add_product, update_stock, get_product
from inventory.transactions import add_transaction, transactions
from inventory.stats import calculate_statistics


def main():
    # Add sample products
    add_product("P001", "Laptop", 750, 10)
    add_product("P002", "Headphones", 50, 20)
    add_product("P003", "Keyboard", 30, 15)

    # Perform transactions
    add_transaction("P001", 2)  # Sell 2 laptops
    add_transaction("P002", 5)  # Sell 5 headphones
    add_transaction("P003", 1)  # Sell 1 keyboard

    # Display recent transactions
    print("\nRecent Transactions:")
    for t in transactions:
        print(t)

    # Calculate and display statistics
    total, average = calculate_statistics(transactions)
    print(f"\nTotal Sales: ${total}")
    print(f"Average Sales: ${average:.2f}")


if __name__ == "__main__":
    main()
