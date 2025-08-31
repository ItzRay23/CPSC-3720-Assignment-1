# study_buddy.py

class Availability:
    def __init__(self, day: str, start_time: str, end_time: str):
        self.day = day
        self.start_time = start_time
        self.end_time = end_time

    def __str__(self):
        return f"{self.day}: {self.start_time} - {self.end_time}"

    def overlaps(self, other) -> bool:
        """Check if two availability slots overlap (same day + overlapping times)."""
        if self.day != other.day:
            return False

        def to_minutes(t):
            h, m = map(int, t.split(":"))
            return h * 60 + m

        start1, end1 = to_minutes(self.start_time), to_minutes(self.end_time)
        start2, end2 = to_minutes(other.start_time), to_minutes(other.end_time)

        return not (end1 <= start2 or end2 <= start1)

class Meeting:
    def __init__(self, student1, student2, course, day, start, end):
        self.student1 = student1
        self.student2 = student2
        self.course = course
        self.day = day
        self.start = start
        self.end = end

    def __str__(self):
        return f"{self.course} Study Session on {self.day} {self.start}-{self.end} with {self.student2.name}"

class Student:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.bio = ""
        self.classes = []
        self.availability = []
        self.meetings = []  # new feature


    # ---------- Profile Methods ----------
    # Adds classes to user profile
    def add_class(self, course: str):
        if course not in self.classes:
            self.classes.append(course)
        else:
            print(f"Class '{course}' already in profile.")
    
    # Removes classes from user profile
    def remove_class(self, course: str):
        if course in self.classes:
            self.classes.remove(course)
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
    def add_availability(self, day, start_time, end_time):
        """Add a new availability slot, ensuring no duplicates are added."""
        for slot in self.availability:
            if (
                slot.day == day
                and slot.start_time == start_time
                and slot.end_time == end_time
            ):
                return
        self.availability.append(Availability(day, start_time, end_time))
    
    # Removes availability slot from user profile by index
    def remove_availability(self, index: int):
        if 0 <= index < len(self.availability):
            removed = self.availability.pop(index)
            print(f"Removed availability: {removed}")
        else:
            print("Invalid availability index.")
    
    def add_meeting(self, meeting):
        self.meetings.append(meeting)

    # ---------- Match Suggestion ----------
    def suggest_matches(self, other_students: list):
        matches = []
        for other in other_students:
            if other.email == self.email:
                continue  # skip self
            shared_classes = set(self.classes) & set(other.classes)
            if shared_classes:
                for my_slot in self.availability:
                    for their_slot in other.availability:
                        if my_slot.overlaps(their_slot):
                            matches.append((other, list(shared_classes), my_slot, their_slot))
                            break
        return matches
    
    def __str__(self):
        classes = ", ".join(self.classes) if self.classes else "None"
        availability = "\n".join(str(a) for a in self.availability) if self.availability else "None"
        meetings = "\n".join(str(m) for m in self.meetings) if self.meetings else "None"
        return (
            f"Name: {self.name}\n"
            f"Email: {self.email}\n"
            f"Bio: {self.bio}\n"
            f"Classes: {classes}\n"
            f"Availability:\n{availability}\n"
            f"Meetings:\n{meetings}\n"
        )

# ---------- Confirm Meetings Feature ----------
def confirm_meeting(current_student, students):
    print("\n--- Confirm a Meeting ---")
    # Show suggested matches first
    possible_matches = []
    for student in students:
        if student.email == current_student.email:
            continue

        shared_classes = set(current_student.classes) & set(student.classes)
        if not shared_classes:
            continue

        shared_availability = [
            (a, b) for a in current_student.availability for b in student.availability if a.day == b.day
        ]
        if shared_availability:
            possible_matches.append((student, shared_classes, shared_availability))

    if not possible_matches:
        print("No available matches to confirm.")
        return

    # Display possible matches
    for i, (student, classes, times) in enumerate(possible_matches):
        print(f"{i}. {student.name} ({student.email})")
        print(f"   Classes: {', '.join(classes)}")
        for j, (a, b) in enumerate(times):
            print(f"     {j}. {a.day}: You({a.start_time}-{a.end_time}) | {student.name}({b.start_time}-{b.end_time})")

    try:
        match_index = int(input("Select a student by index: "))
        chosen_student, shared_classes, shared_times = possible_matches[match_index]

        class_choice = input(f"Choose a class from shared classes {list(shared_classes)}: ")
        if class_choice not in shared_classes:
            print("Invalid class choice.")
            return

        time_index = int(input("Choose a time index from above [0, 1, 2]: "))
        a, b = shared_times[time_index]

        # For simplicity, use the overlap start and end time (not perfect, but workable)
        meeting = Meeting(current_student, chosen_student, class_choice, a.day, a.start_time, a.end_time)
        current_student.add_meeting(meeting)

        # Add reciprocal meeting for partner
        partner_meeting = Meeting(chosen_student, current_student, class_choice, a.day, a.start_time, a.end_time)
        chosen_student.add_meeting(partner_meeting)

        print(f"Meeting confirmed with {chosen_student.name} for {class_choice} on {a.day} {a.start_time}-{a.end_time}")
    except (ValueError, IndexError):
        print("Invalid input. Meeting not created.")



