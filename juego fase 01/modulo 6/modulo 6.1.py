# -------------------
# ESTADO DEL JUGADOR
# -------------------
estado = {
    "vida": 10,
    "energia": 5,
    "nutrientes": 0
}

# -------------------
# INVENTARIO
# -------------------
inventario = [
    {"nombre": "Venda", "cantidad": 3, "cura": 25, "tipo": "vida"},
    {"nombre": "Provisiones", "cantidad": 2, "cura": 50, "tipo": "nutrientes"},
    {"nombre": "Bebida", "cantidad": 3, "cura": 30, "tipo": "energia"}
]


# -------------------
# FUNCIONES
# -------------------

def mostrar_estado(estado):
    print("\n--- ESTADO ---")
    print("Vida:", estado["vida"])
    print("Energia:", estado["energia"])
    print("Nutrientes:", estado["nutrientes"])


def usar_objeto(nombre, estado, inventario):

    for item in inventario:
        if item["nombre"] == nombre and item["cantidad"] > 0:

            if item["tipo"] == "vida":
                estado["vida"] += item["cura"]

            elif item["tipo"] == "energia":
                estado["energia"] += item["cura"]

            elif item["tipo"] == "nutrientes":
                estado["nutrientes"] += item["cura"]

            item["cantidad"] -= 1
            print("Usaste", nombre)
            return estado, inventario

    print("No puedes usar ese objeto")
    return estado, inventario


def accion_juego(accion, estado):

    if accion == "combate":
        estado["vida"] -= 15

    elif accion == "caminar":
        estado["energia"] -= 15

    elif accion == "esperar":
        estado["nutrientes"] -= 15

    return estado


# -------------------
# JUEGO PRINCIPAL
# -------------------

print("Juego iniciado")

while True:

    mostrar_estado(estado)

    accion = input("\n¿que quieres hacer? (inventario / usar / combate / caminar / esperar / salir): ")

    if accion == "inventario":
        for item in inventario:
            print(item["nombre"], "-", item["cantidad"])

    elif accion == "usar":
        nombre = input("¿que objeto quieres usar?: ")
        estado, inventario = usar_objeto(nombre, estado, inventario)

    elif accion in ["combate", "caminar", "esperar"]:
        estado = accion_juego(accion, estado)

    elif accion == "salir":
        break

    # condiciones de muerte
    if estado["vida"] <= 0 or estado["energia"] <= 0 or estado["nutrientes"] <= -10:
        print("Has muerto")
        break

print("Fin del juego")