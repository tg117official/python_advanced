import os

def read_file(file_path):
    if not os.path.exists(file_path):
        return []
    with open(file_path, "r") as f:
        return [line.strip().split(",") for line in f.readlines()]

def write_file(file_path, data):
    with open(file_path, "w") as f:
        for record in data:
            f.write(",".join(record) + "\n")

def append_to_file(file_path, record):
    with open(file_path, "a") as f:
        f.write(",".join(record) + "\n")
