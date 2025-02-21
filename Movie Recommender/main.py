#Fairus Movie recommender


import csv
import pandas as pd

# function to load the movies
def load_movies(csv_file):
    """Load the movie list from a CSV file."""
    return pd.read_csv(csv_file)

# function to filter the movies
def filter_movies(movies, filters):
    """Filter movies based on multiple criteria."""
    filtered = movies.copy()
    for key, value in filters.items():
        if key == 'Length':
            try:
                user_length = int(value.split()[0])
                lower_bound = user_length - 10
                upper_bound = user_length + 10
                if 'Length' in filtered.columns:
                    filtered = filtered[filtered['Length'].apply]
                else:
                    print("Length column is missing or invalid in the dataset.")
                    return pd.DataFrame()
            except ValueError:
                print("Invalid length format. Please use 'XX min' (e.g., '120 min').")
                return pd.DataFrame()
        else:
            filtered = filtered[filtered[key].str.contains(value, case=False, na=False)]
    return filtered

# The mian function to run all the code
def main():
    csv_file = "Movie Recommender\Movies list.csv"
    movies = load_movies(csv_file)
    
    print("Welcome to the Movie Recommender!")
    
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
                filters['Length'] = input("Enter length (e.g., '120 min'): ")
            if input("Filter by actor? (yes/no): ").lower() == "yes":
                filters['Actors'] = input("Enter actor: ")
            
            if len(filters) < 2:
                print("Please select at least two filters.")
                continue
            
            results = filter_movies(movies, filters)
            
            if results.empty:
                print("No movies found with the selected criteria.")
            else:
                print("\nRecommended Movies:")
                print(results[['Title', 'Genre', 'Director', 'Length', 'Actors']].to_string(index=False))
        
        elif choice == "2":
            print("\nFull Movie List (First 10 Movies):")
            print(movies.head(10).to_string(index=False))  # Only prints first 10 rows of the movie list
            
        elif choice == "3":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
