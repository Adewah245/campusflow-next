"""
notes.py - Engineer A's follow-up notes management.
Handles note ID generation, status checks (blocking notes on resolved tickets),
and message length validation.
"""

def generate_next_note_id(ticket):
    """
    Inspects the ticket's existing notes and generates the next ID (e.g., N001, N002).
    """
    notes = ticket.get("notes", [])
    if not notes:
        return "N001"
    
    max_num = 0
    for note in notes:
        note_id = note.get("note_id", "N000")
        try:
            
            num = int(note_id.replace("N", ""))
            if num > max_num:
                max_num = num
        except ValueError:
            pass
            
    
    return f"N{max_num + 1:03d}"

def add_note(ticket, author, message):
    """
    Validates and adds a new follow-up note to a ticket.
    Enforces that resolved tickets cannot accept notes.
    """
    
    status = ticket.get("status", "").strip().lower()
    if status == "resolved":
        raise ValueError("Cannot add notes to a resolved ticket. Reopen it first.")
    
    if status not in {"open", "in_progress"}:
        raise ValueError(f"Cannot add notes to a ticket with status '{status}'.")
        
    
    if not isinstance(author, str) or not author.strip():
        raise ValueError("Author label cannot be blank.")
        
    
    if not isinstance(message, str):
        raise TypeError("Message must be a text string.")
        
    cleaned_message = message.strip()
    if len(cleaned_message) < 5 or len(cleaned_message) > 300:
        raise ValueError("Note message must be between 5 and 300 characters.")
        
    
    if "notes" not in ticket:
        ticket["notes"] = []
        
    
    note_id = generate_next_note_id(ticket)
    
    new_note = {
        "note_id": note_id,
        "author": author.strip(),
        "message": cleaned_message
    }
    
    ticket["notes"].append(new_note)
    return new_note