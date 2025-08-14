# file_io.py

def write_file(file_path, content):
    """Write content to a file at the given path with .txt extension"""
    file_name = f"{file_path}.txt"
    with open(file_name, 'w') as file:
        file.write(content)

def append_file(file_path, content):
    """Append content to a file at the given path with .txt extension"""
    file_name = f"{file_path}.txt"
    with open(file_name, 'a') as file:
        file.write(content)

def read_file(file_path):
    """Read content from a file at the given path with .txt extension"""
    file_name = f"{file_path}.txt"
    with open(file_name, 'r') as file:
        return file.read()