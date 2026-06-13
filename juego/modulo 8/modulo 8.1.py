class LibLao:
    def __init__(self):
        self.estado = "comer"


criatura = LibLao()

turno = 1
dia = 1

print("Empieza la observación de Lib-Lao")

while True:

    print("\n----------------------")
    print(f"Día {dia} - Turno {turno}/24")

    # 👇 ESTO ES LO IMPORTANTE: OBSERVAR
    print("Estado de Lib-Lao:", criatura.estado)
    print("----------------------")

    accion = input("¿esperar o salir?: ")

    if accion == "salir":
        break

    if accion == "esperar":

        if criatura.estado == "comer":
            criatura.estado = "dormir"

        elif criatura.estado == "dormir":
            criatura.estado = "caminar"

        elif criatura.estado == "caminar":
            criatura.estado = "comer"

        turno += 1

        if turno > 24:
            turno = 1
            dia += 1
            print("\n=== CAMBIO DE DÍA ===")