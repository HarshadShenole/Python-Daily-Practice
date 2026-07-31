import numpy as np
import pandas as pd
from database import view_students


def student_statistics():
    students =  view_students()

    if not students:
        print("No Student Data Found.")
        return
    marks = []
    for student in students:
        marks.append(student[5])

    marks = np.array(marks)

    print("\n =========Student Statistics=======")

    print("Average Marks :",np.mean(marks))
    print("Highest Marks :",np.max(marks))
    print("Lowest Marks :",np.nin(marks))
    print("Median Marks :",np.median(marks))
    print("Standard Deviation :",np.std(marks))


def generate_report():
    students = view_students()

    if not students:
        print("No Student Data Found.")
        return 

    df = pd.DataFrame(
        students,
        columns=[
            "Roll No",
            "Name",
            "Age",
            "Email",
            "Course",
            "Marks"
        ]
    )

    print("\n ======Student Report======")
    print(df)

    topper = df[df["Marks"] == df["Marks"].max()]

    print("\n===== Topper ========")
    print(topper)


    failed = df[df["Marks"]<35]
    print("\n=====Failed Students=======")
    print(failed)

    df.to_csv("Student_report.csv",index=False)
