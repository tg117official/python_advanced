# tasks/file_handler.py

def save_to_file(filename, tasks):
    """Save tasks to a file."""
    try:
        with open(filename, 'w') as file:
            for task in tasks:
                file.write(f"{task['name']}|{task['completed']}\n")
    except IOError as e:
        raise IOError(f"Error writing to file: {e}")


def load_from_file(filename):
    """Load tasks from a file."""
    tasks = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                name, completed = line.strip().split('|')
                tasks.append({"name": name, "completed": completed == 'True'})
    except FileNotFoundError:
        pass  # No file to load; start with an empty list
    return tasks
