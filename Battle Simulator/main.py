from character import create_character
from file_handler import save_characters, load_characters, get_character_stats_dataframe
from battle import battle, visualize_character


def display_character(character):
    """
    Displays character stats and a visual representation.
    """
    print(f"\nName: {character.name}\nHealth: {character.health}\nStrength: {character.strength}\nDefense: {character.defense}\nSpeed: {character.speed}\nLevel: {character.level}\nExperience: {character.experience}\n")
    visualize_character(character)  # Visualize stats using a chart


def create_character_menu(characters):
    """
    Creates a new character, adds it to the list, saves the updated list,
    and returns to the main menu.
    """
    new_char = create_character()
    characters.append(new_char)
    save_characters(characters)  # Save character list after creation
    print(f"Character {new_char.name} created successfully!\n")
    main_menu(characters)  # Return to the main menu


def view_characters_menu(characters):
    """
    Displays all created characters along with their stats.
    Provides an overview of character data using Pandas.
    """
    if not characters:
        print("No characters have been created yet.")
        return main_menu(characters)  # Return to menu if no characters exist

    for char in characters:
        display_character(char)
    
    print("\nCharacter Data Analysis:")
    df = get_character_stats_dataframe(characters)
    print(df.describe())  # Display statistical summary of character stats
    
    main_menu(characters)  # Return to main menu


def battle_menu(characters):
    """
    Allows the user to select two characters for a battle.
    Ensures valid selection and saves the updated characters after battle.
    """
    if len(characters) < 2:
        print("Not enough characters to battle. Create at least 2 characters first.")
        return main_menu(characters)  # Redirect to menu to prevent errors

    print("Choose two characters to battle:")
    for i, char in enumerate(characters):
        print(f"{i + 1}. {char.name}")

    try:
        c1 = int(input("First character: ")) - 1
        c2 = int(input("Second character: ")) - 1
        
        # Ensure valid character selection and prevent self-battling
        if c1 == c2 or c1 not in range(len(characters)) or c2 not in range(len(characters)):
            print("Invalid selection.")
            return battle_menu(characters)
    except ValueError:
        print("Invalid input. Enter a number.")  # Handle non-numeric input
        return battle_menu(characters)

    battle(characters[c1], characters[c2])  # Initiate battle
    save_characters(characters)  # Save updated character states
    main_menu(characters)  # Return to menu after battle


def main_menu(characters):
    """
    Displays the main menu options and processes user input.
    """
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
        return  # Exit the program cleanly
    else:
        print("Invalid choice. Try again.")
        main_menu(characters)  # Restart menu on invalid input


if __name__ == "__main__":
    """
    Loads saved characters (if any) and starts the main menu.
    """
    characters = load_characters()
    main_menu(characters)
