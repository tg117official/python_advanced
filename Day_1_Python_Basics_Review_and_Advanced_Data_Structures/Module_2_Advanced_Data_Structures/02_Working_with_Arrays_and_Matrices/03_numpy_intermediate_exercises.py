import numpy as np

# ------------------- Exercise 1 -------------------
# Problem: Create a 5x5 matrix where each element is the sum of its row and column indices.
# Expected Output:
# [[0 1 2 3 4]
#  [1 2 3 4 5]
#  [2 3 4 5 6]
#  [3 4 5 6 7]
#  [4 5 6 7 8]]
matrix1 = np.fromfunction(lambda i, j: i + j, (5, 5), dtype=int)
print("Exercise 1:\n", matrix1)

# Position-based operations are widely used in heatmaps, grid simulations, and representing relational data.

# ------------------- Exercise 2 -------------------
# Problem: Create a 1D array of 20 random integers between 1 and 100.
# Replace all even numbers with 0 and all odd numbers with 1.
# Expected Output: A binary array with 0 for even and 1 for odd values.
array2 = np.random.randint(1, 100, 20)
binary_array = np.where(array2 % 2 == 0, 0, 1)
print("Exercise 2 - Original Array:", array2)
print("Exercise 2 - Binary Array:", binary_array)

# Conditional transformations are essential in binary classification, feature engineering, and preprocessing.

# ------------------- Exercise 3 -------------------
# Problem: Create a 4x4 matrix and normalize it so that all values
# lie between 0 and 1 using Min-Max normalization.
# Expected Output: A normalized matrix with values between 0 and 1.
matrix3 = np.random.randint(1, 100, (4, 4))
normalized_matrix = (matrix3 - matrix3.min()) / (matrix3.max() - matrix3.min())
print("Exercise 3 - Original Matrix:\n", matrix3)
print("Exercise 3 - Normalized Matrix:\n", normalized_matrix)

# Normalization is crucial in machine learning pipelines to standardize features for better model performance.

# ------------------- Exercise 4 -------------------
# Problem: Create two 3x3 matrices. Find the row-wise and column-wise maximum values.
# Expected Output:
# Matrix A:
# [[...]]
# Row-wise Max: [...]
# Column-wise Max: [...]
matrix4_a = np.random.randint(1, 50, (3, 3))
row_max = np.max(matrix4_a, axis=1)
col_max = np.max(matrix4_a, axis=0)
print("Exercise 4 - Matrix A:\n", matrix4_a)
print("Exercise 4 - Row-wise Max:", row_max)
print("Exercise 4 - Column-wise Max:", col_max)

# Identifying maximum values is critical in optimization problems, image processing, and resource allocation tasks.

# ------------------- Exercise 5 -------------------
# Problem: Create a 1D array of 15 elements and split it into 3 equal parts.
# Calculate the mean of each part.
# Expected Output:
# Part 1: [...]
# Part 2: [...]
# Part 3: [...]
# Means: [mean1, mean2, mean3]
array5 = np.arange(15)
split_arrays = np.split(array5, 3)
means = [np.mean(part) for part in split_arrays]
print("Exercise 5 - Array:", array5)
for idx, part in enumerate(split_arrays, 1):
    print(f"Exercise 5 - Part {idx}:", part)
print("Exercise 5 - Means:", means)

# Relevance: Splitting and aggregating data is useful in partitioning datasets, batch processing, and summarizing data.


# ------------------- Exercise 6 -------------------
# Problem: Create a 6x6 matrix with random integers between 10 and 50.
# Extract the diagonal elements and calculate their sum.
# Expected Output:
# Matrix:
# [...]
# Diagonal Elements: [...]
# Sum of Diagonal: <sum>
matrix6 = np.random.randint(10, 50, (6, 6))
diagonal_elements = np.diagonal(matrix6)
sum_diagonal = np.sum(diagonal_elements)
print("Exercise 6 - Matrix:\n", matrix6)
print("Exercise 6 - Diagonal Elements:", diagonal_elements)
print("Exercise 6 - Sum of Diagonal:", sum_diagonal)

# Relevance: Diagonal extraction is important in linear algebra, graph theory (e.g., adjacency matrices), and financial modeling.

# ------------------- Exercise 7 -------------------
# Problem: Create a 3D array of shape (3, 3, 3) with random values.
# Replace all values greater than 0.5 with 1 and others with 0.
# Expected Output: A 3D binary array with values replaced.
array7 = np.random.rand(3, 3, 3)
binary_3d_array = np.where(array7 > 0.5, 1, 0)
print("Exercise 7 - Original 3D Array:\n", array7)
print("Exercise 7 - Binary 3D Array:\n", binary_3d_array)

# Relevance: Thresholding is widely used in image binarization, neural network activation functions, and decision-making processes.

# ------------------- Exercise 8 -------------------
# Problem: Create a 5x5 matrix and compute the cumulative sum along rows and columns.
# Expected Output:
# Matrix:
# [...]
# Row-wise Cumulative Sum:
# [...]
# Column-wise Cumulative Sum:
# [...]
matrix8 = np.random.randint(1, 10, (5, 5))
row_cumsum = np.cumsum(matrix8, axis=1)
col_cumsum = np.cumsum(matrix8, axis=0)
print("Exercise 8 - Matrix:\n", matrix8)
print("Exercise 8 - Row-wise Cumulative Sum:\n", row_cumsum)
print("Exercise 8 - Column-wise Cumulative Sum:\n", col_cumsum)

# Relevance: Cumulative sums are used in rolling aggregates, time-series analysis, and tracking cumulative metrics.

# ------------------- Exercise 9 -------------------
# Problem: Create a 1D array of 20 random numbers and find the indices
# of the three largest values.
# Expected Output:
# Array: [...]
# Indices of Top 3 Largest Values: [...]
array9 = np.random.randint(1, 100, 20)
top_3_indices = np.argsort(array9)[-3:][::-1]
# Returns the indices that would sort an array.
print("Exercise 9 - Array:", array9)
print("Exercise 9 - Indices of Top 3 Largest Values:", top_3_indices)

# Relevance: Finding top elements is key in ranking systems, leaderboard calculations, and feature importance scoring.

# ------------------- Exercise 10 -------------------
# Problem: Create a 10x10 matrix with random integers between 1 and 100.
# Replace all values divisible by 5 with -1.
# Expected Output:
# Original Matrix:
# [...]
# Updated Matrix:
# [...]
matrix10 = np.random.randint(1, 100, (10, 10))
updated_matrix10 = np.where(matrix10 % 5 == 0, -1, matrix10)
print("Exercise 10 - Original Matrix:\n", matrix10)
print("Exercise 10 - Updated Matrix:\n", updated_matrix10)

# Relevance: Value substitution is essential for handling missing data, encoding categories, and applying conditional rules.
