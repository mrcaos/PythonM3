"""
Actividad 2 - Cachipún
El Cachipún, conocido también como chin chan pu, pikachú, jankenpón, yan ken po, pin pon
papas, hakembó o how-are-you-speak, es un juego de manos en el que existen tres
elementos: la piedra que vence a la tijera rompiéndola, la tijera que vence al papel cortándolo
y el papel que vence a la piedra envolviéndola, dando lugar a un círculo o ciclo cerrado. Se
utiliza con mucha frecuencia para decidir quién de dos personas hará algo, tal y como se
hace a veces usando una moneda, o para dirimir algún asunto.
Para poner en práctica lo que hemos aprendido a lo largo de la unidad, se implementará un
programa en Python que permite jugar al cachipún en contra del computador
"""

import random

computador = ["piedra", "papel", "tijeras"]
computador = random.choice(computador)

jugador = ["piedra", "papel", "tijeras"]

jugador == "piedra" or jugador == "papel" or jugador == "tijera"

if jugador == "piedra" and computador == "tijera":
    print(f"Tu jugaste {jugador}\ncomputador jugo {computador}\nGanaste!!")
    
elif jugador == "papel" and computador == "papel":
    print(f"Tu jugaste {jugador}\nComputador jugó {computador}\nEmpataste!!")
    
elif jugador == "papel" and computador == "tijera":
    print(f"Tu jugaste {jugador}\nComputador jugó {computador}\nPerdiste!!")
    
else:
    print("Argumento invalido: Debe ser piedra, papel o tijera.")