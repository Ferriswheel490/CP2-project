import csv
from datetime import datetime
import random

CSV_FILE = "Pet Simulator\pet_data.csv"

def load_pet():
    try:
        with open(CSV_FILE, newline='') as file:
            reader = csv.DictReader(file)
            # Check if the file is empty
            pet = next(reader, None)
            if pet is None:
                print("No pet data found in the file. Starting a new pet.")
                return None
            return pet
    except FileNotFoundError:
        print("Pet data file not found. Creating a new pet.")
        return None


def save_pet(pet):
    with open(CSV_FILE, 'w', newline='') as file:
        fieldnames = ['name', 'type', 'hunger', 'happiness', 'energy', 'last_updated', 'birth_date']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow(pet)

def apply_stat_decay(pet):
    last = datetime.strptime(pet['last_updated'], "%Y-%m-%d %H:%M:%S")
    now = datetime.now()
    elapsed_minutes = int((now - last).total_seconds() / 60)

    if elapsed_minutes > 0:
        pet['hunger'] = max(0, int(pet['hunger']) - elapsed_minutes // 2)
        pet['energy'] = max(0, int(pet['energy']) - elapsed_minutes // 3)
        pet['happiness'] = max(0, int(pet['happiness']) - elapsed_minutes // 4)
        pet['last_updated'] = now.strftime("%Y-%m-%d %H:%M:%S")
        print(f"{elapsed_minutes} minute(s) passed. Stats slightly decreased.")

    return pet

def random_event(pet):
    events = [
        ("Your pet found a toy!", 'happiness', +10),
        ("Your pet got scared!", 'happiness', -5),
        ("Your pet took a nap.", 'energy', +10),
        ("Your pet is a bit more hungry.", 'hunger', -5),
    ]

    if random.random() < 0.3:
        event = random.choice(events)
        print(f"🎉 Random Event: {event[0]}")
        stat = event[1]
        pet[stat] = max(0, min(100, int(pet[stat]) + event[2]))

    return pet

def calculate_age(birth_date_str):
    birth = datetime.strptime(birth_date_str, "%Y-%m-%d %H:%M:%S")
    now = datetime.now()
    return (now - birth).days

def get_milestone(age):
    if age < 3:
        return "Baby"
    elif age < 7:
        return "Child"
    elif age < 15:
        return "Teen"
    else:
        return "Adult"

def stuff():
    pet = load_pet()

    # If no pet data was loaded, start fresh
    if pet is None:
        pet = {
            'name': input("What is your pet's name? "),
            'type': input("What type of pet is it? "),
            'hunger': 100,
            'happiness': 100,
            'energy': 100,
            'last_updated': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'birth_date': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        print(f"Creating a new pet: {pet['name']} the {pet['type']}.")

    pet = apply_stat_decay(pet)
    pet = random_event(pet)

    while True:
        age = calculate_age(pet['birth_date'])
        stage = get_milestone(age)

        print(f"\n🐾 {pet['name']} the {pet['type']} - Age: {age} day(s) | Stage: {stage}")
        print(f"  Hunger: {pet['hunger']} | Happiness: {pet['happiness']} | Energy: {pet['energy']}")
        choice = input("""
What would you like to do?
  1. Feed pet
  2. Play with pet
  3. Put pet to sleep
  4. Check up on pet
  5. Advance to next day
  6. Exit

Choose: """)

        if choice == "1":
            pet['hunger'] = min(100, int(pet['hunger']) + 15)
            print(f"You fed {pet['name']}!")
        elif choice == "2":
            pet['happiness'] = min(100, int(pet['happiness']) + 10)
            pet['energy'] = max(0, int(pet['energy']) - 5)
            print(f"You played with {pet['name']}!")
        elif choice == "3":
            pet['energy'] = min(100, int(pet['energy']) + 20)
            print(f"{pet['name']} is well rested!")
        elif choice == "4":
            print(f"\nStats for {pet['name']}:")
            print(f"  Hunger: {pet['hunger']}")
            print(f"  Happiness: {pet['happiness']}")
            print(f"  Energy: {pet['energy']}")
            print(f"  Age: {age} day(s) | Stage: {stage}")
        elif choice == "5":
            pet['hunger'] = max(0, int(pet['hunger']) - 10)
            pet['happiness'] = max(0, int(pet['happiness']) - 5)
            pet['energy'] = max(0, int(pet['energy']) - 7)
            pet['last_updated'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print("A new day begins...")
        elif choice == "6":
            print("See you next time!")
            break
        else:
            print("Invalid choice.")

        save_pet(pet)
        if int(pet['hunger']) <= 0 or int(pet['happiness']) <= 0 or int(pet['energy']) <= 0:
            print(f"💀 {pet['name']} has passed away. Game over.")
            break