import csv
from datetime import datetime
import random

CSV_FILE = "Pet Simulator\pet_data.csv"

def load_pet():
    try:
        with open(CSV_FILE, newline='') as file:
            reader = csv.DictReader(file)
            pet = next(reader)  # This will raise StopIteration if there's no pet
        return pet
    except StopIteration:
        print("No pets found in the CSV. Please create a pet first.")
        exit()  # or return None and handle it later


def save_pet(pet):
    with open(CSV_FILE, 'w', newline='') as file:
        fieldnames = ['name', 'type', 'hunger', 'happiness', 'energy', 'last_updated']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow(pet)

def apply_stat_decay(pet):
    last = datetime.strptime(pet['last_updated'], "%Y-%m-%d %H:%M:%S")
    now = datetime.now()
    elapsed_minutes = int((now - last).total_seconds() / 60)

    if elapsed_minutes > 0:
        pet['hunger'] = max(0, int(pet['hunger']) - elapsed_minutes)
        pet['energy'] = max(0, int(pet['energy']) - elapsed_minutes // 2)
        pet['happiness'] = max(0, int(pet['happiness']) - elapsed_minutes // 3)
        pet['last_updated'] = now.strftime("%Y-%m-%d %H:%M:%S")
        print(f"{elapsed_minutes} minute(s) passed. Stats have changed.")

    return pet

def random_event(pet):
    events = [
        ("Your pet found a toy and is happier!", 'happiness', +10),
        ("Your pet got scared by a loud noise!", 'happiness', -5),
        ("Your pet took a surprise nap.", 'energy', +10),
        ("Your pet tried to eat your homework...", 'hunger', +5),
    ]

    if random.random() < 0.25:
        event = random.choice(events)
        print("Random event: " + event[0])
        pet[event[1]] = min(100, max(0, int(pet[event[1]]) + event[2]))

    return pet

def stuff():
    pet = load_pet()
    pet = apply_stat_decay(pet)
    pet = random_event(pet)

    while True:
        print(f"\n{pet['name']} the {pet['type']} - Hunger: {pet['hunger']}, Happiness: {pet['happiness']}, Energy: {pet['energy']}")
        choice = input("""
What will you do now:
  1. Feed pet
  2. Play with pet
  3. Put pet to sleep
  4. Check up on pet
  5. Make some money
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
            print(f"{pet['name']} had a nice nap.")
        elif choice == "4":
            print(f"\n{pet['name']}'s current stats:")
            print(f"Hunger: {pet['hunger']}, Happiness: {pet['happiness']}, Energy: {pet['energy']}")
        elif choice == "5":
            print("You did some chores and earned $10 (not implemented yet)")
        elif choice == "6":
            print("See you later!")
            break
        else:
            print("Invalid choice.")

        # Update timestamp and save pet after every action
        pet['last_updated'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        save_pet(pet)
