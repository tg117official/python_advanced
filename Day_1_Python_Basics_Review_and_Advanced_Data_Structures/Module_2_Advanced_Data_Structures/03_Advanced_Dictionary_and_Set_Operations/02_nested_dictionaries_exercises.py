###################################### BASIC #####################################################

# Exercise 1: Create a Nested Dictionary
# Problem:
# Create a nested dictionary to store information about three students. Each student should have keys for "name", "age", and "grades".
#
# Code:

# Nested dictionary
students = {
    1: {"name": "Alice", "age": 20, "grades": [85, 90, 78]},
    2: {"name": "Bob", "age": 22, "grades": [72, 88, 91]},
    3: {"name": "Charlie", "age": 21, "grades": [90, 85, 87]},
}

# Display the nested dictionary
print(students)


# Expected Output:
#
# {
#     1: {'name': 'Alice', 'age': 20, 'grades': [85, 90, 78]},
#     2: {'name': 'Bob', 'age': 22, 'grades': [72, 88, 91]},
#     3: {'name': 'Charlie', 'age': 21, 'grades': [90, 85, 87]}
# }




# Exercise 2: Access a Value in a Nested Dictionary
# Problem:
# Access the age of the student with ID `2` from the nested dictionary.
#
# Code:

# Nested dictionary
students = {
    1: {"name": "Alice", "age": 20, "grades": [85, 90, 78]},
    2: {"name": "Bob", "age": 22, "grades": [72, 88, 91]},
    3: {"name": "Charlie", "age": 21, "grades": [90, 85, 87]},
}

# Access the age of student with ID 2
print(students[2]["age"])


# Expected Output:
#
# 22




# Exercise 3: Add a New Key to a Nested Dictionary
# Problem:
# Add a new key "major" to each student in the nested dictionary.
#
# Code:

# Nested dictionary
students = {
    1: {"name": "Alice", "age": 20, "grades": [85, 90, 78]},
    2: {"name": "Bob", "age": 22, "grades": [72, 88, 91]},
    3: {"name": "Charlie", "age": 21, "grades": [90, 85, 87]},
}

# Add a new key "major"
for student in students.values():
    student["major"] = "Undecided"

# Display the updated nested dictionary
print(students)


# Expected Output:
#
# {
#     1: {'name': 'Alice', 'age': 20, 'grades': [85, 90, 78], 'major': 'Undecided'},
#     2: {'name': 'Bob', 'age': 22, 'grades': [72, 88, 91], 'major': 'Undecided'},
#     3: {'name': 'Charlie', 'age': 21, 'grades': [90, 85, 87], 'major': 'Undecided'}
# }




# Exercise 4: Iterate Over a Nested Dictionary
# Problem:
# Print the name and grades of each student in the nested dictionary.
#
# Code:

# Nested dictionary
students = {
    1: {"name": "Alice", "age": 20, "grades": [85, 90, 78]},
    2: {"name": "Bob", "age": 22, "grades": [72, 88, 91]},
    3: {"name": "Charlie", "age": 21, "grades": [90, 85, 87]},
}

# Iterate and print name and grades
for student_id, student_info in students.items():
    print(f"Student {student_id}: {student_info['name']} - Grades: {student_info['grades']}")


# Expected Output:
#
# Student 1: Alice - Grades: [85, 90, 78]
# Student 2: Bob - Grades: [72, 88, 91]
# Student 3: Charlie - Grades: [90, 85, 87]




# Exercise 5: Delete a Key from a Nested Dictionary
# Problem:
# Remove the "age" key from each student in the nested dictionary.
#
# Code:

# Nested dictionary
students = {
    1: {"name": "Alice", "age": 20, "grades": [85, 90, 78]},
    2: {"name": "Bob", "age": 22, "grades": [72, 88, 91]},
    3: {"name": "Charlie", "age": 21, "grades": [90, 85, 87]},
}

# Remove the "age" key
for student in students.values():
    student.pop("age")

# Display the updated nested dictionary
print(students)


