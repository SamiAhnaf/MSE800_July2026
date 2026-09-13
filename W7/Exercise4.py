"""Exercise 4 
A university needs to maintain information about students from two different areas: academic 
information and contact information. Academic information includes the student's programme 
and GPA, while contact information includes the student's email address and phone number. 
Create suitable Python classes so that a student can have information from both areas. Create a 
student object and display all of the student's academic and contact information."""

class AcademicInfo:
    def __init__(self, programme, gpa):
        self.programme = programme
        self.gpa = gpa

class ContactInfo:
    def __init__(self, email, phone_number):
        self.email = email
        self.phone_number = phone_number

class Student(AcademicInfo, ContactInfo):
    def __init__(self, name, programme, gpa, email, phone_number):
        self.name = name

        AcademicInfo.__init__(self, programme, gpa)
        ContactInfo.__init__(self, email, phone_number)

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Programme: {self.programme}")
        print(f"GPA: {self.gpa}")
        print(f"Email: {self.email}")
        print(f"Phone Number: {self.phone_number}")


student1 = Student(
    "Sami",
    "Software Engineering",
    3.8,
    "sami@email.com",
    "0123456789"
)

student1.display_details()