import json
students = [
    {"name":"Harshad","Marks":90},
    {"name":"shreyash","marks":80},
    {"name":"sujall","marks":70}
]

with open("students.json","w") as file:
    json.dump(students,file)

with open("students.json","r") as file:
    data = json.load(file)

print(data)