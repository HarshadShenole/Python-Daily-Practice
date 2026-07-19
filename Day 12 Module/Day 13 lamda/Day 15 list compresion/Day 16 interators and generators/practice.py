import json
employee = [
    {"name":"harshad","salary":100000,"Department":"Computer Science"}
]
with open("employee.json", "w") as file:
    json.dump(employee,file)

print("employee.json file created successfully")