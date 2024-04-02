import requests
import json

url = "https://reqres.in/users"

request = requests.request("GET", url, headers={}, data={})
users_data = json.load(request.text)
print(users_data)
print(request)

data_ignacio = {
    "nombre: Ignacio",
    "trabajo: Profesor"
}
created_user = requests.post(url, json=data_ignacio)
print(created_user.text)
print(created_user)

data_user = {
    "residence": "zion"
}
response = requests.put("https://reqres.in/api/users/2", json=updated_user_data)
update_user = response.json()
print(update_user.text)
print(update_user)

Tracey = requests.delete("https://reqres.in/api/users/4")
print(Tracey)
