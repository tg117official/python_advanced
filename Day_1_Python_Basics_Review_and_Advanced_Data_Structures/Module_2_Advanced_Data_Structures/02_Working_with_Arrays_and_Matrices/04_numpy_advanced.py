# Understanding Multi Dimensional Matrix and their Axis
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


# Entire Group (Axis 0):
print(array[0])  # First group (shape: (3, 3, 3))

# Single Matrix (Axis 1):
print(array[0, 1])  # Second matrix in the first group (shape: (3, 3))

# Single Row (Axis 2):
print(array[0, 1, 0])  # First row in the second matrix of the first group (shape: (3,))

# Single Element (Axis 3):
print(array[0, 1, 0, 2])  # Third element in the first row of the second matrix in the first group




# ------------------- Exercise 1 -------------------
# Problem: Generate a 10x10 matrix of random integers between 1 and 100.
# Sort the matrix by the sum of each row in ascending order.
# Expected Output:
# Original Matrix:
# [...]
# Row-wise Sum:
# [...]
# Sorted Matrix:
# [...]
matrix1 = np.random.randint(1, 100, (10, 10))
row_sums = np.sum(matrix1, axis=1)
sorted_indices = np.argsort(row_sums)
sorted_matrix1 = matrix1[sorted_indices]
print("Exercise 1 - Original Matrix:\n", matrix1)
print("Exercise 1 - Row-wise Sum:", row_sums)
print("Exercise 1 - Sorted Matrix:\n", sorted_matrix1)

# Relevance: Sorting by aggregated values is essential in ranking systems, priority-based processing, and report generation.

# ------------------- Exercise 2 -------------------
# Problem: Create a 3D array of shape (4, 4, 4) with random values.
# Normalize the array so that all values are scaled between 0 and 1.
# Expected Output:
# Original 3D Array:
# [...]
# Normalized 3D Array:
# [...]
array2 = np.random.rand(4, 4, 4)
normalized_array2 = (array2 - np.min(array2)) / (np.max(array2) - np.min(array2))
print("Exercise 2 - Original 3D Array:\n", array2)
print("Exercise 2 - Normalized 3D Array:\n", normalized_array2)

# Relevance: Normalization of high-dimensional data is critical in simulations, image processing, and machine learning pipelines.

# ------------------- Exercise 3 -------------------
# Problem: Generate a 1D array of 50 random integers between 1 and 100.
# Find the most frequent value in the array and its frequency.
# Expected Output:
# Array: [...]
# Most Frequent Value: <value>
# Frequency: <frequency>
array3 = np.random.randint(1, 100, 50)
unique_values, counts = np.unique(array3, return_counts=True)
most_frequent_value = unique_values[np.argmax(counts)]
frequency = counts[np.argmax(counts)]
print("Exercise 3 - Array:", array3)
print("Exercise 3 - Most Frequent Value:", most_frequent_value)
print("Exercise 3 - Frequency:", frequency)

# Relevance: Frequency analysis is used in recommendation systems, trend detection, and statistical profiling.

# ------------------- Exercise 4 -------------------
# Problem: Create a 6x6 matrix with random integers between 1 and 50.
# Replace all elements with their position-based sum (row_index + col_index).
# Expected Output:
# Original Matrix:
# [...]
# Updated Matrix:
# [...]
matrix4 = np.random.randint(1, 50, (6, 6))
updated_matrix4 = np.fromfunction(lambda i, j: i + j, (6, 6), dtype=int)
print("Exercise 4 - Original Matrix:\n", matrix4)
print("Exercise 4 - Updated Matrix:\n", updated_matrix4)

# Relevance: Position-based data transformation is used in spatial simulations, grid-based computations, and heatmap generation.

# ------------------- Exercise 5 -------------------
# Problem: Simulate rolling a dice 1000 times and calculate the probability of each face appearing.
# Expected Output:
# Rolls: [...]
# Probabilities: [P(1), P(2), P(3), P(4), P(5), P(6)]
dice_rolls = np.random.randint(1, 7, 1000)
face_counts = np.bincount(dice_rolls, minlength=7)[1:]  # Skip index 0
probabilities = face_counts / np.sum(face_counts)
print("Exercise 5 - Rolls:", dice_rolls[:20], "...")  # Showing first 20 rolls for brevity
print("Exercise 5 - Probabilities:", probabilities)

