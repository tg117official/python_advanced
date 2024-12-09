from config.settings import EMPLOYEE_FILE
from utils.file_operations import read_file, write_file, append_to_file
from utils.validations import validate_employee_id, validate_employee_name


def add_employee():
    emp_id = input("Enter Employee ID: ")
    if not validate_employee_id(emp_id):
        print("Invalid Employee ID!")
        return
    name = input("Enter Employee Name: ")
    if not validate_employee_name(name):
        print("Invalid Name!")
        return
    age = input("Enter Employee Age: ")
    department = input("Enter Department: ")

    append_to_file(EMPLOYEE_FILE, [emp_id, name, age, department])
    print("Employee added successfully!")


def view_employees():
    employees = read_file(EMPLOYEE_FILE)
    if not employees:
        print("No employees found!")
        return
    for emp in employees:
        print(f"ID: {emp[0]}, Name: {emp[1]}, Age: {emp[2]}, Department: {emp[3]}")


def main():
    while True:
        print("\nEmployee Management System")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_employee()
        elif choice == "2":
            view_employees()
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
