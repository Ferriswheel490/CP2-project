# Fairus De La Cruz Personal Library with dictionaries


def music():
    print("""
this is the personal library program
here you can
- put the title of the song
- put the artist of said song
- put in the genre
- and release year
""")
    ans = input("do you wanna use it (y/n): ")
    if ans in ("yes", "y"):
        run_program()
    elif ans in ("no", "n"):
        return
    else:
        print("Not a valid option. Returning to portfolio.")



# List to store music items (each item is a dictionary)
music_library = []

# Add a new item to the library
def add_item():
    title = input("Enter the title of the music: ")
    artist = input("Enter the artist of the music: ")
    genre = input("Enter the genre of the music: ")
    year = input("Enter the release year: ")
    
    music_library.append({
        "title": title,
        "artist": artist,
        "genre": genre,
        "year": year
    })
    
    print("Item added.\n")

# Display all items
def display_items():
    if not music_library:
        print("The library is empty.\n")
    else:
        for index, item in enumerate(music_library, start=1):
            print(f"{index}. Title: {item['title']}, Artist: {item['artist']}, Genre: {item['genre']}, Year: {item['year']}")
        print()

# Search for a title or artist
def search_item():
    search_term = input("Enter a title, artist, or genre: ").lower()
    
    found = False
    for item in music_library:
        if (search_term in item["title"].lower() or 
            search_term in item["artist"].lower() or
            search_term in item["genre"].lower()):
            print(f"Found: Title: {item['title']}, Artist: {item['artist']}, Genre: {item['genre']}, Year: {item['year']}")
            found = True
            
    if not found:
        print("No matches found.\n")

# Remove an item
def remove_item():
    display_items()
    try:
        number = int(input("Enter the number of the item to remove: "))
        if 1 <= number <= len(music_library):
            removed_item = music_library.pop(number - 1)
            print(f"Removed: {removed_item['title']} by {removed_item['artist']}\n")
        else:
            print("Invalid number.\n")
    except ValueError:
        print("Please enter a valid number.\n")

# Run the program
def run_program():
    while True:
        print("Music Library Menu:")
        print("1. Add a new item")
        print("2. Display all items")
        print("3. Search for an item")
        print("4. Remove an item")
        print("5. Exit")
        
        try:
            choice = int(input("Enter your choice (1-5): "))
            
            if choice == 1:
                add_item()
            elif choice == 2:
                display_items()
            elif choice == 3:
                search_item()
            elif choice == 4:
                remove_item()
            elif choice == 5:
                break
            else:
                print("Invalid choice. Please try again.\n")
        except ValueError:
            print("Please enter a valid number (1-5).\n")

# Start the program
run_program()
