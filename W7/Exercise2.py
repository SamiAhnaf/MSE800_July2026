"""Exercise 2 
A university wants to develop a student information system. Every person in the university has a 
name. A student is a person and has an additional student ID. A postgraduate student is a student 
and has an additional research topic. Design and implement suitable Python classes for this 
system. Create a postgraduate student object and display the person's name, student ID, and 
research topic. Use super() where appropriate. """

class Person:
    def __init__(self, name):
        self.name = name
class Student(Person):
    def __init__(self, name, student_id):
        super().__init__(name)
        self.student_id = student_id
class PostgraduateStudent(Student):
    def __init__(self, name, student_id, research_topic):
        super().__init__(name, student_id)
        self.research_topic = research_topic

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Student ID: {self.student_id}")
        print(f"Research Topic: {self.research_topic}")

student_sami = PostgraduateStudent("Ahanf", "S01", "Professional Software Engineering")
student_sami.display_details()