# Relevance: Probability simulations are vital in risk assessment, gaming analytics, and predictive modeling


# ------------------- Exercise 6 -------------------
# Problem: Generate a 7x7 matrix with random integers between 1 and 100.
# Replace all elements on the border with 1 and all inner elements with 0.
# Expected Output:
# Original Matrix:
# [...]
# Updated Matrix:
# [...]
matrix6 = np.random.randint(1, 100, (7, 7))
matrix6[1:-1, 1:-1] = 0  # Set inner elements to 0
matrix6[0, :] = matrix6[-1, :] = matrix6[:, 0] = matrix6[:, -1] = 1  # Set borders to 1
print("Exercise 6 - Original Matrix:\n", matrix6)

# Relevance: Border manipulations are useful in image padding, edge detection, and boundary conditions in simulations.

# ------------------- Exercise 7 -------------------
# Problem: Create a 1D array of 30 random integers between 1 and 20.
# Find the unique values, their frequencies, and create a dictionary mapping each value to its frequency.
# Expected Output:
# Array: [...]
# Frequency Dictionary: {value1: freq1, value2: freq2, ...}
array7 = np.random.randint(1, 20, 30)
unique_values, counts = np.unique(array7, return_counts=True)
frequency_dict = dict(zip(unique_values, counts))
print("Exercise 7 - Array:", array7)
print("Exercise 7 - Frequency Dictionary:", frequency_dict)

# Relevance: Frequency mapping is widely applied in natural language processing (NLP), customer segmentation, and market basket analysis.

# ------------------- Exercise 8 -------------------
# Problem: Create a 10x10 matrix with random integers between 1 and 100.
# Find the top 3 largest values in the matrix along with their positions (row, column).
# Expected Output:
# Matrix:
# [...]
# Top 3 Values: [...]
# Positions: [(row1, col1), (row2, col2), (row3, col3)]
matrix8 = np.random.randint(1, 100, (10, 10))
flat_indices = np.argsort(matrix8.ravel())[-3:][::-1]  # Indices of top 3 values in flattened array
top_3_values = matrix8.ravel()[flat_indices]
positions = [np.unravel_index(idx, matrix8.shape) for idx in flat_indices]
print("Exercise 8 - Matrix:\n", matrix8)
print("Exercise 8 - Top 3 Values:", top_3_values)
print("Exercise 8 - Positions:", positions)

# Relevance: Identifying top values is crucial in optimization, resource management, and identifying key insights in datasets.

# ------------------- Exercise 9 -------------------
# Problem: Create a 4D array of shape (3, 3, 3, 3) with random integers between 1 and 10.
# Compute the sum along the third axis and reshape the result into a 2D array.
# Expected Output:
# Original 4D Array:
# [...]
# Sum Along Third Axis:
# [...]
# Reshaped to 2D:
# [...]
array9 = np.random.randint(1, 10, (3, 3, 3, 3))
sum_along_axis = np.sum(array9, axis=2)
reshaped_array = sum_along_axis.reshape(3, -1)
print("Exercise 9 - Original 4D Array:\n", array9)
print("Exercise 9 - Sum Along Third Axis:\n", sum_along_axis)
print("Exercise 9 - Reshaped to 2D:\n", reshaped_array)

# Relevance: Summing and reshaping multi-dimensional data is essential in hierarchical data analysis and neural network preprocessing.

# ------------------- Exercise 10 -------------------
# Problem: Create two 5x5 matrices with random integers between 1 and 50.
# Perform the following operations:
# 1. Element-wise multiplication.
# 2. Find the element-wise maximum of the resulting matrix.
# Expected Output:
# Matrix A:
# [...]
# Matrix B:
# [...]
# Element-wise Multiplication:
# [...]
# Element-wise Maximum: <max_value>
matrix_a = np.random.randint(1, 50, (5, 5))
matrix_b = np.random.randint(1, 50, (5, 5))
elementwise_product = matrix_a * matrix_b
elementwise_max = np.max(elementwise_product)
print("Exercise 10 - Matrix A:\n", matrix_a)
print("Exercise 10 - Matrix B:\n", matrix_b)
print("Exercise 10 - Element-wise Multiplication:\n", elementwise_product)
print("Exercise 10 - Element-wise Maximum:", elementwise_max)

# Relevance: Element-wise operations are key in resource allocation models, pixel-wise computations, and matrix-based transformations.
