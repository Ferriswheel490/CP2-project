import random
from faker import Faker

class RPGCharacter:
    def __init__(self, name=None, health=None, strength=None, defense=None, speed=None, experience=0, level=1):
        self.name = name if name else fake.first_name()
        self.backstory = fake.sentence()
        self.quote = fake.sentence()
        self.max_health = health if health else random.randint(50, 100)  # Store max health
        self.health = self.max_health
        self.strength = strength if strength else random.randint(5, 15)
        self.defense = defense if defense else random.randint(5, 15)
        self.speed = speed if speed else random.randint(5, 15)
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
    fake = Faker()
    random_name = fake.name()  # Generates a random name using Faker
    
    # You can modify the stats as needed, here I'm using random values for demonstration
    health = random.randint(50, 100)
    strength = random.randint(10, 20)
    defense = random.randint(5, 15)
    speed = random.randint(5, 15)

    # Create an RPGCharacter instance with the generated name and random stats
    character = RPGCharacter(random_name, health, strength, defense, speed)
    
    print(f"Character created: {character.name}")
    return character

# Create a character
new_character = create_character()
