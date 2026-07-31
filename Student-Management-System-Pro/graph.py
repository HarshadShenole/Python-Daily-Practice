import matplotlib.pyplot as plt
from database import view_students


def show_graph():
    students = view_students()

    name = []
    marks= []


    for student in students:
        name.append(student[1])
        marks.append(student[5])


    plt.bar(name,marks)

    plt.title("Student Marks")

    plt.xlabel("Students")

    plt.ylabel("Marks")

    plt.show()
