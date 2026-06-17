#----------------------
#Antes de empezar
#----------------------
#----------------------
#Jugador: 
#energía 
#nutrición 
#----------------------
class jugador:
    def __init__(self, nombre, energia, mente, tiempo):
        self.nombre = nombre
        self.energia = energia
        self.mente = mente 
        self.tiempo = tiempo

#----------------------
#Criatura: 
#comer 
#dormir 
#caminar 
#----------------------
class criatura:
    def __init__(self, nombre, energia, mente, tiempo):
        self.nombre = nombre
        self.energia = energia
        self.mente = mente 
        self.tiempo = tiempo
        self.estado = "comer"
criatura0 = criatura("Lib-lao", 100, 100, 1)
tiempo_min=1
tiempo_max=5

        
#----------------------
#Journal: 
#*-----Observas a Lib-Lao
#*-----Descubres que come hierba
#registra descubrimientos 
#*Se registra en journal
#----------------------
Journal = []
hora = 1
dia = 1
# -------------------
# FUNCIONES
# -------------------

def mostrar_estado(estado):
    print("\n--- ESTADO ---")
    print("Energia ", estado["energia"])
    print("Mente: ", estado["mente"])
    print("Tiempo: ", estado["tiempo"])


def usar_objeto(nombre, estado, inventario):

    for item in inventario:
        if item["nombre"] == nombre and item["cantidad"] > 0:

            if item["tipo"] == "uso":
                estado["Uso"] += item["ver"]

            elif item["tipo"] == "arma":
                estado["tiempo"] -= item["daña"]

            item["cantidad"] -= 1
            print("Usaste", nombre)
            return estado, inventario

    print("No puedes usar ese objeto")
    return estado, inventario



#----------------------
#Inventario: 
#recoge objetos

#*-----Recoges hierba
#*-----La hierba entra al inventario
#----------------------

Inventario = [{"nombre": "Binoculares", "cantidad": 3, "cura": 0, "tipo": "uso"},
    {"nombre": "Diario y pluma", "cantidad": 3, "cura": 0, "tipo": "uso"},
    {"nombre": "Daga arrojadiza", "cantidad": 3, "daña": 5, "tipo": "arma"},
    {"nombre": "Daga recoleccion", "cantidad": 3, "recolecta": 1, "tipo": "uso"}]
#----------------------
#Sistema completo
#----------------------
print("Bienvenidos a Shikido")
name = input("\nIntroduce el nombre del Investigador ")
jugador0 = jugador(name, 100, 100, 21)
print("\nNombre:", jugador0.nombre)
print("Energia:", jugador0.energia,"/100")
print("Mente:", jugador0.mente,"/100")
print("Tiempo:", jugador0.tiempo,"/80")

while True:

    print("\n----------------------")
    print(f"Día {dia} - Hora {hora}:00")

    print("Estado de Lib-Lao:", criatura0.estado)
    print("----------------------")

    accion = input("¿esperar o salir?: ")

    if accion == "salir":
        break

    if accion == "esperar":

        if criatura0.estado == "comer":
            criatura0.estado = "dormir"

        elif criatura0.estado == "dormir":
            criatura0.estado = "caminar"

        elif criatura0.estado == "caminar":
            criatura0.estado = "comer"

        hora += 1

        if hora > 24:
            hora = 1
            dia += 1
            print("\n=== CAMBIO DE DÍA ===")