import csv
from datetime import datetime, timedelta
import random

CSV_FILE = "pet_data.csv"

def load_pet():
    with open(CSV_FILE, newline='') as file:
        reader = csv.DictReader(file)
        return next(reader)

def save_pet(pet):
    with open(CSV_FILE, 'w', newline='') as file:
        fieldnames = pet.keys()
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow(pet)

def apply_stat_decay(pet, days=0):
    last = datetime.strptime(pet['last_updated'], "%Y-%m-%d %H:%M:%S")
    now = datetime.now() if days == 0 else last + timedelta(days=days)

    elapsed_minutes = int((now - last).total_seconds() / 60)
    if elapsed_minutes > 0:
        pet['hunger'] = str(max(100, int(pet['hunger']) - elapsed_minutes))
        pet['energy'] = str(max(100, int(pet['energy']) - elapsed_minutes // 2))
        pet['happiness'] = str(max(100, int(pet['happiness']) - elapsed_minutes // 3))
        pet['last_updated'] = now.strftime("%Y-%m-%d %H:%M:%S")

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
        print("🎉 Random event: " + event[0])
        stat = event[1]
        pet[stat] = str(min(100, max(0, int(pet[stat]) + event[2])))

    return pet

def calculate_age(birth_date_str, days_passed):
    birth = datetime.strptime(birth_date_str, "%Y-%m-%d %H:%M:%S")
    age_days = (datetime.now() - birth).days + int(days_passed)
    return age_days

def age_milestone(age):
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
    pet = apply_stat_decay(pet)
    pet = random_event(pet)

    while True:
        age = calculate_age(pet['birth_date'], pet.get('days_passed', "0"))
        stage = age_milestone(age)

        print(f"\n🐾 {pet['name']} the {pet['type']} - Age: {age} day(s) | Stage: {stage}")
        print(f"  Hunger: {pet['hunger']} | Happiness: {pet['happiness']} | Energy: {pet['energy']}")
        choice = input("""\nWhat will you do?
  1. Feed pet
  2. Play with pet
  3. Put pet to sleep
  4. Check up on pet
  5. Make some money
  6. Next day
  7. Exit

Choose: """)

        if choice == "1":
            pet['hunger'] = str(min(100, int(pet['hunger']) + 15))
            print(f"You fed {pet['name']}!")
        elif choice == "2":
            pet['happiness'] = str(min(100, int(pet['happiness']) + 10))
            pet['energy'] = str(max(0, int(pet['energy']) - 5))
            print(f"You played with {pet['name']}!")
        elif choice == "3":
            pet['energy'] = str(min(100, int(pet['energy']) + 20))
            print(f"{pet['name']} had a nice nap.")
        elif choice == "4":
            print(f"\n📋 {pet['name']}'s stats:")
            print(f"  Hunger: {pet['hunger']}, Happiness: {pet['happiness']}, Energy: {pet['energy']}, Age: {age} day(s) | Stage: {stage}")
        elif choice == "5":
            print("You earned $10! (currency system coming soon)")
        elif choice == "6":
            pet['days_passed'] = str(int(pet.get('days_passed', "0")) + 1)
            pet = apply_stat_decay(pet, days=1)
            pet = random_event(pet)
            print("🌅 A new day has begun!")
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

        pet['last_updated'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        save_pet(pet)
