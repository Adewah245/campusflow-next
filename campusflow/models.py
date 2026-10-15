def create_tickets(ticket_id: str, title: str, category: str, urgency: str, affected_users: int) -> dict:
    """
    take a raw input and return a strutured dictionary representing a ticket.
    """
    ticket = {
        "id": ticket_id,
        "title": title,
        "category": category,
        "urgency": urgency,
        "affected_users": affected_users,
        "status": "open",
        "assigned_to": None

    }
    return ticket

    def calculate_priority(urgency: str, affected_users: int) -> str:
        """
        evaluating urgency and affected users to return a priority rating
        """
        urgency_clean = urgency.strip().casefold()
        # rule 1: if urgency and 10 or more user are affected = critical
        if urgency_clean == "high" and affected_users >= 10 :
            return "Critical"
        # rule 2: if urgency == high or affected users is 10 or more = high
        elif urgency_clean == "high" or affected_users >= 10 :
            return "high" 
        # rule 3: if urgency medium and affected user 3 = medium
        elif urgency_clean == "medium" or affected_users >= 3:
            return "medium"
        else:
            return "low"       