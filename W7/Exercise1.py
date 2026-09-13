"""Exercise 1 
A company wants to develop a simple employee management system. The system should store an 
employee's name and employee ID. A manager is also an employee, but a manager has additional 
information about the department they manage. Create suitable Python classes to represent this 
relationship. Use a constructor to initialise the required information and create a manager object 
to display all the details. """

class Employee:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id
class Manager(Employee):
    def __init__(self, name, employee_id, department):
        super().__init__(name, employee_id)
        self.department = department

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Employee ID: {self.employee_id}")
        print(f"Department: {self.department}")

manager_sami = Manager("Sami", "E123", "IT")
manager_sami.display_details()