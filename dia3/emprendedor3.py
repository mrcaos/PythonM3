#Solicitud de datos
precioSuscripcion = float(input("Ingrese precio de suscripcion del clp: \n"))
usuarios = int(input("Ingrese numero de usuarios: \n"))
gastosTotales = float(input("Ingrese gastos totales en clp: \n"))
utilidadesAñoAnterior = float(input("Ingrese las utilidades del año aterior mayor a cero, en clp: \n"))

#Utilidades
utilidadesActuales = precioSuscripcion * usuarios - gastosTotales

#Se divide la utilidad actual por la utilidad del año anterios para obtener la razon
razonUtilidadActualyAnterior = utilidadesActuales / utilidadesAñoAnterior

#Salida
print(f"La razon entre la utilidad actual y del año anterior es: {round(razonUtilidadActualyAnterior,2)} de crecimiento")