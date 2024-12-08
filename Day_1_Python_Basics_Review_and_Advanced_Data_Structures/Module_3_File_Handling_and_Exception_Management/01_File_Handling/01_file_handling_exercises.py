############################### BASIC ##########################################

# Exercise 1: Writing to a file
# Problem: Write a program to write a list of strings to a file, each string on a new line.
# Relevance: Demonstrates basic file writing operations.
lines = ["Hello, World!", "Python is great!", "File handling in Python."]
with open("exercise1.txt", "w") as file:
    for line in lines:
        file.write(line + "\n")
print("Exercise 1: Data written to exercise1.txt")
# Output: File "exercise1.txt" will contain:
# Hello, World!
# Python is great!
# File handling in Python.


# Exercise 2: Reading from a file
# Problem: Write a program to read and print the content of a file line by line.
# Relevance: Demonstrates basic file reading operations.
with open("exercise1.txt", "r") as file:
    for line in file:
        print("Exercise 2:", line.strip())
# Output:
# Exercise 2: Hello, World!
# Exercise 2: Python is great!
# Exercise 2: File handling in Python.


# Exercise 3: Appending to a file
# Problem: Write a program to append new lines to an existing file.
# Relevance: Demonstrates appending data without overwriting existing content.
new_lines = ["Appending new data.", "Python makes it easy!"]
with open("exercise1.txt", "a") as file:
    for line in new_lines:
        file.write(line + "\n")
print("Exercise 3: Data appended to exercise1.txt")
# Output: File "exercise1.txt" will now contain the new lines appended.


# Exercise 4: Checking if a file exists
# Problem: Check if a file exists before trying to read it.
# Relevance: Prevents errors by verifying file existence.
import os
if os.path.exists("exercise1.txt"):
    print("Exercise 4: File exists")
else:
    print("Exercise 4: File does not exist")
# Output: Exercise 4: File exists


# Exercise 5: Counting lines in a file
# Problem: Write a program to count the number of lines in a file.
# Relevance: Useful for analyzing file content.
with open("exercise1.txt", "r") as file:
    line_count = sum(1 for _ in file)
print("Exercise 5: Number of lines in exercise1.txt is", line_count)
# Output: Exercise 5: Number of lines in exercise1.txt is 5


# Exercise 6: Reading specific lines from a file
# Problem: Write a program to read and print the first three lines of a file.
# Relevance: Demonstrates selective reading of file content.
with open("exercise1.txt", "r") as file:
    for i, line in enumerate(file):
        if i < 3:
            print("Exercise 6:", line.strip())
        else:
            break
# Output:
# Exercise 6: Hello, World!
# Exercise 6: Python is great!
# Exercise 6: File handling in Python.


# Exercise 7: Writing and reading binary files
# Problem: Write and read binary data to/from a file.
# Relevance: Demonstrates handling non-text data like images or serialized objects.
binary_data = b"This is binary data."
with open("exercise7.bin", "wb") as file:
    file.write(binary_data)
with open("exercise7.bin", "rb") as file:
    read_binary = file.read()
print("Exercise 7: Binary data read is", read_binary)
# Output: Exercise 7: Binary data read is b'This is binary data.'


# Exercise 8: Deleting a file
# Problem: Write a program to delete a specific file.
# Relevance: Demonstrates safe file management and cleanup.
if os.path.exists("exercise7.bin"):
    os.remove("exercise7.bin")
    print("Exercise 8: exercise7.bin deleted")
else:
    print("Exercise 8: File does not exist")
# Output: Exercise 8: exercise7.bin deleted


# Exercise 9: Copying content from one file to another
# Problem: Write a program to copy the content of one file into another.
# Relevance: Demonstrates reading from one file and writing to another.
with open("exercise1.txt", "r") as source, open("exercise9.txt", "w") as destination:
    for line in source:
        destination.write(line)
print("Exercise 9: Content copied to exercise9.txt")
# Output: File "exercise9.txt" will have the same content as "exercise1.txt".


# Exercise 10: Counting words in a file
# Problem: Write a program to count the number of words in a file.
# Relevance: Useful for analyzing text files and word frequency.
with open("exercise1.txt", "r") as file:
    word_count = sum(len(line.split()) for line in file)
print("Exercise 10: Number of words in exercise1.txt is", word_count)
# Output: Exercise 10: Number of words in exercise1.txt is 12



########################### INTERMEDIATE #########################################


# Exercise 1: Find and replace in a file
# Problem: Write a program to find a specific word in a file and replace it with another word.
# Relevance: Demonstrates advanced reading and writing operations for text processing.
find_word = "Python"
replace_word = "Java"
with open("exercise1.txt", "r") as file:
    content = file.read()
content = content.replace(find_word, replace_word)
with open("exercise1.txt", "w") as file:
    file.write(content)
print("Exercise 1: Replaced all occurrences of", find_word, "with", replace_word)
# Output: All occurrences of "Python" in "exercise1.txt" will be replaced with "Java"


# Exercise 2: Merge multiple files into one
# Problem: Write a program to merge the contents of two files into a single file.
# Relevance: Demonstrates combining data from multiple sources.
file1_content = "File 1: Hello\n"
file2_content = "File 2: World\n"
with open("file1.txt", "w") as file:
    file.write(file1_content)
with open("file2.txt", "w") as file:
    file.write(file2_content)

with open("merged_file.txt", "w") as output_file:
    for input_file in ["file1.txt", "file2.txt"]:
        with open(input_file, "r") as file:
            output_file.write(file.read())
print("Exercise 2: Merged file1.txt and file2.txt into merged_file.txt")
# Output: "merged_file.txt" will contain:
# File 1: Hello
# File 2: World


# Exercise 3: Count the frequency of words in a file
# Problem: Write a program to count the frequency of each word in a file.
# Relevance: Demonstrates reading and processing text data to extract insights.
from collections import Counter
with open("exercise1.txt", "r") as file:
    words = file.read().split()
word_counts = Counter(words)
print("Exercise 3: Word frequencies are", word_counts)
# Output: A dictionary with word frequencies, e.g., {'Java': 2, 'is': 1, 'great!': 1}


# Exercise 4: Read and write JSON data
# Problem: Write a program to read a JSON file, modify its content, and save it back.
# Relevance: Demonstrates handling structured data in JSON format.
import json
data = {"name": "Alice", "age": 25}
with open("data.json", "w") as file:
    json.dump(data, file)

with open("data.json", "r") as file:
    json_data = json.load(file)
json_data["age"] = 30
with open("data.json", "w") as file:
    json.dump(json_data, file)
print("Exercise 4: Updated JSON data to", json_data)
# Output: The file "data.json" will now contain {"name": "Alice", "age": 30}


# Exercise 5: Split a large file into smaller chunks
# Problem: Write a program to split a file into smaller files, each containing a fixed number of lines.
# Relevance: Demonstrates dividing large files for easier processing.
lines_per_chunk = 2
with open("exercise1.txt", "r") as file:
    lines = file.readlines()
for i in range(0, len(lines), lines_per_chunk):
    chunk_lines = lines[i:i + lines_per_chunk]
    with open(f"chunk_{i // lines_per_chunk + 1}.txt", "w") as chunk_file:
        chunk_file.writelines(chunk_lines)
print("Exercise 5: Split exercise1.txt into smaller chunks")
# Output: Files "chunk_1.txt", "chunk_2.txt", etc., each containing 2 lines from "exercise1.txt"
