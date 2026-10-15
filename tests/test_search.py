import unittest
from campusflow.search import search_tickets

class TestSearchTickets(unittest.TestCase):
    def setUp(self):
        self.sample_tickets = [
            {"id": "T001", "title": "Wifi router broken", "category": "Network", "status": "open", "priority": "high"},
            {"id": "T002", "title": "Python installation error", "category": "Software", "status": "in_progress", "priority": "low"},
            {"id": "T003", "title": "Campus Wifi slow", "category": "Network", "status": "resolved", "priority": "medium"}
        ]

    def test_search_by_title_case_insensitive(self):
        results = search_tickets(self.sample_tickets, query="WIFI")
        self.assertEqual(len(results), 2)
        self.assertEqual(results[0]["id"], "T001")
        self.assertEqual(results[1]["id"], "T003")

    def test_combined_filters_use_and(self):
        results = search_tickets(self.sample_tickets, query="wifi", category="Network", status="open")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["id"], "T001")

if __name__ == "__main__":
    unittest.main()