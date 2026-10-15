import unittest
from campusflow.reports import generate_report, get_open_work_queue

class TestReportsAndAnalytics(unittest.TestCase):
    def test_generate_report_normal(self):
        tickets = [
            {"id": "T001", "title": "A", "category": "Network", "status": "open", "priority": "critical"},
            {"id": "T002", "title": "B", "category": "Software", "status": "resolved", "priority": "low"},
            {"id": "T003", "title": "C", "category": "Hardware", "status": "resolved", "priority": "high"}
        ]
        report = generate_report(tickets)
        self.assertEqual(report["total"], 3)
        self.assertEqual(report["resolved"], 2)
        self.assertEqual(report["unresolved"], 1)
        self.assertEqual(report["resolution_percentage"], 66.7)

    def test_generate_report_empty_dataset_safety(self):
        report = generate_report([])
        self.assertEqual(report["total"], 0)
        self.assertEqual(report["resolution_percentage"], 0.0)

    def test_open_work_queue_sorting(self):
        tickets = [
            {"id": "T005", "title": "Low open", "status": "open", "priority": "low"},
            {"id": "T001", "title": "Critical open", "status": "open", "priority": "critical"},
            {"id": "T002", "title": "Resolved ticket", "status": "resolved", "priority": "critical"},
            {"id": "T003", "title": "Critical open earlier ID", "status": "open", "priority": "critical"}
        ]
        queue = get_open_work_queue(tickets)
        self.assertEqual(len(queue), 3)
        self.assertEqual(queue[0]["id"], "T001")
        self.assertEqual(queue[1]["id"], "T003")
        self.assertEqual(queue[2]["id"], "T005")

if __name__ == "__main__":
    unittest.main()