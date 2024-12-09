from tasks.task_handler import TaskHandler
from tasks.file_handler import save_to_file, load_from_file

def task_manager(filename):
    """Closure to manage tasks with file persistence."""
    handler = TaskHandler()

    # Load tasks from file
    handler.tasks = load_from_file(filename)

    def add_task(task_name):
        handler.add_task(task_name)

    def view_tasks():
        return handler.view_tasks()

    def update_task(index, new_name):
        handler.update_task(index, new_name)

    def delete_task(index):
        handler.delete_task(index)

    def save_tasks():
        save_to_file(filename, handler.tasks)

    return add_task, view_tasks, update_task, delete_task, save_tasks


def main():
    print("=== Task Management System ===")
    add_task, view_tasks, update_task, delete_task, save_tasks = task_manager("data/tasks.txt")

    while True:
        print("\n1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Save and Exit")
        choice = input("Choose an option: ")

        try:
            if choice == "1":
                task_name = input("Enter task name: ")
                add_task(task_name)
                print(f"Task '{task_name}' added successfully!")

            elif choice == "2":
                tasks = view_tasks()
                print("\n--- Tasks ---")
                for i, task in enumerate(tasks):
                    status = "Completed" if task["completed"] else "Pending"
                    print(f"{i + 1}. {task['name']} - {status}")

            elif choice == "3":
                index = int(input("Enter task index to update: ")) - 1
                new_name = input("Enter new task name: ")
                update_task(index, new_name)
                print(f"Task {index + 1} updated successfully!")

            elif choice == "4":
                index = int(input("Enter task index to delete: ")) - 1
                delete_task(index)
                print(f"Task {index + 1} deleted successfully!")

            elif choice == "5":
                save_tasks()
                print("Tasks saved successfully! Exiting...")
                break

            else:
                print("Invalid choice! Please try again.")

        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
