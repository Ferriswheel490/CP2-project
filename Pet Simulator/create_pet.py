import csv
from take_care_of_pet import stuff
from hamster import care_loop as hamster_care

def save_pet(pet_type):
    with open("Pet Simulator\pet_data.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([pet_type, "100", "100", "100", "alive", "0"])  # Type, hunger, happiness, health, status, age

def create_pet():
    print("Welcome to the Pet Creator!")
    print("What kind of pet would you like to adopt?")
    print("1. Dog")
    print("2. Cat")
    print("3. Bird")
    print("4. Hamster")

    choice = input("Enter the number of your choice: ")

    if choice == "1":
        print("You've adopted a dog! It's barking excitedly!")
        save_pet("dog")
        stuff()
    elif choice == "2":
        print("You've adopted a cat! It’s already ignoring you.")
        save_pet("cat")
        stuff()
    elif choice == "3":
        print("You've adopted a bird! It chirps a little tune.")
        save_pet("bird")
        stuff()
    elif choice == "4":
        print("You've chosen to adopt a hamster!")
        save_pet("hamster")
        hamster_care()
    else:
        print("Invalid choice. Please select 1–4.")
        create_pet()  # Restart selection if input is invalid
