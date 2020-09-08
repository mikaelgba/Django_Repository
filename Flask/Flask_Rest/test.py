import requests

BASE = "http://127.0.0.1:5000/"

response = requests.get(BASE + "helloworld/Michael")
print(response.json())

response = requests.get(BASE + "helloworld/Belle Delphine")
print(response.json())