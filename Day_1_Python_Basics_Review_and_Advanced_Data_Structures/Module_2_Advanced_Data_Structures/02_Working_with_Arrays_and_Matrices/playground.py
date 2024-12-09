import numpy as np

array = np.array([[[[5, 6, 9],
                    [7, 6, 4],
                    [2, 8, 3]],

                   [[5, 7, 5],
                    [9, 7, 6],
                    [6, 8, 3]],

                   [[4, 4, 7],
                    [3, 3, 9],
                    [7, 6, 4]]],

                  [[[4, 4, 5],
                    [8, 1, 6],
                    [2, 7, 6]],

                   [[8, 7, 4],
                    [1, 4, 1],
                    [3, 7, 8]],

                   [[6, 7, 7],
                    [5, 5, 5],
                    [3, 4, 9]]],

                  [[[4, 2, 8],
                    [9, 2, 4],
                    [9, 9, 4]],

                   [[9, 7, 4],
                    [5, 3, 5],
                    [2, 7, 8]],

                   [[9, 8, 4],
                    [4, 1, 8],
                    [2, 2, 3]]]])

print(array)
# Entire Group (Axis 0):
print("First Element : ", array[0,0,2, 2])  # First group (shape: (3, 3, 3))

# # Single Matrix (Axis 1):
# print(array[0, 1])  # Second matrix in the first group (shape: (3, 3))
#
# # Single Row (Axis 2):
# print(array[0, 1, 0])  # First row in the second matrix of the first group (shape: (3,))
#
# # Single Element (Axis 3):
# print(array[0, 1, 0, 2])  # Third element in the first row of the second matrix in the first group

# [9, 8, 4]

# [4, 2, 8],
# [9, 2, 4],
# [9, 9, 4]



#                      [[[4, 4, 5],
#                     [8, 1, 6],
#                     [2, 7, 6]],
#
#                    [[8, 7, 4],
#                     [1, 4, 1],
#                     [3, 7, 8]],
#
#                    [[6, 7, 7],
#                     [5, 5, 5],
#                     [3, 4, 9]]]


#  3






