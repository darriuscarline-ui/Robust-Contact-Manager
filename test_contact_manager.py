
"""
Unit tests for the Robust Contact Manager.
"""

import unittest
from unittest.mock import patch
from io import StringIO

import contact_manager


class TestContactManager(unittest.TestCase):
    """Test the contact manager functions."""

    def setUp(self):
        """Start each test with an empty contacts dictionary."""
        contact_manager.contacts.clear()

    def test_add_contact(self):
        """Test adding a new contact."""
        with patch("sys.stdout", new_callable=StringIO):
            contact_manager.add_contact("Alice", "555-1234")

        self.assertEqual(
            contact_manager.contacts["Alice"],
            "555-1234"
        )

    def test_find_existing_contact(self):
        """Test finding an existing contact."""
        contact_manager.contacts["Alice"] = "555-1234"

        with patch("sys.stdout", new_callable=StringIO) as output:
            result = contact_manager.find_contact("Alice")

        self.assertEqual(result, "555-1234")
        self.assertIn("Alice: 555-1234", output.getvalue())

    def test_find_missing_contact(self):
        """Test finding a contact that does not exist."""
        with patch("sys.stdout", new_callable=StringIO) as output:
            result = contact_manager.find_contact("Diana")

        self.assertIsNone(result)
        self.assertIn("Contact not found.", output.getvalue())

    def test_delete_existing_contact(self):
        """Test deleting an existing contact."""
        contact_manager.contacts["Bob"] = "555-5678"

        with patch("sys.stdout", new_callable=StringIO):
            result = contact_manager.delete_contact("Bob")

        self.assertTrue(result)
        self.assertNotIn("Bob", contact_manager.contacts)

    def test_delete_missing_contact(self):
        """Test deleting a contact that does not exist."""
        with patch("sys.stdout", new_callable=StringIO) as output:
            result = contact_manager.delete_contact("Ethan")

        self.assertFalse(result)
        self.assertIn("Contact not found.", output.getvalue())

    def test_add_duplicate_contact(self):
        """Test that adding a duplicate raises an exception."""
        contact_manager.contacts["Alice"] = "555-1234"

        with self.assertRaises(
            contact_manager.DuplicateContactError
        ):
            contact_manager.add_contact("Alice", "555-9999")


if __name__ == "__main__":
    unittest.main()
