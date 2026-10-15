"""
storage.py - Engineer A's safe persistence module.
Handles saving tickets to JSON and loading them with strict validation,
corruption checking, and duplicate ID rejection.
"""

import json
import os
from campusflow.validation import (
    validate_title,
    validate_category,
    validate_urgency,
    validate_affected_users,
    validate_status
)

def save_tickets(filepath, tickets):
    """
    Safely writes the current ticket collection to a JSON file.
    """
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(tickets, f, indent=4)
        return True
    except Exception as e:
        print(f"Error saving tickets to {filepath}: {e}")
        return false

def load_tickets(filepath):
    """
    Safely loads tickets from a JSON file. 
    Performs full validation and checks for duplicate IDs before accepting the data.
    If corruption or a duplicate ID is found, it rejects the load and returns None 
    so existing memory is preserved.
    """
    if not os.path.exists(filepath):
        
        return []
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        print(f"Storage Error: File is corrupted or contains invalid JSON ({e}).")
        return None  
    except Exception as e:
        print(f"Storage Error: Could not read file ({e}).")
        return None

    if not isinstance(data, list):
        print("Storage Error: Root structure of JSON file must be a list.")
        return None
    
    validated_tickets = []
    seen_ids = set()

    for item in data:
        if not isinstance(item, dict):
            print("Storage Error: Found non-dictionary record in ticket list.")
            return None

        ticket_id = item.get("id")
        if not ticket_id or not isinstance(ticket_id, str):
            print("Storage Error: Ticket is missing a valid string ID.")
            return None
        
        if ticket_id in seen_ids:
            print(f"Storage Error: Duplicate ticket ID detected ('{ticket_id}'). Load rejected to protect memory.")
            return None
        seen_ids.add(ticket_id)

        try:
            clean_title = validate_title(item.get("title", ""))
            clean_category = validate_category(item.get("category", ""))
            clean_urgency = validate_urgency(item.get("urgency", ""))
            clean_users = validate_affected_users(item.get("affected_users"))
            clean_status = validate_status(item.get("status", "open"))
            
            assigned_to = item.get("assigned_to", "Unassigned")
            notes = item.get("notes", [])
            if not isinstance(notes, list):
                notes = []

            validated_ticket = {
                "id": ticket_id,
                "title": clean_title,
                "category": clean_category,
                "urgency": clean_urgency,
                "affected_users": clean_users,
                "priority": item.get("priority", "low"), 
                "status": clean_status,
                "assigned_to": assigned_to,
                "notes": notes
            }
            validated_tickets.append(validated_ticket)

        except (ValueError, TypeError) as err:
            print(f"Storage Error: Validation failed for ticket {ticket_id}: {err}")
            return None

    return validated_tickets