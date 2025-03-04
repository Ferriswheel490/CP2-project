# Fairus file handling

# functiion to read the file
def read_file(file_name):
    """Reads the contents of the file."""
    try:
        with open(file_name, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
        return ""

#funciton to get the word count
def get_word_count(content):
    """Returns the word count of the content."""
    words = content.split()
    return len(words)

# function to update the file
def update_file(file_name, word_count, timestamp):
    """Updates the file with word count and timestamp."""
    try:
        with open(file_name, 'a') as file:
            file.write(f"\n\nWord Count: {word_count}")
            file.write(f"\nLast Updated: {timestamp}")
        print(f"The file '{file_name}' has been updated.")
    except Exception as e:
        print(f"Error while updating the file: {e}")

# function to append to the file
def append_to_file(file_name, new_content):
    """Appends new content to the file."""
    try:
        with open(file_name, 'a') as file:
            file.write("\n" + new_content)
        print("Content has been added.")
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
    except PermissionError:
        print(f"Error: Permission denied while accessing the file '{file_name}'.")
    except Exception as e:
        print(f"Error while appending to the file: {e}")

