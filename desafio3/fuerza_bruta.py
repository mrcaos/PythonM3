"""Actividad 3 - Fuerza bruta
Determinar cuántos intentos son necesarios para encontrar combinaciones numéricas en 
minúscula. El programa fuerza_bruta.py debe intentar todas las combinaciones de letras 
posibles, en orden alfabético, hasta que la combinación de letras sea igual a la de la 
contraseña indicada. Deberá hacer este proceso letra por letra, de izquierda a derecha
"""

from string import ascii_lowercase

abc = ascii_lowercase

password = input("ingrese la clave: ").lower()
contador = 0

for letra in password:
    for caracter in abc:
        contador += 1
        if letra == caracter:
            break

print(f"La contraseña fue forzada en:", contador, "intentos") 

        
def main():
    password_oculta = input("Ingrese la contraseña: ")
    print(f"La contraseña fue forzada en:",contador, "intentos")

if password == "gato":
    main()