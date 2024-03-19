"""ventas = {
    "Enero": 15000,
    "Febrero": 22000,
    "Marzo": 12000,
    "Abril": 17000,
    "Mayo": 81000,
    "Junio": 13000,
    "Julio": 21000,
    "Agosto": 41200,
    "Septiembre": 25000,
    "Octubre": 21500,
    "Noviembre": 91000,
    "Diciembre": 21000,
}

Actividad 1 - Filtrado compacto
Se solicita devolver un informe resumido que exponga los meses que superan un cierto 
umbral. El programa mayor_a.py debe retornar un diccionario con el mes y el valor asociado 
siempre y cuando superen el umbral especificado.
"""

meses_umbral = ["Mayo","Agosto","Noviembre"]
ventas_mes_umbral = [81000,41200,91000]
print({m:v for m,v in zip(meses_umbral, ventas_mes_umbral)})