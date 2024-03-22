from os import system

tupla_eje = ("Marzo","2024")
print(tupla_eje)
print(type(tupla_eje))#<class 'tuple'>

#Desempaquetamiento
mes, anio = tupla_eje
print(mes)
print(anio)

tupla2 = 3,5,(1,11),7,9
print(type(tupla2))#<class 'tuple'>
#corchetes [PARA LAS LISTAS],  #Llaves {PARA DICCIOARIOS}
print(tupla2)

lista_vocales = ["a","e","i","o","u","a","a","a"]
print(lista_vocales)#['a', 'e', 'i', 'o', 'u']
tupla_vocales = tuple(lista_vocales)
print(tupla_vocales)#('a', 'e', 'i', 'o', 'u')

#Iterar una tuple
for tv in tupla_vocales:
    print(tv)
#Count, cuenta las veces que se encentra un elemento en la tupla
print(tupla_vocales.count("a"))

system("clear")
list_dicc=list({"k1": 5, "k2": 7}.items()) # [('k1', 5), ('k2', 7)]
print(list_dicc)#[('k1', 5), ('k2', 7)]
print("")
print(list_dicc[0])#Accediendo a la tupla  en la posicion cero
print(list_dicc[0][0])#k1
print(list_dicc[0][1])#5

print(list_dicc[1])
print(list_dicc[1][0])#k2
print(list_dicc[1][1])#7


system("clear")

print(dir(list_dicc))