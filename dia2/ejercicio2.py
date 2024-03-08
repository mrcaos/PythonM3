#La separacion de los float es un punto (.)
#la division entre integers, el resultado es un float

print(4/2) #2.0
print(5/2) #2.5
print(5/3.5)
print(2.4*4)

nombre = "juan"
año = "2024"
print(3*nombre)
print(año*2)
#print(nombre/2) no se puede dividir un string

#interpolacion de cadena (otra forma de imprimir) print(f" {nombre_variable}")
mes = 3
dia = 7

print(f"Hola {nombre}, El año es {año} del mes {mes} y el dia {dia}")

#string.format
#print("".format())
print("Hola {}, El año es {} del mes {} y el dia {}".format(nombre,año,mes,dia))

#interpolaciion con % (%s para string y %d para numeros)
print("Hola %s, El año es %s del mes %d y el dia %d" %(nombre, año, mes,dia))

#Metodo count ---> busca y cuenta cuantas veces se encuentra un caracter en un string
print("Santana".count("a"))
print(nombre.count("i"))

#Metodo upper --> todo el string en mayuscula y lower ---> todo el string a minuscula
print("Santana".upper())#SANTANA
print("Santana".lower())#santana
print(nombre.upper())#JUAN
print(nombre.lower())#juan

#Metodo title -----> solo la primera letra a mayuscula
print("12314santana".title())#12314santana

#len ----> cuenta los cracteres del string incluso los espacios
print(len(" juan Aguilera 2024"))#18

#Join ---> unir elementos sparados en un string
print(", ".join(["a","b","c"]))
print(" ".join(["Juan","Aguilera","Duhalde"]))

print("escribir\nlo\nque\nse\nme\nocurra")
"""
    escribir
    lo
    que
    se
    me
    ocurra
"""

mi_direccion =""
miDireccion =""
# cant_alum ??? ----> cantidad_alumnos--> mientras mas claro mejor
cantidas_alumnos = 30
peso = 85.5
verdadero = True

#Tipo de datos, type(nombre_variable)
print(type(nombre)) #<class 'str'>
print(type(año)) #<class 'str'>
print(type(mes)) #<class 'int'>
print(type(peso)) #<class 'float'>
print(type(verdadero)) #<class 'bool'>

type(verdadero) #no imprime el tipo de dato

numero = 2
numero = numero + 3 #numero = 2 + 3
print(numero)#5

nombre = nombre + "Aguilera" #nombre = "Juan"+"Aguilera"
print(nombre)#JuanAguilera

#precision de datos
print(5/9)#0.5555555556
print(f"resultado de la division {5/9:.2f}")
print("el resultado e la division",round(5/9,3))


nombre = input("igrese su nombre")
print("Tu nombre es",nombre)
print(f"Tu nombre es {nombre}")

edad = input("Ingrese su edad:  ")
print("Tu tienes",edad,"años")
print(type(edad)) #<class 'str'>


