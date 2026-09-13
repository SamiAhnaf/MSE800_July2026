is_logged_in = True  # Change this to True to simulate a logged-in user


def login_required(func):
    def wrapper():
        if is_logged_in:
            func()
        else:
            print("Access Denied. Please log in first.")

    return wrapper


@login_required
def view_salary():
    print("Salary: $5,000")


@login_required
def view_personal_details():
    print("Name: John Smith")
    print("Department: IT")


@login_required
def download_report():
    print("Employee report downloaded successfully.")


view_salary()
view_personal_details()
download_report()