"""
test_validation.py - Automated tests for Engineer A's validation bouncer.
Proves that bad inputs (booleans, negative numbers, blank titles, invalid categories)
are strictly rejected.
"""

import unittest
from campusflow.validation import (
    validate_title,
    validate_category,
    validate_urgency,
    validate_affected_users,
    validate_status
)

class TestValidation(unittest.TestCase):
    
    def test_validate_title_success(self):
        self.assertEqual(validate_title("  Fix campus Wi-Fi  "), "Fix campus Wi-Fi")

    def test_validate_title_failures(self):
        with self.assertRaises(ValueError):
            validate_title("   ") 
        with self.assertRaises(TypeError):
            validate_title(123) 

    def test_validate_category_success(self):
        self.assertEqual(validate_category("network"), "Network")
        self.assertEqual(validate_category("HARDWARE"), "Hardware")

    def test_validate_category_failure(self):
        with self.assertRaises(ValueError):
            validate_category("Plumbing") 

    def test_validate_urgency_success(self):
        self.assertEqual(validate_urgency("HIGH"), "high")
        self.assertEqual(validate_urgency("low"), "low")

    def test_validate_urgency_failure(self):
        with self.assertRaises(ValueError):
            validate_urgency("super-urgent")

    def test_validate_affected_users_success(self):
        self.assertEqual(validate_affected_users(5), 5)

    def test_validate_affected_users_failures(self):
        with self.assertRaises(TypeError):
            validate_affected_users(True)
        with self.assertRaises(TypeError):
            validate_affected_users(False)
        with self.assertRaises(TypeError):
            validate_affected_users(3.5)
        with self.assertRaises(TypeError):
            validate_affected_users("10")
        with self.assertRaises(ValueError):
            validate_affected_users(0)
        with self.assertRaises(ValueError):
            validate_affected_users(-4)

    def test_validate_status_success(self):
        self.assertEqual(validate_status("OPEN"), "open")
        self.assertEqual(validate_status("in_progress"), "in_progress")

    def test_validate_status_failure(self):
        with self.assertRaises(ValueError):
            validate_status("pending")

if __name__ == "__main__":
    unittest.main()