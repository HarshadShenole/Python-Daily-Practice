import json
student = [
    {"name":"rahul","marks": 80},
    {"name":"Amit","marks":90},
    {"name":"Harshad","marks":95}
]

with open("students.json","w") as file:
    json.dump(student,file)

print("Data Saved")