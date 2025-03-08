import pygame
import random
import csv

# Initialize Pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("RPG Character Manager")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (100, 149, 237)

# Font
font = pygame.font.Font(None, 36)

# Character class
class RPGCharacter:
    def __init__(self, name, health, strength, defense, speed, experience=0, level=1):
        self.name = name
        self.health = health
        self.strength = strength
        self.defense = defense
        self.speed = speed
        self.experience = experience
        self.level = level

    def level_up(self):
        if self.experience >= self.level * 10:
            self.level += 1
            self.health += 5
            self.strength += 2
            self.defense += 2
            self.speed += 1
            self.experience = 0

# Load and save functions
CHARACTER_FILE = "characters.csv"

def save_characters(characters):
    with open(CHARACTER_FILE, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["name", "health", "strength", "defense", "speed", "experience", "level"])
        for char in characters:
            writer.writerow([char.name, char.health, char.strength, char.defense, char.speed, char.experience, char.level])

def load_characters():
    characters = []
    try:
        with open(CHARACTER_FILE, "r") as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            for row in reader:
                characters.append(RPGCharacter(row[0], int(row[1]), int(row[2]), int(row[3]), int(row[4]), int(row[5]), int(row[6])))
    except FileNotFoundError:
        pass
    return characters

characters = load_characters()

# Button class
class Button:
    def __init__(self, text, x, y, width, height, action):
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)
        self.action = action

    def draw(self):
        pygame.draw.rect(screen, BLUE, self.rect)
        label = font.render(self.text, True, WHITE)
        screen.blit(label, (self.rect.x + 10, self.rect.y + 10))

    def check_click(self, pos):
        if self.rect.collidepoint(pos):
            self.action()

# Screens
current_screen = "main"

def switch_screen(screen_name):
    global current_screen
    current_screen = screen_name

def create_character():
    name = f"Hero{len(characters) + 1}"
    new_char = RPGCharacter(name, random.randint(50, 100), random.randint(5, 15), random.randint(5, 15), random.randint(5, 15))
    characters.append(new_char)
    save_characters(characters)

def view_characters():
    switch_screen("view")

def main_menu():
    switch_screen("main")

def quit_game():
    pygame.quit()
    exit()

# Buttons
buttons_main = [
    Button("Create Character", 200, 100, 200, 50, create_character),
    Button("View Characters", 200, 170, 200, 50, view_characters),
    Button("Exit", 200, 240, 200, 50, quit_game)
]

button_back = Button("Back", 250, 320, 100, 50, main_menu)

# Main loop
running = True
while running:
    screen.fill(WHITE)
    
    if current_screen == "main":
        for button in buttons_main:
            button.draw()
    elif current_screen == "view":
        y_offset = 50
        for char in characters:
            text = font.render(f"{char.name} - HP: {char.health}, STR: {char.strength}", True, BLACK)
            screen.blit(text, (50, y_offset))
            y_offset += 30
        button_back.draw()
    
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if current_screen == "main":
                for button in buttons_main:
                    button.check_click(event.pos)
            elif current_screen == "view":
                button_back.check_click(event.pos)

pygame.quit()
