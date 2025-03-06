# Fairus Battle simulator program

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
                characters.append(RPGCharacter(row["name"], int(row["health"]), int(row["strength"]), int(row["defense"]), int(row["speed"]), int(row["experience"]), int(row["level"])))
    except FileNotFoundError:
        pass
    return characters

def create_character():
    pass