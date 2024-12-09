# tasks/task_handler.py

class TaskHandler:
    """Class to handle task management."""

    def __init__(self):
        self.tasks = []

    def add_task(self, task_name):
        """Add a new task."""
        self.tasks.append({"name": task_name, "completed": False})

    def view_tasks(self):
        """View all tasks."""
        return self.tasks

    def update_task(self, index, new_name):
        """Update a task name by index."""
        if 0 <= index < len(self.tasks):
            self.tasks[index]["name"] = new_name
        else:
            raise IndexError("Task index out of range.")

    def delete_task(self, index):
        """Delete a task by index."""
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
        else:
            raise IndexError("Task index out of range.")
