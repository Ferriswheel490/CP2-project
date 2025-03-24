import json
import pandas as pd
from character import RPGCharacter

def save_characters(characters, filename="characters.json"):
    data = [char.to_dict() for char in characters]
    with open(filename, "w") as f:
        json.dump(data, f)

def load_characters(filename="characters.json"):
    try:
        with open(filename, "r") as f:
            data = json.load(f)
        return [RPGCharacter(**char) for char in data]
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def get_character_stats_dataframe(characters):
    return pd.DataFrame([char.to_dict() for char in characters])