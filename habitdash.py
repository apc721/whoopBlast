import requests

url = "https://api.habitdash.com/v1/fields/"

headers = {
    "accept": "application/json",
    "x-api-key": "PUT_API_KEY_HERE"
}

response = requests.request("GET", url, headers=headers)

print(response.text)
