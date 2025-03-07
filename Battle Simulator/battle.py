# the battle

# function to battle
def battle(attacker, defender):
    if attacker.health <= 0 or defender.health <= 0:
        winner = attacker if attacker.health > 0 else defender
        print(f"\n{winner.name} wins the battle!")
        winner.experience += 10
        winner.level_up()
        return  # Exit recursion

    damage = max(1, attacker.strength - defender.defense // 2)
    defender.health -= damage
    print(f"{attacker.name} attacks {defender.name} for {damage} damage! ({defender.health} HP left)")

    # Swap attacker and defender, then call battle again
    battle(defender, attacker)
