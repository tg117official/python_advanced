import numpy as np

dice_rolls = np.random.randint(1, 7, 1000)
face_counts = np.bincount(dice_rolls, minlength=7)[1:]  # Skip index 0
probabilities = face_counts / np.sum(face_counts)
print("Exercise 5 - Rolls:", dice_rolls[:20], "...")  # Showing first 20 rolls for brevity
print("Exercise 5 - Probabilities:", probabilities)