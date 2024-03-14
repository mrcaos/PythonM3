edad = 27
#Juan es mayor de edad ?
print(edad >= 18)#true
print(edad < 18)#false

edadGraduacionColegio = 17
#Juan se graduo antes de los 18 años?
print(edadGraduacionColegio < 18)#true
print(edadGraduacionColegio >= 18)#false

experienciaLaboral = 4
#Juan no tiene 4 años de experiencia laboral?
print(experienciaLaboral != 4)#false
print(experienciaLaboral == 4)#true

numeroHijos = 0
#Juan tiene hijos?
print(numeroHijos > 0)#false
print(numeroHijos == 0)#true
print(numeroHijos < 1)#true
print(numeroHijos !=0)#false
print(numeroHijos >= 0)#false


"""
- Si las exportaciones disminuyen entonces bajarán las utilidades

- Los precios son altos si y sólo sí los costos aumentan

- Si la producción aumenta entonces bajarán los precios

- Si la contaminación aumenta entonces existirá restricción vehicular adicional

- Ser o no Ser

- La programacion no es facil

"""


nombre = "Juan"
meLLamoJuan = (nombre == "Juan")
print(meLLamoJuan)#True
print(type(meLLamoJuan ))#<class 'bool'>



#Logica proposicional
"""
Quieres helado -----> agregar letra (P)  SI - NO
Quieres bebida -----> agregar letra (Q)  SI - NO

AND (Y , i) 2 ^ 3
Quieres helado y Quieres bebida
El punto critico para el AND (Y) es : ambos verdaderos el resulado es verdadero
P y Q
--------
V y V = V
V y F = F
F y V = F
F y F = F


#Punto critico para el O es: ambos falsos el resultado es falso
P o Q
--------
V o V = V
V o F = V
F o V = V
F o F = F *

XoR
#Punto critico para el XoR es: ambas iguales es resultado es false
P ^ Q


"""