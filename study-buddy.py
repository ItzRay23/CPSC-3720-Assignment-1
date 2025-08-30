class Student:
    def __init__(self, name: str, email: str, bio: str = "", classes=None):
        self.name = name
        self.email = email
        self.bio = bio
        self.classes = classes if classes else []

    def add_class(self, course: str):
        if course not in self.classes:
            self.classes.append(course)
            print(f"Added class: {course}")
        else:
            print(f"Class '{course}' already in profile.")

    def remove_class(self, course: str):
        if course in self.classes:
            self.classes.remove(course)
            print(f"Removed class: {course}")
        else:
            print(f"Class '{course}' not found in profile.")

    def update_bio(self, new_bio: str):
        self.bio = new_bio
        print("Bio updated.")

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
        print("-----------------------\n")


def main_menu(student: Student):
    while True:
        print("\nStudy Buddy - Profile Menu")
        print("1. View Profile")
        print("2. Update Bio")
        print("3. Add Class")
        print("4. Remove Class")
        print("5. Exit")

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
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    # Example initial student (later we can load/save this from storage)
    student = Student(name="John Doe", email="johndoe@example.com")
    main_menu(student)