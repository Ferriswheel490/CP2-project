import random
from character import RPGCharacter

def battle(player_1, player_2):
    print(f"\n {player_1.name} vs. {player_2.name} ⚔️")
    print(f"Battle starts! Good luck!\n")

    # Determine turn order based on speed
    players = sorted([player_1, player_2], key=lambda p: p.speed, reverse=True)

    while player_1.health > 0 and player_2.health > 0:
        for player in players:
            if player.health <= 0:
                continue  # Skip dead players

            enemy = player_1 if player == player_2 else player_2
            print(f"\n{player.name}'s turn! ({player.health} HP)")
            print(f"{enemy.name}: {enemy.health} HP")

            action = input("Choose an action: (1) Attack, (2) Heal, (3) Run: ")

            if action == "1":  # Attack
                damage = max(1, random.randint(player.strength // 2, player.strength) - enemy.defense)
                enemy.health = max(0, enemy.health - damage)
                print(f"{player.name} attacks {enemy.name} for {damage} damage!")

            elif action == "2":  # Heal
                heal_amount = player.health // 4
                player.health = min(100, player.health + heal_amount)  # Assume 100 is max HP
                print(f"{player.name} heals for {heal_amount} HP!")

            elif action == "3":  # Run (50% success)
                if random.random() < 0.5:
                    print(f"{player.name} successfully ran away!")
                    return
                else:
                    print(f"{player.name} failed to run away!")

            # Check if enemy is defeated
            if enemy.health <= 0:
                print(f"{enemy.name} has been defeated! {player.name} wins!")
                player.experience += 10  # Gain EXP
                player.level_up()
                return

    print("The battle has ended.")
