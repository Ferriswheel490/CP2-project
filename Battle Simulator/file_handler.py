# file handling

import csv
from character import RPGCharacter

CHARACTER_FILE = "characters.csv"

def save_characters(characters):
    with open(CHARACTER_FILE, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "health", "strength", "defense", "speed", "experience", "level"])
        writer.writeheader()
        for character in characters:
            writer.writerow(character.to_dict())

def load_characters():
    characters = []
    try:
        with open(CHARACTER_FILE, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                characters.append(RPGCharacter(
                    row["name"], int(row["health"]), int(row["strength"]), int(row["defense"]), int(row["speed"]), int(row["experience"]), int(row["level"])
                ))
    except FileNotFoundError:
        pass
    return characters