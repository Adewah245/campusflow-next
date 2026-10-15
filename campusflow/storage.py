# campusflow/storage.py
import json
import os

DATA_FILE = "data/tickets.json"

def save_tickets(tickets: list) -> None:
    """
    Saves the current list of tickets to a JSON file on disk.
    """
    # Ensure the 'data' directory exists before saving
    os.makedirs("data", exist_ok=True)
    
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        # json.dump converts our Python list of dictionaries into text and writes it
        json.dump(tickets, file, indent=4)


def load_tickets() -> list:
    """
    Loads tickets from the JSON file on startup. 
    Returns an empty list if no file exists yet.
    """
    # If the file doesn't exist yet, start with a fresh empty list
    if not os.path.exists(DATA_FILE):
        return []
        
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            # json.load reads the file text and converts it back into Python lists/dictionaries
            return json.load(file)
    except json.JSONDecodeError:
        print("⚠️ Warning: The tickets.json file is corrupted. Starting with an empty ticket list.")
        return []