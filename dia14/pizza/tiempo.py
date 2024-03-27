def estimar_tiempo(ingredientes):
        n_ingredientes = len(ingredientes['ingredientes'])
        tiempo = 20 + n_ingredientes * 2
        return tiempo
    
if __name__ == "__main__":
        ingrediente_prueba = {"masa": "Masa Tradicional",
                    "salsa": "Salsa de Tomate",
                    "ingredientes": ["queso"]
                    }
        print(estimar_tiempo(ingrediente_prueba))