import unittest
from studyBuddy import Student

class TestStudentAvailability(unittest.TestCase):

    def setUp(self):
        """Create a default student for testing availability."""
        self.student = Student(name="Jane Doe", email="janedoe@example.com")

    def test_add_availability(self):
        """Test adding a valid availability slot."""
        self.student.add_availability("Monday", "10:00", "12:00")
        self.assertEqual(len(self.student.availability), 1)
        self.assertEqual(str(self.student.availability[0]), "Monday: 10:00 - 12:00")

    def test_add_duplicate_availability(self):
        """Test that duplicate availability slots are not added."""
        self.student.add_availability("Monday", "10:00", "12:00")
        initial_count = len(self.student.availability)
        self.student.add_availability("Monday", "10:00", "12:00")
        self.assertEqual(len(self.student.availability), initial_count)

    def test_remove_availability_valid_index(self):
        """Test removing an availability slot by valid index."""
        self.student.add_availability("Tuesday", "14:00", "16:00")
        self.assertEqual(len(self.student.availability), 1)
        self.student.remove_availability(0)
        self.assertEqual(len(self.student.availability), 0)

    def test_remove_availability_invalid_index(self):
        """Test removing an availability slot with an invalid index."""
        self.student.add_availability("Wednesday", "09:00", "11:00")
        self.assertEqual(len(self.student.availability), 1)
        self.student.remove_availability(5)  # Out of range
        # Ensure availability list is unchanged
        self.assertEqual(len(self.student.availability), 1)

    def test_multiple_availability_slots(self):
        """Test adding and managing multiple availability slots."""
        self.student.add_availability("Thursday", "08:00", "10:00")
        self.student.add_availability("Friday", "13:00", "15:00")
        self.assertEqual(len(self.student.availability), 2)
        self.assertIn("Thursday: 08:00 - 10:00", [str(a) for a in self.student.availability])
        self.assertIn("Friday: 13:00 - 15:00", [str(a) for a in self.student.availability])

if __name__ == "__main__":
    unittest.main()
