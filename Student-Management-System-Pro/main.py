from auth import login
from export_json import export_json
from student import student
from reports import student_statistics
from reports import generate_report
from backup import backup_thread 
import os
import sys
print(os.getcwd())           #Currendt Working Directory
print(os.listdir())          #Current working list    
print(sys.version)
from graph import show_graph
from database import (
    create_table,
    add_student,
    view_students,
    search_student,
    update_student,
    delete_student,
    
)

try:

    if not os.path.exists("logs"):
        os.makdir("logs")
        print("logs folder created")


    if not os.path.exists("Data"):
        os.mkdir("data")
        print("data folder created")


    if os.path.exists("data/students.db"):
        print("Database Found")

    else:
        print("Database Not Found")

    if not login():
        exit()

    create_table()

    #backup_thread.start()

    while True:

        print("\n========== STUDENT MANAGEMENT SYSTEM ==========")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Export JSON")
        print("7. student statistics")
        print("8. generate report")
        print("9. show graph")
        print("10. Exit")

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

        # ---------------- EXPORT JSON ----------------

        elif choice == "6":

            export_json()

        # ---------------- EXIT ----------------
        elif choice == "7":
            student_statistics()


        elif choice == "8":
            generate_report()


        elif choice == "9":
            show_graph()

            

        elif choice == "10":

            print("Thank You")
            break

        # ---------------- INVALID CHOICE ----------------

        else:
            print("Invalid Choice")

except Exception as e:
    print("Error:", e)

    