#for each
"""
for variable in iterable
"""
#funcion range() El utimo numero no es considerado

#valor de inicio es el cero [0-10]
for i in range(10):
    print(i)#0,1,2,3,4,5,6,7,8,9
    
print("-----------------------")
# [4-10]
for i in range(4,10):
    print(i)#4,5,6,7,8,9
    
print("-----------------------")
#El tercer valor corresponde a la frecuencia [4-10]
for i in range(4,10,4):
    print(i)#4,8
    
print("-----------ejercicio------------")

for i in range(0,21,2):
    print(i)
    
for i in range(1,21,2):
    print(i+1)
    
"""print("\n"print("\n")
for num in range(1, 21): 
    if num % 2 == 0: 
        print(num)
"""
contador = 1
while contador <= 20:
    if contador% 2 == 0: 
        print(contador)
    contador+=1
    
contador = 0
while contador <= 20:
    print(contador)
    contador+=2
    
    
""" LISTAS ITERABLES """
#Lista: conjunto de datos , todo tipo de datos que conocemos,
#ordenados segun su ingreso, separados por coma
#la primera posicion o el primer elemento esta en la posicion 0
lista = [1,5,8,3,4]
print("--------LISTAS---------")
for elemento in lista:#Elemento = 8
    print(elemento)
    
print("----------STRING-------------")    
#STRING -> Objeto
texto = "hola mundo"
for caracter in texto:
    print(caracter)
    
#Tamaño de la lista es la cantidad de elementos 
opcion = ["piedra","papel","tijera"]

for opcion in opcion:
    print(opcion)
    
    
"""
DICCIONARIO { clave: valor,}
no existen la posiciones
"""

diccionario = {
    "Nombre": "Carlos",
    "Apellido": "Santana",
    "Ocupacion": "Guitarrista"
}
    
print("--------DICCIONARIO-------")

for clave in diccionario:
    print(clave)
print("") 
for clave in diccionario:
    print(f"clave {clave} - valor {diccionario[clave]}")
    
print("")    
for valor in diccionario.values():
    print(f" el valor es {valor}")
    
print("") 
for clave, valor in diccionario.items():
    print(f"clave {clave} - valor {valor}")
    
    
print("-----------------------")   
paises = ['Mexico','Chile','Argentina']
cantidad_usuarios = [70,50,55]
print({p:c for p,c in zip(paises, cantidad_usuarios)})  