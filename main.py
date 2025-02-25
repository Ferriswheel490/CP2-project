# Fairus main code here

import file_handling
import time_handling

# The main function to run the code
def main():
    file_path = input("Enter filename to update: ")

    content = file_handling.read_file(file_path)
    word_count = file_handling.count_words(content)
    timestamp = file_handling.get_current_timestamp()

    file_handling.update_file(file_path, word_count, timestamp)
    print(f"Updated {file_path} with word count: {word_count} and timestamp: {timestamp}")
if __name__ == "__name__":
    main()
