import random,sys

buscar = int(sys.argv[1])
print(buscar,type(buscar))

#Random.Shuffle ==> Desordena la lista
listaNumeros = [1,2,3,4,5,6,7,8,9,0]
random.shuffle(listaNumeros)

print(listaNumeros)

for numero in listaNumeros:
    if buscar == numero:
        print("Numero encontrado")
        break
    
    for position, elemento in enumerate(listaNumeros):
# Si el elemento es igual a lo que buscamos terminamos el ciclo
    if elemento == buscar:
        print("¡Elemento encontrado! Se terminará del ciclo")
        break
    else:
# Si es que no es el elemento buscado lo reportamos
        print("Elemento no encontrado")

print("Ha terminado el ciclo")
print(f'El elemento {buscar} se encontró en la posición {position}')
print(f'La lista mezclada es: {listaNumeros}')    