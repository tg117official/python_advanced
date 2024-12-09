from performance.data_loader import load_employee_data
from performance.analytics import (
    map_bonuses,
    filter_high_performers,
    reduce_total_salary,
)
from performance.iterators import DepartmentIterator, employee_performance_generator

def main():
    try:
        # Load data
        employees = load_employee_data("data/employees.csv")

        # Map: Calculate bonuses
        bonuses = map_bonuses(employees)
        print("\n--- Employee Bonuses ---")
        for emp, bonus in zip(employees, bonuses):
            print(f"{emp['name']} (Performance: {emp['performance_score']}): ${bonus:.2f}")

        # Filter: High Performers
        high_performers = filter_high_performers(employees)
        print("\n--- High Performers ---")
        for emp in high_performers:
            print(f"{emp['name']} (Performance: {emp['performance_score']})")

        # Reduce: Total Salary
        total_salary = reduce_total_salary(employees)
        print(f"\n--- Total Salary Expenses ---\n${total_salary}")

        # Custom Iterator: Department-Wise Employees
        print("\n--- Employees in Engineering ---")
        eng_iterator = DepartmentIterator(employees, "Engineering")
        for emp in eng_iterator:
            print(f"{emp['name']} (Performance: {emp['performance_score']})")

        # Generator: Employee Performance Scores
        print("\n--- Employee Performance Scores ---")
        for score in employee_performance_generator(employees):
            print(score)

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
