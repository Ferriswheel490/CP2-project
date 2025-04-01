import random
from faker import Faker

fake = Faker()  # Create an instance of Faker to generate random data


class RPGCharacter:
    """
    Represents an RPG character with randomly generated or user-defined attributes.
    """
    def __init__(self, name=None, health=None, strength=None, defense=None, speed=None, experience=0, level=1):
        """
        Initializes an RPG character with default or randomized attributes.
        """
        self.name = name if name else fake.first_name()  # Generate a random name if not provided
        self.backstory = fake.sentence()  # Generate a random backstory
        self.quote = fake.sentence()  # Generate a random quote
        self.max_health = health if health else random.randint(50, 100)  # Store max health
        self.health = self.max_health  # Set current health to max
        self.strength = strength if strength else random.randint(5, 15)  # Random strength
        self.defense = defense if defense else random.randint(5, 15)  # Random defense
        self.speed = speed if speed else random.randint(5, 15)  # Random speed
        self.experience = experience  # Initial experience
        self.level = level  # Initial level

    def to_dict(self):
        """
        Converts the RPGCharacter object into a dictionary for saving/loading purposes.
        """
        return {
            "name": self.name,
            "health": self.health,
            "strength": self.strength,
            "defense": self.defense,
            "speed": self.speed,
            "experience": self.experience,
            "level": self.level
        }

    def level_up(self):
        """
        Levels up the character when they reach the required experience threshold.
        Increases attributes upon leveling up.
        """
        if self.experience >= self.level * 10:
            self.level += 1
            self.health += 5
            self.strength += 2
            self.defense += 2
            self.speed += 1
            self.experience = 0  # Reset experience after leveling up
            print(f"{self.name} leveled up to Level {self.level}!")


def create_character():
    """
    Creates a new RPGCharacter with randomized attributes.
    """
    return RPGCharacter()