#Fairus Movie recommender


import csv
import os
import pandas as pd

# Function to load the movies
def load_movies(csv_file):
    """Load the movie list from a CSV file with error handling."""
    if not os.path.exists(csv_file):
        print(f"Error: CSV file '{csv_file}' not found.")
        exit()

    try:
        return pd.read_csv(csv_file, encoding="utf-8")
    except UnicodeDecodeError:
        print("Encoding error! Trying with a different encoding...")
        return pd.read_csv(csv_file, encoding="ISO-8859-1")
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        exit()

# Function to filter the movies
def filter_movies(movies, filters):
    """Filter movies based on multiple criteria."""
    filtered = movies.copy()

    for key, value in filters.items():
        if key == 'Length':
            try:
                user_length = int(value.split()[0])
                lower_bound, upper_bound = user_length - 10, user_length + 10

                if 'Length' in filtered.columns:
                    
                    filtered['Length'] = pd.to_numeric(filtered['Length'].astype(str).str.extract(r'(\d+)')[0], errors='coerce')
                    
                   
                    filtered = filtered.dropna(subset=['Length'])

                    
                    filtered = filtered[filtered['Length'].between(lower_bound, upper_bound)]
                else:
                    print("Error: 'Length' column missing in dataset.")
                    return pd.DataFrame()
            except ValueError:
                print("Invalid length format. Please use 'XX min'.")
                return pd.DataFrame()
        else:
            if key in filtered.columns:
                filtered[key] = filtered[key].astype(str)
                filtered = filtered[filtered[key].str.contains(value, case=False, na=False)]
            else:
                print(f"Warning: Column '{key}' not found in dataset. Skipping this filter.")
    
    return filtered


# Main function
def main():
    csv_file = "Movie Recommender/Movies list.csv"

    print("Welcome to the Movie Recommender!")

    # Load movie data
    movies = load_movies(csv_file)

    while True:
        print("\nOptions:")
        print("1. Get movie recommendations")
        print("2. Print entire movie list")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            print("\nFilter by at least two criteria:")
            filters = {}

            if input("Filter by genre? (yes/no): ").lower() == "yes":
                filters['Genre'] = input("Enter genre: ")
            if input("Filter by director? (yes/no): ").lower() == "yes":
                filters['Director'] = input("Enter director: ")
            if input("Filter by length? (yes/no): ").lower() == "yes":
                filters['Length'] = input("Enter length: ")
            if input("Filter by actor? (yes/no): ").lower() == "yes":
                filters['Actors'] = input("Enter actor: ")

            if len(filters) < 2:
                print("Please select at least two filters.")
                continue

            results = filter_movies(movies, filters)

            if results.empty:
                print("No movies found with the selected criteria.")
            else:
                columns_to_display = ['Title', 'Genre', 'Director', 'Length (min)', 'Notable Actors']
                available_columns = [col for col in columns_to_display if col in results.columns]

                print("\nRecommended Movies:")
                print(results[available_columns].to_string(index=False))

        elif choice == "2":
            print("\nFull Movie List:")
            print(movies.to_string(index=False))

        elif choice == "3":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

# Run program
if __name__ == "__main__":
    main()
