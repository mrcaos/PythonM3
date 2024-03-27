def tipo_salsa(ingredientes, eleccion):
        if eleccion == 'T':
            ingredientes['salsa'] = 'Salsa de Tomate'
        elif eleccion == 'A':
            ingredientes['salsa'] = 'Salsa Alfredo'
        elif eleccion == 'B':
            ingredientes['salsa'] = 'Salsa Barbecue'
        elif eleccion == 'P':
            ingredientes['salsa'] = 'Salsa Pesto'

        if eleccion in ['T','A','B','P']:
            print(f'Su salsa se cambió a {ingredientes["salsa"]}')
        else:
            print('No se ha cambiado su tipo de Salsa')

        return ingredientes
    
if __name__ == "__main__":
        ingrediente_prueba = {"masa": "Masa Tradicional",
                    "salsa": "Salsa de Tomate",
                    "ingredientes": ["queso"]
                    }
        eleccion = input("""Seleccione su tipo de Salsa:
        T). Salsa de Tomate
        A). Salsa Afredo
        B). Salsa Barbecue
        P). Salsa Pesto
        >""")
        ingredientes = tipo_salsa(ingredientes_prueba, eleccion)
        print(ingredientes)