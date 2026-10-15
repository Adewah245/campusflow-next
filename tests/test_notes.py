"""
test_notes.py - Automated tests for Engineer A's follow-up notes module.
Proves that note IDs increment correctly, resolved tickets reject notes,
and message length and author validations are strictly enforced.
"""

import unittest
from campusflow.notes import add_note, generate_next_note_id

class TestNotes(unittest.TestCase):

    def test_generate_next_note_id_empty(self):
        """Tests that an empty notes list starts with N001."""
        ticket = {"notes": []}
        self.assertEqual(generate_next_note_id(ticket), "N001")

    def test_generate_next_note_id_incrementing(self):
        """Tests that note IDs increment correctly based on existing notes."""
        ticket = {
            "notes": [
                {"note_id": "N001", "author": "Alice", "message": "First note here."},
                {"note_id": "N002", "author": "Bob", "message": "Second note here."}
            ]
        }
        self.assertEqual(generate_next_note_id(ticket), "N003")

    def test_add_note_success_on_open_ticket(self):
        """Tests successfully adding a note to an open ticket."""
        ticket = {
            "id": "T001",
            "status": "open",
            "notes": []
        }
        note = add_note(ticket, "Mentor A", "Wi-Fi router reboot attempted successfully.")
        self.assertEqual(note["note_id"], "N001")
        self.assertEqual(note["author"], "Mentor A")
        self.assertEqual(len(ticket["notes"]), 1)

    def test_add_note_success_on_in_progress_ticket(self):
        """Tests successfully adding a note to an in_progress ticket."""
        ticket = {
            "id": "T002",
            "status": "in_progress",
            "notes": [{"note_id": "N001", "author": "Staff", "message": "Started."}]
        }
        note = add_note(ticket, "Mentor B", "Checking network cables now.")
        self.assertEqual(note["note_id"], "N002")
        self.assertEqual(len(ticket["notes"]), 2)

    def test_resolved_ticket_rejects_notes(self):
        """CRITICAL: Tests that a resolved ticket rejects new notes and does not consume an ID."""
        ticket = {
            "id": "T003",
            "status": "resolved",
            "notes": [{"note_id": "N001", "author": "Staff", "message": "All fixed."}]
        }
        with self.assertRaises(ValueError):
            add_note(ticket, "Mentor C", "Trying to add a note to closed ticket.")
        
        self.assertEqual(len(ticket["notes"]), 1)

    def test_rejects_blank_author(self):
        """Tests that blank or whitespace-only author names are rejected."""
        ticket = {"status": "open", "notes": []}
        with self.assertRaises(ValueError):
            add_note(ticket, "   ", "Valid message text here.")

    def test_rejects_invalid_message_length(self):
        """Tests that messages shorter than 5 characters or longer than 300 characters are rejected."""
        ticket = {"status": "open", "notes": []}
        
        with self.assertRaises(ValueError):
            add_note(ticket, "Alice", "Hi")
        
        long_msg = "A" * 301
        with self.assertRaises(ValueError):
            add_note(ticket, "Alice", long_msg)

if __name__ == "__main__":
    unittest.main()