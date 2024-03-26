from os import sys


"""Funciones

print('Opciones: ')
print('1) De acuerdo')
print('2) En desacuerdo')
print('3) No me interesa')


"""

def imprimir_menu():
    print('Opciones: ')
    print('1). De acuerdo')
    print('2). En desacuerdo')
    print('3). No me interesa')













def suma(valor1,valor2): #valor1 = 3 , valor2 = 5
    suma = valor1 + valor2  #suma = 3 + 5; suma = 8
    return suma  #return 8

def suma2(valor1,valor2):
    return valor1 + valor2
print("qwerty123456") #Nunca se ejecutara

suma(3,5)
print("valor de respuesta",suma(1,9))  #Se imprime el valor del retorno

resultado = suma(6,7) #Capturando el valor de retorno



#RETORNO MULTIPLE
def cuadrado_cubo(base):
    cuadrado = base**2
    cubo = base**3
    return cuadrado, cubo

print(cuadrado_cubo(2)) #Retorno de una dupla (4 , 8)

valor_cuadrado,valor_cubo = cuadrado_cubo(3) #(9,27)
print(valor_cuadrado,valor_cubo)


def filtrar(diccionario, umbral):
    filtro = {k:v for k,v in diccionario.items() if v > umbral}
    return filtro

precios = {'Notebook': 700000,
'Teclado': 25000,
'Mouse': 12000,
'Monitor': 250000,
'Escritorio': 135000,
'Tarjeta de Video': 1500000}

print(filtrar(precios, 12000))

#

def extremo_multiplicado(lista,factor):
    minimo = min(lista)
    maximo = max(lista)
    return factor*minimo, factor*maximo

#print(extremo_multiplicado(4,[1,2,3,4])) #error de elementos 

print(extremo_multiplicado([1,2,3,4], 4)) 

# se entregan en orden
print(extremo_multiplicado(factor = 4, lista = [1,2,3,4]))


#PARAMETROS OPCIONALES O POR DEFAULT
def elevar(base, exponente, redondear = False):
    if redondear:
        valor = round(base**exponente,2)
    else:
        valor = base**exponente
    return valor
print(elevar(2, 3))#19.241905543136184

print(elevar(2, 3, redondear = True))#19.24



# **KWARGS --> Se resive un diccionario 
def parametros(**kwargs):
    print(kwargs)
    print(kwargs["lista1"])

parametros(numero1= 23, texto ="Hola", lista1 = [2,3,4,5,6])#
print("")

# *ARGS ---> Se resive una tupla
def argumentos(*args):
    print(args)
    print(args[0])#23
    print(args[2])#[2,3,4,5,6]

argumentos(23, "hola", [2,3,4,5,6])


# VARIABLES LOCALES Y VARIABLES GLOBALES

pais = "Chile" #VARIABLE GLOBAL

def ciudades():
    #SCOPE DE LA VARIABLE "CAPITAL" es solo en el metodo ciudades
    capital = "Santiago"
    print(pais,capital)
    #pais = "peru" #NO SE PUEDE / RECOMIENDO MODIFICAR EL VALOR DE UNA VARIABLE GLOBAL
    return capital #return "SANTIAGO"
    
print(pais)
ciudades()
#print(capital)#Variable no definida
print(pais)