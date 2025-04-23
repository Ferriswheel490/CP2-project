from create_pet import create_pet
from take_care_of_pet import stuff
import os

def main():
    if not os.path.exists("pet_data.csv"):
        print("No existing pet found.")
        choice = input("Do you want to create a new pet? (y/n): ").lower()
        if choice in ("y", "yes"):
            create_pet()
        else:
            print("Come back when you're ready for a pet!")
            return
    else:
        choice = input("Do you already have a pet or want to create a new one? (have/new): ").lower()
        if choice == "new":
            create_pet()

    stuff()

if __name__ == "__main__":
    main()
