def agregar_ingrediente(ingredientes, eleccion):

        disponibles = ['Tomate','Champiñones','Aceituna','Cebolla','Pollo',
                        'Jamón','Carne','Tocino','Queso']
        nuevo_ingrediente = disponibles[eleccion-1]

        if nuevo_ingrediente in ingredientes['ingredientes']:
            print('El ingrediente ya existe')
        else:
            ingredientes['ingredientes'].append(nuevo_ingrediente)
            print(f'Se ha agregado {nuevo_ingrediente}')

        return ingredientes
    
if __name__ == "__main__":
        ingrediente_prueba = {"masa": "Masa Tradicional",
                    "salsa": "Salsa de Tomate",
                    "ingredientes": ["queso"]
                    }
        eleccion = int(input("""Seleccione su Ingrediente:
        1). Tomate
        2). Campiñones
        3). Aceituna
        4). Cebolla
        5). Pollo
        6). Jamon
        7). Carne
        8). Tocino
        9). Queso
        >"""))
        ingredientes = agregar_ingrediente(ingredientes_prueba, eleccion)
        print(ingredientes)