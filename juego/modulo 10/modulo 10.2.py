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
journal = []
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

inventario = [{"nombre": "Binoculares", "cantidad": 3, "cura": 0, "tipo": "uso"},
    {"nombre": "Diario y pluma", "cantidad": 3, "cura": 0, "tipo": "uso"},
    {"nombre": "Daga arrojadiza", "cantidad": 3, "daña": 5, "tipo": "arma"},]
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

    accion = input("¿Continuar, inventario, usar, esperar o salir?: ")
#----------
    if accion == "inventario":
        for item in inventario:
            print(item["nombre"], ":", item["cantidad"])

    elif accion == "usar":
        nombre = input("¿que objeto quieres usar?: ")
        estado, inventario = usar_objeto(nombre, estado, inventario)

#-------------
    elif accion == "Continuar":
            while True:
                print ("Lib-lao esta comiendo")
                accion = input ("Observar / Nada ")
                if accion == "Observar":
                    if criatura0.estado == "comer":
                        criatura0.estado = "dormir"
                        print ("Observas a Lib-lao hasta que deja de comer y parece buscar un lugar donde dormir")
                        journal.append ("Observacion 1: Lib-lao se va a dormir luego de comer")
                        print("\n--- JOURNAL ---")
                        for entrada in journal:
                            print("*", entrada)
                        break
                    elif criatura0.estado == "dormir":
                        criatura0.estado = "correr"
                        print ("Observas a Lib-lao durmiendo durante una hora, al despertar defeca y sale corriendo")
                        journal.append ("Observacion 2: Lib-lao defeca y sale corriendo luego de dormir")
                        print("\n--- JOURNAL ---") 
                        for entrada in journal:
                            print("*", entrada)
                        break
                    elif criatura0.estado == "correr":
                        criatura0.estado = "comer"
                        print ("Observas a Lib-lao corriendo rapidamente junto a los de su especie buscando hierba, hasta que se queda sin energia y comienza a comer")
                        journal.append ("Observacion 3: Lib-lao se pone a comer luego de correr durante una hora")
                        print("\n--- JOURNAL ---") 
                        for entrada in journal:
                            print("*", entrada)
                        break
                elif accion == "Nada":
                    print("ves pasar el tiempo una hora")
                else:
                    print("Error de escritura")
                print (journal)
                
            hora += 1

            if hora > 24:
                hora = 1
                dia += 1
                print("\n=== CAMBIO DE DÍA ===")
#---------------
    if accion == "salir":
        break

    elif accion == "esperar":

        if criatura0.estado == "comer":
            criatura0.estado = "dormir"

        elif criatura0.estado == "dormir":
            criatura0.estado = "correr"

        elif criatura0.estado == "correr":
            criatura0.estado = "comer"

        hora += 1

        if hora > 24:
            hora = 1
            dia += 1
            print("\n=== CAMBIO DE DÍA ===")