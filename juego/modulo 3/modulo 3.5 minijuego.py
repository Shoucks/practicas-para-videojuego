print("¡Comienza el juego!")
print("comer disminuye el hambre en 60 y descansar disminuye cansancio en 60, con 100 mueres y cada dia aumenta 30 en cada uno")
hambre = 30
cansancio = 30
vivo = True
for dia in range(1, 6):
    print(f"\nDía {dia}")

    hambre += 30
    cansancio += 30

    if hambre >= 100:
        print("Has muerto de hambre")
        vivo = False
        break

    if cansancio >= 100:
        print("Has muerto de agotamiento")
        vivo = False
        break

    print("Hambre:", hambre)
    print("Cansancio:", cansancio)

    accion = input("¿comer o descansar? ")

    if accion == "comer":
        hambre -= 60
    elif accion == "descansar":
        cansancio -= 60

    print("Hambre al final del día:", hambre)
    print("Cansancio al final del dia:", cansancio)
if vivo:
    print("¡Has sobrevivido 5 días!")