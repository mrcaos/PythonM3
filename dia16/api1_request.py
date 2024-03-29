import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)


"""Una API REST es una interfaz de comunicación entre sistemas de información que 
usa el protocolo de transferencia de hipertexto (HTTP).
"""