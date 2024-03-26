import sys

precios = { 
    "Notebook": 700000,
    "Teclado": 25000,
    "Mouse": 12000,
    "Monitor": 250000,
    "Escritorio": 135000,
    "Tarjeta de Video": 1500000
}

filtro = ""

if len(sys.argv) < 3:
    umbral = int(sys.argv[1])
else:
    umbral = int(sys.argv[1])
    filtro = sys.argv[2]

def fil():
    if filtro == "mayor" or filtro == "":
        mayor_umbral = ', '.join(list({k for k , v in precios.items() if v > umbral }))
        print(f"Los productos mayores al umbral son: {mayor_umbral}")
    elif filtro == "menor":
        menor_umbral = ', '.join(list({k for k , v in precios.items() if v < umbral }))
        print(f"Los productos menores al umbral son: {menor_umbral}")
    else:
        print("Lo sentimos, no es una operacion valida")
fil()