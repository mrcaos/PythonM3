"""
Actividad 1 - IMC
El IMC, conocido también como el Índice de masa corporal, es una medida que asocia el
peso de una persona con su talla (su altura). Este valor es utilizado normalmente como un
indicador nutricional y constituye un índice fácil y sencillo de calcular para determinar el
estado de obesidad y sobrepeso de una persona. El IMC se calcula de la siguiente manera:
    IMC=W/H^2

"""

pesoKilogramo = float(input("Ingrese su peso en kg: \n"))
alturaMetros = float(input("Ingrese su altura en m: \n"))

indiceMasaCorporal = float(pesoKilogramo/alturaMetros**2)
print("Su IMC es ", pesoKilogramo/alturaMetros**2)


if indiceMasaCorporal < 18.5:
    print("La clasificacion OMS es Bajo Peso")
elif indiceMasaCorporal >= 18.5 and indiceMasaCorporal < 25:
    print("La clasificacion OMS es Adecuado")
elif indiceMasaCorporal >= 25 and indiceMasaCorporal < 30:
    print("La clasificacion OMS es Sobrepeso")
elif indiceMasaCorporal >= 30 and indiceMasaCorporal < 35:
    print("La clasificacion OMS es Obesidad Grado I")
elif indiceMasaCorporal >= 35 and indiceMasaCorporal < 40:
    print("La clasificacion OMS es Obesidad Grado II")
elif indiceMasaCorporal >= 40:
    print("La clasificacion OMS es Obesidad Grado III")
    
    
    
"""
OPTIMIZACION

import sys
# se ejecuta en la terminal: python3 desafio2/imc.py 81 178
print(sys.argv)     #['desafio2/imc.py', '81', '178']
print(sys.argv[1])  #81
print(sys.argv[2])  #178

peso_kilogramos= float(sys.argv[1])
estatura = float(sys.argv[2])/100

print(type(peso_kilogramos))
print(type(estatura))

#calculo del imc
#imc = peso_kilogramos/ (estatura * estatura)
imc = peso_kilogramos/ (estatura ** 2 )
print(f"Tu IMC es de {round(imc,2)}")
#print(f"Tu IMC es de {imc:.2}")

if imc < 18.5:
    clasificacion = "Bajo Peso"
elif imc >=18.5 and imc < 25:
    clasificacion = "Adecuado"
elif imc < 30:
    clasificacion = "Sobrepeso"
elif imc < 35:
    clasificacion = "Obesidad grado I"
elif imc < 40:
    clasificacion = "Obesidad grado II"
elif imc >=40:
    clasificacion = "Obesidad grado III"

print(f"Tu clasificación según la OMS es: {clasificacion}")

"""