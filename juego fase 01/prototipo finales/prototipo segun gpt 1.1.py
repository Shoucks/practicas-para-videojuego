# -------------------
# ESTADO DEL JUGADOR
# -------------------
vida = 10
energia = 5
nutrientes = 0


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

def estado():
    print("\n--- ESTADO ---")
    print("Vida:", vida)
    print("Energia:", energia)
    print("Nutrientes:", nutrientes)


def usar_objeto(nombre):
    global vida, energia, nutrientes

    for item in inventario:
        if item["nombre"] == nombre and item["cantidad"] > 0:

            if item["tipo"] == "vida":
                vida += item["cura"]

            elif item["tipo"] == "energia":
                energia += item["cura"]

            elif item["tipo"] == "nutrientes":
                nutrientes += item["cura"]

            item["cantidad"] -= 1
            print("Usaste", nombre)
            return

    print("No puedes usar ese objeto")


# -------------------
# JUEGO PRINCIPAL
# -------------------

print("Juego iniciado")

while True:

    estado()

    accion = input("\n¿que quieres hacer? (inventario/usar/combate/caminar/esperar/salir): ")

    if accion == "inventario":
        for item in inventario:
            print("\ntienes", item["cantidad"], item["nombre"], "que cura", item["cura"], "de", item["tipo"], "cada uno")
    elif accion == "usar":
        nombre = input("¿que objeto quieres usar?: ")
        usar_objeto(nombre)
    elif accion == "combate":
        vida -= 15
    elif accion == "caminar":
        energia -= 15
    elif accion == "esperar":
        nutrientes -= 15
    elif accion == "salir":
        break


    # condiciones de muerte
    if vida <= 0 or energia <= 0 or nutrientes <= -10:
        print("Has muerto")
        break


print("Fin del juego")