def profile_menu(student: Student):
    while True:
        print("\nProfile Menu")
        print("1. View Profile")
        print("2. Update Bio")
        print("3. Back to Main Menu")
        choice = input("Select an option: ")

        if choice == "1":
            student.display_profile()
        elif choice == "2":
            bio = input("Enter new bio: ")
            student.update_bio(bio)
        elif choice == "3":
            break
        else:
            print("Invalid choice.")


def classes_menu(student: Student):
    while True:
        print("\nClasses Menu")
        print("1. View Classes")
        print("2. Add Class")
        print("3. Remove Class")
        print("4. Back to Main Menu")
        choice = input("Select an option: ")

        if choice == "1":
            print("Your Classes:")
            if student.classes:
                for c in student.classes:
                    print(f"- {c}")
            else:
                print("None")
        elif choice == "2":
            course = input("Enter class name to add: ")
            student.add_class(course)
        elif choice == "3":
            course = input("Enter class name to remove: ")
            student.remove_class(course)
        elif choice == "4":
            break
        else:
            print("Invalid choice.")


def availability_menu(student: Student):
    while True:
        print("\nAvailability Menu")
        print("1. View Availability")
        print("2. Add Availability")
        print("3. Remove Availability")
        print("4. Back to Main Menu")
        choice = input("Select an option: ")

        if choice == "1":
            print("Your Availability:")
            if student.availability:
                for i, slot in enumerate(student.availability):
                    print(f"{i}. {slot}")
            else:
                print("None")
        elif choice == "2":
            day = input("Enter day (e.g., Monday): ")
            start = input("Enter start time (HH:MM): ")
            end = input("Enter end time (HH:MM): ")
            student.add_availability(day, start, end)
        elif choice == "3":
            if student.availability:
                for i, slot in enumerate(student.availability):
                    print(f"{i}. {slot}")
                try:
                    idx = int(input("Enter index to remove: "))
                    student.remove_availability(idx)
                except ValueError:
                    print("Invalid input.")
            else:
                print("No availability to remove.")
        elif choice == "4":
            break
        else:
            print("Invalid choice.")


def main_menu(student: Student, all_students: list):
    while True:
        print("\nStudy Buddy - Main Menu")
        print("1. Profile")
        print("2. Classes")
        print("3. Availability")
        print("4. Suggest Matches")
        print("5. Confirm Meeting")
        print("6. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            profile_menu(student)
        elif choice == "2":
            classes_menu(student)
        elif choice == "3":
            availability_menu(student)
        elif choice == "4":
            matches = student.suggest_matches(all_students)
            if matches:
                print("\nSuggested Matches:")
                for match in matches:
                    other, classes, my_slot, their_slot = match
                    print(f"- {other.name} ({other.email})")
                    print(f"  Shared Classes: {', '.join(classes)}")
                    print(f"  Your Availability: {my_slot}")
                    print(f"  Their Availability: {their_slot}")
            else:
                print("No matches found.")
        elif choice == "5":
            confirm_meeting(student, all_students)
        elif choice == "6":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    print("Welcome to Study Buddy!")
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    user_student = Student(name, email)

    # Example preloaded students
    student2 = Student("Jane Smith", "janesmith@example.com")
    student2.add_class("Math 101")
    student2.add_class("Physics 101")
    student2.add_availability("Monday", "11:00", "13:00")

    student3 = Student("Alice Brown", "aliceb@example.com")
    student3.add_class("History 202")
    student3.add_availability("Tuesday", "09:00", "11:00")

    all_students = [user_student, student2, student3]

    main_menu(user_student, all_students)