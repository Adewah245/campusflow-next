# tests/test_storage.py

import unittest
import os
from campusflow.storage import save_tickets, load_tickets

class TestStorage(unittest.TestCase):
    
    def setUp(self):
        """Setup a temporary test file path for our storage tests."""
        self.test_filepath = "test_tickets_temp.json"

    def tearDown(self):
        """Clean up the temporary test file after each test runs."""
        if os.path.exists(self.test_filepath):
            os.remove(self.test_filepath)

    def test_save_and_load_tickets(self):
        """Verify we can successfully write tickets to disk and read them back identically."""
        sample_tickets = [
            {"id": "T001", "title": "Projector broken", "status": "open", "priority": "high"}
        ]
        
        save_tickets(self.test_filepath, sample_tickets)
        loaded_tickets = load_tickets(self.test_filepath)
        
        self.assertEqual(loaded_tickets, sample_tickets)

    def test_load_nonexistent_file_safety(self):
        """Verify that trying to load a file that doesn't exist returns [] safely instead of crashing."""
        loaded_tickets = load_tickets("nonexistent_helpdesk_file.json")
        self.assertEqual(loaded_tickets, [])

if __name__ == "__main__":
    unittest.main()