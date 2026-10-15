# main.py
from campusflow.storage import load_tickets, save_tickets
from campusflow.models import create_ticket
from campusflow.workflow import assign_ticket, update_ticket_status
from campusflow.reports import get_open_work_queue, generate_report

def run_helpdesk():
    """
    Launches the CampusFlow interactive CLI menu.
    """
    tickets = load_tickets()
    print("==========================================")
    print("  Welcome to CampusFlow Helpdesk CLI 🚀")
    print("==========================================")
    
    while True:
        print("\n--- MAIN MENU ---")
        print("1. View Open Work Queue")
        print("2. Create New Ticket")
        print("3. Assign Ticket to Staff")
        print("4. Update Ticket Status")
        print("5. View System Insights Report")
        print("6. Exit & Save")
        
        choice = input("\nEnter your choice (1-6): ").strip()
        
        if choice == "1":
            queue = get_open_work_queue(tickets)
            if not queue:
                print("\n📭 No open tickets in the queue. All clear!")
            else:
                print(f"\n📋 Open Work Queue ({len(queue)} tickets):")
                print("-" * 65)
                for t in queue:
                    print(f"ID: {t['id']} | Priority: {t['priority'].upper()} | Status: {t['status']}")
                    print(f"Title: {t['title']}")
                    print(f"Assigned To: {t['assigned_to'] or 'Unassigned'} | Users Affected: {t['affected_users']}")
                    print("-" * 65)
                    
        elif choice == "2":
            print("\n--- Create New Ticket ---")
            ticket_id = input("Enter Ticket ID (e.g., T001): ").strip()
            title = input("Enter ticket title/description: ").strip()
            category = input("Enter category (Network, Hardware, Software): ").strip()
            urgency = input("Enter urgency (low, medium, high): ").strip()
            
            try:
                affected_users = int(input("Enter number of affected users: ").strip())
            except ValueError:
                print("❌ Invalid number. Defaulting to 1 affected user.")
                affected_users = 1
                
            new_t = create_ticket(ticket_id, title, category, urgency, affected_users)
            tickets.append(new_t)
            save_tickets(tickets)
            print(f"✅ Success! Ticket {ticket_id} created with priority: {new_t['priority'].upper()}")
            
        elif choice == "3":
            print("\n--- Assign Ticket ---")
            ticket_id = input("Enter Ticket ID to assign: ").strip()
            staff_name = input("Enter staff member's name: ").strip()
            
            success = assign_ticket(tickets, ticket_id, staff_name)
            if success:
                save_tickets(tickets)
                print(f"✅ Ticket {ticket_id} successfully assigned to {staff_name}!")
            else:
                print("❌ Assignment failed. Check if ticket ID exists or if staff member is overloaded (max 3 active tickets).")
                
        elif choice == "4":
            print("\n--- Update Ticket Status ---")
            ticket_id = input("Enter Ticket ID: ").strip()
            new_status = input("Enter new status (open, in_progress, resolved): ").strip()
            
            success = update_ticket_status(tickets, ticket_id, new_status)
            if success:
                save_tickets(tickets)
                print(f"✅ Ticket {ticket_id} status updated to '{new_status}'!")
            else:
                print("❌ Status update failed. Check workflow rules (e.g., must be assigned before 'in_progress').")

        elif choice == "5":
            insights = generate_report(tickets)
            print("\n📊 --- System Insights Report ---")
            print(f"Total Tickets: {insights['total_tickets']}")
            print(f"Open Tickets: {insights['open_tickets']}")
            print(f"Resolved Tickets: {insights['resolved_tickets']}")
            print("Priority Breakdown:")
            for prio, count in insights['priority_breakdown'].items():
                print(f"  - {prio.upper()}: {count}")
            print("-" * 35)
                
        elif choice == "6":
            save_tickets(tickets)
            print("\n💾 Tickets saved successfully. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    run_helpdesk()