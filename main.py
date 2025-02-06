# Fairus De La Cruz Personal Library

# List music items
music_library = []

# add new item to library
def add_item():
    title = input("Enter the title of the music: ")
    artist = input("Enter the artist of the music: ")
    
    # library as list
    print("Item added.\n")

# show items
def display_items():
    if len(music_library) == 0:
        print("The library is empty.\n")
    else:
        for item in music_library:
            print("Title: " + item[0] + ", Artist: " + item[1])
        print()

# find the title and artist
def search_item():
    search_term = input("Enter a title, artist: ").lower()
    
    found = False
    for item in music_library:
        if search_term in item[0].lower() or search_term in item[1].lower():
            print("Found: Title: " + item[0] + ", Artist: " + item[1])
            found = True
            
    if not found:
        print("No matches found.\n")

# remove stuff from library
def remove_item():
    display_items()
    try:
        number = int(input("Enter the number of the item to remove: "))
        if number > 0 and number <= len(music_library):
            music_library.pop(number - 1)
            print("Item removed.\n")
        else:
            print("Invalid number.\n")
    except ValueError:
        print("Please enter a valid number.\n")

# run the program
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
                print("Exiting program...")
                break
            else:
                print("Invalid choice. Please try again.\n")
        except ValueError:
            print("Please enter a valid number (1-5).\n")

# Start the program
run_program()
