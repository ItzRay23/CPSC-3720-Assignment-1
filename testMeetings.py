# test_study_buddy_meetings.py
import unittest
from unittest.mock import patch
from studyBuddy import Student, Availability, confirm_meeting

class TestConfirmMeetings(unittest.TestCase):

    def setUp(self):
        # Create two students with overlapping classes and availability
        self.alice = Student("Alice", "alice@example.com")
        self.bob = Student("Bob", "bob@example.com")

        self.alice.add_class("Math 101")
        self.bob.add_class("Math 101")

        self.alice.add_availability("Monday", "10:00", "12:00")
        self.bob.add_availability("Monday", "11:00", "13:00")

        self.students = [self.alice, self.bob]

    @patch("builtins.input", side_effect=["0", "Math 101", "0"])
    def test_confirm_meeting_success(self, mock_input):
        """Test successfully confirming a meeting."""
        confirm_meeting(self.alice, self.students)
        self.assertEqual(len(self.alice.meetings), 1)
        self.assertEqual(len(self.bob.meetings), 1)
        self.assertIn("Math 101", self.alice.meetings[0].course)
        self.assertEqual(self.alice.meetings[0].student2.name, "Bob")

    @patch("builtins.input", side_effect=["0", "History 201", "0"])
    def test_confirm_meeting_invalid_class(self, mock_input):
        """Test confirming a meeting with invalid class input."""
        confirm_meeting(self.alice, self.students)
        self.assertEqual(len(self.alice.meetings), 0)
        self.assertEqual(len(self.bob.meetings), 0)

    @patch("builtins.input", side_effect=["5"])  # invalid index
    def test_confirm_meeting_invalid_index(self, mock_input):
        """Test confirming a meeting with invalid student index."""
        confirm_meeting(self.alice, self.students)
        self.assertEqual(len(self.alice.meetings), 0)
        self.assertEqual(len(self.bob.meetings), 0)

    def test_no_matches(self):
        """Test when no possible matches exist."""
        charlie = Student("Charlie", "charlie@example.com")
        charlie.add_class("Physics 101")
        charlie.add_availability("Tuesday", "09:00", "11:00")

        confirm_meeting(self.alice, [self.alice, charlie])
        self.assertEqual(len(self.alice.meetings), 0)
        self.assertEqual(len(charlie.meetings), 0)


if __name__ == "__main__":
    unittest.main()
