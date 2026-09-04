class Course:
    def __init__(self, course_id, course_name, credits, lecturer):
        self.course_id = course_id
        self.course_name = course_name
        self.credits = credits
        self.lecturer = lecturer
        self.students = []

    def addStudent(self, student):
        if student not in self.students:
            self.students.append(student)

    def removeStudent(self, student):
        if student in self.students:
            self.students.remove(student)

    def viewStudents(self):
        if not self.students:
            print("\nNo students are enrolled in this course.")
            return

        print(f"\nStudents enrolled in {self.course_name}:")
        for student in self.students:
            print(f"{student.student_id} - {student.name}")


class Student:
    def __init__(self, student_id, name, email, programme):
        self.student_id = student_id
        self.name = name
        self.email = email
        self.programme = programme
        self.courses = []

    def enrollCourse(self, course):
        if course in self.courses:
            print("\nYou are already enrolled in this course.")
            return

        self.courses.append(course)
        course.addStudent(self)
        print(f"\nSuccessfully enrolled in {course.course_name}.")

    def viewCourses(self):
        if not self.courses:
            print("\nYou are not enrolled in any courses.")
            return

        print("\nMy Enrollments:")
        for course in self.courses:
            print(
                f"{course.course_id} - {course.course_name} "
                f"({course.credits} credits)"
            )

    def viewLecturer(self, course):
        print(f"\nCourse: {course.course_name}")
        print(f"Lecturer: {course.lecturer.name}")
        print(f"Email: {course.lecturer.email}")


class Lecturer:
    def __init__(self, lecturer_id, name, email, specialization):
        self.lecturer_id = lecturer_id
        self.name = name
        self.email = email
        self.specialization = specialization
        self.courses = []

    def teachCourse(self, course):
        if course not in self.courses:
            self.courses.append(course)

    def viewStudents(self):
        if not self.courses:
            print("\nYou currently have no courses.")
            return

        for course in self.courses:
            course.viewStudents()

    def updateCourse(self, course):
        print("\nUpdate Course")

        new_name = input(
            f"Course name [{course.course_name}]: "
        ).strip()

        new_credits = input(
            f"Credits [{course.credits}]: "
        ).strip()

        if new_name:
            course.course_name = new_name

        if new_credits:
            try:
                course.credits = int(new_credits)
            except ValueError:
                print("Invalid credits. Existing value kept.")

        print("\nCourse updated successfully.")


