# study_buddy.py

class Availability:
    def __init__(self, day: str, start_time: str, end_time: str):
        self.day = day
        self.start_time = start_time
        self.end_time = end_time

    def __str__(self):
        return f"{self.day}: {self.start_time} - {self.end_time}"


class Student:
    def __init__(self, name: str, email: str, bio: str = "", classes=None):
        self.name = name
        self.email = email
        self.bio = bio
        self.classes = classes if classes else []
        self.availability = []

    # ---------- Profile Methods ----------
    # Adds classes to user profile
    def add_class(self, course: str):
        if course not in self.classes:
            self.classes.append(course)
            print(f"Added class: {course}")
        else:
            print(f"Class '{course}' already in profile.")
    
    # Removes classes from user profile
    def remove_class(self, course: str):
        if course in self.classes:
            self.classes.remove(course)
            print(f"Removed class: {course}")
        else:
            print(f"Class '{course}' not found in profile.")
    
    # Updates bio in user profile
    def update_bio(self, new_bio: str):
        self.bio = new_bio
        print("Bio updated.")

    # Displays user profile information
    def display_profile(self):
        print("\n--- Student Profile ---")
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Bio: {self.bio if self.bio else 'N/A'}")
        print("Classes:")
        if self.classes:
            for c in self.classes:
                print(f"  - {c}")
        else:
            print("  None")
        print("Availability:")
        if self.availability:
            for slot in self.availability:
                print(f"  - {slot}")
        else:
            print("  None")
        print("-----------------------\n")

    # ---------- Availability Methods ----------
    # Adds availability slot to user profile
    def add_availability(self, day: str, start_time: str, end_time: str):
        slot = Availability(day, start_time, end_time)
        if slot not in self.availability:
            self.availability.append(slot)
            print(f"Added availability: {slot}")
        else:
            print("This availability slot already exists.")
    
    # Removes availability slot from user profile by index
    def remove_availability(self, index: int):
        if 0 <= index < len(self.availability):
            removed = self.availability.pop(index)
            print(f"Removed availability: {removed}")
        else:
            print("Invalid availability index.")


def main_menu(student: Student):
    while True:
        print("\nStudy Buddy - Main Menu")
        print("1. View Profile")
        print("2. Update Bio")
        print("3. Add Class")
        print("4. Remove Class")
        print("5. Add Availability")
        print("6. Remove Availability")
        print("7. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            student.display_profile()
        elif choice == "2":
            bio = input("Enter new bio: ")
            student.update_bio(bio)
        elif choice == "3":
            course = input("Enter class name to add: ")
            student.add_class(course)
        elif choice == "4":
            course = input("Enter class name to remove: ")
            student.remove_class(course)
        elif choice == "5":
            day = input("Enter day (e.g., Monday): ")
            start = input("Enter start time (HH:MM): ")
            end = input("Enter end time (HH:MM): ")
            student.add_availability(day, start, end)
        elif choice == "6":
            if student.availability:
                print("Select availability to remove:")
                for i, slot in enumerate(student.availability):
                    print(f"{i}. {slot}")
                try:
                    idx = int(input("Enter index: "))
                    student.remove_availability(idx)
                except ValueError:
                    print("Invalid input.")
            else:
                print("No availability slots to remove.")
        elif choice == "7":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    # Example student
    student = Student(name="John Doe", email="johndoe@example.com")
    main_menu(student)