# Expected Output:
#
# {
#     1: {'name': 'Alice', 'grades': [85, 90, 78]},
#     2: {'name': 'Bob', 'grades': [72, 88, 91]},
#     3: {'name': 'Charlie', 'grades': [90, 85, 87]}
# }

############################################ INTERMEDIATE ############################################

# Exercise 1: Merge Two Nested Dictionaries
# Problem:
# Merge two nested dictionaries such that the keys in common have their inner dictionaries merged.
#
# Code:

# Input dictionaries
dict1 = {
    'student1': {'name': 'Alice', 'age': 20},
    'student2': {'name': 'Bob', 'age': 22}
}
dict2 = {
    'student2': {'grade': 'A'},
    'student3': {'name': 'Charlie', 'age': 21, 'grade': 'B'}
}

# Merge the dictionaries
merged_dict = {key: {dict1.get(key, {}), dict2.get(key, {})} for key in dict1.keys() | dict2.keys()}

# Display the result
print(merged_dict)


# Expected Output:
#
# {
#     'student1': {'name': 'Alice', 'age': 20},
#     'student2': {'name': 'Bob', 'age': 22, 'grade': 'A'},
#     'student3': {'name': 'Charlie', 'age': 21, 'grade': 'B'}
# }




# Exercise 2: Find Maximum Value in a Nested Dictionary
# Problem:
# Find the student with the highest grade from a nested dictionary.
#
# Code:

# Input nested dictionary
students = {
    'student1': {'name': 'Alice', 'grade': 85},
    'student2': {'name': 'Bob', 'grade': 90},
    'student3': {'name': 'Charlie', 'grade': 78}
}

# Find the student with the highest grade
max_student = max(students.items(), key=lambda x: x[1]['grade'])

# Display the result
print(f"Top student: {max_student[1]['name']} with grade {max_student[1]['grade']}")


# Expected Output:
#
# Top student: Bob with grade 90




# Exercise 3: Add a Nested Key
# Problem:
# Add a nested key-value pair to each student in the dictionary.
#
# Code:

# Input nested dictionary
students = {
    'student1': {'name': 'Alice', 'age': 20},
    'student2': {'name': 'Bob', 'age': 22},
    'student3': {'name': 'Charlie', 'age': 21}
}

# Add a new key-value pair
for student in students.values():
    student['status'] = 'active'

# Display the result
print(students)


# Expected Output:
#
# {
#     'student1': {'name': 'Alice', 'age': 20, 'status': 'active'},
#     'student2': {'name': 'Bob', 'age': 22, 'status': 'active'},
#     'student3': {'name': 'Charlie', 'age': 21, 'status': 'active'}
# }




# Exercise 4: Filter Nested Dictionary
# Problem:
# Filter the nested dictionary to include only students older than 21.
#
# Code:

# Input nested dictionary
students = {
    'student1': {'name': 'Alice', 'age': 20},
    'student2': {'name': 'Bob', 'age': 22},
    'student3': {'name': 'Charlie', 'age': 21}
}

# Filter the dictionary
filtered_students = {key: value for key, value in students.items() if value['age'] > 21}

# Display the result
print(filtered_students)


# Expected Output:
#
# {
#     'student2': {'name': 'Bob', 'age': 22}
# }




# Exercise 5: Flatten a Nested Dictionary
# Problem:
# Flatten a nested dictionary into a single-level dictionary with keys as tuples.
#
# Code:

# Input nested dictionary
nested_dict = {
    'student1': {'name': 'Alice', 'age': 20},
    'student2': {'name': 'Bob', 'age': 22},
    'student3': {'name': 'Charlie', 'age': 21}
}

# Flatten the dictionary
flattened_dict = {(outer_key, inner_key): inner_value
                  for outer_key, inner_dict in nested_dict.items()
                  for inner_key, inner_value in inner_dict.items()}

# Display the result
print(flattened_dict)


# Expected Output:
#
# {
#     ('student1', 'name'): 'Alice',
#     ('student1', 'age'): 20,
#     ('student2', 'name'): 'Bob',
#     ('student2', 'age'): 22,
#     ('student3', 'name'): 'Charlie',
#     ('student3', 'age'): 21
# }


