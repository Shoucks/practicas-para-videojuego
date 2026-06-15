#----------------------
# JUGADOR
#----------------------

class jugador:
    def __init__(self, nombre, energia, mente, tiempo):
        self.nombre = nombre
        self.energia = energia
        self.mente = mente
        self.tiempo = tiempo


#----------------------
# CRIATURA
#----------------------

class criatura:
    def __init__(self, nombre, energia, mente, tiempo):
        self.nombre = nombre
        self.energia = energia
        self.mente = mente
        self.tiempo = tiempo
        self.tiempo_max = 5
        self.estado = "comer"


criatura0 = criatura("Lib-lao", 100, 100, 1)


#----------------------
# JOURNAL
#----------------------

journal = []

hora = 1
dia = 1


#----------------------
# INVENTARIO
#----------------------

inventario = [
    {"nombre": "Binoculares", "cantidad": 1, "tipo": "uso"},
    {"nombre": "Diario y pluma", "cantidad": 1, "tipo": "uso"},
    {"nombre": "Daga arrojadiza", "cantidad": 3, "daña": 2, "tipo": "arma"}
]


#----------------------
# FUNCIONES
#----------------------

def mostrar_journal():

    print("\n--- JOURNAL ---")

    if len(journal) == 0:
        print("No hay observaciones.")

    for entrada in journal:
        print("*", entrada)


def usar_objeto(nombre):

    global inventario

    for item in inventario:

        if item["nombre"] == nombre and item["cantidad"] > 0:

            if item["tipo"] == "arma":

                criatura0.tiempo += item["daña"]

                item["cantidad"] -= 1

                print("\nLanzas una daga a Lib-lao.")

                print(
                    "Tiempo biológico:",
                    criatura0.tiempo,
                    "/",
                    criatura0.tiempo_max
                )

                if criatura0.tiempo >= criatura0.tiempo_max:

                    print("\nLib-lao ha muerto.")

                    inventario.append(
                        {
                            "nombre": "Lana",
                            "cantidad": 1,
                            "tipo": "recurso"
                        }
                    )

                    print("Obtienes Lana.")

                return

    print("No puedes usar ese objeto.")


#----------------------
# INICIO
#----------------------

print("Bienvenidos a Shikido")

name = input("\nIntroduce el nombre del Investigador: ")

jugador0 = jugador(name, 100, 100, 21)

print("\nNombre:", jugador0.nombre)
print("Energia:", jugador0.energia, "/100")
print("Mente:", jugador0.mente, "/100")
print("Tiempo:", jugador0.tiempo, "/80")


#----------------------
# BUCLE PRINCIPAL
#----------------------

while True:

    print("\n----------------------")
    print(f"Día {dia} - Hora {hora}:00")
    print("Estado de Lib-lao:", criatura0.estado)
    print(
        "Tiempo biológico:",
        criatura0.tiempo,
        "/",
        criatura0.tiempo_max
    )
    print("----------------------")

    accion = input(
        "¿Continuar, inventario, usar, esperar o salir?: "
    )

    #----------------------
    # INVENTARIO
    #----------------------

    if accion == "inventario":

        print("\n--- INVENTARIO ---")

        for item in inventario:
            print(item["nombre"], ":", item["cantidad"])

    #----------------------
    # USAR OBJETO
    #----------------------

    elif accion == "usar":

        nombre = input(
            "¿Que objeto quieres usar?: "
        )

        usar_objeto(nombre)

    #----------------------
    # OBSERVAR
    #----------------------

    elif accion == "Continuar":

        if criatura0.estado == "comer":

            print(
                "\nObservas a Lib-lao comiendo hierba."
            )

            journal.append(
                "Lib-lao come hierba."
            )

            criatura0.estado = "dormir"

        elif criatura0.estado == "dormir":

            print(
                "\nObservas a Lib-lao durmiendo."
            )

            journal.append(
                "Lib-lao duerme durante varias horas."
            )

            criatura0.estado = "correr"

        elif criatura0.estado == "correr":

            print(
                "\nObservas a Lib-lao corriendo con su grupo."
            )

            journal.append(
                "Lib-lao corre buscando nuevas zonas de pasto."
            )

            criatura0.estado = "comer"

        mostrar_journal()

        hora += 1

    #----------------------
    # ESPERAR
    #----------------------

    elif accion == "esperar":

        if criatura0.estado == "comer":
            criatura0.estado = "dormir"

        elif criatura0.estado == "dormir":
            criatura0.estado = "correr"

        elif criatura0.estado == "correr":
            criatura0.estado = "comer"

        hora += 1

    #----------------------
    # SALIR
    #----------------------

    elif accion == "salir":
        break

    #----------------------
    # CAMBIO DE DIA
    #----------------------

    if hora > 24:

        hora = 1
        dia += 1

        print("\n=== CAMBIO DE DÍA ===")