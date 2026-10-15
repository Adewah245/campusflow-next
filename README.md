# campusflow-next
# CampusFlow Helpdesk CLI 🚀

CampusFlow is a professional-grade, terminal-based IT helpdesk management system built with Python. It features automated priority calculation, intelligent staff workload balancing, strict workflow lifecycle security, and persistent JSON storage.

---

## 📁 Project File Structure

```text
campusflow-next/
│
├── campusflow/
│   ├── __init__.py      # Package initializer
│   ├── models.py        # Ticket blueprint & automated priority engine
│   ├── workflow.py      # Staff assignment, workload limits & status transitions
│   ├── reports.py       # Custom work queue sorting (priority + tie-breaker ID)
│   └── storage.py       # JSON persistence (saving and loading data)
│
├── data/
│   └── tickets.json     # Local database file storing persistent records
│
├── main.py              # Application launcher & interactive CLI menu
└── README.md            # Project 

⚙️ Core Engineering Features
Robust Input Normalization: Uses .strip().casefold() across all text inputs (urgency, status, staff names) to prevent whitespace and capitalization bugs.

Automated Priority Engine (models.py): Dynamically calculates ticket priority (critical, high, medium, low) based on urgency and affected users.

Smart Workload Balancing (workflow.py): Protects IT staff from burnout by enforcing a maximum active ticket limit (default: 3 active tickets per staff member).

Workflow Lifecycle Locking (workflow.py):

Unassigned tickets cannot move to in_progress.

Resolved tickets are locked and require explicit reopening.

Custom Multi-Level Sorting (reports.py): Sorts open work queues using tuple mapping and lambda keys (Priority score first, chronological ID tie-breaker second).

Data Persistence (storage.py): Automatically saves and loads state using formatted JSON files with built-in corruption error handling.

🚀 How to Run the Application
Ensure you have Python 3 installed.

Clone or open the project folder in your terminal.

Launch the application:

Bash


python3 main.py
Follow the interactive menu prompts (1–5) to view queues, create tickets, assign work, update statuses, or exit and save.