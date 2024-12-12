# Input dictionaries
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 20, 'c': 30, 'd': 40}

# Dictionary comprehension
merged_dict = {key: dict2.get(key, dict1.get(key)) for key in dict1.keys() | dict2.keys()}

# for key in dict1.keys() | dict2.keys() :
#     merged_dict[key] = dict2.get(key, dict1.get(key))
# #   merged_dict['b'] = dict2.get('b', dict1.get('b'))
# #   merged_dict['b'] = 20
#     print(key)

# Display the result
# print(merged_dict)