"""Example: University and Department.. Composition Exercise"""

class Department:
    def __init__(self, department_name, head):
        self.department_name = department_name
        self.head = head
    def show_department_details(self):
        print(f"Department Name: {self.department_name}")
        print(f"Head of Department: {self.head}")

class University:
    def __init__(self, university_name, department_name, head):
        self.university_name = university_name
        self.department = Department(department_name, head)

    def show_university_details(self):
        print(f"University Name: {self.university_name}")
        self.department.show_department_details()

university1 = University(
    "Auckland University of Technology",
    "Computer Science & Engineering",
    "Dr. John Snow"
)

university1.show_university_details()