import requests
from string import Template

html_template = Template("""
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Aves de Chile</title>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="author" content="Juan Aguilera">
    <meta name="description" content="Descubriendo las Aves de Chile">
    <meta name="keywords" content="Visitando los cielos de Chile">
    <link rel="shortcut icon" type="image/png" href="./assets/img/bird.png">
    <link href="https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,100;0,300;0,400;0,500;0,700;0,900;1,100;1,300;1,400;1,500;1,700;1,900&display=swap" rel="stylesheet">
    <style>
        body {
            background-color: green;
            color: black;
            font-family: "Roboto", sans-serif;
        }
    </style>
</head>

<body>                         

$body

</body>

</html>  

""")

elementos_template = Template('''<h2><u>Nombre Ave Español:</u> $nombre_espaniol</h2>
                            <h2><u>Nombre Ave Ingles:</u> $nombre_ingles</h2>
                            <img src="$url">
                            ''')

def request_get(url):
    return requests.get(url).json()

def build_html(url):
    response = request_get(url)
    texto =''
    
    for aves in response:
        nombre_esp = aves['name']['spanish']
        nombre_eng = aves['name']['english']
        imagen_url = aves['images']['main']
        texto += elementos_template.substitute(nombre_espaniol=nombre_esp, nombre_ingles=nombre_eng, url=imagen_url)
    return html_template.substitute(body=texto)
    
html = build_html('https://aves.ninjas.cl/api/birds')
with open('aves_chile.html', 'w') as f:
    f.write(html)