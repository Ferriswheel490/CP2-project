from character import create_character
from file_handler import save_characters, load_characters, get_character_stats_dataframe
from battle import battle, visualize_character

def display_character(character):
    print(f"\nName: {character.name}\nHealth: {character.health}\nStrength: {character.strength}\nDefense: {character.defense}\nSpeed: {character.speed}\nLevel: {character.level}\nExperience: {character.experience}\n")
    visualize_character(character)


def create_character_menu(characters):
    new_char = create_character()
    characters.append(new_char)
    save_characters(characters)  # Save after creation
    print(f"Character {new_char.name} created successfully!\n")
    main_menu(characters)  # Return to menu


def view_characters_menu(characters):
    if not characters:
        print("No characters have been created yet.")
        return main_menu(characters)  # Return to the menu instead of breaking

    for char in characters:
        display_character(char)
    
    print("\nCharacter Data Analysis:")
    df = get_character_stats_dataframe(characters)
    print(df.describe())
    
    main_menu(characters)  # Return to menu after displaying characters

    

def battle_menu(characters):
    if len(characters) < 2:
        print("Not enough characters to battle. Create at least 2 characters first.")
        return main_menu(characters)  # Return to menu instead of breaking

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
    main_menu(characters)  # Return to menu after battle

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
        return
    else:
        print("Invalid choice. Try again.")
        main_menu(characters)

if __name__ == "__main__":
    characters = load_characters()
    main_menu(characters)
