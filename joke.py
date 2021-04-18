import requests

url = "https://api.icndb.com/jokes/random"

payload={}
headers = {
  'Accept': 'application/json'
}

response = requests.request("GET", url, headers=headers, data=payload)

print("Here is your joke!")
print(response.text)
