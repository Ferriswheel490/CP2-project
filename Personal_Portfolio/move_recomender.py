import os
import pandas as pd


def show():
    print("""
hello there, you have clicked on the movie recommender!
This program will let you pick genre, actors, and more.
You can get suggestions or browse the whole movie list.
""")
    ans = input("\nDo you want to see it in action? (y/n): ")
    if ans.lower() in ["yes", "y"]:
        movie_recommender()
    else:
        print("Returning to portfolio...")

def load_movies(csv_file):
    if not os.path.exists(csv_file):
        print(f"Error: CSV file '{csv_file}' not found.")
        exit()

    try:
        return pd.read_csv(csv_file, encoding="utf-8")
    except UnicodeDecodeError:
        return pd.read_csv(csv_file, encoding="ISO-8859-1")

def filter_movies(movies, filters):
    filtered = movies.copy()

    for key, value in filters.items():
        if key == 'Length (min)':
            try:
                user_length = int(value.split()[0])
                lower, upper = user_length - 10, user_length + 10

                filtered['Length (min)'] = pd.to_numeric(
                    filtered['Length (min)'].astype(str).str.extract(r'(\d+)')[0],
                    errors='coerce'
                )
                filtered = filtered.dropna(subset=['Length (min)'])
                filtered = filtered[filtered['Length (min)'].between(lower, upper)]
            except ValueError:
                print("Invalid length format.")
                return pd.DataFrame()
        else:
            if key in filtered.columns:
                filtered[key] = filtered[key].astype(str)
                filtered = filtered[filtered[key].str.contains(value, case=False, na=False)]

    return filtered

def movie_recommender():
    csv_file = "Movie Recommender/Movies list.csv"

    print("Welcome to the Movie Recommender ")

    movies = load_movies(csv_file)

    while True:
        print("\nOptions:")
        print("1. Get movie recommendations")
        print("2. View full movie list")
        print("3. Return to portfolio")

        choice = input("Enter your choice: ")

        if choice == "1":
            filters = {}
            if input("Filter by genre? (y/n): ").lower() == "y":
                filters['Genre'] = input("Genre: ")
            if input("Filter by director? (y/n): ").lower() == "y":
                filters['Director'] = input("Director: ")
            if input("Filter by length? (y/n): ").lower() == "y":
                filters['Length (min)'] = input("Length (e.g., '120 min'): ")
            if input("Filter by actor? (y/n): ").lower() == "y":
                filters['Actors'] = input("Actor: ")

            if len(filters) < 2:
                print("Please select at least two filters.")
                continue

            results = filter_movies(movies, filters)
            if results.empty:
                print("No movies found.")
            else:
                cols = ['Title', 'Genre', 'Director', 'Length (min)', 'Notable Actors']
                print("\nRecommended Movies:")
                print(results[[c for c in cols if c in results.columns]].to_string(index=False))

        elif choice == "2":
            print("\nFull Movie List:")
            print(movies.to_string(index=False))

        elif choice == "3":
            break
        else:
            print("Invalid input.")
