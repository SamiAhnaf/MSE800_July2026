"""Exercise 6 
Design a small real-world system of your choice, such as a hospital, banking system, university, 
online shopping system, or transport system. Your system should contain at least four classes and 
demonstrate at least two different types of inheritance. Draw the class diagram first and then 
implement the classes in Python. Use constructors, inheritance, super(), and appropriate 
methods. Finally, create objects and demonstrate that the inheritance relationships work correctly."""

class Person:
    def __init__(self, name):
        self.name = name

    def display_name(self):
        print(f"Name: {self.name}")

class Student(Person):
    def __init__(self, name, student_id):
        super().__init__(name)
        self.student_id = student_id

    def display_student(self):
        print(f"Name: {self.name}")
        print(f"Student ID: {self.student_id}")


class PostgraduateStudent(Student):
    def __init__(self, name, student_id, research_topic):
        super().__init__(name, student_id)
        self.research_topic = research_topic

    def display_postgraduate(self):
        print(f"Name: {self.name}")
        print(f"Student ID: {self.student_id}")
        print(f"Research Topic: {self.research_topic}")


class Lecturer(Person):
    def __init__(self, name, employee_id, subject):
        super().__init__(name)
        self.employee_id = employee_id
        self.subject = subject

    def display_lecturer(self):
        print(f"Name: {self.name}")
        print(f"Employee ID: {self.employee_id}")
        print(f"Teaching Subject: {self.subject}")


student1 = Student("John", "S1001")

postgraduate1 = PostgraduateStudent(
    "Sami",
    "S1002",
    "Artificial Intelligence"
)

lecturer1 = Lecturer(
    "Ahnaf",
    "E2001",
    "Software Engineering"
)


print("Student Details")
student1.display_student()

print("\nPostgraduate Student Details")
postgraduate1.display_postgraduate()

print("\nLecturer Details")
lecturer1.display_lecturer()