#string ------> cadena de caracteres (se escriben entre comillas)
nombre = "Juan"
apellido1 = "Aguilera"
apellido2 = "Duhalde"
edad = "38"
año = 2024 #es un numero

#pyhton no permite sumar letras con numeros 
#suma de string = concatenar

print(nombre+apellido1+apellido2)
print("vvv     "+nombre+"     vvv")
print("vvv    "+apellido1+"   vvv")
print("vvv    "+apellido2+"    vvv")
print("vv       "+edad+"      vv")

#La edad continuara si es que no se modifica, si se modifica
#cambia desde la line que se agego una nueva.
edad = 40



edad = 45.5

print(edad)


edad = 50

#comillas simples resalta string dentr de ""
print("tu nombre ‘es’ " + nombre)


print("tu nombre es " + nombre )
print("tu apellido es " + apellido1)
print("el año es ",año)


#imprimiendo string y numeros en una misma linea
print("el año es ",año," mes ",3," dia ",7)


#Interpolacion de cadenas (otra forma de imprimir)
#se interpreta con la letra (f"")
mes = 3
dia = 7

print(f"El año es {año} del mes {mes} y el dia {dia}")