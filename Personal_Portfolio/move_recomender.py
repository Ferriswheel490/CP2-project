import os
import pandas as pd

# Function that provides an introduction and asks if the user wants to proceed with the recommender
def show():
    print("""
hello there, you have clicked on the movie recommender!
This program will let you pick genre, actors, and more.
You can get suggestions or browse the whole movie list.
I learn this in clas and made it
I learned how bad bugs can get and how to put a list in a csv and use that csv
""")
    ans = input("\nDo you want to see it in action? (y/n): ")
    if ans.lower() in ["yes", "y"]:  # If the user wants to proceed, call movie_recommender()
        movie_recommender()
    else:
        print("Returning to portfolio...")

# Load movie data from a CSV file
def load_movies(csv_file):
    # Check if the file exists, and if not, print an error and exit
    if not os.path.exists(csv_file):
        print(f"Error: CSV file '{csv_file}' not found.")
        exit()

    # Try to load the CSV file, handling possible encoding issues
    try:
        return pd.read_csv(csv_file, encoding="utf-8")
    except UnicodeDecodeError:
        return pd.read_csv(csv_file, encoding="ISO-8859-1")

# Function that filters movies based on various criteria like genre, director, length, or actor
def filter_movies(movies, filters):
    filtered = movies.copy()  # Create a copy to avoid modifying the original DataFrame

    for key, value in filters.items():  # Loop through the filters and apply them
        if key == 'Length (min)':  # Special handling for movie length
            try:
                # Extract the numerical value for length and filter it within a range
                user_length = int(value.split()[0])
                lower, upper = user_length - 10, user_length + 10

                # Ensure the length is numeric and filter based on the length range
                filtered['Length (min)'] = pd.to_numeric(
                    filtered['Length (min)'].astype(str).str.extract(r'(\d+)')[0],
                    errors='coerce'
                )
                filtered = filtered.dropna(subset=['Length (min)'])
                filtered = filtered[filtered['Length (min)'].between(lower, upper)]
            except ValueError:
                print("Invalid length format.")
                return pd.DataFrame()  # Return an empty DataFrame if there's an issue
        else:
            if key in filtered.columns:
                filtered[key] = filtered[key].astype(str)
                filtered = filtered[filtered[key].str.contains(value, case=False, na=False)]  # Filter by the given value

    return filtered  # Return the filtered DataFrame

# Main function that runs the movie recommender logic
def movie_recommender():
    csv_file = "Movie Recommender/Movies list.csv"  # Define the path to the CSV file containing the movie list

    print("Welcome to the Movie Recommender ")

    movies = load_movies(csv_file)  # Load the movies data

    while True:
        print("\nOptions:")
        print("1. Get movie recommendations")
        print("2. View full movie list")
        print("3. Return to portfolio")

        choice = input("Enter your choice: ")  # Prompt the user to select an option

        if choice == "1":  # If the user wants recommendations
            filters = {}  # Initialize an empty dictionary to hold the filters

            # Ask the user for various filters (genre, director, length, actor)
            if input("Filter by genre? (y/n): ").lower() == "y":
                filters['Genre'] = input("Genre: ")
            if input("Filter by director? (y/n): ").lower() == "y":
                filters['Director'] = input("Director: ")
            if input("Filter by length? (y/n): ").lower() == "y":
                filters['Length (min)'] = input("Length (e.g., '120 min'): ")
            if input("Filter by actor? (y/n): ").lower() == "y":
                filters['Actors'] = input("Actor: ")

            if len(filters) < 2:  # Ensure at least two filters are selected
                print("Please select at least two filters.")
                continue

            results = filter_movies(movies, filters)  # Filter the movie list based on user input
            if results.empty:
                print("No movies found.")  # If no movies match the filters
            else:
                cols = ['Title', 'Genre', 'Director', 'Length (min)', 'Notable Actors']
                print("\nRecommended Movies:")
                # Display the recommended movies (columns available in the CSV)
                print(results[[c for c in cols if c in results.columns]].to_string(index=False))

        elif choice == "2":  # If the user wants to see the full movie list
            print("\nFull Movie List:")
            print(movies.to_string(index=False))  # Display the entire movie list

        elif choice == "3":  # If the user wants to return to the portfolio
            break  # Exit the loop and return to the portfolio
        else:
            print("Invalid input.")  # Handle invalid choices

