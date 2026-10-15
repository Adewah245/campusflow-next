# campusflow/search.py

def search_tickets(tickets: list, query: str = "") -> list:
    """
    Performs a smart unified search across ID, title, category, status, and priority.
    If query is empty, returns all tickets.
    """
    if not query.strip():
        return tickets

    query_clean = query.strip().casefold()
    matching_tickets = []

    for ticket in tickets:
        # Extract all searchable fields as lowercase strings
        t_id = str(ticket.get("id", "")).casefold()
        t_title = str(ticket.get("title", "")).casefold()
        t_category = str(ticket.get("category", "")).casefold()
        t_status = str(ticket.get("status", "")).casefold()
        t_priority = str(ticket.get("priority", "")).casefold()

        # If the query appears in ANY of these fields, it's a match!
        if (query_clean in t_id or 
            query_clean in t_title or 
            query_clean in t_category or 
            query_clean in t_status or 
            query_clean in t_priority):
            matching_tickets.append(ticket)

    return matching_tickets