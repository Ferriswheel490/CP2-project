# Fairus Battle simulator program

from character import create_character
from file_handler import save_characters, load_characters
from battle import battle

def display_character(character):
    print(f"\nName: {character.name}\nHealth: {character.health}\nStrength: {character.strength}\nDefense: {character.defense}\nSpeed: {character.speed}\nLevel: {character.level}\nExperience: {character.experience}\n")

def create_character_menu(characters):
    new_char = create_character()
    characters.append(new_char)
    save_characters(characters)
    main_menu(characters)

def view_characters_menu(characters):
    for char in characters:
        display_character(char)
    main_menu(characters)

def battle_menu(characters):
    if len(characters) < 2:
        print("Not enough characters to battle.")
        return main_menu(characters)

    print("Choose two characters to battle:")
    for i, char in enumerate(characters):
        print(f"{i + 1}. {char.name}")
    
    try:
        c1 = int(input("First character: ")) - 1
        c2 = int(input("Second character: ")) - 1
        if c1 == c2 or c1 not in range(len(characters)) or c2 not in range(len(characters)):
            print("Invalid selection.")
            return battle_menu(characters)
    except ValueError:
        print("Invalid input.")
        return battle_menu(characters)

    battle(characters[c1], characters[c2])
    save_characters(characters)
    main_menu(characters)

def main_menu(characters):
    print("\n1. Create Character\n2. View Characters\n3. Battle\n4. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        create_character_menu(characters)
    elif choice == "2":
        view_characters_menu(characters)
    elif choice == "3":
        battle_menu(characters)
    elif choice == "4":
        print("Goodbye!")
        return  # Ends recursion, exiting the program
    else:
        print("Invalid choice. Try again.")
        main_menu(characters)  # Recursively call main_menu until a valid choice is made

if __name__ == "__main__":
    characters = load_characters()
    main_menu(characters)

import random
import csv

Charater_file = "character.csv"

class RPGCharacter:
    def __init__(self, name, health, strength, defense, speed, experience=0, level=1):
        self.name = name
        self.health = health
        self.strength = strength
        self.defense = defense
        self.speed = speed
        self.experience = experience
        self.level = level

    def to_dict(self):
        return{
            "name": self.name,
            "health": self.health,
            "strength": self.strength,
            "defense": self.defense,
            "speed": self.speed,
            "experience": self.experience,
            "level": self.level
        }
    
    def level_up(self):
        if self.experience >= self.level * 10:
            self.level += 1
            self.health += 5
            self.strength += 2
            self.defense += 2
            self.speed += 1
            self.experience = 0
            print(f"{self.name} leveled up to Level {self.level}!")

def save_characters(characters):
    with open(Charater_file, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["self", "name", "health", "strength", "defense", "speed", "experience", "level"])
        writer.writeheader()
        for character in characters:
            writer.writerow(character.to.dict())

def load_characters():
    character = []
    try:
        with open(Charater_file, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                character.append(RPGCharacter(row["name"], int(row["health"]), int(row["strength"]), int(row["defense"]), int(row["speed"]), int(row["experience"]), int(row["level"])))
    except FileNotFoundError:
        pass
    return character

def create_character():
    pass

def invitory_system():
    pass

def main():
    print("hello and welcome to the battle simulator")
    ans =  int(input("1. create a new character and start a new adventure\n 2. continue an adventure\n 3. exit\n your choice here: "))
    if ans == "1":
        pass
    if ans == "2":
        pass
    if ans == "3":
        pass

main()