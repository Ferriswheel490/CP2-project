#Fairus Movie recommender


import csv

class Movie:
    # function for titles, genre, directors, length, and actors
    def __init__(self, title, genre, director, length, actors):
        self.title = title
        self.genre = genre
        self.director = director
        self.length = length
        self.actors = actors

    def __str__(self):
        return f"{self.title} ({self.genre}) - Directed by {self.director}, {self.length} mins, starring {', '.join(self.actors)}"

# Function to load movies from a CSV file
def load_movies(filename):
    movies = []
    with open(filename, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            title = row['title']
            genre = row['genre']
            director = row['director']
            length = int(row['length'])
            actors = row['actors'].split(', ')
            movies.append(Movie(title, genre, director, length, actors))
    return movies

# Function to filter the movies based on genre and the other things
def filter_movies(movies, filters):
    filtered_movies = movies

    for filter_key, filter_value in filters.items():
        if filter_key == 'genre':
            filtered_movies = [movie for movie in filtered_movies if movie.genre.lower() == filter_value.lower()]
        elif filter_key == 'director':
            filtered_movies = [movie for movie in filtered_movies if movie.director.lower() == filter_value.lower()]
        elif filter_key == 'length':
            min_length, max_length = filter_value
            filtered_movies = [movie for movie in filtered_movies if min_length <= movie.length <= max_length]
        elif filter_key == 'actor':
            filtered_movies = [movie for movie in filtered_movies if any(actor.lower() == filter_value.lower() for actor in movie.actors)]

    return filtered_movies

# Main function to run the whole code
def main():
    print("Welcome to the Movie Recommendation Program!\n")
    
    movies = load_movies('Movie Recommender/Movies list.csv')

    while True:
        print("\nPlease choose at least 2 filters from the following options:")
        print("1. Genre")
        print("2. Director")
        print("3. Length (in minutes)")
        print("4. Actor")
        print("5. Print all movies")
        print("6. Exit")

        selected_filters = {}

        while len(selected_filters) < 2:
            choice = input("\nEnter your choice (or '6' to exit): ")

            if choice == '6':
                print("Exiting program.")
                break

            if choice == '1':
                genre = input("Enter genre: ")
                selected_filters['genre'] = genre
            elif choice == '2':
                director = input("Enter director: ")
                selected_filters['director'] = director
            elif choice == '3':
                min_length = int(input("Enter minimum length: "))
                max_length = int(input("Enter maximum length: "))
                selected_filters['length'] = (min_length, max_length)
            elif choice == '4':
                actor = input("Enter actor name: ")
                selected_filters['actor'] = actor
            elif choice == '5':
                print("\nAll Movies:")
                if len(movies) == 0:
                    print("No movies available.")
                else:
                    for movie in movies:
                        print(movie)
                continue 
            else:
                print("Invalid choice. Please try again.")

            if len(selected_filters) < 2:
                print("You must select at least 2 filters to proceed.")

        if choice == '6':
            break

        recommended_movies = filter_movies(movies, selected_filters)

        if recommended_movies:
            print("\nRecommended Movies:")
            for movie in recommended_movies:
                print(movie)
        else:
            print("\nNo movies match your filters.")

if __name__ == "__main__":
    main()
