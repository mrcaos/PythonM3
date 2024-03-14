"""
Determinar si un numero ingresado por el usuario
es par o impar
utilizaremso el modulo    
"""

#Paso 1: solicitud de igreso de datos
numero = input("Ingresa numero a evaluar\n")

#Paso 2: transformar string a numeros
numero = int(numero)

#Paso 3: evaluar con las condiciones
if numero == 0:
    print("El numero ingresado es cero")
elif numero%2 == 0: 
    print("El numero ingresado es par")
else:
    print("El numero ingresado es impar")
    
# 0/2 = 0
0
#-35/2 = -17
1
