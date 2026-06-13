class jugador:
    def __init__(self, nombre, energia, mente, tiempo):
        self.nombre = nombre
        self.energia = energia
        self.mente = mente 
        self.tiempo = tiempo

name = input ("Cual es tu nombre? ")

jugador1 = jugador(name, 100, 100, 21)

print("Nombre:", jugador1.nombre)
print("Energia:", jugador1.energia,"/100")
print("Mente:", jugador1.mente,"/100")
print("Tiempo:", jugador1.tiempo,"/80")

class enemigo:
    def __init__(self, nombre, energia, mente, tiempo):
        self.nombre = nombre
        self.energia = energia
        self.mente = mente 
        self.tiempo = tiempo

enemigo000 = enemigo("lib-lao", 100, 0, 1)

while True:
    print ("\nCriatura a la vista")
    accion = input("\n¿que quieres hacer? (observar? / salir): ")

    if accion == "observar":
        print("Nombre:", enemigo000.nombre)
        print("Energia:", enemigo000.energia, "/100")
        print("Mente:", enemigo000.mente,"/0")
        print("Tiempo:", enemigo000.tiempo,"/10")

    elif accion == "salir":
        break