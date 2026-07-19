import json
student = {
    "name" : "Harshad",
    "age": 21
}

with open("student.json", "w") as file:
    json.dump(student,file)