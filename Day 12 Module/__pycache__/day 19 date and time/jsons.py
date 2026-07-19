import json
student = {
    "name":"Harshad",
    "age":21
}
result = json.dumps(student)
print(result)
print(type(result))