from math import sqrt

#Paso 1 : Captura string y conversion
#radio = float(input("inIngrese el radio en kilometros")) * 1000
radioKilometros = input("Ingrese el radio en kilometros")
radioKilometros = float(radioKilometros)
radioMetros = radioKilometros * 1000

constanteGravitacional = input("Ingrese la constante de gravedad del planeta en [mt/s]")
constanteGravitacional = float(constanteGravitacional)#conversion de string a float

#Paso 2: Resolver formula velocidadEscape = raizCuadrada(2 * constanteGravitacional * radioMetros)
multiplicacion = 2 * constanteGravitacional * radioMetros
velocidadEscape = sqrt(multiplicacion)


#Paso 3: 
print(f"La velocidad de escape es {round(velocidadEscape,1)} [m/s]")


