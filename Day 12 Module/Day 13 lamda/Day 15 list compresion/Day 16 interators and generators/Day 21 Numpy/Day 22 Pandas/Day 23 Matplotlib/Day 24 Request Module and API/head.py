import requests
headers = {
        "User-Agent":"Python App"
    }
response = requests.get(
    "http:/httpbin.org/get",
    headers = headers
)

print(response.json)
