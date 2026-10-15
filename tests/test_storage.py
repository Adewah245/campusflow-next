"""
test_storage.py - Automated tests for Engineer A's safe storage module.
Proves that corrupted JSON files and duplicate ticket IDs are safely rejected
without crashing or wiping out working memory.
"""

import unittest
import os
import tempfile
import json
from campusflow.storage import save_tickets, load_tickets

class TestStorage(unittest.TestCase):
    
    def setUp(self):
        """Create a temporary file before each test so we don't mess up real files."""
        self.test_fd, self.test_path = tempfile.mkstemp()

    def tearDown(self):
        """Clean up and delete the temporary file after each test finishes."""
        os.close(self.test_fd)
        if os.path.exists(self.test_path):
            os.remove(self.test_path)

    def test_save_and_load_valid_tickets(self):
        """Tests that normal, valid tickets save and load successfully."""
        tickets = [
            {
                "id": "T001",
                "title": "Broken Wi-Fi in Lab",
                "category": "Network",
                "urgency": "high",
                "affected_users": 15,
                "priority": "critical",
                "status": "open",
                "assigned_to": "Unassigned",
                "notes": []
            }
        ]
        
        save_success = save_tickets(self.test_path, tickets)
        self.assertTrue(save_success)
        
        loaded = load_tickets(self.test_path)
        self.assertIsNotNone(loaded)
        self.assertEqual(len(loaded), 1)
        self.assertEqual(loaded[0]["id"], "T001")
        self.assertEqual(loaded[0]["title"], "Broken Wi-Fi in Lab")

    def test_rejects_corrupted_json(self):
        """Tests that a broken JSON file returns None safely instead of crashing."""
        with open(self.test_path, 'w', encoding='utf-8') as f:
            f.write("[{'id': 'T001', 'title': 'Bad syntax'") 
            
        loaded = load_tickets(self.test_path)
        self.assertIsNone(loaded)

    def test_rejects_duplicate_ticket_ids(self):
        """Tests that two tickets sharing the same ID cause the load to be rejected."""
        tickets = [
            {
                "id": "T001",
                "title": "First Ticket",
                "category": "Hardware",
                "urgency": "low",
                "affected_users": 2,
                "priority": "low",
                "status": "open",
                "assigned_to": "Unassigned",
                "notes": []
            },
            {
                "id": "T001",  
                "title": "Conflicting Ticket",
                "category": "Software",
                "urgency": "high",
                "affected_users": 5,
                "priority": "medium",
                "status": "open",
                "assigned_to": "Unassigned",
                "notes": []
            }
        ]
        
        with open(self.test_path, 'w', encoding='utf-8') as f:
            json.dump(tickets, f)
            
        loaded = load_tickets(self.test_path)
        self.assertIsNone(loaded)

if __name__ == "__main__":
    unittest.main()