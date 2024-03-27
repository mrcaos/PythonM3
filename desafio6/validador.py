def validate(opciones, eleccion):
    
    while eleccion not in opciones:
        print("Opcion no valida, ingrese una de las opciones validas: ")
        eleccion = input("Ingresa una opcion: ").lower()
        
    return eleccion


if __name__ == '__main__':
    
    eleccion = input('Ingresa una Opción: ').lower()
    # letras = ['a','b','c','d'] # pueden probar con letras también para verificar su funcionamiento.
    numeros = ['0','1']
    # Si se ingresan valores no validos a eleccion debe seguir preguntando
    validate(numeros, eleccion)