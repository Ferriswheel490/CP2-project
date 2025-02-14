#Fairus Movie recommender


#name = open("Movie Recommender/Movies list.csv", "rt")
#print(name.read())

def main():
    print("Hello there user I am the movie recommender.")
    print("here are your options")
    recommendations = input("what kind of genre, directors, actors, or length do you like: ")
    print_all = input("the whole list: ")
    length = int(input("how long do you want the movie to be: "))
    actors =  input("what actors do you want: ")
    directors = input("what directors do you like: ")