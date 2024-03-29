import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

response = requests.get(url)

print(response)

if response.status_code == 200:
    print("Obtencion Correcta")
    print(response.json())
    print("")
    post = response.json()
    print(post("title"))
else:
    print("Error en el solicitud")