from os import system

computador = {
    'notebook': 489990, 
    'tablet': 120000, 
    'cargador': 12400
    }
print(computador.keys())#dict_keys(['notebook', 'tablet', 'cargador'])
for key in computador.keys():
    print(key)
    
print("")
system("clear")
print(computador.values())#dict_values([489990, 120000, 12400])
for valor in computador.values():
    print(valor)

print("")
system("clear")
print(computador.items())#dict_items([('notebook', 489990), ('tablet', 120000), ('cargador', 12400)])
for clave,valor in computador.items():
    print(f"clave {clave} - valor {valor}")


"""
Sets
#Se escriben con llaves {}, no tienen claves, no permiten datos repetidos 
#no tienen un orden especifico 
"""
system("clear")
muchos_animales = {'Gato', 'Perro', 'Tortuga', 
'Gato', 'Perro', 'Tortuga', 
'Gato', 'Perro', 'Tortuga', 
'Gato', 'Perro', 'Tortuga', 
'Hurón', 'Hamster', 'Erizo de Tierra',2,2,2.5,2.6}

print(muchos_animales)
muchos_animales.add(7)
print(muchos_animales)
muchos_animales.remove("Hamster")
muchos_animales.discard("Huron")
muchos_animales.discard("Raton")
muchos_animales.pop()#Elimina cualquiera 
print(muchos_animales)
muchos_animales.clear()
print(muchos_animales)#set() , vacio