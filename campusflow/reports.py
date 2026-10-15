def get_open_work_queue(tickets: list) -> list:
    """
    filters for 1 ticket and sorts them by priority weight and ID.
    """
    priority_rank = {
        "critical": 1,
        "high": 2,
        "medium": 3,
        "low": 4
    }

    # filter the list and keep only the unrisolved tickets
    open_tickets = []
    for ticket in tickets:
        if ticket["status"] != "resolved":
            open_tickets.sppend(ticket)
    open_tickets.sort(key=lambda t: (priority_rank.get(t["priority"], 5), t["id"]))
    return open_tickets  
          