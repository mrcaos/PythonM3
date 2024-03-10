"""
Mi nombre es Bill, tengo 52 años y me desempeño como CEO en Microsoft.
Soy Creativo, Apasionado y Visionario.
Mi pasatiempo es jugar Golf y me gustaría poder jubilarme pronto
"""

nombre = input('Ingrese su Nombre: Bill')
edad = input('Ingrese Edad: 52 años')
ocupacion = input('Ingrese Ocupación: Ceo')
lugar = input('En dónde?: Microsoft')
caracteristica_1 = input('Ingrese 3 características:\n1. > Creativo')
caracteristica_2 = input('2. > Apasionado')
caracteristica_3 = input('3. > Visionario')
pasatiempo = input('Cuál es tu pasatiempo: Jugar Golf')
hacer = input('¿Que quieres hacer? Jubilarme pronto')

print(f'''
Mi nombre es {nombre}, tengo {edad} años y me desempeño como {ocupacion} en {lugar}.
Soy una persona {caracteristica_1}, {caracteristica_2} y {caracteristica_3}.

Mi pasatiempo es {pasatiempo} y me gustaría poder {hacer}.''')