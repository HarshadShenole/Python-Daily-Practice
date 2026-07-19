import requests
data = {
    "name":"Harshad",
    "age":22

}
response = requests.post(
    "http://httpbin.org/post",
    json = data
)
print(response.json())