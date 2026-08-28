# Week 5 - Activity 3: Inheritance
class Person:
    """Base class representing a person."""

    def __init__(self, person_id, name):
        self.id = person_id
        self.name = name

    def display_info(self):
        print(f"ID: {self.id}")
        print(f"Name: {self.name}")

class Student(Person):
    """Represents a student who inherits from Person."""

    def __init__(self, student_id, name):
        super().__init__(student_id, name)
        self.student_id = student_id

    def display_info(self):
        print(f"Student ID: {self.student_id}")
        print(f"Name: {self.name}")

class Staff(Person):
    """Represents staff who inherit from Person."""

    def __init__(self, staff_id, name, tax_num):
        super().__init__(staff_id, name)
        self.staff_id = staff_id
        self.tax_num = tax_num

    def display_info(self):
        print(f"Staff ID: {self.staff_id}")
        print(f"Name: {self.name}")
        print(f"Tax Number: {self.tax_num}")

class General(Staff):
    """Represents general staff members."""

    def __init__(self, staff_id, name, tax_num, rate_of_pay):
        super().__init__(staff_id, name, tax_num)
        self.rate_of_pay = rate_of_pay

    def calculate_pay_rate(self):
        return self.rate_of_pay

    def display_info(self):
        super().display_info()
        print(f"Pay Rate: ${self.calculate_pay_rate():.2f} per hour")

class Academic(Staff):
    """Represents academic staff/lecturers."""

    def __init__(self, staff_id, name, tax_num, publications):
        super().__init__(staff_id, name, tax_num)
        self.publications = publications

    def calculate_publications(self):
        return self.publications

    def display_info(self):
        super().display_info()
        print(f"Number of Publications: {self.calculate_publications()}")

# Create objects
student = Student("S001", "Robert Baratheon")

general_staff = General(
    "GS001",
    "Jamie Lannister",
    "TX12345",
    28.50
)

lecturer = Academic(
    "AC001",
    "Dr. Tyrion Lannister",
    "TX67890",
    12
)
# Display student information
print("===== STUDENT =====")
student.display_info()

# Display general staff information
print("\n===== GENERAL STAFF =====")
general_staff.display_info()

# Display lecturer information
print("\n===== LECTURER =====")
lecturer.display_info()