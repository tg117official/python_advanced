import numpy as np


# ------------------- Exercise 1 -------------------
# Problem: Create a 1D NumPy array of numbers from 0 to 9.
# Expected Output: [0 1 2 3 4 5 6 7 8 9]
array1 = np.arange(10)
print("Exercise 1:", array1)

# Relevance: Frequently used to initialize sequential data for testing, indexing, or creating time-series sequences.

# ------------------- Exercise 2 -------------------
# Problem: Create a 2D NumPy array of shape (3, 3) with numbers from 1 to 9.
# Expected Output:
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]
array2 = np.arange(1, 10).reshape(3, 3)
print("Exercise 2:\n", array2)

# Relevance: 2D arrays (matrices) are essential for representing tabular data, images, or modeling relationships.

# ------------------- Exercise 3 -------------------
# Problem: Perform element-wise addition, subtraction, multiplication, and division
#          between two arrays: [1, 2, 3] and [4, 5, 6].
# Expected Output:
# Addition: [5 7 9]
# Subtraction: [-3 -3 -3]
# Multiplication: [4 10 18]
# Division: [0.25 0.4 0.5]
array3 = np.array([1, 2, 3])
array4 = np.array([4, 5, 6])
print("Exercise 3 - Addition:", array3 + array4)
print("Exercise 3 - Subtraction:", array3 - array4)
print("Exercise 3 - Multiplication:", array3 * array4)
print("Exercise 3 - Division:", array3 / array4)

# Relevance: Element-wise operations are fundamental in data preprocessing, feature scaling, and mathematical modeling.


# ------------------- Exercise 4 -------------------
# Problem: Create a 3x3 identity matrix.
# Expected Output:
# [[1. 0. 0.]
#  [0. 1. 0.]
#  [0. 0. 1.]]
identity_matrix = np.eye(3)
print("Exercise 4:\n", identity_matrix)

# - Relevance: Identity matrices are widely used in linear algebra applications like solving equations and initializing machine learning models.

# ------------------- Exercise 5 -------------------
# Problem: Find the mean, median, and standard deviation of the array [10, 20, 30, 40, 50].
# Expected Output:
# Mean: 30.0
# Median: 30.0
# Standard Deviation: 14.14 (approximately)
array5 = np.array([10, 20, 30, 40, 50])
print("Exercise 5 - Mean:", np.mean(array5))
print("Exercise 5 - Median:", np.median(array5))
print("Exercise 5 - Standard Deviation:", np.std(array5))

# Relevance: Statistical operations are crucial for exploratory data analysis (EDA) to summarize data and detect patterns.

# ------------------- Exercise 6 -------------------
# Problem: Create a 4x4 matrix with random integers between 1 and 100.
# Expected Output: A random matrix of shape (4, 4).
random_matrix = np.random.randint(1, 100, (4, 4))
print("Exercise 6:\n", random_matrix)

# Relevance: Random data generation is useful for simulating datasets and testing algorithms under various conditions.

# ------------------- Exercise 7 -------------------
# Problem: Stack two arrays [1, 2, 3] and [4, 5, 6] vertically and horizontally.
# Expected Output:
# Vertical Stack:
# [[1 2 3]
#  [4 5 6]]
# Horizontal Stack: [1 2 3 4 5 6]
array7 = np.array([1, 2, 3])
array8 = np.array([4, 5, 6])
print("Exercise 7 - Vertical Stack:\n", np.vstack((array7, array8)))
print("Exercise 7 - Horizontal Stack:\n", np.hstack((array7, array8)))

# Relevance: Array stacking is a common operation in feature engineering and merging datasets for model training.

# ------------------- Exercise 8 -------------------
# Problem: Perform matrix multiplication between two 2x2 matrices:
# Matrix A:
# [[1 2]
#  [3 4]]
# Matrix B:
# [[5 6]
#  [7 8]]
# Expected Output:
# Result:
# [[19 22]
#  [43 50]]
matrix_a = np.array([[1, 2], [3, 4]])
matrix_b = np.array([[5, 6], [7, 8]])
matrix_mul = np.dot(matrix_a, matrix_b)
print("Exercise 8:\n", matrix_mul)

# Relevance: Matrix multiplication is a core operation in graphics rendering, neural networks, and recommendation systems.

# ------------------- Exercise 9 -------------------
# Problem: Create an array of 10 elements equally spaced between 0 and 1.
# Expected Output: [0. 0.111... 0.222... ... 1.0]
linspace_array = np.linspace(0, 1, 10)
print("Exercise 9:", linspace_array)

# Relevance: Equally spaced arrays are used in numerical simulations, interpolation, and plotting functions.

# ------------------- Exercise 10 -------------------
# Problem: Replace all elements greater than 10 in the array [5, 15, 10, 20, 25] with -1.
# Expected Output: [5 -1 10 -1 -1]
array10 = np.array([5, 15, 10, 20, 25])
array10[array10 > 10] = -1
print("Exercise 10:", array10)

# Relevance: Conditional filtering and replacement are key to data cleaning, anomaly detection, and handling outliers in datasets.
