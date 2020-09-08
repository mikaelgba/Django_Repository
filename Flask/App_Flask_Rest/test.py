import requests

BASE = "http://127.0.0.1:5000/"


data = [{"name":"test A", "link": "abc", "views":1000, "likes":111},
        {"name":"test B", "link": "def", "views":2000, "likes":222},
        {"name":"test C", "link": "ghi", "views":3000, "likes":333}]

for i in range (len(data)):
    response = requests.put(BASE + "video/" + str(i), data[i])
    print(response.json())

input()
response = requests.get(BASE + "video/1")
print(response.json())
