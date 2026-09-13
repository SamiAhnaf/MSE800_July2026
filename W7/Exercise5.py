"""Exercise 5 
A hospital wants to develop a system to manage information about its staff and patients. Every 
person in the hospital has a name. A doctor is a person and has a doctor ID, while a nurse is also a 
person and has a nurse ID. A senior nurse can have both the characteristics of a nurse and 
additional information related to their role, such as a ward they supervise. Design and implement 
suitable Python classes to represent these relationships. Create a SeniorNurse object and display 
all relevant information. Use constructors and super() where appropriate. Finally, identify the type 
of inheritance used and draw a class diagram before implementing the solution. """

class Person:
    def __init__(self, name):
        self.name = name

class Doctor(Person):
    def __init__(self, name, doctor_id):
        super().__init__(name)
        self.doctor_id = doctor_id

class Nurse(Person):
    def __init__(self, name, nurse_id):
        super().__init__(name)
        self.nurse_id = nurse_id

class SeniorNurse(Nurse):
    def __init__(self, name, nurse_id, ward):
        super().__init__(name, nurse_id)
        self.ward = ward

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Nurse ID: {self.nurse_id}")
        print(f"Supervised Ward: {self.ward}")

senior_nurse1 = SeniorNurse(
    "Teresa",
    "N1001",
    "Emergency Ward"
)

senior_nurse1.display_details()