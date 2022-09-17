from urllib import response
import requests

BASE = "HTTP://127.0.0.1:5000/"

response = requests.get(BASE + "video/3", {"likes":10, "name": "andrea", "views": 10})
print(response.json())