emp_dict = {
             'id' : 114,
             'name' : 'Xyz',
             'dept' : 'IT',
             'salary': 5000
}

# Accessing Elements
# print(emp_dict['name'])
# print(emp_dict.get('dept', 'NA'))

# Adding New Elements
# emp_dict['email'] = 'xyz@abc.com'
# print(emp_dict)

# Updating existing element
# emp_dict['salary'] = 5500
# print(emp_dict)

# Remove elements
# emp_dict.pop('name')
# print(emp_dict)

# emp_dict.popitem()
# print(emp_dict)

print(tuple(emp_dict.keys()))
print(tuple(emp_dict.values()))
print(tuple(emp_dict.items()))
