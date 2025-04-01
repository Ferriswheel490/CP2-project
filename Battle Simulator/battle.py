import random
import matplotlib.pyplot as plt
from character import RPGCharacter

def visualize_character(character):
    """
    Displays a bar chart of the character's stats using Matplotlib.
    """
    stats = [character.health, character.strength, character.defense, character.speed]
    labels = ["Health", "Strength", "Defense", "Speed"]
    plt.bar(labels, stats, color=['green', 'red', 'blue', 'orange'])
    plt.title(f"{character.name} Stats")
    plt.show()

def battle(player1, player2):
    """
    Simulates a turn-based battle between two RPG characters.
    """
    print(f"{player1.name} VS {player2.name} - Battle Begins!")
    turn = 0
    
    while player1.health > 0 and player2.health > 0:
        current_player = player1 if turn % 2 == 0 else player2
        opponent = player2 if current_player == player1 else player1
        tries = 0
        
        while tries < 3:
            action = input(f"{current_player.name}, choose: 1) Fight 2) Heal 3) Run: ")
            
            if action == "1":  # Attack
                damage = max(1, current_player.strength - opponent.defense + random.randint(0, 5))
                opponent.health -= damage
                print(f"{current_player.name} attacks {opponent.name} for {damage} damage!")
                break
            
            elif action == "2":  # Heal
                heal_amount = random.randint(5, 15)
                current_player.health += heal_amount
                print(f"{current_player.name} heals for {heal_amount} HP!")
                break
            
            elif action == "3":  # Run
                print(f"{current_player.name} runs away! Battle over.")
                return
            
            else:
                tries += 1
                print("Invalid choice. Try again.")
        
        if tries == 3:
            print(f"{current_player.name} failed to act. Switching turns.")
        
        turn += 1
    
    winner = player1 if player1.health > 0 else player2
    print(f"{winner.name} wins the battle!")
    
    # Grant experience and check for level up
    winner.experience += 10
    winner.level_up()
    
    # Restore health for both characters after battle
    player1.health = player1.max_health
    player2.health = player2.max_health
    print(f"{player1.name} and {player2.name} have recovered to full health!")
