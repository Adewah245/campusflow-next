# campusflow/cli.py

import os
from campusflow.storage import load_tickets, save_tickets
from campusflow.search import search_tickets
from campusflow.reports import generate_report, get_open_work_queue

DATA_FILE = "tickets_data.json"

def display_menu():
    print("\n==============================")
    print("   CAMPUSFLOW NEXT - HELPDESK ")
    print("==============================")
    print("1. View Open Work Queue")
    print("2. Search Tickets")
    print("3. Generate Status Report")
    print("4. Exit")
    print("==============================\n")

def run_cli():
    """Main loop for the CampusFlow CLI helpdesk application."""
    # Load initial tickets from disk (or start with sample data if file doesn't exist)
    tickets = load_tickets(DATA_FILE)
    
    if not tickets:
        # Seed some default demo tickets if the file is brand new
        tickets = [
            {"id": "T001", "title": "Wi-Fi router down in Library", "category": "Network", "status": "open", "priority": "critical"},
            {"id": "T002", "title": "Python compiler error in Lab 3", "category": "Software", "status": "open", "priority": "high"},
            {"id": "T003", "title": "Projector bulb replacement needed", "category": "Hardware", "status": "resolved", "priority": "medium"}
        ]
        save_tickets(DATA_FILE, tickets)

    while True:
        display_menu()
        choice = input("Select an option (1-4): ").strip()

        if choice == "1":
            print("\n--- OPEN WORK QUEUE ---")
            queue = get_open_work_queue(tickets)
            if not queue:
                print("No open tickets! Great job.")
            else:
                for t in queue:
                    print(f"[{t['id']}] Priority: {t['priority'].upper()} | Category: {t['category']} | Title: {t['title']}")

        elif choice == "2":
            print("\n--- SEARCH TICKETS ---")
            print("Tip: You can search by ID (e.g. T001), keyword (e.g. wifi), category, or status.")
            query = input("Enter search term: ")

            results = search_tickets(tickets, query=query)
            print(f"\nFound {len(results)} matching ticket(s):")
            for t in results:
                print(f"[{t['id']}] Status: {t['status'].upper()} | Category: {t['category']} | Title: {t['title']}")

        elif choice == "3":
            print("\n--- HELPDESK SUMMARY REPORT ---")
            report = generate_report(tickets)
            print(f"Total Tickets: {report['total']}")
            print(f"Resolved: {report['resolved']}")
            print(f"Unresolved: {report['unresolved']}")
            print(f"Resolution Rate: {report['resolution_percentage']}%")
            print("\nStatus Breakdown:", report["status_counts"])
            print("Priority Breakdown:", report["priority_counts"])

        elif choice == "4":
            print("\nSaving tickets and exiting CampusFlow. Goodbye, Engineer!")
            save_tickets(DATA_FILE, tickets)
            break
        else:
            print("\nInvalid choice! Please enter a number between 1 and 4.")

if __name__ == "__main__":
    run_cli()