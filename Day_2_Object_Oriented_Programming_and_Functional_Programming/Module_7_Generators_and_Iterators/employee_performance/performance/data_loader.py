import csv

def load_employee_data(filepath):
    """Load employee data from a CSV file."""
    try:
        with open(filepath, 'r') as file:
            reader = csv.DictReader(file)
            return [row for row in reader]
    except FileNotFoundError as e:
        raise FileNotFoundError(f"Error: File not found at {filepath}") from e
