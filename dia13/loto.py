import random

pool = [n for n in range(1,42)]
elegido = random.choice(pool)
print("El primer número es", elegido)

pool.remove(elegido)
print(pool)
elegido = random.choice(pool)
print("El segundo número es", elegido)

pool.remove(elegido)
print(pool)
elegido = random.choice(pool)
print("El tercer número es", elegido)

pool.remove(elegido)
print(pool)
elegido = random.choice(pool)
print("El cuarto número es", elegido)

pool.remove(elegido)
print(pool)
elegido = random.choice(pool)
print("El quinto número es", elegido)

pool.remove(elegido)
print(pool)
elegido = random.choice(pool)
print("El sexto número es", elegido)

pool.remove(elegido)
print(pool)
elegido = random.choice(pool)
print("El Comodín número es", elegido)
print(pool)

def sacar_numero(posicion):
    global pool
    elegido = random.choice(pool)
    pool.remove(elegido)
    print(f'El {posicion} es {elegido}')
    
print("Sorteo Terminado")