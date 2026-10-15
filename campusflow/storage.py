# campusflow/storage.py

import json
import os

def save_tickets(filepath: str, tickets: list) -> None:
    """
    Saves a list of ticket dictionaries into a JSON file on disk.
    We use indent=4 so the file is human-readable.
    """
    try:
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(tickets, f, indent=4)
    except IOError as e:
        print(f"Warning: Could not save tickets to {filepath}. Error: {e}")


def load_tickets(filepath: str) -> list:
    """
    Loads tickets from a JSON file on disk.
    Edge case protection: If the file doesn't exist or is empty, 
    we return an empty list [] instead of crashing the program.
    """
    if not os.path.exists(filepath):
        return []

    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read().strip()
            if not content:
                return []
            return json.loads(content)
    except (json.JSONDecodeError, IOError) as e:
        print(f"Warning: Could not read tickets from {filepath}. Error: {e}")
        return []