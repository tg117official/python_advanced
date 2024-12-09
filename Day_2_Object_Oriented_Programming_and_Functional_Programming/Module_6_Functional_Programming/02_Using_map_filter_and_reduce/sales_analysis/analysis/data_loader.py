import csv

def load_sales_data(filepath):
    """Load sales data from a CSV file."""
    with open(filepath, 'r') as file:
        reader = csv.DictReader(file)
        return list(reader)

def clean_data(sales_data):
    """Clean data by converting price and quantity to integers and filtering valid rows."""
    def parse_row(row):
        try:
            row['price'] = float(row['price'])
            row['quantity'] = int(row['quantity'])
            return row
        except ValueError:
            return None

    return list(filter(None, map(parse_row, sales_data)))
