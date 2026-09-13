"""Exercise 3 
A university employs different types of employees. All employees have a name and employee ID. 
However, lecturers have a teaching subject, administrators have a department, and technicians 
have a technical specialisation. Create suitable Python classes to represent these employees. 
Create objects for a lecturer, administrator, and technician and display their information."""

class Employee:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

class Lecturer(Employee):
    def __init__(self, name, employee_id, teaching_subject):
        super().__init__(name, employee_id)
        self.teaching_subject = teaching_subject
    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Employee ID: {self.employee_id}")
        print(f"Teaching Subject: {self.teaching_subject}")

class Administrator(Employee):
    def __init__(self, name, employee_id, department):
        super().__init__(name, employee_id)
        self.department = department
    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Employee ID: {self.employee_id}")
        print(f"Department: {self.department}")

class Technician(Employee):
    def __init__(self, name, employee_id, technical_specialisation):
        super().__init__(name, employee_id)
        self.technical_specialisation = technical_specialisation
    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Employee ID: {self.employee_id}")
        print(f"Technical Specialisation: {self.technical_specialisation}")

lecturer_sami = Lecturer("Sami", "E1001", "Professional Software Engineering")
administrator_wadud = Administrator("Wadud", "E1002", "Administrative Services")
technician_syed = Technician("Syed", "E1003", "IT Support")


lecturer_sami.display_details()
print()

administrator_wadud.display_details()
print()

technician_syed.display_details()