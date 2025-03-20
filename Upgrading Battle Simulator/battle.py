import random
from character import RPGCharacter

def battle(player_1, player_2):
    print(f"\n{player_1.name} vs. {player_2.name}")
    print(f"The battle begins!\n")

    # Determine turn order by speed
    players = sorted([player_1, player_2], key=lambda p: p.speed, reverse=True)

    while player_1.health > 0 and player_2.health > 0:
        for player in players:
            if player.health <= 0:
                continue  # Skip if the player is already defeated

            enemy = player_1 if player == player_2 else player_2
            print(f"\n{player.name}'s turn! ({player.health} HP)")
            print(f"{enemy.name}: {enemy.health} HP")

            invalid_attempts = 0  # Counter for invalid inputs

            while invalid_attempts < 3:
                action = input("Choose an action: (1) Attack, (2) Heal, (3) Run: ")

                if action == "1":  # Attack
                    damage = max(1, random.randint(player.strength // 2, player.strength) - enemy.defense)
                    enemy.health = max(0, enemy.health - damage)
                    print(f"{player.name} attacks {enemy.name} for {damage} damage!")
                    break  # Exit loop after valid action

                elif action == "2":  # Heal
                    heal_amount = random.randint(5, 15)
                    player.health = min(100, player.health + heal_amount)  # Assume 100 is max HP
                    print(f"{player.name} heals for {heal_amount} HP!")
                    break

                elif action == "3":  # Run (50% chance to escape)
                    if random.random() < 0.5:
                        print(f"{player.name} successfully ran away!")
                        return
                    else:
                        print(f"{player.name} failed to run away!")
                    break

                else:
                    invalid_attempts += 1
                    print(f"That's not an option! Please choose a valid action. ({invalid_attempts}/3)")

            if invalid_attempts == 3:
                print(f"{player.name} took too long! Their turn is skipped.")
            
            # Check if enemy is defeated
            if enemy.health <= 0:
                print(f"{enemy.name} has been defeated! {player.name} wins!")
                player.experience += 10  # Gain EXP
                player.level_up()
                return  # End battle


