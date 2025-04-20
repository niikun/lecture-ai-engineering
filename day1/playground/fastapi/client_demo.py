import requests
import json

# res = requests.get("http://localhost:8000/0")
# print(res.status_code)
# print(res.json())

res = requests.post("http://localhost:8000/items", 
                    json={"name": "hat",
                          "price":"1500",
                          "description":"straw hat"})
print(res.status_code)
print(res.json())