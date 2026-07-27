import json
from database import view_students

def export_json():
    students = view_students()

    data = []

    for student in students :
        data.append({
            "roll_no": student[0],
            "name":student[1],
            "age":student[2],
            "email":student[3],
            "course": student[4],
            "mark":student[5]
        })

        with open("students.json","w") as file :
            json.dump(data,file,indent = 4)


        print("Data Export Succesful")