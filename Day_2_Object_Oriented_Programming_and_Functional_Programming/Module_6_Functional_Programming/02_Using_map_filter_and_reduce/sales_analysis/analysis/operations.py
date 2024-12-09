from functools import reduce

def calculate_total_revenue(sales_data):
    """Calculate total revenue using map and reduce."""
    revenues = map(lambda row: row['price'] * row['quantity'], sales_data)
    return reduce(lambda x, y: x + y, revenues)

def filter_valid_transactions(sales_data):
    """Filter out transactions with negative quantities or invalid prices."""
    return list(filter(lambda row: row['quantity'] > 0 and row['price'] > 0, sales_data))

def average_sales_by_category(sales_data):
    """Calculate average sales per category using map, filter, and reduce."""
    categories = set(map(lambda row: row['category'], sales_data))
    averages = {}
    for category in categories:
        category_sales = list(filter(lambda row: row['category'] == category, sales_data))
        total_sales = reduce(lambda x, y: x + y, map(lambda row: row['price'] * row['quantity'], category_sales))
        averages[category] = total_sales / len(category_sales)
    return averages
