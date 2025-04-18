from hamster import hamster
from take_care_of_pet import *


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
    if pet == "Dog" or "Cat" or "Rabbit" or "Goldfish" or "Bird" or "Frog":
        name_pet()
    elif pet == "Hamster":
        hamster()
    else:
        print("that is not a pet in our list please pick one of them")
        create_pet()

def name_pet(pet):
    name = input("what you wanna name your" + pet)
