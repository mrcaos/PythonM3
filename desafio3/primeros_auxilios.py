"""INICIO"""

responde_estimulo = input("Responde a Estimulos? (Si/No): ")
if responde_estimulo == "si":
    print("Valorar la necesidad de llevarlo al hospital mas cercano")
    print("Fin")
elif responde_estimulo == "no":
    print("Abrir la via Aerea")
    
respira = input("La persona respira? (Si/No): ")
if respira == "si":
    print("Permitirle una posicion de suficiente respiracion")
    print("Fin")
elif respira == "no":
    print("Administrar 5 Ventilaciones y llamar a Ambulancia")
    
signos_vida = input("Signos de Vida? (Si/No): ")
if signos_vida == "no":
    print("Administrar Compresiones Toracicas hasta que llegue ambulancia")
elif signos_vida == "si":
    print("Reevaluarr a la espera de la Ambulancia")
    
llego_ambulancia = input("Llego la Ambulancia (Si/No): ")
if llego_ambulancia == "no":
    print("Reevaluar signos de vida")
elif llego_ambulancia == "si":
    print("Fin")
    
    """FIN"""