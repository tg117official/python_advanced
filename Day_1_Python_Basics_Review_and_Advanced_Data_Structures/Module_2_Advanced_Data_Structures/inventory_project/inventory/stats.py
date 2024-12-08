import numpy as np

def calculate_statistics(transactions):
    # Convert transaction amounts to a NumPy array
    sales = np.array([t[2] for t in transactions], dtype=float)
    total_sales = np.sum(sales)
    average_sales = np.mean(sales) if len(sales) > 0 else 0
    return total_sales, average_sales
