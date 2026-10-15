# campusflow/models.py

def calculate_priority(urgency: str, affected_users: int) -> str:
    """
    Calculates priority based on urgency and affected users.
    """
    clean_urgency = urgency.strip().casefold()
    
    if clean_urgency == "high" or affected_users > 50:
        return "critical"
    elif clean_urgency == "medium" or affected_users > 10:
        return "high"
    elif clean_urgency == "low" and affected_users <= 5:
        return "low"
    else:
        return "medium"


def create_ticket(ticket_id: str, title: str, category: str, urgency: str, affected_users: int) -> dict:
    """
    Creates a new ticket dictionary with automated priority and default status.
    """
    clean_id = ticket_id.strip()
    clean_title = title.strip()
    clean_category = category.strip().casefold()
    clean_urgency = urgency.strip().casefold()
    
    priority = calculate_priority(clean_urgency, affected_users)
    
    return {
        "id": clean_id,
        "title": clean_title,
        "category": clean_category,
        "urgency": clean_urgency,
        "affected_users": affected_users,
        "priority": priority,
        "status": "open",
        "assigned_to": None
    }

# Backward compatibility alias
create_tickets = create_ticket