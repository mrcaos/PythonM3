"""
preguntas = ['Enunciado Pregunta 1','Enunciado Pregunta 2','Enunciado Pregunta 3']
respuestas = []

print(pregunta [0])
print('Opciones: ')
print('1). De acuerdo')
print('2). En desacuerdo')
print('3). No me interesa')
respuestas.append(input("> \n"))


print(pregunta [1])
print('Opciones: ')
print('1). De acuerdo')
print('2). En desacuerdo')
print('3). No me interesa')
respuestas.append(input("> \n"))


print(pregunta [2])
print('Opciones: ')
print('1). De acuerdo')
print('2). En desacuerdo')
print('3). No me interesa')
respuestas.append(input("> \n"))

print(f'La respuesta a la pregunta 1 fue {respuestas[0]}')
print(f'La respuesta a la pregunta 2 fue {respuestas[1]}')
print(f'La respuesta a la pregunta 3 fue {respuestas[2]}')
"""

#OPTIMIZACION

def imprimir_menu():
    print('Opciones: ')
    print('1). De acuerdo')
    print('2). En desacuerdo')
    print('3). No me interesa')
    
preguntas = ['Enunciado Pregunta 1','Enunciado Pregunta 2','Enunciado Pregunta 3']
respuestas = []

for pregunta in preguntas:    #singular/plural
    print(pregunta)
    imprimir_menu()
    respuestas.append(input("> "))
    print("")
    
for i in range(len(respuestas)):   #[0,1,2]   len= 3
    print(f'La respuesta a la pregunta {i+1} es: {respuestas[i]}')
    
    
