# campusflow/workflow.py

def assign_ticket(tickets: list, ticket_id: str, staff_name: str, max_workload: int = 3) -> bool:
    """
    Assigns a ticket to a staff member only if:
    1. The ticket exists.
    2. The staff name is not blank.
    3. The staff member hasn't exceeded their maximum active workload (default is 3).
    """
    clean_name = staff_name.strip()
    if not clean_name:
        return False  # Reject blank staff names!
        
    active_ticket_count = 0
    target_ticket = None
    
    for ticket in tickets:
        if ticket["id"] == ticket_id:
            target_ticket = ticket
            
        if ticket.get("assigned_to") == clean_name and ticket.get("status") != "resolved":
            active_ticket_count += 1
            
    if target_ticket is None:
        return False  # Ticket ID not found
        
    if active_ticket_count >= max_workload:
        print(f"⚠️ Assignment rejected: {clean_name} is too busy ({active_ticket_count} active tickets).")
        return False
        
    target_ticket["assigned_to"] = clean_name
    return True


def update_ticket_status(tickets: list, ticket_id: str, new_status: str) -> bool:
    """
    Safely updates a ticket's status based on strict workflow rules:
    - open -> in_progress (must be assigned first!)
    - in_progress -> resolved
    - resolved -> open (reopening)
    """
    clean_status = new_status.strip().casefold()
    allowed_statuses = ["open", "in_progress", "resolved"]
    
    if clean_status not in allowed_statuses:
        print(f"❌ Invalid status: '{new_status}'. Allowed: {allowed_statuses}")
        return False
        
    for ticket in tickets:
        if ticket["id"] == ticket_id:
            current_status = ticket.get("status", "open")
            
            if clean_status == "in_progress" and ticket.get("assigned_to") is None:
                print(f"❌ Cannot move ticket {ticket_id} to in_progress because it is unassigned.")
                return False
                
            if current_status == "resolved" and clean_status != "open":
                print(f"❌ Ticket {ticket_id} is resolved and locked. You must reopen it to 'open' first.")
                return False
                
            ticket["status"] = clean_status
            return True
            
    print(f"❌ Ticket ID {ticket_id} not found.")
    return False