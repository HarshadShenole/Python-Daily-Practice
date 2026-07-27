from auth import login
from export_json import export_json
from student import student
from database import (
    create_table,
    add_student,
    view_students,
    search_student,
    update_student,
    delete_student
)
if not login():
    exit()

create_table()

while True:

    print("\n========== STUDENT MANAGEMENT SYSTEM ==========")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. export JSON")
    print("7. Exit")

    choice = input("\nEnter Your Choice: ")

    # ---------------- ADD STUDENT ----------------

    if choice == "1":

        roll = int(input("Enter Roll No: "))
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        email = input("Enter Email: ")
        course = input("Enter Course: ")
        marks = float(input("Enter Marks: "))

        student1 = student(
            roll,
            name,
            age,
            email,
            course,
            marks
        )

        add_student(student1)

    # ---------------- VIEW STUDENTS ----------------

    elif choice == "2":

        students = view_students()

        print("\n------ Student List ------")

        for student_data in students:
            print(f"""
Roll No : {student_data[0]}
Name    : {student_data[1]}
Age     : {student_data[2]}
Email   : {student_data[3]}
Course  : {student_data[4]}
Marks   : {student_data[5]}

---------------------------------------
""")

    # ---------------- SEARCH STUDENT ----------------

    elif choice == "3":

        roll = int(input("Enter Roll Number to Search: "))

        student_data = search_student(roll)

        if student_data:
            print("\nStudent Found")
            print("-----------------------")
            print("Roll No :", student_data[0])
            print("Name    :", student_data[1])
            print("Age     :", student_data[2])
            print("Email   :", student_data[3])
            print("Course  :", student_data[4])
            print("Marks   :", student_data[5])
        else:
            print("Student Not Found")

    # ---------------- UPDATE STUDENT ----------------

    elif choice == "4":

        roll = int(input("Enter Roll Number to Update: "))

        student_data = search_student(roll)

        if student_data:

            print("\nEnter New Details")

            name = input("Name: ")
            age = int(input("Age: "))
            email = input("Email: ")
            course = input("Course: ")
            marks = float(input("Marks: "))

            updated_student = student(
                roll,
                name,
                age,
                email,
                course,
                marks
            )

            update_student(updated_student)

        else:
            print("Student Not Found")

    # ---------------- DELETE STUDENT ----------------

    elif choice == "5":

        roll = int(input("Enter Roll Number to Delete: "))

        student_data = search_student(roll)

        if student_data:
            delete_student(roll)
        else:
            print("Student Not Found")

    elif choice =="6":
        export_json()
        

     # ---------------- EXIT ----------------

    elif choice == "7":
        
        print("Thank You")
        break

    # ---------------- INVALID CHOICE ----------------

    else:
        print("Invalid Choice")