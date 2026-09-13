class Student:
    def __init__(self, full_name, age, address, student_id):

        self.full_name = full_name #String

        self.age = age #Integer

        self.address = address #String

        self.student_id = student_id #String

    def display(self): # Display the information of one student.
        print(
            f"Name: {self.full_name}, "
            f"Age: {self.age}, "
            f"Address: {self.address}, "
            f"Student ID: {self.student_id}"
        )


def main():
    number_of_students = int(input("Enter the number of students: "))    # Ask how many students the user wants to enter.

    students = []     # A list is used to store multiple Student objects.

    for i in range(number_of_students): # Loop to collect information for each student.
        print(f"\nEnter information for student {i + 1}")

        full_name = input("Full name: ") 

        age = int(input("Age: ")) 

        address = input("Address: ")

        student_id = input("Student ID: ") # Student ID is stored as a string because IDs may contain leading zeros or letters.

        student = Student(full_name, age, address, student_id) #create a new Student object

        students.append(student)  # Add the Student object to the list.

    students.sort(key=lambda student: student.age)     # Sort the list of Student objects by age in ascending order.

    print("\n===== Students Sorted by Age =====")

    for student in students: # Loop through the sorted list and display each student's information.
        student.display()


if __name__ == "__main__":
    main()