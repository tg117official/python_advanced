# Custom Iterator: Department-wise Employee Iterator
class DepartmentIterator:
    """Iterator to iterate over employees by department."""
    def __init__(self, employees, department):
        self.employees = [emp for emp in employees if emp["department"] == department]
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.employees):
            raise StopIteration
        employee = self.employees[self.index]
        self.index += 1
        return employee

# Generator: Employee Performance Generator
def employee_performance_generator(employees):
    """Generate employee performance scores."""
    for employee in employees:
        yield int(employee["performance_score"])
