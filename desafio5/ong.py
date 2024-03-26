import math

def factorial(n):
    calculo = 1
    for i in range(1, n + 1):
        calculo *= i
    return calculo

def productoria(lista):
    calculo = 1
    for numero in lista:
        calculo *= numero
    return calculo   
        
        
def calcular(**kwargs):
    for key, valor in kwargs.items():
        if "fact" in key:
            print(f"El factorial de {valor} es {factorial(valor)}")
        elif "prod" in key:
            print(f"La productoria de {valor} es {productoria(valor)}")     
            
calcular(fact_1 = 5, prod_1 = [3,6,4,2,8], fact_2 = 6)