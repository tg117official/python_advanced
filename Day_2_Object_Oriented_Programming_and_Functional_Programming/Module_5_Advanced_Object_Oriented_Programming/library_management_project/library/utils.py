def save_data(filename, data):
    """Save data to a file."""
    with open(filename, 'w') as file:
        file.write(data)


def load_data(filename):
    """Load data from a file."""
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return ""
