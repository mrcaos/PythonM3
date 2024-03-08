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