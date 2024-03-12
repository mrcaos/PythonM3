#Solicitud de datos
precioSuscripcion = float(input("Ingrese el precio de suscripcion \n"))
numUsuarioNormal = int(input("Ingrese cantidad de usuasrios normales \n"))
numUsuariosPremium = int(input("Ingrese cantidad de usuarios premium \n"))
gastosTotales = float(input("Ingrese los gastos totales en clp: \n"))

#Utilidades
utilidades = precioSuscripcion * numUsuarioNormal + (precioSuscripcion * 1.5)  * numUsuariosPremium - gastosTotales
    
#Salida
print(f"Las utilidades del proyecto son: ${round(utilidades,1)}.")