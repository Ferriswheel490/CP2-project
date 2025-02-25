# Fairus file handling

# functiion to read the file
def read_file(file_path):
    try:
        with open(file_path, "r", encoding="uft = 8") as file:
            return file.read()
        
    except FileNotFoundError:
        print("Error file not found")
        return ""

#function to count the words 
def count_words(text):
    return len(text.split())

#function to update the file
def update_file(file_path, word_count, timestamp):
    with open(file_path, "a", encoding="uft = 8") as file:
        file.write(f"\n\nWord count: {word_count}\nLast update: {timestamp}\n")
