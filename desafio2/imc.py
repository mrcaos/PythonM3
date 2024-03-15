"""
Actividad 1 - IMC
El IMC, conocido también como el Índice de masa corporal, es una medida que asocia el
peso de una persona con su talla (su altura). Este valor es utilizado normalmente como un
indicador nutricional y constituye un índice fácil y sencillo de calcular para determinar el
estado de obesidad y sobrepeso de una persona. El IMC se calcula de la siguiente manera:
    IMC=W/H^2

"""

pesoKilogramo = float(input("Ingrese su peso en kg: \n"))
alturaMetros = float(input("Ingrese su altura en m: \n"))

indiceMasaCorporal = float(pesoKilogramo/alturaMetros**2)
print("Su IMC es ", pesoKilogramo/alturaMetros**2)


if indiceMasaCorporal<18.5:
    print("La clasificacion OMS es Bajo Peso")
elif 18.5<=indiceMasaCorporal and indiceMasaCorporal<25:
    print("La clasificacion OMS es Adecuado")
elif 25>=indiceMasaCorporal and indiceMasaCorporal<30:
    print("La clasificacion OMS es Sobrepeso")
elif 30>=indiceMasaCorporal and indiceMasaCorporal<35:
    print("La clasificacion OMS es Obesidad Grado I")
elif 35>=indiceMasaCorporal and indiceMasaCorporal<40:
    print("La clasificacion OMS es Obesidad Grado II")
elif 40>=indiceMasaCorporal:
    print("La clasificacion OMS es Obesidad Grado III")