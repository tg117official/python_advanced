from analysis.data_loader import load_sales_data, clean_data
from analysis.operations import calculate_total_revenue, filter_valid_transactions, average_sales_by_category

def main():
    # Load and clean data
    filepath = "data/sales_data.csv"
    sales_data = load_sales_data(filepath)
    cleaned_data = clean_data(sales_data)

    # Filter valid transactions
    valid_data = filter_valid_transactions(cleaned_data)

    # Calculate total revenue
    total_revenue = calculate_total_revenue(valid_data)
    print(f"Total Revenue: ${total_revenue:.2f}")

    # Calculate average sales by category
    averages = average_sales_by_category(valid_data)
    print("\nAverage Sales by Category:")
    for category, avg in averages.items():
        print(f"{category}: ${avg:.2f}")

if __name__ == "__main__":
    main()
