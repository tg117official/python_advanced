from functools import reduce

# First-Class Function: Calculate Bonus
def calculate_bonus(employee):
    """Calculate bonus based on performance score."""
    performance = int(employee["performance_score"])
    salary = int(employee["salary"])
    return salary * 0.1 if performance >= 80 else 0

# Map: Calculate bonuses for all employees
def map_bonuses(employees):
    """Calculate bonuses for all employees."""
    return list(map(calculate_bonus, employees))

# Filter: Select high-performing employees
def filter_high_performers(employees, threshold=80):
    """Filter employees with performance scores above the threshold."""
    return list(filter(lambda emp: int(emp["performance_score"]) > threshold, employees))

# Reduce: Calculate total salary expenses
def reduce_total_salary(employees):
    """Calculate total salary expenses."""
    return reduce(lambda acc, emp: acc + int(emp["salary"]), employees, 0)
