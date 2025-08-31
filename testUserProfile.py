import unittest
from studyBuddy import Student

class TestStudentProfile(unittest.TestCase):

    def setUp(self):
        """Setup a default student profile for tests."""
        self.student = Student(name="John Doe", email="johndoe@example.com")

    def test_initial_profile(self):
        """Test if the initial profile displays correctly."""
        self.assertEqual(self.student.name, "John Doe")
        self.assertEqual(self.student.email, "johndoe@example.com")
        self.assertEqual(self.student.bio, "")
        self.assertEqual(self.student.classes, [])

    def test_add_class(self):
        """Test adding a class to the student's profile."""
        self.student.add_class("Math 101")
        self.assertIn("Math 101", self.student.classes)

    def test_add_class_duplicate(self):
        """Test adding a duplicate class."""
        self.student.add_class("Math 101")
        initial_classes = len(self.student.classes)
        self.student.add_class("Math 101")
        # Ensure duplicate class is not added
        self.assertEqual(len(self.student.classes), initial_classes)

    def test_remove_class(self):
        """Test removing a class from the student's profile."""
        self.student.add_class("Math 101")
        self.student.remove_class("Math 101")
        self.assertNotIn("Math 101", self.student.classes)

    def test_remove_class_not_found(self):
        """Test attempting to remove a class that is not in the profile."""
        self.student.remove_class("Math 101")
        self.assertEqual(len(self.student.classes), 0)

    def test_update_bio(self):
        """Test updating the bio in the student's profile."""
        self.student.update_bio("An aspiring software developer.")
        self.assertEqual(self.student.bio, "An aspiring software developer.")

    def test_display_profile(self):
        """Test the string representation of a student's profile."""
        self.student.add_class("Math 101")
        self.student.bio = "An aspiring software developer."  # direct assignment since update_bio doesn't exist
        profile_output = str(self.student)  # __str__ method gives profile details

        self.assertIn("Name: John Doe", profile_output)
        self.assertIn("Bio: An aspiring software developer.", profile_output)
        self.assertIn("Classes:", profile_output)
        self.assertIn("Math 101", profile_output)

    def tearDown(self):
        """Cleanup after each test (if needed)."""
        pass

if __name__ == "__main__":
    unittest.main()