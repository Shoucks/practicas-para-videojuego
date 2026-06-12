inventario = ["espada", "agua"]

accion = input("¿agregar, eliminar o ver?")
if accion == "agregar":
    agregar = input("¿que quieres agregar?: escudo o capa")
    if agregar == "escudo":
        inventario.append ("escudo")
    elif agregar == "capa":
        inventario.append ("capa")
elif accion == "eliminar":
    eliminar = input("¿espada o agua? ")
    if eliminar == "espada":
        inventario.remove ("espada")
    elif eliminar == "agua":
        inventario.remove ("agua")
elif accion == "ver":
    print(inventario)