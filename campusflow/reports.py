# campusflow/reports.py

def get_open_work_queue(tickets: list) -> list:
    """
    Filters for open tickets and sorts them by priority weight and ID.
    """
    priority_rank = {
        "critical": 1,
        "high": 2,
        "medium": 3,
        "low": 4
    }
    
    open_tickets = []
    for ticket in tickets:
        if ticket["status"] != "resolved":
            open_tickets.append(ticket)
            
    open_tickets.sort(key=lambda t: (priority_rank.get(t["priority"], 5), t["id"]))
    
    return open_tickets


def generate_report(tickets: list) -> dict:
    """
    Generates summary insights for the helpdesk tickets:
    total count, open vs resolved counts, and priority breakdowns.
    """
    total = len(tickets)
    resolved = sum(1 for t in tickets if t.get("status") == "resolved")
    open_count = total - resolved
    
    # Priority breakdown stats
    priority_counts = {"critical": 0, "high": 0, "medium": 0, "low": 0}
    for ticket in tickets:
        p = ticket.get("priority", "low").casefold()
        if p in priority_counts:
            priority_counts[p] += 1
            
    return {
        "total_tickets": total,
        "open_tickets": open_count,
        "resolved_tickets": resolved,
        "priority_breakdown": priority_counts
    }