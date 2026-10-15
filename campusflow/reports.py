def generate_report(tickets: list) -> dict:
    total = len(tickets)
    status_counts = {"open": 0, "in_progress": 0, "resolved": 0}
    priority_counts = {"critical": 0, "high": 0, "medium": 0, "low": 0}
    category_counts = {}

    for ticket in tickets:
        st = ticket.get("status", "").lower()
        if st in status_counts:
            status_counts[st] += 1
        pr = ticket.get("priority", "").lower()
        if pr in priority_counts:
            priority_counts[pr] += 1
        cat = ticket.get("category", "Other")
        category_counts[cat] = category_counts.get(cat, 0) + 1

    resolved_count = status_counts["resolved"]
    unresolved_count = status_counts["open"] + status_counts["in_progress"]

    if total > 0:
        resolution_percentage = (resolved_count / total) * 100
    else:
        resolution_percentage = 0.0

    return {
        "total": total,
        "unresolved": unresolved_count,
        "resolved": resolved_count,
        "resolution_percentage": round(resolution_percentage, 1),
        "status_counts": status_counts,
        "priority_counts": priority_counts,
        "category_counts": category_counts
    }

def get_open_work_queue(tickets: list) -> list:
    open_tickets = [t for t in tickets if t.get("status", "").lower() == "open"]
    priority_rank = {"critical": 0, "high": 1, "medium": 2, "low": 3}

    def sort_key(ticket):
        pri = ticket.get("priority", "low").lower()
        rank = priority_rank.get(pri, 4)
        ticket_id_str = ticket.get("id", "T0")
        try:
            numeric_id = int(''.join(filter(str.isdigit, ticket_id_str)))
        except ValueError:
            numeric_id = 0
        return (rank, numeric_id)

    return sorted(open_tickets, key=sort_key)