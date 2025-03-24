import random
from faker import Faker

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
        return {
            "name": self.name,
            "health": self.health,
            "strength": self.strength,
            "defense": self.defense,
            "speed": self.speed,
            "experience": self.experience,
            "level": self.level,
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

def create_character():
   return RPGCharacter()
