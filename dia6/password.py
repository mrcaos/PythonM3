contraseña = input("Ingrese una contraseña (min 6 caractees)")

#string.count("") 
if contrasenia.count(" ") > 0:
    print("El password no puede contener espacios")
elif contrasenia == "12345":
    print("El password es incorrecto")
elif len(contrasenia) < 6:
    print("El password es demasiado corto")


#12345

"""
else:
    #len -> contar los caracteres
    if len(contrasenia) < 6:
        print("El password es demasiado corto")
"""