import re

FILE_NAME = "students.txt"


def validate_email(email):
    pattern = r'^[\w.-]+@[\w.-]+\.\w+$'
    return re.match(pattern, email)


def read_students():
    try:
        with open(FILE_NAME, "r") as file:
            students = file.readlines()

        if not students:
            print("\nNo student records found.")
            return

        print("\n----- Student Records -----")

        for line in students:
            line = line.strip()

            if line:
                data = line.split(",")

                if len(data) == 3:
                    roll_no, name, email = data
                    print("Roll Number :", roll_no)
                    print("Name        :", name)
                    print("Email       :", email)
                    print("---------------------------")

    except FileNotFoundError:
        print("\nStudent file not found.")


def add_student():
    try:
        roll_no = int(input("Enter Roll Number: "))
        name = input("Enter Student Name: ")
        email = input("Enter Email: ")

        if not validate_email(email):
            raise ValueError("Invalid email format.")

        with open(FILE_NAME, "a") as file:
            file.write(f"{roll_no},{name},{email}\n")

        print("\nStudent added successfully.")

    except ValueError as e:
        print("\nError:", e)


def find_student():
    try:
        roll_no = input("Enter Roll Number to search: ")

        with open(FILE_NAME, "r") as file:
            students = file.readlines()

        found = False

        for line in students:
            line = line.strip()

            if line:
                data = line.split(",")

                if len(data) == 3:
                    student_roll, name, email = data

                    if student_roll == roll_no:
                        print("\n----- Student Found -----")
                        print("Roll Number :", student_roll)
                        print("Name        :", name)
                        print("Email       :", email)
                        found = True
                        break

        if not found:
            print("\nStudent not found.")

    except FileNotFoundError:
        print("\nStudent file not found.")


def menu():
    while True:
        print("\n========== STUDENT RECORD MANAGER ==========")
        print("1. Add Student")
        print("2. Read Student Data")
        print("3. Find Student Using Roll Number")
        print("4. Exit")
        print("============================================")

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                add_student()

            elif choice == 2:
                read_students()

            elif choice == 3:
                find_student()

            elif choice == 4:
                print("\nProgram exited successfully.")
                break

            else:
                raise ValueError("Please enter a number between 1 and 4.")

        except ValueError as e:
            print("\nInvalid input:", e)


menu()