import sqlite3

# Create/connect to SQLite database
connection = sqlite3.connect("college_enrollment.db")
cursor = connection.cursor()

# Enable foreign keys
cursor.execute("PRAGMA foreign_keys = ON")

# CREATE TABLES

# Student table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Student (
    student_id INTEGER PRIMARY KEY,
    nid TEXT UNIQUE NOT NULL,
    f_name TEXT NOT NULL,
    l_name TEXT NOT NULL,
    b_date TEXT,
    email TEXT,
    phone_number TEXT
)
""")
# Lecturer table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Lecturer (
    lecturer_id INTEGER PRIMARY KEY,
    l_firstname TEXT NOT NULL,
    l_lastname TEXT NOT NULL,
    l_email TEXT,
    l_address TEXT,
    l_phone TEXT
)
""")
# Course table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Course (
    course_id INTEGER PRIMARY KEY,
    course_name TEXT UNIQUE NOT NULL
)
""")
# Subjects table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Subjects (
    subject_code TEXT PRIMARY KEY,
    subject_unit INTEGER NOT NULL,
    subject_description TEXT
)
""")
# Lecture table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Lecture (
    lecture_id INTEGER PRIMARY KEY,
    lecture_name TEXT NOT NULL,
    date TEXT NOT NULL,
    time TEXT NOT NULL,
    course_id INTEGER NOT NULL,
    subject_code TEXT NOT NULL,
    lecturer_id INTEGER NOT NULL,

    FOREIGN KEY (course_id)
        REFERENCES Course(course_id),

    FOREIGN KEY (subject_code)
        REFERENCES Subjects(subject_code),

    FOREIGN KEY (lecturer_id)
        REFERENCES Lecturer(lecturer_id)
)
""")
# Enrollment table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Enrollment (
    enrollment_id INTEGER PRIMARY KEY,
    student_id INTEGER NOT NULL,
    course_id INTEGER NOT NULL,
    student_code TEXT NOT NULL,
    date_of_enrolment TEXT NOT NULL,
    enrollment_status TEXT DEFAULT 'Active',

    FOREIGN KEY (student_id)
        REFERENCES Student(student_id),

    FOREIGN KEY (course_id)
        REFERENCES Course(course_id),

    UNIQUE(student_id, course_id)
)
""")

# INSERT SAMPLE DATA

# 5 Students
students = [
    (1, "NID001", "Ahnaf", "Sami", "2001-03-15",
     "sami@example.com", "0220000001"),

    (2, "NID002", "Wadud", "Khan", "2002-07-22",
     "wadud@example.com", "0220000002"),

    (3, "NID003", "Yellow", "Brown", "2001-11-10",
     "yellow@example.com", "0220000003"),

    (4, "NID004", "Blue", "Singh", "2003-01-05",
     "blue@example.com", "0220000004"),

    (5, "NID005", "James", "Wth", "2002-09-18",
     "james@example.com", "0220000005")
]

cursor.executemany("""
INSERT OR IGNORE INTO Student
(student_id, nid, f_name, l_name, b_date, email, phone_number)
VALUES (?, ?, ?, ?, ?, ?, ?)
""", students)


# 2 Lecturers
lecturers = [
    (1, "Robert", "Stark",
     "robert.stark@example.com", "Auckland", "0211000001"),

    (2, "Spider", "Jones",
     "spider.jones@example.com", "Auckland", "0211000002")
]

cursor.executemany("""
INSERT OR IGNORE INTO Lecturer
(lecturer_id, l_firstname, l_lastname,
 l_email, l_address, l_phone)
VALUES (?, ?, ?, ?, ?, ?)
""", lecturers)


# 3 Courses
courses = [
    (1, "Master of Software Engineering"),
    (2, "Master of Information Technology"),
    (3, "Bachelor of Computer Science")
]

cursor.executemany("""
INSERT OR IGNORE INTO Course
(course_id, course_name)
VALUES (?, ?)
""", courses)


# Subjects
subjects = [
    ("SE101", 15, "Software Engineering Fundamentals"),
    ("DB102", 15, "Database Systems"),
    ("DA103", 15, "Data Analytics")
]

cursor.executemany("""
INSERT OR IGNORE INTO Subjects
(subject_code, subject_unit, subject_description)
VALUES (?, ?, ?)
""", subjects)

# Lectures
lectures = [
    (1, "Introduction to Software Engineering",
     "2026-08-03", "09:00", 1, "SE101", 1),

    (2, "Database Fundamentals",
     "2026-08-04", "10:00", 1, "DB102", 2),

    (3, "Data Analytics Basics",
     "2026-08-05", "11:00", 1, "DA103", 1),

    (4, "Introduction to IT",
     "2026-08-06", "09:00", 2, "SE101", 2),

    (5, "Database Systems",
     "2026-08-07", "10:00", 2, "DB102", 1),

    (6, "Computer Science Fundamentals",
     "2026-08-08", "11:00", 3, "DA103", 2)
]

cursor.executemany("""
INSERT OR IGNORE INTO Lecture
(lecture_id, lecture_name, date, time,
 course_id, subject_code, lecturer_id)
VALUES (?, ?, ?, ?, ?, ?, ?)
""", lectures)

# Enrolment records
enrollments = [
    (1, 1, 1, "ST001", "2026-07-27", "Active"),
    (2, 1, 2, "ST001", "2026-07-27", "Active"),

    (3, 2, 1, "ST002", "2026-07-28", "Active"),
    (4, 2, 3, "ST002", "2026-07-28", "Active"),

    (5, 3, 1, "ST003", "2026-07-29", "Active"),

    (6, 4, 2, "ST004", "2026-07-30", "Active"),

    (7, 5, 3, "ST005", "2026-07-31", "Active"),
    (8, 5, 1, "ST005", "2026-07-31", "Active")
]

cursor.executemany("""
INSERT OR IGNORE INTO Enrollment
(enrollment_id, student_id, course_id,
 student_code, date_of_enrolment, enrollment_status)
VALUES (?, ?, ?, ?, ?, ?)
""", enrollments)

# Save changes
connection.commit()

# QUESTION 1

print("\nQUESTION 1")
print("How many students are registered in each course?\n")

query1 = """
SELECT
    Course.course_name,
    COUNT(Enrollment.student_id) AS number_of_students
FROM Course
LEFT JOIN Enrollment
    ON Course.course_id = Enrollment.course_id
GROUP BY Course.course_id, Course.course_name
ORDER BY Course.course_id;
"""

cursor.execute(query1)

results = cursor.fetchall()

for course_name, number_of_students in results:
    print(course_name, ":", number_of_students, "students")

# QUESTION 2

print("\nQUESTION 2")
print("Students who have enrolled in more than one course:\n")

query2 = """
SELECT
    Student.student_id,
    Student.f_name || ' ' || Student.l_name AS student_name,
    COUNT(Enrollment.course_id) AS number_of_courses
FROM Student
JOIN Enrollment
    ON Student.student_id = Enrollment.student_id
GROUP BY
    Student.student_id,
    Student.f_name,
    Student.l_name
HAVING COUNT(Enrollment.course_id) > 1
ORDER BY Student.student_id;
"""

cursor.execute(query2)

results = cursor.fetchall()

for student_id, student_name, number_of_courses in results:
    print(
        "Student ID:", student_id,
        "| Name:", student_name,
        "| Courses:", number_of_courses
    )

# Close database connection
connection.close()

print("\nDatabase created successfully!")