import json
import pandas as pd
from character import RPGCharacter


def save_characters(characters, filename="characters.json"):
    """
    Saves the list of RPGCharacter objects to a JSON file.
    """
    data = [char.to_dict() for char in characters]  # Convert characters to dictionaries
    with open(filename, "w") as f:
        json.dump(data, f)  # Save data as JSON


def load_characters(filename="characters.json"):
    """
    Loads RPGCharacter objects from a JSON file.
    Returns an empty list if the file does not exist or is corrupted.
    """
    try:
        with open(filename, "r") as f:
            data = json.load(f)  # Load character data from JSON
        return [RPGCharacter(**char) for char in data]  # Convert dictionaries back to RPGCharacter objects
    except (FileNotFoundError, json.JSONDecodeError):
        return []  # Return an empty list if loading fails


def get_character_stats_dataframe(characters):
    """
    Converts a list of RPGCharacter objects into a Pandas DataFrame.
    This allows for easy analysis and visualization of character statistics.
    """
    return pd.DataFrame([char.to_dict() for char in characters])
