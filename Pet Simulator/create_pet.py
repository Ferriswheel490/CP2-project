import csv
from datetime import datetime
from take_care_of_pet import CSV_FILE

def create_pet():
    pet_type = input("What kind of pet do you want? (Dog, Cat, Rabbit, Hamster, Goldfish, Bird, Frog): ")
    name = input(f"What would you like to name your {pet_type}? ")

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    pet = {
        "name": name,
        "type": pet_type,
        "hunger": "100",
        "happiness": "100",
        "energy": "100",
        "last_updated": now,
        "birth_date": now,
        "days_passed": "0"
    }

    with open(CSV_FILE, 'w', newline='') as file:
        fieldnames = pet.keys()
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow(pet)

    print(f"{name} the {pet_type} has been created!")
