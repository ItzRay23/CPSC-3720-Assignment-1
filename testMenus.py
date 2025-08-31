# test_study_buddy_menus.py
import unittest
from unittest.mock import patch
from studyBuddy import Student, Availability, profile_menu, classes_menu, availability_menu

class TestStudyBuddyMenus(unittest.TestCase):

    def setUp(self):
        self.student = Student("Test User", "test@example.com")

    # ---------- Profile Menu ----------
    @patch("builtins.input", side_effect=["1", "3"])  # View Profile, then Back
    def test_profile_menu_view(self, mock_input):
        profile_menu(self.student)  # Should print profile without errors

    @patch("builtins.input", side_effect=["2", "This is my new bio", "3"])
    def test_profile_menu_update_bio(self, mock_input):
        profile_menu(self.student)
        self.assertEqual(self.student.bio, "This is my new bio")

    # ---------- Classes Menu ----------
    @patch("builtins.input", side_effect=["2", "Math 101", "1", "4"])
    def test_classes_menu_add_class(self, mock_input):
        classes_menu(self.student)
        self.assertIn("Math 101", self.student.classes)

    @patch("builtins.input", side_effect=["2", "Math 101", "3", "Math 101", "4"])
    def test_classes_menu_remove_class(self, mock_input):
        classes_menu(self.student)
        self.assertNotIn("Math 101", self.student.classes)

    # ---------- Availability Menu ----------
    @patch("builtins.input", side_effect=["2", "Monday", "10:00", "12:00", "1", "4"])
    def test_availability_menu_add(self, mock_input):
        availability_menu(self.student)
        self.assertEqual(len(self.student.availability), 1)
        self.assertEqual(str(self.student.availability[0]), "Monday: 10:00 - 12:00")

    @patch("builtins.input", side_effect=["2", "Tuesday", "09:00", "11:00", "3", "0", "4"])
    def test_availability_menu_remove(self, mock_input):
        availability_menu(self.student)
        self.assertEqual(len(self.student.availability), 0)


if __name__ == "__main__":
    unittest.main()
