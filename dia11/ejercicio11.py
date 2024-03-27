from os import system

notas = {
    "Camila": 7, 
    "Antonio": 7, 
    "Felipe": 6, 
    "Antonia": 7,
    "Antonia": 6,
    }

print(notas)#{'Camila': 7, 'Antonio': 7, 'Felipe': 6, 'Antonia': 6}
print(len(notas))#4

#print(notas[2])#KeyError: 2
#print(nota["FElipe"])#KeyError: "Felipe"
print(notas.get("FElipe"))#None
print(notas["Felipe"])#6
print(notas.get("Camila"))#7
print(notas.get("Mijail","valor no encontrado"))#10

prueba = notas.get("Julio")
print(prueba)#None
print(type(prueba))#<class "NoneType">

#agregar
notas["Israel"]= "FulLStack Python"
print(notas)#
#{'Camila': 7, 'Antonio': 7, 'Felipe': 6, 'Antonia': 6, 'Israel': 'FulLStack Python'}

notas["Israel"]= 4
print(notas)
print("")
#{'Camila': 7, 'Antonio': 7, 'Felipe': 6, 'Antonia': 6, 'Israel': 4}

notas.setdefault("Juan",10)
print(notas)
#{'Camila': 7, 'Antonio': 7, 'Felipe': 6, 'Antonia': 6, 'Israel': 4, 'Juan': 10}

notas.setdefault("Juan",2)
#Si la clave existe, retorna el valor actual, NO LO REEMPLAZA

print(notas.setdefault("Juan",2))
print(notas)
notas.setdefault("Valeria")
print(notas)
#{'Camila': 7, 'Antonio': 7, 'Felipe': 6, 'Antonia': 6, 'Israel': 4, 'Juan': 10, 'Valeria': None}

print("")
del notas ["Felipe"]
print(notas)
print("")
eliminado = notas.pop("Antonio")
print(eliminado,notas)
eliminados={}
#elminados = eliminados.setdefault(notas.pop("Camila"))
eliminados ["Camila"]=notas.pop("Camila")
print(notas)#{'Antonia': 6, 'Israel': 4, 'Juan': 10, 'Valeria': None}
print(eliminados)#("Camila": 7)

print("")
tupla1=notas.popitem()#Elinina y devulve la tupla(clave:valor)
print(tupla1)
print(notas)
###Tuplas => similas a las listas pero son inmutables (valor1, valor2.......valorn)
print(tupla1[0])
print(tupla1[1])
#tupla1[1]= "Mishi"

notas.clear()#Elimina los elemenos, dejando un diccionario vacio
print(notas)#

###Comparar diccionarios
dic1 = {1:"uno",2:"dos"}
dic2 = {2:"dos",1:"uno"}
dic3 = {2:"dos",3:"tres"}
dic4 = {2:"dos",3:"cuatro"}
print(dic1==dic2) #True
print(dic1==dic3) #False
print(dic4==dic3) #False

##Diccionarios Anidados
system("cls")#system("cls")

pares_impares ={
    "pares":{
        2:"dos",
        4:"cuatro",
        6:"seis",
        8:"ocho",
        10:"diez",
    },
    "impar":{"uno":1,"tres":3,"cinco":5,"siete":7,"nueve":9},
} 

#imprimir el valor "seis"
print(pares_impares["pares"])#{2: 'dos', 4: 'cuatro', 6: 'seis', 8: 'ocho', 10: 'diez'}
print(pares_impares["pares"][6])#'seis'
#imprimir el valor 5
print(pares_impares["impar"])#{'uno': 1, 'tres': 3, 'cinco': 5, 'siete': 7, 'nueve': 9}
print(pares_impares["impar"]["cinco"])#5