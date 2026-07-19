import requests
params = {
    "city": "pune"
}

response = requests.get("https://api.github.com/search/repositories",params=params )

print(response.url)