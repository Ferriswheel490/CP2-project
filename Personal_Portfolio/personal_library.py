# Fairus De La Cruz Personal Library with dictionaries

# This function is responsible for displaying the intro to the personal library program and asking if the user wants to use it
def music():
    print("""
this is the personal library program
here you can
- put the title of the song
- put the artist of said song
- put in the genre
- and release year
I learned this in class
I learned how to sace things when the user puts stuff in
""")
    # Ask the user if they want to use the program and store their answer in 'ans'
    ans = input("do you wanna use it (y/n): ")
    
    # If the user wants to use it, call run_program to start the library features
    if ans in ("yes", "y"):
        run_program()
    # If the user doesn't want to use it, exit the function
    elif ans in ("no", "n"):
        return
    # If the user enters an invalid option, print a message and return to the portfolio
    else:
        print("Not a valid option. Returning to portfolio.")

# List to store music items (each item is a dictionary with title, artist, genre, and year)
music_library = []

# Function to add a new item (song) to the library
def add_item():
    # Prompt user for music details and store in variables
    title = input("Enter the title of the music: ")
    artist = input("Enter the artist of the music: ")
    genre = input("Enter the genre of the music: ")
    year = input("Enter the release year: ")
    
    # Add the music details to the music_library list as a dictionary
    music_library.append({
        "title": title,
        "artist": artist,
        "genre": genre,
        "year": year
    })
    
    # Print a confirmation message
    print("Item added.\n")

# Function to display all items in the music library
def display_items():
    # If the library is empty, print a message
    if not music_library:
        print("The library is empty.\n")
    else:
        # Loop through all items and display them
        for index, item in enumerate(music_library, start=1):
            print(f"{index}. Title: {item['title']}, Artist: {item['artist']}, Genre: {item['genre']}, Year: {item['year']}")
        print()

# Function to search for an item by title, artist, or genre
def search_item():
    # Ask the user to input a search term (case-insensitive)
    search_term = input("Enter a title, artist, or genre: ").lower()
    
    # Initialize a flag to check if a match is found
    found = False
    # Loop through each item in the library to check if the search term matches any of the details
    for item in music_library:
        if (search_term in item["title"].lower() or 
            search_term in item["artist"].lower() or
            search_term in item["genre"].lower()):
            # If a match is found, print the item details and set the found flag to True
            print(f"Found: Title: {item['title']}, Artist: {item['artist']}, Genre: {item['genre']}, Year: {item['year']}")
            found = True
            
    # If no matches were found, print a message
    if not found:
        print("No matches found.\n")

# Function to remove an item from the library
def remove_item():
    # Display all items in the library
    display_items()
    try:
        # Ask the user to enter the number of the item they want to remove
        number = int(input("Enter the number of the item to remove: "))
        # Check if the entered number is valid
        if 1 <= number <= len(music_library):
            # Remove the item from the list and print the details of the removed item
            removed_item = music_library.pop(number - 1)
            print(f"Removed: {removed_item['title']} by {removed_item['artist']}\n")
        else:
            # If the number is not valid, print an error message
            print("Invalid number.\n")
    except ValueError:
        # If the input is not a number, print an error message
        print("Please enter a valid number.\n")

# Main function to run the program
def run_program():
    while True:
        # Display the menu of options
        print("Music Library Menu:")
        print("1. Add a new item")
        print("2. Display all items")
        print("3. Search for an item")
        print("4. Remove an item")
        print("5. Exit")
        
        try:
            # Ask the user to choose an option from the menu
            choice = int(input("Enter your choice (1-5): "))
            
            # Call the appropriate function based on the user's choice
            if choice == 1:
                add_item()
            elif choice == 2:
                display_items()
            elif choice == 3:
                search_item()
            elif choice == 4:
                remove_item()
            elif choice == 5:
                break  # Exit the loop and stop the program
            else:
                print("Invalid choice. Please try again.\n")
        except ValueError:
            # If the user doesn't enter a valid number, print an error message
            print("Please enter a valid number (1-5).\n")
