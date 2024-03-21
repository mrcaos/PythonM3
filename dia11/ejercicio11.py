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