class CollegeManagementSystem:
    def __init__(self):
        self.lecturers = []
        self.students = []
        self.courses = []

        self.setup_data()

    def setup_data(self):
        lecturer = Lecturer(
            1,
            "Mohammad Norouzifard",
            "lecturer@college.com",
            "Software Engineering"
        )

        student = Student(
            1,
            "Student",
            "student@college.com",
            "Master of Software Engineering"
        )

        self.lecturers.append(lecturer)
        self.students.append(student)

        course1 = Course(
            101,
            "Software Engineering",
            15,
            lecturer
        )

        course2 = Course(
            102,
            "Data Analytics",
            15,
            lecturer
        )

        self.courses.append(course1)
        self.courses.append(course2)

        lecturer.teachCourse(course1)
        lecturer.teachCourse(course2)

    def login(self):
        print("=" * 45)
        print("       COLLEGE MANAGEMENT SYSTEM")
        print("=" * 45)

        while True:
            print("\nLogin As")
            print("1. Lecturer")
            print("2. Student")
            print("3. Exit")

            choice = input("\nSelect an option: ").strip()

            if choice == "1":
                self.lecturerLogin()

            elif choice == "2":
                self.studentLogin()

            elif choice == "3":
                print("\nGoodbye!")
                break

            else:
                print("\nInvalid option. Please try again.")

    def lecturerLogin(self):
        email = input("\nLecturer Email: ").strip()

        for lecturer in self.lecturers:
            if lecturer.email.lower() == email.lower():
                print(f"\nLogin successful. Welcome {lecturer.name}!")
                self.lecturerDashboard(lecturer)
                return

        print("\nInvalid lecturer credentials.")

    def studentLogin(self):
        email = input("\nStudent Email: ").strip()

        for student in self.students:
            if student.email.lower() == email.lower():
                print(f"\nLogin successful. Welcome {student.name}!")
                self.studentDashboard(student)
                return

        print("\nInvalid student credentials.")

    def lecturerDashboard(self, lecturer):
        while True:
            print("\n" + "=" * 40)
            print("LECTURER DASHBOARD")
            print("=" * 40)

            print("1. Create Course")
            print("2. Upload/View My Courses")
            print("3. Update Course")
            print("4. Delete Course")
            print("5. View Enrolled Students")
            print("6. Logout")

            choice = input("\nSelect activity: ").strip()

            if choice == "1":
                self.createCourse(lecturer)

            elif choice == "2":
                self.viewLecturerCourses(lecturer)

            elif choice == "3":
                self.selectCourseToUpdate(lecturer)

            elif choice == "4":
                self.deleteCourse(lecturer)

            elif choice == "5":
                lecturer.viewStudents()

            elif choice == "6":
                print("\nLogged out successfully.")
                break

            else:
                print("\nInvalid option.")

    def createCourse(self, lecturer):
        print("\nCreate Course")

        try:
            course_id = int(input("Course ID: "))
            credits = int(input("Credits: "))
        except ValueError:
            print("\nCourse ID and credits must be numbers.")
            return

        for course in self.courses:
            if course.course_id == course_id:
                print("\nCourse ID already exists.")
                return

        course_name = input("Course Name: ").strip()

        new_course = Course(
            course_id,
            course_name,
            credits,
            lecturer
        )

        self.courses.append(new_course)
        lecturer.teachCourse(new_course)

        print("\nCourse created successfully.")

    def viewLecturerCourses(self, lecturer):
        if not lecturer.courses:
            print("\nNo courses available.")
            return

        print("\nMy Courses:")

        for course in lecturer.courses:
            print(
                f"{course.course_id} - "
                f"{course.course_name} - "
                f"{course.credits} credits"
            )

    def selectCourseToUpdate(self, lecturer):
        self.viewLecturerCourses(lecturer)

        if not lecturer.courses:
            return

        try:
            course_id = int(input("\nEnter Course ID to update: "))
        except ValueError:
            print("\nInvalid Course ID.")
            return

        for course in lecturer.courses:
            if course.course_id == course_id:
                lecturer.updateCourse(course)
                return

        print("\nCourse not found.")

    def deleteCourse(self, lecturer):
        self.viewLecturerCourses(lecturer)

        if not lecturer.courses:
            return

        try:
            course_id = int(input("\nEnter Course ID to delete: "))
        except ValueError:
            print("\nInvalid Course ID.")
            return

        for course in lecturer.courses:
            if course.course_id == course_id:

                for student in course.students:
                    if course in student.courses:
                        student.courses.remove(course)

                lecturer.courses.remove(course)
                self.courses.remove(course)

                print("\nCourse deleted successfully.")
                return

        print("\nCourse not found.")

    def studentDashboard(self, student):
        while True:
            print("\n" + "=" * 40)
            print("STUDENT DASHBOARD")
            print("=" * 40)

            print("1. View Available Courses")
            print("2. View Course Details")
            print("3. Enroll in a Course")
            print("4. View My Enrollments")
            print("5. Logout")

            choice = input("\nSelect activity: ").strip()

            if choice == "1":
                self.viewAllCourses()

            elif choice == "2":
                self.viewCourseDetails()

            elif choice == "3":
                self.enrollStudent(student)

            elif choice == "4":
                student.viewCourses()

            elif choice == "5":
                print("\nLogged out successfully.")
                break

            else:
                print("\nInvalid option.")

    def viewAllCourses(self):
        if not self.courses:
            print("\nNo courses are currently available.")
            return

        print("\nAvailable Courses:")

        for course in self.courses:
            print(
                f"{course.course_id} - "
                f"{course.course_name} - "
                f"{course.credits} credits"
            )

    def findCourse(self, course_id):
        for course in self.courses:
            if course.course_id == course_id:
                return course

        return None

    def viewCourseDetails(self):
        self.viewAllCourses()

        if not self.courses:
            return

        try:
            course_id = int(input("\nEnter Course ID: "))
        except ValueError:
            print("\nInvalid Course ID.")
            return

        course = self.findCourse(course_id)

        if course:
            print("\nCourse Details")
            print("-" * 30)
            print(f"Course ID: {course.course_id}")
            print(f"Course Name: {course.course_name}")
            print(f"Credits: {course.credits}")
            print(f"Lecturer: {course.lecturer.name}")
        else:
            print("\nCourse not found.")

    def enrollStudent(self, student):
        self.viewAllCourses()

        if not self.courses:
            return

        try:
            course_id = int(
                input("\nEnter Course ID to enroll: ")
            )
        except ValueError:
            print("\nInvalid Course ID.")
            return

        course = self.findCourse(course_id)

        if course:
            student.enrollCourse(course)
        else:
            print("\nCourse is not available.")


if __name__ == "__main__":
    system = CollegeManagementSystem()
    system.login()