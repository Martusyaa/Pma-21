import requests
import json

base_url = 'http://127.0.0.1:5000/assets'

response = requests.get(base_url)
print("GET Response:", response.json())

new_asset = {
    "id": 4,
    "name": "Oil",
    "quantity": 150,
    "price": 60
}
response = requests.post(base_url, json=new_asset)
print("POST Response:", response.json())

update_data = {
    "quantity": 200,
    "price": 65
}
update_url = base_url + '/4'
response = requests.patch(update_url, json=update_data)
print("PATCH Response:", response.json())

delete_url = base_url + '/4'
response = requests.delete(delete_url)
print("DELETE Response:", response.json())
