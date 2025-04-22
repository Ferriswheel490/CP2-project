from hamster import hamster
from take_care_of_pet import stuff


def create_pet():
    print("great you wanna make a pet but first what kinda of pet do you want")
    print("""
the list of pets:
        - Dog

        - Cat

        - Rabbit

        - Hamster

        - Goldfish

        - Bird

        - Frog


""")
    pet = input("which one do you want: ")
    if pet in ["Dog", "Cat", "Rabbit", "Goldfish", "Bird", "Frog"]:
        name_pet(pet)
    elif pet == "Hamster":
        hamster()
    else:
        print("That is not a pet in our list. Please pick one of them.")
        create_pet()


def name_pet(pet):
    name = input("What do you want to name your " + pet + "? ")
    stuff()

