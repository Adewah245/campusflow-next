"""
validation.py - Engineer A's validation bouncer.
Ensures all incoming ticket data is clean, legal, and safe before any changes are made.
"""

VALID_CATEGORIES = {"Network", "Hardware", "Software", "Other"}
VALID_URGENCIES = {"low", "medium", "high"}
VALID_STATUSES = {"open", "in_progress", "resolved"}

def validate_title(title):
    """Ensures the title is a valid, non-blank string after trimming spaces."""
    if not isinstance(title, str):
        raise TypeError("Title must be a text string.")
    
    cleaned_title = title.strip()
    if not cleaned_title:
        raise ValueError("Title cannot be blank or just whitespace.")
        
    return cleaned_title

def validate_category(category):
    """Normalizes and validates the category name."""
    if not isinstance(category, str):
        raise TypeError("Category must be a text string.")
    
    normalized = category.strip().capitalize()
    if normalized not in VALID_CATEGORIES:
        raise ValueError(f"Invalid category '{category}'. Must be one of: {list(VALID_CATEGORIES)}")
        
    return normalized

def validate_urgency(urgency):
    """Validates that urgency is low, medium, or high (case-insensitive)."""
    if not isinstance(urgency, str):
        raise TypeError("Urgency must be a text string.")
        
    normalized = urgency.strip().lower()
    if normalized not in VALID_URGENCIES:
        raise ValueError(f"Invalid urgency '{urgency}'. Must be one of: {list(VALID_URGENCIES)}")
        
    return normalized

def validate_affected_users(value):
    """
    Validates that affected_users is a strictly positive integer (> 0).
    Explicitly rejects booleans, floats, strings, zeros, and negative numbers.
    """
    if isinstance(value, bool):
        raise TypeError("affected_users cannot be a boolean (True/False).")
        
    if not isinstance(value, int):
        raise TypeError("affected_users must be an integer.")
        
    if value <= 0:
        raise ValueError("affected_users must be a strictly positive integer greater than 0.")
        
    return value

def validate_status(status):
    """Validates that the ticket status is open, in_progress, or resolved."""
    if not isinstance(status, str):
        raise TypeError("Status must be a text string.")
        
    normalized = status.strip().lower()
    if normalized not in VALID_STATUSES:
        raise ValueError(f"Invalid status '{status}'. Must be one of: {list(VALID_STATUSES)}")
        
    return normalized