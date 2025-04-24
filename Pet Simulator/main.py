from create_pet import create_pet
from take_care_of_pet import stuff
import os

CSV_FILE = "pet_data.csv"

def main():
    print("""
Welcome to the Pet Simulator!
You can create a new pet or take care of your existing one.
""")
    if os.path.exists(CSV_FILE):
        print(f"Found existing pet data in {CSV_FILE}.")
        choice = input("Do you already have a pet? (y/n): ").strip().lower()
        if choice in ['y', 'yes']:
            print("Taking care of your existing pet...")
            stuff()
        elif choice in ['n', 'no']:
            print("Creating a new pet...")
            create_pet()
            stuff()
        else:
            print("Invalid input. Please enter 'y' or 'n'.")
    else:
        print("No pet found. Let's create one!")
        create_pet()
        stuff()

if __name__ == "__main__":
    main()